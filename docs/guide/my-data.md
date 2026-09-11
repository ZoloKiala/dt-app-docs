---
title: My Data
---

# My Data

The **My Data** section lets you bring your own datasets into the map for
localised analysis and visualisation. Reach it from the **Upload** icon, or
from the **Explore Map Data** page.

<figure markdown="span">
  ![Description of the Upload Data feature](../assets/images/image45.png)
  <figcaption>Figure 41: The &ldquo;Upload Data&rdquo; feature.</figcaption>
</figure>

!!! success "Your data stays on your machine"
    Data added through My Data is **not uploaded or saved to the internet**. It
    is rendered locally in your browser, so sensitive information stays
    private.

## Adding local data

Drag and drop files into the My Data section to view them immediately. Nothing
is uploaded to the cloud.

Supported formats:

- GeoTIFF
- Shapefiles
- KML / KMZ
- GeoJSON
- CSV with location coordinates

### Steps to add local data

1. **Drag and drop** — drag the file from local storage into the area labelled
   *"Drag and drop a file here to view it locally on the map"*.
2. **View on the map** — the platform renders the data automatically, ready
   for you to view and interact with.
3. **Manipulate the data** — use the [Workbench](workbench.md) tools to toggle
   visibility, adjust opacity, and compare your dataset against other layers.

<figure markdown="span">
  ![The drag-and-drop area in the My Data section](../assets/images/image46.png)
  <figcaption>Figure 42: The drag-and-drop area in the My Data section, where local files are added to the map.</figcaption>
</figure>

## Adding web data

You can also pull in datasets from external web sources with **Add Web Data**.
This accepts URLs from Web Map Services (WMS), Web Feature Services (WFS), and
other compatible online geospatial data sources.

### Steps to add web data

1. **Select Add Web Data** — click the *Add Web Data* button.
2. **Enter the URL** — paste the URL of the web service or data source.
3. **Visualise** — the platform fetches the data from the URL and displays it
   on the map.

!!! tip "Finding a service URL"
    Datasets in the built-in catalogue expose a **GetCapabilities URL** in
    their preview panel. That same style of URL is what *Add Web Data* expects
    from external services.

## Why use My Data

| Benefit | What it means |
| --- | --- |
| **Flexibility** | Visualise your datasets without uploading or storing them on the platform |
| **Privacy** | Data is not uploaded or saved to the internet, so sensitive information stays secure |
| **Integration** | Combine your own data with the platform's catalogue for richer analysis |
