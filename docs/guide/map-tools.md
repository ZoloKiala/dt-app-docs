---
title: Map Tools
---

# Map Tools

## Watch: quick tour

<div class="video-wrap" markdown>
<video controls preload="metadata" poster="../../assets/v2/v2-map-settings.png">
  <source src="../../assets/video/quick-map-tools.mp4" type="video/mp4">
  <track kind="captions" src="../../assets/video/quick-map-tools.vtt" srclang="en" label="English">
  Your browser does not support embedded video.
  <a href="../../assets/video/quick-map-tools.mp4">Download the video</a>.
</video>
</div>

*A one-minute walkthrough of map settings, navigation, compare and measure. Narration uses a synthetic voice; turn on captions with the **CC** button.*


The controls down the right-hand side of the map handle orientation,
navigation, comparison and measurement; the top bar carries Map Settings and
Share / Print; and v2 adds two new tools — an AI chatbot and a SWAT extraction
tool.

## Map Settings

**Map Settings** (top bar) customises how the map is drawn.

<figure markdown="span">
  ![The Map Settings panel](../assets/v2/v2-map-settings.png)
  <figcaption>Figure 7: Map Settings — view mode, terrain, basemaps, timeline and quality.</figcaption>
</figure>

- **Map View** — **3D Terrain**, **3D Smooth** or **2D**.
- **Show Terrain on the** — Left / Both / Right, with an option so **terrain
  hides underground features**.
- **Base Map** — v2 offers a wider set than the 2024 release: **Bing Aerial
  with Labels** (default), **Bing Aerial**, **Bing Roads**, **OpenStreetMap**,
  **OpenTopoMap**, **Esri World Imagery**, **Esri Topographic**, **Dark
  Matter**, **Positron (Light)** and **Natural Earth II**.
- **Timeline → Always show** — keeps the time-series controls on screen.
- **Image Optimisation** — use native device resolution.
- **Map Quality** — a Quality ↔ Performance slider.

## View controls

The **Change view** control (the ring-and-cross icon) rotates the map through
360°, and a double-click resets it. Beneath it:

| Control | Action |
| --- | --- |
| **Home** | Returns to the default globe view |
| **+ / –** | Zoom in / out (the mouse wheel also zooms) |
| **Location** | Live location tracking — click *Allow* in the popup |
| **Pan** | Drag the map with the left mouse button |

## Compare

The **Compare** tool (*Enable side-by-side comparison between two different sets
of data*) puts two datasets side by side in split-screen mode.

<figure markdown="span">
  ![Split-screen compare mode](../assets/v2/v2-compare.png)
  <figcaption>Figure 8: Side-by-side comparison mode.</figcaption>
</figure>

1. Click **Compare** to enter split-screen mode.
2. Choose the two datasets to compare.
3. Drag the split bar to align them; assign each dataset to **Left**, **Right**
   or **Both**.

!!! warning "Terrain note"
    Terrain layers can obscure underground features — relevant depending on the
    datasets being compared.

## Pedestrian mode

**Pedestrian Mode** gives a street-level view for detailed exploration.

<figure markdown="span">
  ![Pedestrian mode](../assets/v2/v2-pedestrian.png)
  <figcaption>Figure 9: Pedestrian Mode — a ground-level view of the data.</figcaption>
</figure>

Use the control tool to rotate the view; ++space++ moves forward and ++shift++
moves backward.

## Measure

The **Line Measure** tool (*Measure distance between locations*) measures the
distance between two or more points on the map.

<figure markdown="span">
  ![Measure tool](../assets/v2/v2-measure.png)
  <figcaption>Figure 10: Measuring distance between points.</figcaption>
</figure>

## Water Copilot chatbot

!!! note "New in v2"
    **Open Chatbot** (bottom-right of the map) launches **Water Copilot**, an
    AI assistant. Ask questions about the basin and its data in plain language
    and get guided answers and navigation help. The assistant opens in a panel
    beside the map. See [Water Copilot](water-copilot.md) for what it can
    answer and how to ask.

## SWAT Extraction Tool

!!! note "New in v2"
    The **SWAT Extraction Tool** queries modelled flows from the SWAT
    hydrological model for a specific river channel.

<figure markdown="span">
  ![The SWAT Extraction Tool](../assets/v2/v2-swat-tool.png)
  <figcaption>Figure 11: The SWAT Extraction Tool — choose a flow type, channel and date range, then fetch data. Tabs switch between Map, Table, Help and ProbFlo.</figcaption>
</figure>

- **Select Flow Type** — e.g. *Natural Flows*.
- **Channel ID** — the channel to query.
- **Start Date / End Date** — the period of interest.
- **Condition** — a filter on the flow condition.
- **FETCH DATA** — retrieves the modelled series; the **MAP / TABLE / HELP /
  PROBFLO** tabs switch between the map picker, the results table, help, and the
  ProbFlo view.

## Feedback

The **Give Feedback** tool sends comments or questions directly to the
developers.

<figure markdown="span">
  ![The feedback form](../assets/v2/v2-feedback.png)
  <figcaption>Figure 12: The feedback form — name and email are optional; you can include your current map view.</figcaption>
</figure>

## Data attribution and basemap selection

Along the bottom of the map are data attribution, the basemap selector, and the
disclaimers that apply to the data in use, plus a live **Lat / Lon / Elev**
readout and a scale bar.
