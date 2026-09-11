---
title: My Data
---

# My Data

The **My Data** feature lets you bring your own datasets onto the map for
localised analysis. In v2 it is the second tab of the Data Catalogue: click
**Upload data** in the workbench (or **Explore data**, then the **My Data**
tab).

<figure markdown="span">
  ![The My Data tab with its drag-and-drop area](../assets/v2/v2-my-data.png)
  <figcaption>Figure 5: The My Data tab — drag and drop a file, or use Add Local Data / Add Web Data.</figcaption>
</figure>

!!! success "Your data stays on your machine"
    Data added through My Data is **not saved or uploaded to the internet** —
    the panel says so explicitly. It is rendered locally in your browser, so
    sensitive information stays private.

## Adding local data

Drag a file into the area marked *"Drag and drop a file here to view it locally
on the map"*, or click **Add Local Data** and choose a file. Supported formats:

- GeoTIFF
- Shapefiles
- KML / KMZ
- GeoJSON
- CSV with location coordinates

The platform renders the data immediately, ready to view and interact with. Use
the [Workbench](workbench.md) tools to toggle visibility, adjust opacity and
compare your dataset against other layers.

## Adding web data

Click **Add Web Data** to pull in a dataset from an external service. This
accepts URLs from **WMS** (Web Map Service), **WFS** (Web Feature Service) and
other compatible online geospatial sources.

1. Click **Add Web Data**.
2. Paste the service or data-source URL.
3. The platform fetches the data and draws it on the map.

!!! tip "Finding a service URL"
    Catalogue datasets expose a **GetCapabilities URL** in their preview — that
    is the style of URL *Add Web Data* expects from external services.

## Why use My Data

| Benefit | What it means |
| --- | --- |
| **Flexibility** | Visualise your datasets without uploading or storing them on the platform |
| **Privacy** | Data is not uploaded or saved to the internet, so sensitive information stays secure |
| **Integration** | Combine your own data with the platform's catalogue for richer analysis |
