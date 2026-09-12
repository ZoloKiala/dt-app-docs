---
title: Water accounting
---

# Water accounting

## The question

A basin planner or LIMCOM analyst needs a **consistent balance of the basin's
water**: how much arrives as rain, how much leaves as evaporation and
transpiration, how much runs off, how much is consumed by each sector, and how
that balance is changing — the evidence base for allocation between the four
riparian countries.

## Data you will use

| Term in the balance | Dataset | Where in the catalogue |
| --- | --- | --- |
| **Inflow: rainfall** | **CHIRPS Historical Rainfall** · **Rainfall Stations (LIMIS)** · **Number of Rainy Days** | Natural Basin Characteristic → Climate; Water Use Monitoring and Analysis → Water Accounting |
| **Outflow: consumption** | **Evaporation Africa** · **Transpiration Africa** · **Interception Africa** | Water Use Monitoring and Analysis → Water Accounting → Evapotranspiration & Water Use |
| **Consumption by source** | **Blue ET Africa** (irrigation / surface & groundwater) · **Green ET Africa** (rain-fed) | same group |
| **Productivity of use** | **Beneficial Fraction Africa** · **ET Fraction Africa** · **Evaporative Stress Index Africa** | same group |
| **Outflow: runoff** | **Mean Annual Runoff (LIMIS)** · **Runoff Zones (LIMIS)** · **SWAT Incremental Contributions** | Climate; → Basin Water Balance |
| **Sectoral demand** | **Hydropower Evaporation Footprint (Africa)** · **Irrigation Areas (LIMIS)** · **Water Use Time-series (Irrigated Areas) (Polygon)** | → Sectoral Demand; Water Resources; Water Use Monitoring and Analysis |
| **Transfers & storage** | **Inter-basin Water Transfers (LIMIS)** · **Dams & Reservoirs Basin Level Estimates** | Water Resources |
| **Ground truth** | **Water Balance Stations (LIMIS)** · **Evaporation Stations (LIMIS)** · **Streamflow Gauging Stations (LIMIS)** | Water Resources → Streamflow Monitoring; Climate |
| **The accounts themselves** | **Water Balance Dashboard** | Opened from the portal's menu — the compiled basin water accounts |

## Walkthrough

1. **Frame the balance.** Explore data → add **CHIRPS Historical Rainfall** and
   **Evaporation Africa**. Set the timeline to the same month on both. Rain in,
   evaporation out: where evaporation exceeds rainfall the landscape is drawing
   down storage.
2. **Split consumption.** Replace *Evaporation* with **Blue ET Africa** and
   **Green ET Africa**, using **Compare** side by side. Blue ET is water that had
   to be supplied — the managed part of the balance; Green ET is rain used in
   place.
3. **Judge productivity.** Add **Beneficial Fraction Africa**. High consumption
   with a low beneficial fraction is water lost without benefit — the first place
   to look for savings.
4. **Follow the runoff.** Add **SWAT Incremental Contributions** and **Mean
   Annual Runoff (LIMIS)**: which sub-catchments generate the river, and how does
   modelled contribution compare with the long-term mean.
5. **Attribute sectors.** Add **Irrigation Areas (LIMIS)** and **Hydropower
   Evaporation Footprint (Africa)**; for a scheme-level number, run **Water Use
   Time-series (Irrigated Areas) (Polygon)** over the scheme boundary.
6. **Account for transfers and storage.** Add **Inter-basin Water Transfers
   (LIMIS)** and **Dams & Reservoirs Basin Level Estimates** — water that moves
   across the boundary or sits in storage closes the balance.
7. **Check against stations.** Add **Water Balance Stations (LIMIS)** and
   **Evaporation Stations (LIMIS)**; click a station for observed values to
   validate the satellite terms.
8. **Open the Water Balance Dashboard** from the portal menu for the compiled
   accounts, and cross-reference the map layers you have assembled.
9. Save the assembled view as a **Story**, one scene per term of the balance.

## Reading the result

- Think in **one unit**: the ET layers are in mm over a period; multiply by area
  for volume, and keep rainfall and ET on the same period when comparing.
- **Blue ET is the negotiable water.** Where it concentrates — and in which
  country — is the core of the allocation conversation.
- A rising **Blue ET trend** with flat rainfall and falling reservoir levels is
  the signature of over-allocation.

## Limits to keep in mind

- The Africa-wide ET products are **model outputs at continental resolution**;
  they are consistent across the basin (which is what accounting needs) but
  should be calibrated against stations before being quoted as volumes.
- **Mean Annual Runoff (LIMIS)** is a long-term average, not a current value.
- Groundwater abstraction is only partly visible (through Blue ET and the
  groundwater layers); a full account needs borehole data.
- The dashboard and the polygon time-series process require a **signed-in
  session**.

## Related

[Irrigation water use](irrigation.md) · [Reservoir monitoring](reservoirs.md) ·
[Droughts](droughts.md) · [Data Catalogue](../guide/data-catalogue.md)
