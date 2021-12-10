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

Renders as:

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

`mkdocs-charts-plugin` becomes really powerfull when used with datasets. You could re-write the example below with:

````json hl_lines="5"
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

Note that the URL is relative to the `docs/` folder, which means you can re-order the hierarchy of markdown pages without breaking charts. If you prefer specifying URLs relative to the location of the markdown page, set `use_data_path` to `False` (see [options](options.md)).

Note you could also use an absolute URL to a dataset somewhere on the web or a public git repository, for example `https://raw.githubusercontent.com/timvink/mkdocs-charts-plugin/main/docs/assets/charts/data/basic_bar_chart.json`.

## Specifying schema-URLs

In you have multiple charts in a markdown page with large schemas, you could also save then separately in a `.json` file and point to it using a `schema-url`:

````
```vegalite
{
  "schema-url": "assets/charts/chart_basic_bar_chart.json"
}
```
````

