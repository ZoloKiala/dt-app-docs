---
title: Glossary
---

# Glossary

Terms and acronyms used across this documentation.

### Platform and project

**Digital Twin (DT)**
: A virtual representation of the Limpopo River basin, assembled from satellite
  imagery, in-situ sensor data and numerical model outputs.

**TerriaJS**
: The open-source geospatial framework the portal is built on. It assembles
  spatial data catalogues through manual curation and live querying of online
  services.

**IWMI**
: International Water Management Institute — the organisation the portal was
  developed for.

**DE Africa**
: Digital Earth Africa, one of the platforms that inspired the portal's design.

**NationalMap**
: Australia's national map platform, also built on TerriaJS.

**Cesium ion**
: The platform component providing 3D mapping, data attribution and base map
  selection.

### Interface

**Workbench**
: The left-hand panel listing every dataset currently active on the map, with
  controls for visibility, opacity, styling and removal.
  See [Workbench](../guide/workbench.md).

**Data Catalogue**
: The thematic collection of curated datasets available to add to the map.
  See [Data Catalogue](../guide/data-catalogue.md).

**My Data**
: The section for adding your own local files or web services, without
  uploading them to the platform. See [My Data](../guide/my-data.md).

**Story / Story Editor**
: The narrative tool for capturing map scenes with accompanying text.
  See [Stories & Sharing](../guide/sharing.md).

**Capture Scene**
: The action that saves the current map view, title and description as a step
  in a story.

**Split Screen Mode**
: The compare view that places two datasets side by side.
  See [Compare feature](../guide/map-tools.md#compare).

**Pedestrian Mode**
: A street-level, ground-based view of the map data.

**Ideal Zoom**
: A per-dataset option that moves the map to the view best framing that
  dataset.

**Feature Information**
: The panel reporting the underlying attributes of a clicked map feature, with
  CSV and JSON export.

### Data and services

**WMS**
: Web Map Service — a standard for serving georeferenced map images, accepted
  by *Add Web Data*.

**WFS**
: Web Feature Service — a standard for serving map feature geometry and
  attributes, accepted by *Add Web Data*.

**GetCapabilities URL**
: The service URL exposed in a dataset preview, used to integrate the dataset
  into other GIS software.

**GeoTIFF**
: A raster image format carrying embedded georeferencing; supported by
  *My Data*.

**GeoJSON**
: A JSON-based format for encoding geographic features; supported by *My Data*.

**KML / KMZ**
: Keyhole Markup Language (and its zipped form) for geographic annotation;
  supported by *My Data*.

**Shapefile**
: A widely used vector data format; supported by *My Data*.

**DOI**
: Digital Object Identifier — the persistent citation identifier given in a
  dataset's preview panel.

### Hydrology and environment

**SWAT**
: Soil and Water Assessment Tool — the hydrological model providing present-day
  flow and incremental contribution datasets.

**E-flow**
: Environmental flow — the water regime needed to sustain the basin's
  ecosystems. The portal publishes E-flow regions, monitoring and forecasting,
  alert levels and warnings.

**Availability Surplus**
: In the E-flow chart, the amount or unit of surplus available.

**Deficit**
: In the E-flow chart, the shortfall or lack of data.

**CHIRPS**
: Climate Hazards Group InfraRed Precipitation with Station data — the source
  of the historical rainfall dataset.

**VCI**
: Vegetation Condition Index — a land-cover dataset available as a time series.

**GeoMAD**
: The geomedian and median absolute deviation product, published here as
  Rolling Monthly GeoMAD (Sentinel-2).

**Sentinel-2**
: The satellite mission behind the portal's rolling monthly imagery.

**Water Observations from Space**
: An all-time summary satellite dataset of observed surface water.

**3D Point Cloud**
: High-resolution drone-collected elevation data, available for the Oliphants
  River and the Crocodile River System (Upper and Lower).
