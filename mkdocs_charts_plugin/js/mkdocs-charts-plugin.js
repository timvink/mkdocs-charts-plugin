// Adapted from https://github.com/koaning/justcharts/blob/main/justcharts.js
async function fetchSchema(url){
    var resp = await fetch(url);
    var schema = await resp.json();
    return schema
}


function classnameInParents(el, classname) {
    // check if class name in any parents
    while (el.parentNode) {
        el = el.parentNode;
        if (el.classList === undefined) {
            continue;
        }
        if (el.classList.contains(classname) ){
            return true;
        }
    }
    return false;
}

function findElementInParents(el, classname) {
    while (el.parentNode) {
        el = el.parentNode;
        if (el.classList === undefined) {
            continue;
        }
        if (el.classList.contains(classname) ){
            return el;
        }
    }
    return null;
}

function findProperChartWidth(el) {

    // mkdocs-material theme uses 'md-content'
    var parent = findElementInParents(el, "md-content")
    
    // mkdocs theme uses 'col-md-9'
    if (parent === undefined || parent == null) {
        var parent = findElementInParents(el, "col-md-9")        
    }
    if (parent === undefined || parent == null) {
        // we can't find a suitable content parent
        // 800 width is a good default
        return '800'
    } else {
        // Use full width of parent
        // Should bparent.offsetWidth - parseFloat(computedStyle.paddingLeft) - parseFloat(computedStyle.paddingRight) e equilavent to width: 100%
        computedStyle = getComputedStyle(parent)
        return parent.offsetWidth - parseFloat(computedStyle.paddingLeft) - parseFloat(computedStyle.paddingRight) 
    }
}

function updateURL(url) {
    // detect if absolute UR:
    // credits https://stackoverflow.com/a/19709846
    var r = new RegExp('^(?:[a-z]+:)?//', 'i');
    if (r.test(url)) {
        return url;
    }

    // If 'use_data_path' is set to true
    // schema and data urls are relative to
    // 'data_path', not the to current page
    // We need to update the specified URL
    // to point to the actual location relative to current page
    // Example:
    // Actual location data file: docs/assets/data.csv
    // Page: docs/folder/page.md
    // data url in page's schema: assets/data.csv
    // data_path in plugin settings: ""
    // use_data_path in plugin settings: True
    // path_to_homepage: ".." (this was detected in plugin on_post_page() event)
    // output url: "../assets/data.csv"
    if (mkdocs_chart_plugin['use_data_path'] == "True")  {
        new_url = window.location.href
        new_url = new_url.endsWith('/') ? new_url.slice(0, -1) : new_url;
        
        if (mkdocs_chart_plugin['path_to_homepage'] != "") {
            new_url += "/" + mkdocs_chart_plugin['path_to_homepage']
        }

        new_url = new_url.endsWith('/') ? new_url.slice(0, -1) : new_url;
        new_url += "/" + url
        new_url = new_url.endsWith('/') ? new_url.slice(0, -1) : new_url;

        if (mkdocs_chart_plugin['data_path'] != "") {
            new_url += "/" + mkdocs_chart_plugin['data_path']
        }

        return new_url
    }
    return url;
}

function embedChart(block, schema) {

    // Make sure the schema is specified
    let baseSchema = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    }
    schema = Object.assign({}, baseSchema, schema);

    // If width is not set at all, 
    // default is set to 'container'
    // Note we inserted <vegachart style='width: 100%'>..
    // So 'container' will use 100% width
    if (!('width' in schema)) {
        schema.width = mkdocs_chart_plugin['vega_width']
    }

    // Set default height if not specified
    // if (!('height' in schema)) {
    //     schema.height = mkdocs_chart_plugin['default_height']
    // }

    // charts widths are screwed in content tabs (thinks its zero width)
    // https://squidfunk.github.io/mkdocs-material/reference/content-tabs/?h=
    // we need to set an explicit, absolute width in those cases
    // detect if chart is in tabbed-content:
    if (classnameInParents(block, "tabbed-content")) {
      var chart_width = schema.width || 'notset';
      if (isNaN(chart_width)) {
          schema.width = findProperChartWidth(block);
      }
    }

    // Update URL if 'use_data_path' is configured
    if ("data" in schema) {
        if ("url" in schema.data) {
            schema.data.url = updateURL(schema.data.url)
        }
    }

    // Render the chart
    vegaEmbed(block, schema, {
        actions: false, 
        "theme": mkdocs_chart_plugin['vega_theme'], 
        "renderer": mkdocs_chart_plugin['vega_renderer']
    });
}

// Adapted from 
// https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#uml-diagram-example
// https://github.com/koaning/justcharts/blob/main/justcharts.js
const chartplugin = className => {

    // Find all of our vegalite sources and render them.
    const blocks = document.querySelectorAll('vegachart');

    for (let i = 0; i < blocks.length; i++) {

      const block = blocks[i]
      const block_json = JSON.parse(block.textContent);

      // get the vegalite JSON
      if ('schema-url' in block_json) {

        var url = updateURL(block_json['schema-url'])
        fetchSchema(url).then(
            schema => embedChart(block, schema)
        );
      } else {
        embedChart(block, block_json);
      }  

    }
  }
  

// Load when DOM ready
if (typeof document$ !== "undefined") {
    // compatibility with mkdocs-material's instant loading feature 
    document$.subscribe(function() {
        chartplugin("vegalite")
    })
} else {
    document.addEventListener("DOMContentLoaded", () => {chartplugin("vegalite")})
}
