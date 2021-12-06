# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

```
    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
```

## Two charts

```vegalite
{
    "schema-url": "assets/charts/schemaone.json"
}
```

```vegalite
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {
    "url": "https://cdn.jsdelivr.net/gh/koaning/justcharts/bigmac.csv", 
    "format": {
        "type": "csv"
    }
    },
    "mark": "line",
    "encoding": {
    "x": {"field": "date", "type": "temporal"},
    "y": {"field": "local_price", "type": "quantitative"},
    "color": {"field": "currency_code", "type": "nominal"}
    },
    "width": "container",
    "autosize": {
        "type": "fit",
        "contains": "padding",
        "resize": "true"
    }
}
```



## Charts in tabs

=== "hi" 

    ```vegalite
    {
        "data":{
            "url": "https://cdn.jsdelivr.net/gh/koaning/justcharts/bigmac.csv",
            "format": {
                "type": "csv"
            }
        },
        "mark": "line",
        "encoding": {
            "x": {"field": "date", "type": "temporal"},
            "y": {"field": "local_price", "type": "quantitative"},
            "color": {"field": "currency_code", "type": "nominal"}
        },
        "width": "container",
        "title": "hello there 2"
    }
    ```

=== "there"
 

    ```vegalite
    {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "data": {
        "url": "https://cdn.jsdelivr.net/gh/koaning/justcharts/bigmac.csv", 
        "format": {
            "type": "csv"
        }
        },
        "mark": "line",
        "encoding": {
        "x": {"field": "date", "type": "temporal"},
        "y": {"field": "local_price", "type": "quantitative"},
        "color": {"field": "currency_code", "type": "nominal"}
        },
        "width": "600",
        "height": "350",
        "autosize": {
            "type": "fit",
            "contains": "padding",
            "resize": "true"
        }
    }
    ```

