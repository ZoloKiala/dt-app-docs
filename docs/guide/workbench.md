---
title: Workbench
---

# Workbench

The **Workbench** is the panel on the left that manages the datasets currently
on the map. Anything you add from the [Data Catalogue](data-catalogue.md) or
[My Data](my-data.md) appears here under a **DATASETS (n)** heading.

<figure markdown="span">
  ![The workbench with a dataset's actions menu open](../assets/v2/v2-workbench-actions.png)
  <figcaption>Figure 6: The workbench. Each dataset card carries Ideal Zoom, About Data and a three-dot menu (Export / Remove).</figcaption>
</figure>

## Managing the whole list

Above the dataset list, three actions apply to everything at once:

| Control | Effect |
| --- | --- |
| **Disable All** | Hides every dataset without removing it |
| **Collapse All** | Minimises every dataset card for a cleaner view |
| **Remove All** | Clears every dataset from the workbench |

## Per-dataset controls

Each dataset card gives you:

- **Toggle** — the switch at the top of the card turns the dataset on or off.
- **Ideal Zoom** — moves the map to the view that best frames the dataset.
- **About Data** — returns to the catalogue entry and its full description.
- **Three-dot menu (⋮)** — **Show more actions**, opening:
    - **Export** — export the dataset.
    - **Remove** — remove just this dataset from the map and workbench.
- **Dropdown (▾)** — expands the card for opacity, the **display variable**
  (which attribute the layer is drawn by), styling, and — where available —
  charts and a timeline.

## Styling a dataset

The **display variable** decides which attribute a dataset is drawn by. For
finer control, open the three-dot menu and choose the style editor, then apply
your changes. Population data, for example, can be styled by sub-basin, area,
polygon ID or population.

## Time series

Datasets with a temporal dimension expose a timeline beneath the map and in the
workbench card; the left and right arrows step through time. Turn on
**Timeline → Always show** in [Map Settings](map-tools.md#map-settings) to keep
it visible.

## Comparing datasets

The compare tool works directly against the workbench contents — see
[Compare](map-tools.md#compare) in Map Tools.
