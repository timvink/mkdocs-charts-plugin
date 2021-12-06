# mkdocs-charts-plugin

Mkdocs plugin to create plots from data.


# TODO:


## set width correctly 

IDea:

- recusirve look up all parent nodes
    - https://stackoverflow.com/questions/7332179/how-to-recursively-search-all-parentnodes
- if in a tabbedContent
    if not width explicitly set
    set width to be at least 800
    try to detect actual width

if width not set
- else set width to be 100%

if height not set
 set to 300 or so

 https://vega.github.io/vega-lite/docs/size.html


## support data files located in `docs/` folder

we need a relative URL for the data

--> parse it in the fence_ function?
- is valid json
- convert to json
- look for .get('data').get('url')
- is absolute?
- some mkdocs function to get absolute url

- in the plugin docs, is the URL relative to mkdocs.yml or to `docs/` ?


## set plugin options:

- default_renderer [svg/canvas]
- default_theme
- default_height

pass via CSS data-attributes to javascript, vega-embed? 


## validator fences

- add a validator python function for is valid JSON

## plugin to include JS and set the markdown_extension also?



## Toggle dark mode

- theme, switch to dark mode with mkdocs-material

toggle themes
there's a refresh() function shown in the <script> source
https://vega.github.io/vega-themes/?renderer=canvas&theme=quartz

## Styling

- CSS for styling colors to use/match mkdocs-material ?

## More

- write docs
    - page on how it works
- use the plugin in the print-site demo
- promote the plugin
- add plotly express backend also?

# Credits 

https://github.com/koaning/justcharts
https://facelessuser.github.io/pymdown-extensions/extras/mermaid/
https://vega.github.io/vega-lite/docs/config.html
