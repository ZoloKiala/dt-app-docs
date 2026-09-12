---
title: Floods
---

# Floods

## The question

A disaster-management officer or basin authority needs three answers as an
event develops: **is a flood coming, where will the rivers peak, and who and
what is exposed** — and afterwards, **how does this event compare with the past**.

## Data you will use

| Dataset | Where in the catalogue | What it tells you |
| --- | --- | --- |
| **GPM IMERG Precipitation Rate (Daily)** | Flood Monitoring & Early Warning → Real-Time Flood Detection | Yesterday's satellite rainfall — the trigger |
| **Accumulated Precipitation (10-day)** · **Precipitation Prob. > 50 / 150 / 300 mm (10-day)** | → Discharge Forecasting (GloFAS) | How much rain is forecast, and how likely extreme totals are |
| **Flood Summary Days 1–3 / 4–10 / 11–30** | → Discharge Forecasting (GloFAS) | Where river flooding is forecast, by lead time |
| **Reporting Points (% Exceedance)** · **5-Year / 20-Year Exceedance Prob. (30-day)** | → Discharge Forecasting (GloFAS) | Probability that river points exceed flood thresholds |
| **GloFAS Discharge Forecast – SWAT Channels** · **– Verified Gauges** | → Discharge Forecasting (GloFAS) | Forecast hydrographs at channels and gauges (click for a chart) |
| **MODIS NRT Flood (1-Day)** · **VIIRS NRT Flood (1-Day)** | → Real-Time Flood Detection | Water actually observed on the ground today |
| **Rapid Flood Mapping (1 km extent)** · **Rapid Impact Assessment** | → Impact & Inundation | Event extent and first impact estimate |
| **100-year Flood Hazard (Climatology)** · **20 / 50-Year Flood Lines – Lower Limpopo (LIMIS)** | → Flood Hazard & Exposure | Where floods are *expected* to reach — planning baselines |
| **MODIS Flood Frequency (2001–2024)** · **MODIS Flood Exposure – Longterm** · **Year 2000 Flood Inundation Boundaries (LIMIS)** | → Flood Hazard & Exposure | Historical footprint, including the landmark 2000 flood |
| **Population** · **Settlements (LIMIS)** | Socio-Economic Profile | Who is in the way |
| **Dams & Reservoirs Basin Level Estimates** | → Supporting Hydrological Data | Storage that may attenuate — or release — the flood wave |

## Walkthrough

**Before the event — outlook**

1. **Explore data → `Accumulated Precipitation (10-day)` → Add to the map**, then
   add **Precipitation Prob. > 150 mm (10-day)**. Large probabilities over the
   upper catchments (Botswana / Gauteng–Limpopo headwaters) mean the lower basin
   should prepare.
2. Add **Flood Summary Days 1–3**, then **4–10**, and step through them: the
   flood signal should propagate downstream as lead time grows.
3. Add **Reporting Points (% Exceedance)** and click a point on the map. The
   **Feature Information** panel gives the exceedance probability; use
   **Show Raw Data** for the numbers.

**During the event — observe and confirm**

4. Add **GPM IMERG Precipitation Rate (Daily)** and **MODIS NRT Flood (1-Day)**.
   Where rain fell yesterday and standing water appears today, the forecast is
   verifying.
5. Add **GloFAS Discharge Forecast – Verified Gauges** and click the gauge nearest
   the community of concern: the chart shows forecast discharge against
   thresholds.

**Exposure**

6. Add **Population** and **Settlements (LIMIS)** beneath the flood layers
   (drag to reorder in the Workbench, lower the flood layer's opacity). Use
   **Compare** with **100-year Flood Hazard (Climatology)** to see whether the
   forecast footprint is within or beyond the design baseline.

**After the event**

7. Add **Rapid Flood Mapping (1 km extent)** and **Rapid Impact Assessment**, and
   compare the mapped extent with **MODIS Flood Frequency (2001–2024)** and the
   **Year 2000 Flood Inundation Boundaries (LIMIS)** to rank the event
   historically.
8. Capture the key scenes as a **Story** and **Share / Print** for the situation
   report.

## Reading the result

- **Probability layers are not extents.** *Flood Summary* and *Exceedance*
  layers say how *likely* flooding is, not where water will stand — pair them
  with the NRT observation layers for actual extent.
- Consistency across sources is the strongest signal: rainfall forecast →
  discharge exceedance → observed NRT water, all lining up along one reach.
- **Flood Lines (LIMIS)** for the Lower Limpopo are engineering baselines; a
  forecast footprint beyond the 50-year line is exceptional.

## Limits to keep in mind

- **IMERG shows nothing on dry days** — an empty layer is not a broken layer. It
  is also near-real-time with a lag; check the date in the timeline.
- NRT flood detection from MODIS/VIIRS is **daily, optical**, and misses water
  under cloud and vegetation; use it to confirm, not to rule out.
- GloFAS is a **global model** downscaled to basin channels; verified gauges are
  the anchor — trust channel forecasts more where a gauge agrees.
- Several LIMIS layers are **historical snapshots** (e.g. the 2000 flood); they
  do not update.

## Related

[Reservoir monitoring](reservoirs.md) · [Droughts](droughts.md) ·
[Map Tools — Compare](../guide/map-tools.md#compare) ·
[Feature information](../guide/data-catalogue.md#feature-information)
