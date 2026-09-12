---
title: Droughts
---

# Droughts

## The question

An agricultural extension officer, a water utility or a basin committee wants
to know **whether a drought is developing, how severe it is compared with past
years, which sectors are at risk, and what the coming season looks like**.

Drought builds in stages, and the catalogue is organised the same way:
meteorological (rain), then soil and vegetation stress, then hydrological
(rivers and groundwater), then sectoral risk.

## Data you will use

| Stage | Dataset | Where in the catalogue |
| --- | --- | --- |
| Rain deficit | **CHIRPS Historical Rainfall** · **Number of Rainy Days** · **Rainfall Anomalies** | Drought Monitoring & Risk Assessment → Meteorological Drought |
| Rain deficit (indices) | **Drought Hazard – SPEI 3-month / 6-month / 12-month (2010–2021)** | → Meteorological Drought |
| Soil | **SMAP Surface Soil Moisture (L4, Daily)** · **SMAP Root Zone Soil Moisture (L4, Daily)** · **SMAP-Sentinel High-Res Soil Moisture (1 km)** | → Soil Moisture |
| Vegetation | **The Vegetation Condition Index (VCI)** · **MODIS NDVI 16-Day Composite** · **VIIRS NDVI 8-Day Composite** · **NDVI Anomaly (DEA)** | → Vegetation & Crop Stress |
| Water stress | **Evaporative Stress Index Africa** | → Evaporative Stress & Water Use |
| Rivers | **E-flow Monitoring and Forecasting** · **Eflow Alert Levels** · **Eflow Warnings** | → Hydrological Drought & E-flows |
| Groundwater | **Groundwater Drought Risk (Updated)** · **Groundwater Level Points** | Water Resources → Groundwater |
| Risk by sector | **Drought Risk – Agriculture / Food & Nutrition / Water Sector (3, 6, 12-month)** | → Sectoral Drought Risk |
| Outlook | **Limpopo Rainfall Anomaly Forecast** · **Limpopo Temperature Anomaly Forecast** · **Seasonal Forecast Anomaly (7-month)** · **Sub-Seasonal Outlook (5–6 weeks)** | Natural Basin Characteristic → Climate; Flood Monitoring → Seasonal & Sub-Seasonal |

## Walkthrough

1. **Start with vegetation — the most visible signal.** Explore data → search
   `VCI` → add **The Vegetation Condition Index (VCI)**. Use the timeline to
   compare this month with the same month in previous years; VCI is already
   normalised against history, so low values mean *worse than usual*, not just
   *dry season*.
2. **Confirm with NDVI Anomaly (DEA)** (add it, use **Compare** against VCI).
   Agreement between two independent vegetation products is a robust drought
   signal.
3. **Check the cause — rainfall.** Add **CHIRPS Historical Rainfall** and step
   the timeline back through the season; add **Rainfall Anomalies** and click a
   station circle for its chart. Then add **Drought Hazard – SPEI 3-month** for
   the standardised deficit.
4. **Check the soil.** Add **SMAP Root Zone Soil Moisture (L4, Daily)**. Root-zone
   deficit, not just surface dryness, is what limits crops.
5. **Check the rivers.** Add **Eflow Warnings** and **Eflow Alert Levels**, then
   **E-flow Monitoring and Forecasting** and click a site for its chart. Rivers
   below environmental-flow levels mark the transition to hydrological drought
   (see [Environmental flows](eflows.md)).
6. **Translate to risk.** Add **Drought Risk – Agriculture (3-month)** and
   **Drought Risk – Water Sector (3-month)** with **Population** underneath to
   see where stressed conditions meet people.
7. **Look ahead.** Add **Limpopo Rainfall Anomaly Forecast** and the
   **Seasonal Forecast Anomaly (7-month)**: a dry outlook on top of an existing
   deficit is the trigger for early action.
8. Save the sequence as a **Story** — one scene per stage makes a compelling
   briefing.

## Reading the result

- **Convergence matters.** One index can mislead; VCI + NDVI anomaly + SPEI +
  soil moisture all pointing the same way is a drought.
- Use the **3-, 6- and 12-month** SPEI and risk layers together: 3-month
  captures a failed season, 12-month a multi-year deficit that hits reservoirs
  and groundwater.
- Groundwater drought **lags** surface drought by months; rising risk in the
  groundwater layers signals a long recovery even after rain returns.

## Limits to keep in mind

- **SPEI hazard layers cover 2010–2021** — a climatology baseline, not a live
  index. Use CHIRPS and the anomaly forecasts for the current season.
- NDVI/VCI respond to **any** vegetation change (harvest, fire, land clearing),
  not only drought — cross-check with rainfall.
- SMAP is coarse (the 1 km SMAP-Sentinel product is sharper but less frequent).
- Seasonal forecasts are **probabilistic anomalies**; read them as odds, not
  predictions.

## Related

[Environmental flows](eflows.md) · [Irrigation water use](irrigation.md) ·
[Workbench — time series](../guide/workbench.md#time-series)
