---
title: Technical Implementation
---

# Technical Implementation

## Platform architecture

The WebGIS Portal is built on the **TerriaJS** framework, chosen for its
ability to assemble spatial data catalogues through a mix of manual curation
and live querying of online services. TerriaJS also underpins leading platforms
such as Australia's NationalMap and the New South Wales Digital Twin
Visualisation Service.

<figure markdown="span">
  ![The homepage of the TerriaJS framework](../assets/images/image1.png)
  <figcaption>Figure 1: The homepage of the TerriaJS framework.</figcaption>
</figure>

### Data source integration

The platform integrates several classes of data:

| Source | Contribution |
| --- | --- |
| **Satellite imagery** | Sourced from Google Earth Engine and AWS open data registries |
| **Numerical model outputs** | Real-time predictions and simulations of the basin's hydrology |
| **In-situ data** | Sensor data collected across the basin, giving ground-truth validation for the satellite and model data |

## Key features and functionalities

The feature set was shaped by Phase 1 feedback and by platforms such as Digital
Earth Africa.

- **Data visualisation** — enhanced 2D and 3D visualisation capabilities.
- **Data synchronisation** — real-time synchronisation with data sources.
- **Layer control** — a robust layer management panel organised by thematic
  area.
- **Interactive tools** — map export, sharing options, and a time series
  slider.
- **Search functionality** — a geocoding search bar restricted to the study
  area.
- **Data catalogue** — a comprehensive catalogue for data exploration and
  selection.

### Interactive map controls

- **Zoom and pan** — standard map controls for intuitive navigation of the
  spatial datasets.
- **Layer control panel** — toggle thematic layers on and off for targeted
  analysis.

### Data visualisation tools

- **Time series analysis** — explore temporal change in the datasets, such as
  water levels or land use over time.
- **Customisable basemaps** — view data against a choice of background maps.

### Data export and sharing

- **Map export** — export the current map view as an image file, including any
  selected data layers and annotations.
- **Sharing capability** — generate shareable links so colleagues can open a
  specific view or data configuration.

### AI-driven chatbot

An AI-driven chatbot is integrated into the portal to assist users with queries
and navigation.

## User experience and interface design

The user interface is designed to be intuitive, with a focus on simplicity and
accessibility. The design mirrors the DE Africa platform and NationalMap, with
enhancements that serve the specific requirements of IWMI and the Limpopo River
basin project.

### Accessibility features

- **Cross-browser compatibility** — compatible with all major browsers, giving
  a consistent experience across devices.
- **Responsive design** — the UI adapts to various screen sizes, including
  tablets and mobile devices.

## Version and system information

- **Portal:** <https://limpopo.digitaltwins.iwmi.org/>
- **TerriaMap version:** `0.4.1`
- **TerriaJS version:** `8.9.5`
- **Build date:** 2026-05-15
- **Platform components:** Cesium ion for 3D mapping, data attribution and base
  map selection.
