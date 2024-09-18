# Options

You can customize the plugin by setting options in `mkdocs.yml`. For example:

=== ":octicons-file-code-16: mkdocs.yml"

  ```yaml
  plugins:
    - charts:
        vega_width: container
        vega_theme_light: default
        vega_theme_dark: dark
        vega_renderer: svg
        use_data_path: True
        data_path: ""
        integrations:
          mkdocs_material:
            themes_light:
              - default
            themes_dark:
              - slate
  ```

- `vega_width` (default is `container`). When not specified explicitly in the JSON schema, the `width` to use (see [vegalite customizing size](https://vega.github.io/vega-lite/docs/size.html)). When set to `container` width will be 100%.
- `vega_theme_light` (default is `default`). Specify one of the available [vegalite themes](https://vega.github.io/vega-themes/) to use when in light mode. When using the [mkdocs-material](https://squidfunk.github.io/mkdocs-material) theme with a light mode or the user's preferred color scheme in the browser or OS is "light", automatically render charts using this theme. [Color pallete toggle](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/#color-palette-toggle) is also supported.
- `vega_theme_dark` (default is `dark`). Specify one of the available [vegalite themes](https://vega.github.io/vega-themes/) to use when in dark mode. When using the [mkdocs-material](https://squidfunk.github.io/mkdocs-material) theme with a dark mode or the user's preferred color scheme in the browser or OS is "dark", automatically render charts using this theme. [Color pallete toggle](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/#color-palette-toggle) is also supported.
- `vega_renderer` (default is `svg`). Specify one of `canvas` or `svg`. See the [demo vegalite renderers](https://vega.github.io/vega-themes/).
- `use_data_path` (default is `True`). When `True`, any relative urls used in the JSON schema are relative to the `data_path`. When `False`, relative urls should be relative to the URL of the page.
- `data_path` (default is `""`). When `use_data_path` is enabled, the base path relative to the `docs/` folder.
- `integrations.mkdocs_material.themes_light` (default is `[default]`). When using the [mkdocs-material](https://squidfunk.github.io/mkdocs-material) theme, specify the light [color schemes](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/#color-scheme).
- `integrations.mkdocs_material.themes_dark` (default is `[slate]`). When using the [mkdocs-material](https://squidfunk.github.io/mkdocs-material) theme, specify the dark [color schemes](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/#color-scheme).

