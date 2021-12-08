# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).


## charts on invalid json


This one should give a plugin error because we can parse the JSOn in python (notice the trailing komma makes the JSON invalid):

```chartvegalite
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
    "autosize": {
        "type": "fit",
        "contains": "padding",
        "resize": "true"
    }
}
```