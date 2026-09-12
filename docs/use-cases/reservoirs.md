---
title: Reservoir monitoring
---

# Reservoir monitoring

## The question

A dam operator, a bulk-water utility or LIMCOM staff want to know **how full
the basin's reservoirs are, how each has trended through the season, and what
inflows the coming weeks are likely to bring** — including for dams with no
telemetry, by watching them from space.

## Data you will use

| Dataset | Where in the catalogue | What it tells you |
| --- | --- | --- |
| **Dams and Reservoirs (LIMIS)** | Water Resources → Reservoirs and Storage | The registered dams: location, name, attributes |
| **Dams & Reservoirs Basin Level Estimates** | same group (also under Flood Monitoring → Supporting Hydrological Data) | Estimated storage level per dam, basin-wide |
| **Reservoir Levels – Water Area Timeseries** | same group | Water surface area over time, derived from satellite — a proxy for level, works for any dam |
| **Reservoir Levels – DEA by Original ID** · **– Aggregated by Channel** · **– Yearly Aggregated by Channel** | same group | The same signal per waterbody, per river channel, and as yearly summaries |
| **Waterbodies from DEA (Raster WMS)** · **Water Observations – All-Time Frequency** | Water Resources → Surface Waterbodies | Where water is normally present and how often — the reference footprint |
| **Rolling Monthly GeoMAD (Sentinel-2)** | Satellite Images | A cloud-free monthly image to inspect a reservoir by eye |
| **Streamflow Gauging Stations (LIMIS)** · **Verified Monitoring Stations (LIMIS)** · **SWAT and Observed Sites** | Water Resources → Streamflow Monitoring | Inflow gauges upstream of the dam |
| **GloFAS Discharge Forecast – SWAT Channels** | Flood Monitoring → Discharge Forecasting | Forecast inflow for the channel feeding the dam |
| **Reservoir forecast chart** | Click a forecast-enabled reservoir | Forecast level for the coming period |

## Walkthrough

1. **Explore data → search `Reservoir` → add `Dams & Reservoirs Basin Level
   Estimates`**, then **Dams and Reservoirs (LIMIS)** for names. Use **Ideal
   Zoom**.
2. **Click a dam.** The **Feature Information** panel gives its attributes and,
   where forecasting is enabled, a **reservoir forecast chart**. Use **Show Raw
   Data** or the CSV/JSON download for the table.
3. Add **Reservoir Levels – Water Area Timeseries** and click the same reservoir:
   the chart shows water-surface area through time. A shrinking area through
   the dry season and recovery after rains is the normal cycle; a multi-year
   decline is the concern.
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

## Reading the result

- **Water area is a proxy for volume.** Convert with the dam's area–capacity
  curve where you have one; otherwise read it as a *relative* indicator and
  trend.
- Compare the current footprint with the **All-Time Frequency** layer: the gap
  between where water *usually* is and where it is *now* is the visual storage
  deficit.
- **Yearly aggregates** smooth out seasonality and expose structural decline
  from sedimentation, over-allocation or drought.

## Limits to keep in mind

- Satellite water-area series are **optical**: cloud gaps in the wet season and
  narrow, tree-lined arms of a reservoir reduce accuracy.
- Area does not capture **depth**; a shallow reservoir can look full while
  holding little.
- Level *estimates* and forecasts are **modelled** where telemetry is absent —
  they replace nothing where a gauge exists.
- Forecast charts require a **signed-in session**.

## Related

[Floods](floods.md) · [Environmental flows](eflows.md) ·
[Water accounting](water-accounting.md) ·
[Map Tools — Compare](../guide/map-tools.md#compare)
