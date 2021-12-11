# Usage

!!! quote "What is vegalite?"

    Vega-Lite is a high-level grammar of interactive graphics. It provides a concise, declarative JSON syntax to create an expressive range of visualizations for data analysis and presentation. [source](https://vega.github.io/vega-lite/)

`mkdocs-charts-plugin` makes it easy to insert any valid vega-lite specification into your markdown pages. For example:

````
```vegalite
{
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```
````

will render as:

```vegalite
{
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```

For more examples, see the [demo](demo.md) page.

## How to specify URLs

`mkdocs-charts-plugin` becomes really powerful when used with datasets. You could re-write the example above by referring to a data file:

````json hl_lines="4"
```vegalite 
{
  "description": "A simple bar chart with embedded data.",
  "data": {"url" : "assets/charts/data/basic_bar_chart.json"},
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```
````

Note that the URL is relative to the `docs/` folder, which means you can re-order the hierarchy of markdown pages without breaking charts. If you prefer specifying URLs relative to the location of the markdown page, set `use_data_path` to `False` (see plugin [options](options.md)).

Note you could also use an absolute URL to a dataset somewhere on the web or a public git repository, for example `https://raw.githubusercontent.com/timvink/mkdocs-charts-plugin/main/docs/assets/charts/data/basic_bar_chart.json`.

## Specifying schema-URLs

To avoid long, distracting chart schemas in your markdown files you can choose to save a chart schema separately in a `.json` file and point to it using a `schema-url`:

````
```vegalite
{
  "schema-url": "assets/charts/chart_basic_bar_chart.json"
}
```
````

## Altair

[Altair](https://altair-viz.github.io/index.html) is a declarative statistical visualization library for Python.

Because Altair is built on [Vega-Lite](http://vega.github.io/vega-lite), you can [save Altair Charts](https://altair-viz.github.io/user_guide/saving_charts.html) in vega-lite format. 

For example, the altair gallery has this [bar chart with highlighted bar](https://altair-viz.github.io/gallery/bar_chart_with_highlighted_bar.html):

```python
import altair as alt
from vega_datasets import data

source = data.wheat()

alt.Chart(source).mark_bar().encode(
    x='year:O',
    y="wheat:Q",
    # The highlight will be set on the result of a conditional statement
    color=alt.condition(
        alt.datum.year == 1810,  # If the year is 1810 this test returns True,
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
    )
).properties(width=600)
```

That chart can be exported using `.save("chartname.json")` or `.to_json()` and quickly inserted into a mkdocs project. It will render as:

```vegalite
{  "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json",  "config": {    "view": {      "continuousHeight": 300,      "continuousWidth": 400    }  },  "data": {    "name": "data-76d1ce26ea5761007c35827e1564d86c"  },  "datasets": {    "data-76d1ce26ea5761007c35827e1564d86c": [      {        "wages": 5.0,        "wheat": 41.0,        "year": 1565      },      {        "wages": 5.05,        "wheat": 45.0,        "year": 1570      },      {        "wages": 5.08,        "wheat": 42.0,        "year": 1575      },      {        "wages": 5.12,        "wheat": 49.0,        "year": 1580      },      {        "wages": 5.15,        "wheat": 41.5,        "year": 1585      },      {        "wages": 5.25,        "wheat": 47.0,        "year": 1590      },      {        "wages": 5.54,        "wheat": 64.0,        "year": 1595      },      {        "wages": 5.61,        "wheat": 27.0,        "year": 1600      },      {        "wages": 5.69,        "wheat": 33.0,        "year": 1605      },      {        "wages": 5.78,        "wheat": 32.0,        "year": 1610      },      {        "wages": 5.94,        "wheat": 33.0,        "year": 1615      },      {        "wages": 6.01,        "wheat": 35.0,        "year": 1620      },      {        "wages": 6.12,        "wheat": 33.0,        "year": 1625      },      {        "wages": 6.22,        "wheat": 45.0,        "year": 1630      },      {        "wages": 6.3,        "wheat": 33.0,        "year": 1635      },      {        "wages": 6.37,        "wheat": 39.0,        "year": 1640      },      {        "wages": 6.45,        "wheat": 53.0,        "year": 1645      },      {        "wages": 6.5,        "wheat": 42.0,        "year": 1650      },      {        "wages": 6.6,        "wheat": 40.5,        "year": 1655      },      {        "wages": 6.75,        "wheat": 46.5,        "year": 1660      },      {        "wages": 6.8,        "wheat": 32.0,        "year": 1665      },      {        "wages": 6.9,        "wheat": 37.0,        "year": 1670      },      {        "wages": 7.0,        "wheat": 43.0,        "year": 1675      },      {        "wages": 7.3,        "wheat": 35.0,        "year": 1680      },      {        "wages": 7.6,        "wheat": 27.0,        "year": 1685      },      {        "wages": 8.0,        "wheat": 40.0,        "year": 1690      },      {        "wages": 8.5,        "wheat": 50.0,        "year": 1695      },      {        "wages": 9.0,        "wheat": 30.0,        "year": 1700      },      {        "wages": 10.0,        "wheat": 32.0,        "year": 1705      },      {        "wages": 11.0,        "wheat": 44.0,        "year": 1710      },      {        "wages": 11.75,        "wheat": 33.0,        "year": 1715      },      {        "wages": 12.5,        "wheat": 29.0,        "year": 1720      },      {        "wages": 13.0,        "wheat": 39.0,        "year": 1725      },      {        "wages": 13.3,        "wheat": 26.0,        "year": 1730      },      {        "wages": 13.6,        "wheat": 32.0,        "year": 1735      },      {        "wages": 14.0,        "wheat": 27.0,        "year": 1740      },      {        "wages": 14.5,        "wheat": 27.5,        "year": 1745      },      {        "wages": 15.0,        "wheat": 31.0,        "year": 1750      },      {        "wages": 15.7,        "wheat": 35.5,        "year": 1755      },      {        "wages": 16.5,        "wheat": 31.0,        "year": 1760      },      {        "wages": 17.6,        "wheat": 43.0,        "year": 1765      },      {        "wages": 18.5,        "wheat": 47.0,        "year": 1770      },      {        "wages": 19.5,        "wheat": 44.0,        "year": 1775      },      {        "wages": 21.0,        "wheat": 46.0,        "year": 1780      },      {        "wages": 23.0,        "wheat": 42.0,        "year": 1785      },      {        "wages": 25.5,        "wheat": 47.5,        "year": 1790      },      {        "wages": 27.5,        "wheat": 76.0,        "year": 1795      },      {        "wages": 28.5,        "wheat": 79.0,        "year": 1800      },      {        "wages": 29.5,        "wheat": 81.0,        "year": 1805      },      {        "wages": 30.0,        "wheat": 99.0,        "year": 1810      },      {        "wages": null,        "wheat": 78.0,        "year": 1815      },      {        "wages": null,        "wheat": 54.0,        "year": 1820      }    ]  },  "encoding": {    "color": {      "condition": {        "test": "(datum.year === 1810)",        "value": "orange"      },      "value": "steelblue"    },    "x": {      "field": "year",      "type": "ordinal"    },    "y": {      "field": "wheat",      "type": "quantitative"    }  },  "mark": "bar"}
```

The only modification to the output JSON was removing `"width": 600` to make the chart use the full width of the page container.