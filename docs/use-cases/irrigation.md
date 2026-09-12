---
title: Irrigation water use
---

# Irrigation water use monitoring

## The question

A water-resources planner or scheme manager wants to know **where irrigated
land is, whether it is growing, and how much water it consumes** over a season —
without waiting for licence returns or field surveys.

## Data you will use

| Dataset | Where in the catalogue | What it tells you |
| --- | --- | --- |
| **Irrigated Mapping** | Natural Basin Characteristic → Land Cover and Land Use | Satellite-derived irrigated areas, as a time series |
| **Irrigation Areas (LIMIS)** | Water Resources → Water Infrastructure | Registered / mapped irrigation schemes (reference boundaries) |
| **Water Use Time-series (Irrigated Areas) (Polygon)** | Water Use Monitoring and Analysis | An analysis process: choose an area and get its water-use time series |
| **WaPOR Downscaled** · **ETa Monthly Limpopo** | Natural Basin Characteristic → Climate | Actual evapotranspiration — the water actually consumed by crops |
| **Blue ET Africa** · **Green ET Africa** | Water Use Monitoring and Analysis → Water Accounting → Evapotranspiration & Water Use | Splits consumption into irrigation-supplied (*blue*) and rain-fed (*green*) water |
| **Beneficial Fraction Africa** · **ET Fraction Africa** | same group | How much of the water consumed does useful work (crop growth) |
| **Land Use** · **Land Use (LIMIS)** | Natural Basin Characteristic → Land Cover and Land Use | Context: cropland vs. natural vegetation vs. settlements |

## Walkthrough

1. **Explore data → Search the catalogue → `Irrigated Mapping` → Add to the map.**
   The layer is time-varying, so a timeline appears beneath the map.
2. Use **Ideal Zoom** on the Workbench card to frame the layer, then use the
   timeline arrows to step between dates. Irrigated fields stand out as sharp,
   regular shapes that stay green through the dry season.
3. Add **Irrigation Areas (LIMIS)** and compare: irrigation detected *outside*
   the registered schemes is a first signal of unlicensed or expanding use.
4. Add **Blue ET Africa**. In the Workbench, lower its **opacity** to ~60% so the
   fields remain visible underneath. Bright blue-ET over a field means it is
   drawing on irrigation water, not rain.
5. Use **Compare** ([Map Tools](../guide/map-tools.md#compare)) to put **Blue ET**
   on the left and **Green ET** on the right for the same month — the contrast
   separates irrigated from rain-fed agriculture at a glance.
6. To quantify a scheme: open **Water Use Time-series (Irrigated Areas)
   (Polygon)** from *Water Use Monitoring and Analysis*, select or draw the area
   of interest and run it. The result is a time series of water use for that
   polygon that you can read directly or download.
7. **Story → Capture Scene** for the before/after dates, and **Share / Print**
   the link.

## Reading the result

- **Growth in irrigated extent** between years is the headline indicator; use the
  timeline on *Irrigated Mapping* and capture a scene per year.
- **Blue ET ≫ Green ET** over a field confirms irrigation dependence and gives a
  consumption estimate in mm — multiply by area for volume.
- A low **Beneficial Fraction** over an irrigated block points to water lost to
  soil evaporation rather than crop growth — a candidate for efficiency work.

## Limits to keep in mind

- Satellite ET products are **modelled estimates** at their native resolution
  (WaPOR downscaled, Africa-wide ET layers); use them for patterns and trends,
  and validate volumes against metered abstractions where they exist.
- **Irrigated Mapping** is classified from imagery; cloud cover in the wet season
  can reduce confidence for individual dates — look at several.
- The polygon **Water Use Time-series** runs a server-side process; large areas
  take longer, and it needs a signed-in session.

## Related

[Water accounting](water-accounting.md) · [Droughts](droughts.md) ·
[Workbench — time series](../guide/workbench.md#time-series)
