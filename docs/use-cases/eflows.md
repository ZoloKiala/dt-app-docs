---
title: Environmental flows
---

# Environmental flows (e-flows)

## The question

An ecologist, a river-basin regulator or a dam operator needs to know **whether
each reach of the Limpopo is receiving the flow its ecosystem needs**, where
flows have fallen below alert levels, and **how a change in releases or
abstraction would alter the ecological risk**.

## Data you will use

| Dataset | Where in the catalogue | What it tells you |
| --- | --- | --- |
| **E-flow Monitoring and Forecasting** | Drought Monitoring & Risk Assessment → Hydrological Drought & E-flows | Modelled present flow vs. the environmental-flow requirement, per site, with a forecast — click for a chart |
| **Eflow Alert Levels** | same group | Current alert class at each monitored site |
| **Eflow Warnings** · **E-Flow Warning Status (LIMIS)** | same group; Ecosystems → E-Flow Modeling & Risk | Reaches currently in warning |
| **E-flow Risk Regions** | same group | The ecological regions used for risk assessment |
| **SWAT Modelled Discharge** · **SWAT and Observed Sites** | Water Resources → Streamflow Monitoring | Present-day modelled flow and the gauges it is checked against |
| **SWAT Incremental Contributions** | Water Use Monitoring and Analysis → Basin Water Balance | How much flow each sub-catchment adds to the river |
| **Aquatic Ecoregions (LIMIS)** · **Suitability Class / Suitability Map layers** | Ecosystems → Ecological Monitoring | Ecological context for interpreting a deficit |
| **SWAT Extraction Tool** | Map tools (bottom right) | Query modelled flows for a channel and date range; the **PROBFLO** tab links flow to ecological risk |

## Walkthrough

1. **Explore data → search `E-flow` → add `E-flow Monitoring and Forecasting`.**
   Sites appear along the river network.
2. Add **Eflow Alert Levels** on top. The colour tells you the current class;
   start with the worst.
3. **Click a site.** The chart opens with four series — **SWAT Present Flow**,
   **E-Flow** (the requirement), **Availability Surplus** and **Deficit**. Hover
   any point to read values; drag across the chart or pick start and end dates to
   zoom to a season.
4. Add **SWAT Incremental Contributions** to understand *why*: a deficit at a
   downstream site with healthy upstream contributions points to abstraction or
   storage in between, rather than a dry catchment.
5. Add **SWAT and Observed Sites** and compare modelled flow with the nearest
   gauge in the chart — this is how much to trust the model at that reach.
6. **Scenario testing.** Open the **SWAT Extraction Tool** (bottom-right icon).
   Choose the **Flow Type** (e.g. *Natural Flows*), enter the **Channel ID** from
   the site you clicked, set the **Start / End Date**, and **FETCH DATA**. Use the
   **MAP** tab to confirm the channel, **TABLE** for the numbers, and **PROBFLO**
   to see the ecological risk category the flow implies.
7. Add **Aquatic Ecoregions (LIMIS)** and the **Suitability** layers to weigh a
   deficit by the sensitivity of the reach.
8. Capture the alert map and the chart as a **Story** for the e-flow committee.

## Reading the result

- **Deficit** is the operational number: how far below the requirement the
  river is, in flow units, for how long. Short deficits in the dry season may be
  natural; **prolonged deficits in the wet season** are the red flag.
- Forecast series let you act before the alert class changes — a falling
  present-flow forecast crossing the E-Flow line is your lead time.
- Use **Incremental Contributions** to attribute the shortfall to a
  sub-catchment, which is where an intervention (release, abstraction limit)
  would act.

## Limits to keep in mind

- All flows here are **SWAT model outputs**, calibrated against gauges. Where the
  nearest gauge disagrees with the model, weight the gauge.
- E-flow requirements are themselves the product of an assessment method; the
  **PROBFLO** risk categories are probabilistic, not thresholds of harm.
- Site charts and the SWAT Extraction Tool call the IWMI data API and **require
  a signed-in session**.

## Related

[Droughts](droughts.md) · [Reservoir monitoring](reservoirs.md) ·
[Map Tools — SWAT Extraction Tool](../guide/map-tools.md#swat-extraction-tool)
