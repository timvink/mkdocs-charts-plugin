# Options

- `vega_width` (default is `container`). When not specified explicitly in the JSON schema, the `width` to use (see [vegalite customizing size](https://vega.github.io/vega-lite/docs/size.html)). When set to `container` width will be 100%.
- `vega_theme` (default is `default`). Specify one of the available [vegalite themes](https://vega.github.io/vega-themes/).
- `vega_theme_dark` (default is `dark`). When using the [mkdocs-material](https://squidfunk.github.io/mkdocs-material) theme with a dark mode, automatically render charts using this theme. Dark mode toggle is also supported. Specify one of the available [vegalite themes](https://vega.github.io/vega-themes/).
- `vega_renderer` (default is `svg`). Specify one of the available [vegalite renderers](https://vega.github.io/vega-themes/).
- `use_data_path` (default is `True`). When `True`, any relative urls used in the JSON schema are relative to the `data_path`. When `False`, relative urls should be relative to the URL of the page.
- `data_path` (default is `""`). When `use_data_path` is enabled, the base path relative to the `docs/` folder.

