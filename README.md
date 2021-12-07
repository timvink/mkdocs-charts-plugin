[![Actions Status](https://github.com/timvink/mkdocs-charts-plugin/workflows/pytest/badge.svg)](https://github.com/timvink/mkdocs-charts-plugin/actions)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-charts-plugin)
![PyPI](https://img.shields.io/pypi/v/mkdocs-charts-plugin)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mkdocs-charts-plugin)
![GitHub contributors](https://img.shields.io/github/contributors/timvink/mkdocs-charts-plugin)
![PyPI - License](https://img.shields.io/pypi/l/mkdocs-charts-plugin)

# mkdocs-charts-plugin

[MkDocs](https://www.mkdocs.org/) plugin to create plots from data using the declarative [vegalite](https://vega.github.io/vega-lite/) syntax.

This makes it easier to build reproducible reports.

## Installation

Install the plugin using `pip3`:

```shell
pip3 install mkdocs-charts-plugin
```

Next, add the following lines to your `mkdocs.yml`:

```yml
plugins:
  - search
  - table-reader

extra_javascript:
  - https://cdn.jsdelivr.net/npm/vega@5
  - https://cdn.jsdelivr.net/npm/vega-lite@5
  - https://cdn.jsdelivr.net/npm/vega-embed@6

markdown_extensions:
  - pymdownx.superfences:
      disable_indented_code_blocks: true
      preserve_tabs: true
      custom_fences:
        - name: vegalite
          class: vegalite
          format: !!python/name:mkdocs_charts_plugin.fence_vegalite_custom
```

> If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set.

## Usage

You can insert any valid [vegalite](https://vega.github.io/vega-lite/) JSON into a markdown file using:

````
```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple bar chart with embedded data.",
  "data": {
    "values": [
      {"a": "A", "b": 28}, {"a": "B", "b": 55}, {"a": "C", "b": 43},
      {"a": "D", "b": 91}, {"a": "E", "b": 81}, {"a": "F", "b": 53},
      {"a": "G", "b": 19}, {"a": "H", "b": 87}, {"a": "I", "b": 52}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "a", "type": "nominal", "axis": {"labelAngle": 0}},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```
````

## Options

- `vega_width` (default is `container`). When not specified explicitly in the JSON schema, the `width` to use (see [vegalite customizing size](https://vega.github.io/vega-lite/docs/size.html)). When set to `container` width will be 100%.
- `vega_theme` (default is `default`). Specify one of the available [vegalite themes](https://vega.github.io/vega-themes/)
- `vega_renderer` (default is `svg`). Specify one of the available [vegalite renderers](https://vega.github.io/vega-themes/)
- `use_data_path` (default is `True`). When `True`, any relative urls used in the JSON schema are relative to the `data_path`. When `False`, relative urls should be relative to the URL of the page.
- `data_path` (default is `""`). When `use_data_path` is enabled, the base path relative to the `docs/` folder.



## More

- promote the plugin
  - blogpost, twitter
  - plugin wiki
  - refer to it from table-reader
  - add to demo in print-site

# Credits 

https://github.com/koaning/justcharts
https://facelessuser.github.io/pymdown-extensions/extras/mermaid/
https://vega.github.io/vega-lite/docs/config.html
