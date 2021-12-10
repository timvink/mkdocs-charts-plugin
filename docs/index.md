[![Actions Status](https://github.com/timvink/mkdocs-charts-plugin/workflows/pytest/badge.svg)](https://github.com/timvink/mkdocs-charts-plugin/actions)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mkdocs-charts-plugin)
![PyPI](https://img.shields.io/pypi/v/mkdocs-charts-plugin)
![GitHub contributors](https://img.shields.io/github/contributors/timvink/mkdocs-charts-plugin)
![PyPI - License](https://img.shields.io/pypi/l/mkdocs-charts-plugin)

# mkdocs-charts-plugin

[MkDocs](https://www.mkdocs.org/) plugin to create plots from data using the declarative [vegalite](https://vega.github.io/vega-lite/) syntax. This makes it easier to build reproducible reports.

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



