"""
Builds the charts embedded in docs/use-cases/*.md from data served by the
IWMI Digital Twins API (https://api.digitaltwins.iwmi.org) - the same API the
portal's feature-info charts call.

    python tools/use_case_charts.py            # download (cached) + render
    python tools/use_case_charts.py --refresh  # re-download everything

Raw responses are cached in tools/.cache/use-cases/ (git-ignored); PNGs land in
docs/assets/charts/. Every chart states its source and the "as of" date in the
subtitle, so re-running keeps the pages honest.
"""
from __future__ import annotations

import gzip
import io
import json
import os
import ssl
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "tools" / ".cache" / "use-cases"
OUT = ROOT / "docs" / "assets" / "charts"
API = "https://api.digitaltwins.iwmi.org"
REFRESH = "--refresh" in sys.argv

# IWMI brand palette (branding.iwmi.org/our-colours)
DARK = "#28537D"
BLUE = "#5088C6"
SKY = "#46BBD4"
TEAL = "#0297A6"
GREEN = "#22AD7A"
ORANGE = "#E86933"
YELLOW = "#DD9103"
GREY = "#E8E7E7"
INK = "#1F2A37"
MUTED = "#6B7280"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": "#CBD5E1",
    "axes.labelcolor": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.grid": True,
    "grid.color": "#EEF2F7",
    "grid.linewidth": 0.8,
    "axes.axisbelow": True,
    "legend.frameon": False,
    "figure.dpi": 100,
    "savefig.dpi": 170,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

_ctx = ssl.create_default_context()


def fetch(path: str, name: str, timeout: int = 300) -> bytes:
    """GET an API path, transparently gunzipping, with an on-disk cache."""
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / name
    if f.exists() and f.stat().st_size > 50 and not REFRESH:
        return f.read_bytes()
    req = urllib.request.Request(API + path, headers={"Accept-Encoding": "gzip", "User-Agent": "dt-limpopo-docs"})
    with urllib.request.urlopen(req, timeout=timeout, context=_ctx) as r:
        b = r.read()
    if b[:2] == b"\x1f\x8b":
        b = gzip.decompress(b)
    f.write_bytes(b)
    print(f"  fetched {name} ({len(b):,} B)")
    return b


def fetch_json(path, name):
    return json.loads(fetch(path, name).decode("utf-8"))


def fetch_csv(path, name, **kw):
    return pd.read_csv(io.BytesIO(fetch(path, name)), **kw)


def frame(fig, ax, title, subtitle):
    """Consistent chart chrome: bold left title, muted subtitle with source."""
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    # offsets are in inches so short figures get the same title/subtitle gap
    h = fig.get_figheight()
    fig.text(0.01, 1 - 0.07 / h, title, ha="left", va="top", fontsize=13, fontweight="bold", color=INK)
    fig.text(0.01, 1 - 0.36 / h, subtitle, ha="left", va="top", fontsize=8.5, color=MUTED)
    fig.subplots_adjust(top=1 - 0.78 / h)


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / name
    fig.savefig(p)
    plt.close(fig)
    print(f"  wrote {p.relative_to(ROOT)}")


TODAY = date.today().isoformat()

# --------------------------------------------------------------------------- floods


def floods():
    st = "A7H004"  # Limpopo River @ Beit Bridge - the main-stem reference gauge
    csv = fetch_csv(f"/csv/glofas/{st}/csv", f"glofas_{st}.csv", parse_dates=["date"])
    an = fetch_json(f"/visualizations/glofas_flood_analytics?station={st}", f"glofas_flood_analytics_{st}.json")
    summ = fetch_json("/chatbot/flood_summary?limit=20", "flood_summary.json")
    thr = an["thresholds_avg"]

    # -- 1. recent reanalysis + latest forecast against percentile thresholds
    leads = [c for c in csv.columns if c.startswith("lead_")]
    run = pd.Timestamp(an["model_run"])
    # The CSV holds every archived forecast; the portal chart shows the latest
    # run, so window on it: 90 days of hindsight, 30 days of outlook.
    win = csv[(csv.date >= run - pd.Timedelta(days=90)) & (csv.date <= run + pd.Timedelta(days=30))].copy()
    past = win[win.date <= run].copy()
    # where the reanalysis has not caught up yet, the 1-day-ahead forecast is the best analysis
    past["obs"] = past.reanalysis.fillna(past.lead_24)
    fut = win[win.date > run].copy()
    fut["fc"] = fut[leads].bfill(axis=1).iloc[:, 0]  # shortest lead available for that day
    fut = fut.dropna(subset=["fc"])

    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(past.date, past.obs, color=DARK, lw=2, label="Recent flow (GloFAS analysis)")
    if len(fut):
        ax.plot([run, fut.date.iloc[0]], [past.obs.iloc[-1], fut.fc.iloc[0]], color=ORANGE, lw=2, ls="--")
        ax.plot(fut.date, fut.fc, color=ORANGE, lw=2, ls="--", marker="o", ms=3, label=f"30-day forecast (run {run:%d %b %Y})")
    ax.axvline(run, color=MUTED, lw=0.8, ls="--")
    ax.text(run, ax.get_ylim()[1] * 0.02 if False else 0, " today", fontsize=8, color=MUTED, va="bottom")
    ymax = max(thr["p95"] * 1.1, past.obs.max() * 1.25, (fut.fc.max() if len(fut) else 0) * 1.25)
    for k, c, lab in (("p90", YELLOW, "p90 - elevated"), ("p95", ORANGE, "p95 - high"), ("p99", "#B91C1C", "p99 - extreme")):
        if thr[k] < ymax:
            ax.axhline(thr[k], color=c, lw=1, ls=":")
            ax.text(past.date.iloc[0], thr[k], f" {lab} ({thr[k]:.0f} m³/s)", va="bottom", fontsize=8, color=c)
    ax.set_ylabel("Discharge (m³/s)")
    ax.set_ylim(0, ymax)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    ax.legend(loc="upper left", fontsize=8.5, ncol=2)
    cr = pd.DataFrame(an["current_risk"])
    frame(fig, ax, f"Discharge outlook - Limpopo River at Beit Bridge (gauge {st})",
          f"What the GloFAS Discharge Forecast chart shows when you click a gauge, in the dry season. Dotted lines are the station's own flood thresholds "
          f"(p99 = {thr['p99']:.0f} m³/s, off-scale here); current alert level: {cr.alert_level.iloc[0]}. Source: GloFAS via IWMI DT API, as of {TODAY}.")
    save(fig, "floods-glofas-forecast.png")

    # -- 2. annual maxima 1979-present (flood history)
    am = pd.DataFrame(an["annual_maxima"])
    fig, ax = plt.subplots(figsize=(10, 4.4))
    cols = [("#B91C1C" if v >= thr["p99"] else ORANGE if v >= thr["p95"] else BLUE) for v in am.peak_discharge]
    ax.bar(am.year, am.peak_discharge, color=cols, width=0.8)
    ax.axhline(thr["p95"], color=ORANGE, lw=1, ls=":")
    ax.axhline(thr["p99"], color="#B91C1C", lw=1, ls=":")
    ax.text(am.year.min() - 0.4, thr["p99"], f" p99 = {thr['p99']:.0f} m³/s", va="bottom", fontsize=8, color="#B91C1C")
    top = am.nlargest(3, "peak_discharge")
    for _, r in top.iterrows():
        ax.annotate(f"{r.peak_date[:7]}\n{r.peak_discharge:,.0f}", (r.year, r.peak_discharge), textcoords="offset points",
                    xytext=(0, 4), ha="center", fontsize=7.5, color=INK)
    ax.set_ylabel("Annual peak discharge (m³/s)")
    ax.set_xlim(am.year.min() - 1, am.year.max() + 1)
    frame(fig, ax, f"Flood history - annual peak discharge at Beit Bridge ({am.year.min()}-{am.year.max()})",
          "Red = peak above the p99 threshold, orange = above p95. The February 2000 flood is the benchmark event for the lower basin. "
          f"Source: GloFAS reanalysis via IWMI DT API, as of {TODAY}.")
    save(fig, "floods-annual-maxima.png")

    # -- 3. basin-wide flow status today
    s = summ["summary"]
    order = [("normal", "Normal", GREEN), ("elevated", "Elevated (> p90)", YELLOW), ("high", "High (> p95)", ORANGE), ("extreme", "Extreme (> p99)", "#B91C1C")]
    fig, ax = plt.subplots(figsize=(10, 2.9))
    left = 0
    for k, lab, c in order:
        v = s[k]
        ax.barh(0, v, left=left, color=c, height=0.6)
        if v / s["total"] > 0.05:
            ax.text(left + v / 2, 0, f"{lab}\n{v} ({v / s['total']:.0%})", ha="center", va="center", fontsize=8.5, color="white", fontweight="bold")
        left += v
    ax.set_xlim(0, s["total"])
    ax.set_yticks([])
    ax.set_xlabel(f"Forecast points (SWAT channels + gauges), n = {s['total']}")
    ax.grid(False)
    frame(fig, ax, "Basin flow status - how the Reporting Points layer is classified",
          f"Each point is compared with its own historical percentiles, so 'extreme' in the dry season can still be a modest flow in m³/s. "
          f"Source: IWMI DT API flood summary, updated {summ['updated_at'][:10]}.")
    save(fig, "floods-basin-status.png")


# --------------------------------------------------------------------------- droughts


def droughts():
    ch, stn, place = "cha0036", "s20592s27943e", "Ingwizi (upper Shashe, Zimbabwe)"
    anom = fetch_csv(f"/csv/rainfall_anomaly/{ch}/csv", f"rain_anom_{ch}.csv", parse_dates=["date"])
    an = fetch_json(f"/visualizations/rainfall_analytics?station={stn}&start_date=2001-01-01&end_date={TODAY}", f"rain_analytics_{ch}.json")

    # -- 1. monthly anomaly bars
    fig, ax = plt.subplots(figsize=(10, 4.4))
    ax.bar(anom.date, anom.anomaly, width=26, color=np.where(anom.anomaly < 0, ORANGE, BLUE))
    ax.axhline(0, color=INK, lw=0.8)
    ax.set_ylabel("Departure from monthly mean (mm)")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    frame(fig, ax, f"Monthly rainfall anomaly - {place}",
          "The Rainfall Anomalies layer chart: orange months received less than the 2001-present mean for that month, blue more. "
          f"Runs of orange through a wet season (Nov-Mar) are the meteorological-drought signal. Source: CHIRPS via IWMI DT API, as of {TODAY}.")
    save(fig, "droughts-rainfall-anomaly.png")

    # -- 2. annual totals vs mean
    at = pd.DataFrame(an["annual_totals"])
    at = at[at.year < int(TODAY[:4])]  # drop the incomplete current year
    mean = an["statistics"]["mean_annual"]
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.bar(at.year, at.total, color=np.where(at.total < mean * 0.75, ORANGE, np.where(at.total < mean, YELLOW, BLUE)))
    ax.axhline(mean, color=DARK, lw=1.2, ls="--")
    ax.text(at.year.min() - 0.4, mean, f" mean {mean:.0f} mm", va="bottom", fontsize=8.5, color=DARK)
    ax.axhline(mean * 0.75, color=ORANGE, lw=1, ls=":")
    ax.text(at.year.min() - 0.4, mean * 0.75, " 75 % of mean", va="top", fontsize=8, color=ORANGE)
    ax.set_ylabel("Annual rainfall (mm)")
    frame(fig, ax, f"Annual rainfall {at.year.min()}-{at.year.max()} - {place}",
          "Orange = below 75 % of the long-term mean (a failed year), yellow = below mean. "
          f"Consecutive dry years drive hydrological and groundwater drought. Source: CHIRPS via IWMI DT API, as of {TODAY}.")
    save(fig, "droughts-annual-rainfall.png")

    # -- 3. SPI 3 / 12 month
    spi = an["spi"]

    def series(lst):
        df = pd.DataFrame(lst)
        dcol = [c for c in df.columns if "date" in c.lower()][0]
        vcol = [c for c in df.columns if c != dcol][0]
        df[dcol] = pd.to_datetime(df[dcol])
        return df[dcol], pd.to_numeric(df[vcol], errors="coerce")

    fig, ax = plt.subplots(figsize=(10, 4.4))
    for key, c, lab in (("spi_3", SKY, "SPI-3 (season)"), ("spi_12", DARK, "SPI-12 (year)")):
        x, y = series(spi[key])
        ax.plot(x, y, color=c, lw=1.6 if key == "spi_12" else 1.1, label=lab)
    ax.axhspan(-1.5, -1.0, color=YELLOW, alpha=0.12)
    ax.axhspan(-2.0, -1.5, color=ORANGE, alpha=0.14)
    ax.axhspan(-3.5, -2.0, color="#B91C1C", alpha=0.14)
    for yv, lab in ((-1.0, "moderate"), (-1.5, "severe"), (-2.0, "extreme")):
        ax.text(x.iloc[-1], yv - 0.05, f"{lab} drought ", va="top", ha="right", fontsize=7.5, color=MUTED)
    ax.axhline(0, color=INK, lw=0.8)
    ax.set_ylim(-3.5, 3.5)
    ax.set_ylabel("Standardised Precipitation Index")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="upper left", fontsize=8.5, ncol=2)
    frame(fig, ax, f"Standardised Precipitation Index - {place}",
          "How to read the SPI/SPEI drought-hazard layers: below -1 is drought, below -2 extreme. SPI-3 flags a failed season; "
          f"SPI-12 flags multi-year deficits that reach reservoirs and boreholes. Source: CHIRPS via IWMI DT API, as of {TODAY}.")
    save(fig, "droughts-spi.png")


# --------------------------------------------------------------------------- e-flows


def eflows():
    croc = fetch_json("/visualizations/eflow_analytics?river_code=CROC-A24J-ROOIB", "eflow_analytics_croc.json")
    mapun = fetch_json("/visualizations/eflow_analytics?river_code=LIMP-A71L-MAPUN", "eflow_analytics_mapun.json")
    ts = fetch_csv("/csv/eflow_data/LIMP-A71L-MAPUN/csv", "eflow_LIMP-A71L-MAPUN.csv", parse_dates=["date"])

    # -- 1. monthly regime: natural vs present vs e-flow requirement
    fr = pd.DataFrame(croc["flow_regime"])
    x = np.arange(12)
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.bar(x - 0.2, fr.natural, 0.4, color=GREY, edgecolor="#CBD5E1", label="Natural flow (SWAT, no abstraction)")
    ax.bar(x + 0.2, fr.present, 0.4, color=BLUE, label="Present-day flow (SWAT)")
    ax.plot(x, fr.eflow, color=ORANGE, lw=2.2, marker="o", ms=4, label="E-flow requirement")
    for i, a in enumerate(fr.alteration_pct):
        if abs(a) >= 25:
            ax.text(i + 0.2, fr.present[i] + fr.natural.max() * 0.02, f"{a:+.0f}%", ha="center", fontsize=7.5, color=ORANGE if a < 0 else TEAL)
    ax.set_xticks(x, fr.month)
    ax.set_ylabel("Mean monthly flow (m³/s)")
    ax.legend(fontsize=8.5, loc="upper right")
    frame(fig, ax, "Flow regime - Crocodile (West) at Rooibokkraal (CROC-A24J-ROOIB)",
          "The e-flow chart's three series averaged by month, 2015-2026. Labels show the % change from natural where it exceeds 25 %: "
          f"winter (Jul-Aug) flows are cut by two-thirds while wet-season flows are near natural. Source: IWMI DT API e-flow analytics, as of {TODAY}.")
    save(fig, "eflows-regime-croc.png")

    # -- 2. time series with deficit shading
    t = ts[ts.date >= "2015-01-01"]
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(t.date, t.Present_Day_Flow, color=BLUE, lw=1.4, label="Present-day flow")
    ax.plot(t.date, t.Eflow, color=ORANGE, lw=1.6, label="E-flow requirement")
    ax.fill_between(t.date, t.Present_Day_Flow, t.Eflow, where=t.Present_Day_Flow < t.Eflow, color=ORANGE, alpha=0.35, label="Deficit (present < requirement)")
    ax.set_yscale("symlog", linthresh=10)
    ax.set_ylabel("Monthly flow (m³/s, log scale)")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(fontsize=8.5, loc="upper left", ncol=3)
    frame(fig, ax, "Present flow vs e-flow requirement - Limpopo, Shashe to Mzingwane (LIMP-A71L-MAPUN)",
          "The requirement rises in the wet season; shaded gaps are months the river fell short. A log axis keeps dry-season deficits visible next to "
          f"wet-season peaks of 2,500 m³/s. Source: IWMI DT API /csv/eflow_data, as of {TODAY}.")
    save(fig, "eflows-timeseries-mapun.png")

    # -- 3. annual compliance
    a1 = pd.DataFrame(croc["annual_summary"])
    a2 = pd.DataFrame(mapun["annual_summary"])
    yrs = sorted(set(a1.year) | set(a2.year))
    x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.bar(x - 0.2, a1.set_index("year").reindex(yrs).compliance_pct, 0.4, color=TEAL, label="Crocodile (West) - CROC-A24J-ROOIB")
    ax.bar(x + 0.2, a2.set_index("year").reindex(yrs).compliance_pct, 0.4, color=DARK, label="Limpopo - LIMP-A71L-MAPUN")
    ax.set_xticks(x, yrs)
    ax.set_ylim(90, 100.5)
    ax.set_ylabel("% of days meeting the e-flow requirement")
    ax.legend(fontsize=8.5, loc="lower left", ncol=2)
    frame(fig, ax, "E-flow compliance by year - two monitored sites",
          "Compliance is the share of days the modelled present flow met or exceeded the requirement. Note the axis starts at 90 %: "
          f"a drop of one point is several days of ecological deficit. Source: IWMI DT API e-flow analytics, as of {TODAY}.")
    save(fig, "eflows-compliance.png")


# --------------------------------------------------------------------------- reservoirs


def reservoirs():
    stor = fetch_csv("/csv/reservoir_storage/403/csv", "storage_403_Massingir.csv", parse_dates=["date"])
    an = fetch_json("/visualizations/reservoir_analytics?gdw_id=403", "analytics_massingir.json")
    enso = fetch_json("/enso/briefing/hydrology/reservoirs", "enso_reservoirs.json")
    losk = fetch_json("/visualizations/reservoir_analytics?gdw_id=2047", "analytics_loskop.json")

    # -- 1. Massingir storage history + forecast fan
    s = stor.dropna(subset=["pct_capacity"])
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(s.date, s.pct_capacity, color=DARK, lw=1.6, label="Estimated storage (% of capacity)")
    obs = s.dropna(subset=["observed_volume_mcm"])
    ax.scatter(obs.date, obs.observed_volume_mcm / an["dam"]["capacity_mcm"] * 100, s=9, color=SKY, zorder=3, label="Observed (gauge / altimetry)")
    cur = pd.Timestamp(an["forecast"]["pc50"][0]["date"])

    def fc(key):
        df = pd.DataFrame(an["forecast"][key])
        df["date"] = pd.to_datetime(df.date)
        return df[df.date >= cur].sort_values("date")

    p10, p50, p90 = fc("pc10"), fc("pc50"), fc("pc90")
    ax.fill_between(p10.date, p10.pct_capacity, p90.pct_capacity, color=ORANGE, alpha=0.2, label="Forecast range (10th-90th pct)")
    ax.plot(p50.date, p50.pct_capacity, color=ORANGE, lw=2, ls="--", label=f"Forecast median -> {p50.pct_capacity.iloc[-1]:.0f}% by {p50.date.iloc[-1]:%b %Y}")
    for yv, lab, c in ((25, "Low", YELLOW), (10, "Critical", "#B91C1C")):
        ax.axhline(yv, color=c, lw=1, ls=":")
        ax.text(s.date.iloc[0], yv, f" {lab} (<{yv}%)", va="bottom", fontsize=8, color=c)
    ax.set_ylim(0, 120)
    ax.set_ylabel("% of full supply capacity")
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(fontsize=8, loc="upper center", ncol=2, bbox_to_anchor=(0.5, -0.1))
    d = an["dam"]
    frame(fig, ax, f"Storage history and outlook - {d['name']} Dam, {d['river']} River ({d['country']})",
          f"Capacity {d['capacity_mcm']:,.0f} Mm³; the largest reservoir in the basin. Currently {an['statistics']['current_pct']:.0f}% full; "
          f"the 2002-06 drawdown lasted {an['drawdown_spells'][0]['duration']} months. Source: Dams & Reservoirs Basin Level Estimates, IWMI DT API, as of {TODAY}.")
    save(fig, "reservoirs-massingir-storage.png")

    # -- 2. by country
    bc = enso["by_country"]
    names = list(bc.keys())
    cap = np.array([bc[n]["capacity_mcm"] for n in names])
    vol = np.array([bc[n]["volume_mcm"] for n in names])
    fig, ax = plt.subplots(figsize=(10, 4.2))
    y = np.arange(len(names))
    ax.barh(y, cap, color=GREY, height=0.6, label="Capacity (monitored dams)")
    ax.barh(y, vol, color=BLUE, height=0.6, label="Current storage")
    for i, n in enumerate(names):
        ax.text(cap[i] + cap.max() * 0.01, i, f"{bc[n]['pct']:.0f}%  ({bc[n]['dam_count']} dams)", va="center", fontsize=9, color=INK)
    ax.set_yticks(y, names)
    ax.invert_yaxis()
    ax.set_xlabel("Million m³")
    ax.set_xlim(0, cap.max() * 1.25)
    ax.legend(fontsize=8.5, loc="lower right")
    b = enso["basin"]
    frame(fig, ax, f"Reservoir storage by country - {b['n_dams']} monitored dams, {b['pct_capacity_all_dams']:.0f}% full basin-wide",
          f"Ensemble forecast: {enso['forecast']['direction']} to ~{enso['forecast']['median_end_pct']:.0f}% by {enso['forecast']['horizon_date']} (median scenario). "
          f"Source: IWMI reservoir monitoring (satellite area->volume + DWS gauges), as of {enso['as_of']}.")
    save(fig, "reservoirs-by-country.png")

    # -- 3. Loskop seasonal profile
    sp = pd.DataFrame(losk["seasonal_profile"])
    x = np.arange(12)
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.fill_between(x, sp["min"], sp["max"], color=SKY, alpha=0.18, label="Min-max (all years)")
    ax.fill_between(x, sp.q1, sp.q3, color=SKY, alpha=0.4, label="Interquartile range")
    ax.plot(x, sp["median"], color=DARK, lw=2.2, marker="o", ms=4, label="Median")
    ax.axhline(100, color=INK, lw=0.8, ls=":")
    ax.set_xticks(x, sp.month)
    ax.set_ylabel("% of capacity")
    ax.set_ylim(30, 115)
    ax.legend(fontsize=8.5, loc="lower left", ncol=3)
    ld = losk["dam"]
    frame(fig, ax, f"Seasonal storage profile - {ld['name']} Dam, {ld['river']} River ({ld['main_use'].lower()} supply)",
          "The normal annual cycle: full after summer rains, drawn down for irrigation through Sep-Nov. A level below the band for the month is the early warning. "
          f"Source: IWMI DT API reservoir analytics, as of {TODAY}.")
    save(fig, "reservoirs-loskop-seasonal.png")


# --------------------------------------------------------------------------- water accounting


def water_accounting():
    bal = fetch_csv("/chatbot/balance/annual?basin=limpopo&return_type=csv&start=2003&end=2024", "balance_annual.csv", comment="#")
    lu = fetch_json("/wa_accounting/landuse?basin_code=LIMPOPO", "wa_landuse.json")
    wa = fetch_csv("/csv/water_acc_data/1/csv", "water_acc_1.csv", parse_dates=["date"])

    # -- 1. annual balance
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.bar(bal.year - 0.2, bal.rainfall_km3, 0.4, color=BLUE, label="Rainfall (inflow)")
    ax.bar(bal.year + 0.2, bal.total_et_km3, 0.4, color=GREEN, label="Total evapotranspiration (consumed)")
    ax.plot(bal.year, bal.outflow_km3, color=ORANGE, lw=2, marker="o", ms=4, label="River outflow to the sea")
    ax.set_ylabel("km³ per year")
    ax.legend(fontsize=8.5, loc="upper left", ncol=3)
    r, e, o = bal.rainfall_km3.mean(), bal.total_et_km3.mean(), bal.outflow_km3.mean()
    frame(fig, ax, "Basin water balance 2003-2024 - what comes in, what is consumed, what leaves",
          f"Averages: rainfall {r:.0f} km³/yr, ET {e:.0f} km³/yr ({e / r:.0%} of rainfall), outflow {o:.1f} km³/yr ({o / r:.1%}). "
          f"In dry years ET exceeds rainfall - the landscape draws on storage. Source: WA+ accounts via IWMI DT API (/chatbot/balance/annual), as of {TODAY}.")
    save(fig, "wa-annual-balance.png")

    # -- 2. ET share by land-use class (WA+ sheet 1)
    classes = ["Protected", "Utilized", "Modified", "Managed"]
    colors = [GREEN, SKY, YELLOW, ORANGE]
    wa["year"] = wa.date.dt.year
    full = wa.groupby("year").size()
    yrs = [y for y in full.index if full[y] == 12]
    parts = {}
    for c in classes:
        cols = [k for k in wa.columns if k.startswith("OUTFLOW_ET LANDSCAPE_" + c) or k.startswith("OUTFLOW_ET UTILIZED FLOW_" + c)]
        parts[c] = wa[wa.year.isin(yrs)].groupby("year")[cols].sum().sum(axis=1)
    inc = [k for k in wa.columns if k.startswith("OUTFLOW_ET INCREMENTAL_Manmade")]
    parts["Managed"] = parts["Managed"] + wa[wa.year.isin(yrs)].groupby("year")[inc].sum().sum(axis=1)
    df = pd.DataFrame(parts)
    share = df.div(df.sum(axis=1), axis=0) * 100
    fig, ax = plt.subplots(figsize=(10, 4.6))
    bottom = np.zeros(len(share))
    for c, col in zip(classes, colors):
        ax.bar(share.index, share[c], bottom=bottom, color=col, width=0.8, label=f"{c} land use")
        bottom += share[c].values
    ax.set_ylim(0, 100)
    ax.set_xticks(list(share.index)[::2])
    ax.set_ylabel("Share of basin ET (%)")
    ax.legend(fontsize=8.5, loc="upper center", ncol=4, bbox_to_anchor=(0.5, -0.12))
    m = share["Managed"].mean()
    frame(fig, ax, "Who consumes the water - ET by WA+ land-use class",
          f"Managed water use (irrigation, reservoirs, urban) averages {m:.1f}% of basin ET but is the only part that can be reallocated. "
          f"Utilized land (rangeland, dryland crops) dominates. Source: WA+ resource-base sheet via IWMI DT API, {yrs[0]}-{yrs[-1]}.")
    save(fig, "wa-et-by-landuse.png")

    # -- 3. land-use area share
    rows = pd.DataFrame(lu["rows"])
    fig, ax = plt.subplots(figsize=(10, 3.6))
    order = ["protected_landuse", "utilized_landuse", "modified_landuse", "managed_wateruse"]
    rows = rows.set_index("class_key").loc[order].reset_index()
    left = 0
    for (_, r), col in zip(rows.iterrows(), colors):
        ax.barh(0, r.percent_of_basin, left=left, color=col, height=0.6)
        lab = f"{r.class_label.replace(' Landuse', '').replace(' Wateruse', ' water use')}\n{r.percent_of_basin:.1f}% · {r.area_km2 / 1000:,.0f}k km²"
        if r.percent_of_basin > 8:
            ax.text(left + r.percent_of_basin / 2, 0, lab, ha="center", va="center", fontsize=8.5, color="white", fontweight="bold")
        else:
            ax.text(left + r.percent_of_basin / 2, 0.42, lab, ha="center", va="bottom", fontsize=8, color=INK)
        left += r.percent_of_basin
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.5, 0.9)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_xlabel("% of basin area")
    frame(fig, ax, f"Basin area by WA+ land-use class - {lu['basin']['basin_name']}",
          "Managed water use is under 2 % of the area yet carries the whole allocation debate. "
          f"Source: IWMI DT API /wa_accounting/landuse, as of {TODAY}.")
    save(fig, "wa-landuse-share.png")


# --------------------------------------------------------------------------- irrigation


def irrigation():
    meta = pd.DataFrame(fetch_json("/chatbot/irrigation_metadata", "irrigation_metadata.json"))
    wa = fetch_csv("/csv/water_acc_data/1/csv", "water_acc_1.csv", parse_dates=["date"])
    losk = fetch_json("/visualizations/reservoir_analytics?gdw_id=2047", "analytics_loskop.json")

    # -- 1. schemes: command vs currently irrigated
    m = meta.copy()
    m["command_area_ha"] = pd.to_numeric(m.command_area_ha)
    m["currently_irrigated_ha"] = pd.to_numeric(m.currently_irrigated_ha)
    m = m[~m.main_water_source.str.contains("Save", na=False)]  # Save basin schemes are outside the Limpopo
    m = m.sort_values("command_area_ha")
    y = np.arange(len(m))
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.barh(y, m.command_area_ha, color=GREY, height=0.62, label="Command area (designed)")
    ax.barh(y, m.currently_irrigated_ha, color=TEAL, height=0.62, label="Currently irrigated")
    for i, (_, r) in enumerate(m.iterrows()):
        ax.text(r.command_area_ha + 600, i, f"{r.currently_irrigated_ha / r.command_area_ha:.0%} · {r.primary_crops.split(',')[0]}", va="center", fontsize=8, color=INK)
    ax.set_yticks(y, [f"{a} ({c[:3].upper() if c != 'South Africa' else 'ZA'})" for a, c in zip(m.scheme_area, m.country)])
    ax.set_xlabel("hectares")
    ax.set_xlim(0, m.command_area_ha.max() * 1.45)
    ax.legend(fontsize=8.5, loc="lower right")
    frame(fig, ax, "Major irrigation schemes in the basin - designed vs currently irrigated area",
          "Label = utilisation and main crop. The Mozambican lowland schemes (Lower Limpopo, Chókwè) dominate area; Loskop is the largest in South Africa. "
          f"Source: IWMI DT API irrigation scheme metadata, as of {TODAY}.")
    save(fig, "irrigation-schemes.png")

    # -- 2. managed (irrigated) ET seasonality vs rainfall
    wa["month"] = wa.date.dt.month
    man = [k for k in wa.columns if ("_Managed" in k and k.startswith("OUTFLOW_ET")) or k.startswith("OUTFLOW_ET INCREMENTAL_Manmade")]
    mm = wa.groupby("month").agg(rain=("INFLOW_PRECIPITATION_Rainfall", "mean"))
    mm["managed_et"] = wa.groupby("month")[man].mean().sum(axis=1)
    inc = wa.groupby("month")[[k for k in man if "INCREMENTAL" in k]].mean().sum(axis=1)
    mm["blue_et"] = inc
    x = np.arange(12)
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.bar(x, mm.rain / mm.rain.max() * 100, color=BLUE, alpha=0.35, width=0.8, label="Basin rainfall (index, max = 100)")
    ax2 = ax.twinx()
    ax2.plot(x, mm.managed_et, color=ORANGE, lw=2.2, marker="o", ms=4, label="ET from managed (irrigated) land")
    ax2.plot(x, mm.blue_et, color=DARK, lw=1.8, ls="--", marker="s", ms=3.5, label="of which supplied by withdrawals (blue ET)")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Rainfall index")
    ax2.set_ylabel("Mean monthly ET, managed land (WA+ units)")
    ax2.grid(False)
    for s in ("top",):
        ax2.spines[s].set_visible(False)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=8.5, loc="upper center", ncol=3, bbox_to_anchor=(0.5, -0.12))
    frame(fig, ax, "When irrigation draws water - managed-land ET against the rainfall calendar",
          "Irrigated ET stays high into the dry winter while rainfall collapses: that gap is the water that must come from rivers, dams and boreholes. "
          f"Source: WA+ monthly accounts via IWMI DT API, 2003-2021 means.")
    save(fig, "irrigation-managed-et.png")

    # -- 3. Loskop annual mean storage (supply security for the largest SA scheme)
    a = pd.DataFrame(losk["annual_summary"]).sort_values("year")
    a["max_pct"] = a.max_vol / losk["dam"]["capacity_mcm"] * 100
    fig, ax = plt.subplots(figsize=(10, 4.0))
    ax.bar(a.year, a.mean_pct, color=np.where(a.min_pct < 50, ORANGE, TEAL), width=0.7, label="Annual mean storage")
    ax.errorbar(a.year, a.mean_pct, yerr=[a.mean_pct - a.min_pct, a.max_pct - a.mean_pct], fmt="none", ecolor=INK, elinewidth=1, capsize=3, label="Annual min-max")
    ax.axhline(50, color=ORANGE, lw=1, ls=":")
    ax.set_ylim(0, 115)
    ax.set_ylabel("% of capacity")
    ax.legend(fontsize=8.5, loc="lower left", ncol=2)
    ld = losk["dam"]
    frame(fig, ax, f"Supply security - {ld['name']} Dam storage by year (feeds the Loskop Irrigation Scheme)",
          "Orange = a year in which the dam dipped below 50 %. Irrigation quotas are cut when storage falls through the dry season. "
          f"Source: IWMI DT API reservoir analytics, as of {TODAY}.")
    save(fig, "irrigation-loskop-supply.png")


if __name__ == "__main__":
    for fn in (floods, droughts, eflows, reservoirs, water_accounting, irrigation):
        print(f"[{fn.__name__}]")
        fn()
    print("done")
