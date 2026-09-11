---
title: Data Catalogue
---

# Data Catalogue

The Data Catalogue is organised into thematic categories, each holding datasets
relevant to the Limpopo River basin: **Natural Basin Characteristics**,
**Socio-Economic Profile**, **Water Resources**, **Ecosystems** and
**Satellite Images**.

<figure markdown="span">
  ![Data Catalogue featuring the thematic layers](../assets/images/image8.png)
  <figcaption>Figure 7: The Data Catalogue, showing the thematic layers.</figcaption>
</figure>

For what each category contains, see [Dataset Themes](datasets.md).

## Searching the catalogue

Use **Search the Catalogue** to find a specific dataset by name. This gets you
to data of interest quickly, without walking the whole category tree.

## Previewing and adding data

Selecting a dataset opens a **Data Preview** panel with a short description and
the option to add the dataset to the map. Taking "Soil maps" under *Natural
Basin Characteristics* as an example, the preview gives you:

1. **Dataset description** — the significance of the dataset, including its
   relevance to sustainable land management and conservation efforts.
2. **Add to the Map** — visualise the dataset directly on the map.
3. **Service contact** — contact information for further enquiries about the
   dataset.
4. **GetCapabilities URL** — a URL for integrating the dataset into other GIS
   software.
5. **DOI and data source** — the dataset's origin, including a DOI for
   citation and the primary data provider.

<figure markdown="span">
  ![Adding a dataset to the map view page](../assets/images/image9.png)
  <figcaption>Figure 8: Adding a dataset to the map view.</figcaption>
</figure>

<figure markdown="span">
  ![Preview of the Soil maps dataset](../assets/images/image10.png)
  <figcaption>Figure 9: The &ldquo;Soil maps&rdquo; dataset preview, with options to add it to the map and detailed descriptions.</figcaption>
</figure>

<figure markdown="span">
  ![Displayed soil maps of the geology dataset](../assets/images/image11.png)
  <figcaption>Figure 10: The added soil maps layer displayed on the map.</figcaption>
</figure>

!!! info "About Data"
    The **About Data** icon returns you to the data catalogue page and shows
    the information about the dataset currently displayed.

## Navigating the data

Once a dataset is added to the map it appears in the [Workbench](workbench.md)
for further manipulation. From there you can adjust visibility and opacity, and
compare datasets. The platform supports both 2D and 3D visualisation, depending
on the dataset.

<figure markdown="span">
  ![Workbench and data preview](../assets/images/image37.png)
  <figcaption>Figure 11: The Workbench alongside the data preview.</figcaption>
</figure>

### 3D dataset tools

Point-cloud and other 3D data carry extra controls:

- **Shadows** — cast only, receive only, or both cast and receive.
- **Clip Model** — clip the data inside or outside a box, zoom to the box, and
  reposition it.

<figure markdown="span">
  ![Clip model feature](../assets/images/image38.png)
  <figcaption>Figure 12: The clip model feature applied to a 3D dataset.</figcaption>
</figure>

## The Feature Information icon

**Feature Information** reports the details behind a specific point on the map,
and lets you export them.

<figure markdown="span">
  ![Feature information of explored dam locations dataset](../assets/images/image39.png)
  <figcaption>Figure 13: Feature information for the dam locations dataset.</figcaption>
</figure>

For the dam locations example, the panel gives you:

- **Dam Locations — Site Data** — information about specific dam sites.
- **Data download options** — download the data table as CSV or JSON.
- **Show Raw Data** — view the unprocessed data.

## Styling a dataset

The **display variable** control in the Workbench lets you style and customise
how a dataset is drawn. For finer control, click the **three-dot icon**, choose
**Edit Style**, and click **Done** when you have finished.

<figure markdown="span">
  ![Exploring the features of the E-flow dataset](../assets/images/image40.png)
  <figcaption>Figure 14: Exploring the features of the E-flow Monitoring and Forecasting dataset.</figcaption>
</figure>

<figure markdown="span">
  ![Styling of the E-Flow Monitoring and Forecasting dataset](../assets/images/image41.png)
  <figcaption>Figure 15: Styling the E-flow Monitoring and Forecasting dataset.</figcaption>
</figure>

## Charts and time series

Datasets with a temporal dimension can be charted. Select a start and end date
to restrict the chart to a period of interest.

<figure markdown="span">
  ![Chart display of the E-flow dataset with selected dates](../assets/images/image42.png)
  <figcaption>Figure 16: Chart of the E-flow Monitoring and Forecasting dataset, showing a selected start and end date.</figcaption>
</figure>

<figure markdown="span">
  ![Graph of the E-flow Monitoring and Forecasting dataset](../assets/images/image43.png)
  <figcaption>Figure 17: Graph of the E-flow Monitoring and Forecasting dataset.</figcaption>
</figure>

Hovering over a point on the curve reveals the values behind it. For the E-flow
dataset these attributes are:

| Attribute | Meaning |
| --- | --- |
| **Availability Surplus** | The amount or unit of surplus available |
| **Deficit** | The shortfall or lack of data |
| **SWAT Present Flow** | The flow data from the SWAT model |
| **E-Flow** | The environmental flow data |

<figure markdown="span">
  ![The data graph adjusted with the time-series feature](../assets/images/image44.png)
  <figcaption>Figure 18: The graph adjusted using the time-series control in the chart.</figcaption>
</figure>
