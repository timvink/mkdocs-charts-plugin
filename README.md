[![Actions Status](https://github.com/timvink/mkdocs-charts-plugin/workflows/pytest/badge.svg)](https://github.com/timvink/mkdocs-charts-plugin/actions)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-charts-plugin)
![PyPI](https://img.shields.io/pypi/v/mkdocs-charts-plugin)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mkdocs-charts-plugin)
![GitHub contributors](https://img.shields.io/github/contributors/timvink/mkdocs-charts-plugin)
![PyPI - License](https://img.shields.io/pypi/l/mkdocs-charts-plugin)

# mkdocs-charts-plugin

[MkDocs](https://www.mkdocs.org/) plugin to create plots from data using the declarative [vegalite](https://vega.github.io/vega-lite/) syntax. This makes it easier to [build reproducible reports with MkDocs](https://timvink.nl/reproducible-reports-with-mkdocs/).

👉 See it in action on the [demo page](https://timvink.github.io/mkdocs-charts-plugin/demo/)

Includes supports for [mkdocs-material](https://github.com/squidfunk/mkdocs-material) theme features like [instant loading](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/?h=reload#instant-loading) and [dark color themes](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/#color-palette-toggle).

## Installation

Install the plugin using `pip3`:

```shell
pip3 install mkdocs-charts-plugin
```

Next, add the following lines to your `mkdocs.yml`:

```yml
plugins:
  - search
  - charts

extra_javascript:
  - https://cdn.jsdelivr.net/npm/vega@5
  - https://cdn.jsdelivr.net/npm/vega-lite@5
  - https://cdn.jsdelivr.net/npm/vega-embed@6

markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: vegalite
          class: vegalite
          format: !!python/name:mkdocs_charts_plugin.fences.fence_vegalite
```

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

## Usage

You can insert any valid [vegalite](https://vega.github.io/vega-lite/) JSON into a markdown file. But the real magic is that you can visualize `.json` or `.csv` files:

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

See the [vegalite editor](https://vega.github.io/editor/#/) for a range of examples.

## Documentation

See the documentation [timvink.github.io/mkdocs-charts-plugin](https://timvink.github.io/mkdocs-charts-plugin/) for examples, use cases and options.

Do checkout the other [charting plugins for mkdocs](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins#images-tables-charts--graphs) that might suit your specific use-case better.