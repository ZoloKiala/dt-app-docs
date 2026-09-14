---
title: Reservoir monitoring
---

# Reservoir monitoring

## The question

A dam operator, a bulk-water utility or LIMCOM staff want to know **how full
the basin's reservoirs are, how each has trended through the season, and what
inflows the coming weeks are likely to bring** — including for dams with no
telemetry, by watching them from space.

| Who | Decision | Cadence |
| --- | --- | --- |
| Dam operators and national water authorities (DWS, ZINWA, ARA-Sul, WUC) | Release schedules, irrigation quotas, spill preparedness | Weekly |
| Bulk-water and municipal utilities | Restriction levels, alternative sources | Monthly; weekly below 30 % |
| Irrigation boards | Seasonal allocation (typically set in Oct) | Seasonal |
| LIMCOM | Basin-wide storage reporting, drought / flood coordination | Monthly |

!!! abstract "At a glance — 14 September 2026"
    - **231 dams** with storage estimates (445 dams in the layer); **84 % full basin-wide** (7,107 of 8,454 Mm³).
    - By country: **Botswana 90 %** (10 dams) · **Mozambique 91 %** (4) · **South Africa 82 %** (147) · **Zimbabwe 75 %** (70).
    - Status: 128 *Full*, 25 *Adequate*, 20 *Low*, 56 *Critical / Empty* — the critical ones are mostly small farm dams, but **Middle Letaba (180 Mm³) stood at 10.5 %** in July 2026.
    - **Outlook:** the ensemble forecast has basin storage **falling ~15 points to ~70 % by 30 November 2026** before the rains.
    - **Massingir** (2,260 Mm³, the largest) is at 90 %; **Loskop** at 104 %; **De Hoop** at 120 % (over full supply).

## How the workflow fits together

```mermaid
flowchart TD
    A[Dams & Reservoirs<br/>Basin Level Estimates] --> B{Status per dam<br/>Full / Adequate / Low / Critical}
    B --> C[Click dam:<br/>storage history + forecast chart]
    C --> D[Cross-check<br/>Reservoir Levels – Water Area Timeseries<br/>Rolling Monthly GeoMAD]
    D --> E[Inflow outlook<br/>Streamflow Gauging Stations<br/>GloFAS Discharge Forecast – SWAT Channels]
    E --> F{Low & falling?}
    F -- yes --> G[Restrictions · quota cuts<br/>see Droughts]
    F -- no --> H{Full & inflow rising?}
    H -- yes --> I[Spill / pre-release<br/>see Floods]
    H -- no --> J[Routine report<br/>Story + Share]
```

## Data you will use

| Dataset | Where in the catalogue | What it tells you |
| --- | --- | --- |
| **Dams and Reservoirs (LIMIS)** · **Dam locations** | Water Resources → Reservoirs and Storage / Water Infrastructure | The registered dams: location, name, attributes |
| **Dams & Reservoirs Basin Level Estimates** | same group (also under Flood Monitoring → Supporting Hydrological Data) | Estimated storage (%, Mm³), status class, method and confidence per dam — click for the storage chart and forecast |
| **Reservoir Levels – Water Area Timeseries** | same group | Water surface area over time, derived from satellite — a proxy for level, works for any dam (104 reservoirs) |
| **Reservoir Levels – DEA by Original ID** · **– Aggregated by Channel** · **– Yearly Aggregated by Channel** | same group | The same signal per waterbody, per river channel (1,424 channels), and as yearly summaries |
| **Waterbodies from DEA (Raster WMS)** · **Water Observations – All-Time Frequency** | Water Resources → Surface Waterbodies | Where water is normally present and how often — the reference footprint |
| **Rolling Monthly GeoMAD (Sentinel-2)** | Satellite Images | A cloud-free monthly image to inspect a reservoir by eye |
| **Streamflow Gauging Stations (LIMIS)** · **Verified Monitoring Stations (LIMIS)** · **SWAT and Observed Sites** | Water Resources → Streamflow Monitoring | Inflow gauges upstream of the dam (183 real-time stations) |
| **GloFAS Discharge Forecast – SWAT Channels** | Flood Monitoring → Discharge Forecasting | Forecast inflow for the channel feeding the dam |
| **Hydropower Evaporation Footprint (Africa)** · **Hydropower Open Water Surface (Africa)** | Water Use Monitoring → Sectoral Demand | Evaporation losses from the reservoir surface |

### How storage is estimated

Each dam in **Basin Level Estimates** carries a `method` and a confidence tier;
read them in the feature-info panel before quoting a number.

| Confidence | Method | Typical error |
| --- | --- | --- |
| **High** (Tier 1) | Gauged level or satellite altimetry with a dam-specific area–capacity curve (Massingir: R² 0.997, MAPE 1.8 %) | ± a few % |
| **Medium** (Tier 2) | Truncated-cone geometry, or capacity fraction with known dam height | ± 10 % |
| **Low** (Tier 3) | Capacity-fraction / empirical power law from surface area alone | ± 20 % or more |
| **No data** | No storage model (214 of the 445 dams) | — |

## Walkthrough

1. **Explore data → search `Reservoir` → add `Dams & Reservoirs Basin Level
   Estimates`**, then **Dams and Reservoirs (LIMIS)** for names. Use **Ideal
   Zoom**. Symbol colour is the status class.
2. **Click a dam.** The **Feature Information** panel gives current %, volume,
   capacity, method, confidence and the **storage chart with forecast**
   (Figure 1). Use **Show Raw Data** or the CSV download for the table.
3. Add **Reservoir Levels – Water Area Timeseries** and click the same reservoir:
   the chart shows water-surface area through time. A shrinking area through
   the dry season and recovery after rains is the normal cycle (Figure 3); a
   multi-year decline is the concern.
4. For a **long-term view**, add **Reservoir Levels – Yearly Aggregated by
   Channel** and compare years side by side.
5. **See it.** Add **Rolling Monthly GeoMAD (Sentinel-2)** and step the timeline
   to two dates a year apart; use **Compare** (left/right) to watch the shoreline
   move. Add **Water Observations – All-Time Frequency** to see the full-supply
   footprint the reservoir *should* fill.
6. **Inflows.** Add **Streamflow Gauging Stations (LIMIS)** and **GloFAS Discharge
   Forecast – SWAT Channels**; click the channel upstream of the dam for the
   forecast hydrograph. Rising forecast inflow against a low reservoir is good
   news; against a full one it is a spill risk (see [Floods](floods.md)).
7. Capture a scene per reservoir as a **Story** for the operations meeting.

## Reading the charts

<figure markdown="span">
  ![Massingir storage history and forecast](../assets/charts/reservoirs-massingir-storage.png)
  <figcaption>Figure 1: The chart you get when you click Massingir Dam — estimated storage since 2002, observed points, and the ensemble forecast to the end of the dry season.</figcaption>
</figure>

- Massingir went from **4 % (2003, 2005) to 110 % (2008)** — the basin's largest
  reservoir can empty and refill within a few seasons; a 20-month drawdown
  (2002–06) is the historical worst case.
- Since 2021 it has cycled between **60 and 105 %**, and the median forecast
  takes it to **~73 % by November 2026** — comfortable, but the fan's lower
  bound (~70 %) is what a dry start to the season would give.
- Blue dots are the **observations the estimate is calibrated against**; where
  the line runs without dots (2010–13, 2016–19) the estimate is interpolated
  and should be read as a trend, not a value.

<figure markdown="span">
  ![Storage by country](../assets/charts/reservoirs-by-country.png)
  <figcaption>Figure 2: Capacity and current storage of monitored dams by country. Percentages are volume-weighted.</figcaption>
</figure>

- **South Africa holds 43 % of monitored capacity** (3,620 Mm³ in 147 dams);
  **Mozambique's 4 dams** hold 29 %, almost all of it Massingir.
- Zimbabwe's dams are the **lowest at 75 %** and mostly Low-confidence
  estimates — verify against ZINWA bulletins before acting.
- A country average hides individual dams: South Africa's 82 % includes
  Middle Letaba at 10 % and Eerste Poort at 49 %.

<figure markdown="span">
  ![Loskop seasonal storage profile](../assets/charts/reservoirs-loskop-seasonal.png)
  <figcaption>Figure 3: Loskop Dam's storage by calendar month across all years — the "normal band" against which a current reading is judged.</figcaption>
</figure>

- The normal cycle: **full in Feb–May, drawn down to ~85–90 % by Oct–Nov** as
  irrigation quotas are used, refilled by the summer rains.
- A reading **below the interquartile band for its month** is the early
  warning; below the min–max envelope (as in 2016, when Loskop reached 42 %) is
  a supply emergency.
- Compare the current dot on the portal's chart with this band rather than
  with last month: a fall from 100 % to 92 % in October is normal, the same
  fall in April is not.

## Indicators and what to do

| Indicator | Where | Threshold | Typical action |
| --- | --- | --- | --- |
| Storage class | *Basin Level Estimates* symbol | *Low* < 25 %, *Critical* < 10 % | Restrictions (Low); emergency supply (Critical) |
| Storage vs seasonal band | Click dam → storage chart | Below interquartile band for the month | Review quotas; check inflow gauges |
| Forecast median at 30 Nov | Storage chart forecast | < 40 % | Cut next season's irrigation allocation |
| Forecast median at 30 Nov | Storage chart forecast | > 95 % with wet outlook | Pre-release plan; notify downstream |
| Water-area trend | *Water Area Timeseries* chart | Falling for > 3 consecutive years at the same month | Investigate sedimentation / over-allocation |
| Inflow forecast | *GloFAS – SWAT Channels* upstream | Rising through p95 into a full dam | Spill warning (see Floods) |

## Worked example — a September operations review

1. Add **Dams & Reservoirs Basin Level Estimates**. Sort by eye: most large
   dams are *Full*; **Middle Letaba** is red.
2. Click **Middle Letaba** (Vhembe): 10.5 % on 5 July 2026, 18.9 of 180 Mm³,
   method *ml_isotonic*, Medium confidence. The storage chart shows a
   multi-year decline. Click **Reservoir Levels – Water Area Timeseries** on the
   same dam — the satellite area confirms the shrinkage, independent of the
   model.
3. Add **Streamflow Gauging Stations (LIMIS)** and **GloFAS Discharge Forecast –
   SWAT Channels**; the Middle Letaba inflow channel forecasts negligible flow
   for 30 days. No relief before the rains: the **Middle Letaba scheme's
   allocation must be cut** (see [Irrigation water use](irrigation.md)).
4. Click **Massingir**: 90 %, forecast 73 % by November. Irrigation releases to
   Chókwè can continue at plan — but note the *Extreme* reporting points on the
   Elefantes below the dam are those releases (see [Floods](floods.md)).
5. Click **De Hoop**: 120 % — above full supply, so any early-season storm on
   the Steelpoort spills straight through. Flag for the flood watch.
6. Capture the three dams as a **Story**; **Share / Print** the link with the
   meeting minutes.

## Operations-report checklist

- [ ] Basin, country and sub-basin storage % with the "as of" date
- [ ] Dams *Low* / *Critical*, with method and confidence
- [ ] Dams above full supply, with inflow forecast
- [ ] Each key dam's position relative to its seasonal band
- [ ] Forecast storage at 30 November (median and dry scenario)
- [ ] Recommended quota, restriction or pre-release actions
- [ ] Story link

## Limits to keep in mind

- Satellite water-area series are **optical**: cloud gaps in the wet season and
  narrow, tree-lined arms of a reservoir reduce accuracy.
- Area does not capture **depth**; a shallow reservoir can look full while
  holding little — this is why *Low*-confidence dams carry ± 20 % error.
- Level *estimates* and forecasts are **modelled** where telemetry is absent —
  they replace nothing where a gauge exists. Readings above 100 % are real
  (water above full-supply level) but short-lived.
- The estimate date varies by dam (some are weeks old); always quote
  `current_date` from the feature info.
- Storage and forecast charts require a **signed-in session**.

## Related

[Floods](floods.md) · [Droughts](droughts.md) · [Environmental flows](eflows.md) ·
[Water accounting](water-accounting.md) ·
[Map Tools — Compare](../guide/map-tools.md#compare)
