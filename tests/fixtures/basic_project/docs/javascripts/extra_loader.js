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

    // mkdocs-material uses 'md-content'
    var parent = findElementInParents(el, "md-content")

    if (parent === undefined) {
        // we can't find a suitable content parent
        // 800 width is a good default
        return '800'
    } else {
        // Use full width of parent
        // Should be equilavent to width: 100%
        return parent.offsetWidth
    }
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
    // is chart in tabbed-content?
    if (classnameInParents(block, "tabbed-content")) {
      var chart_width = schema.width || 'notset';
      if (isNaN(chart_width)) {
          schema.width = findProperChartWidth(block);
      }
    }

    console.log(schema)
    
    // Render the chart
    vegaEmbed(block, schema, {
        actions: false, 
        "theme": mkdocs_chart_plugin['vega_theme'], 
        "renderer": mkdocs_chart_plugin['vega_renderer']
    });
}

// Adapted from 
// https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#uml-diagram-example
//  https://github.com/koaning/justcharts/blob/main/justcharts.js
const chartplugin = className => {

  
    // Find all of our vegalite sources and render them.
    const blocks = document.querySelectorAll('vegachart');

    for (let i = 0; i < blocks.length; i++) {

      const block = blocks[i]
      const block_json = JSON.parse(block.textContent);

      // get the vegalite JSON
      if ('schema-url' in block_json) {
        fetchSchema(block_json['schema-url']).then(
            schema => embedChart(block, schema)
        );
      } else {
        embedChart(block, block_json);
      }  

    }
  }
  
  // This should be run on document load
  document.addEventListener("DOMContentLoaded", () => {chartplugin("vegalite")})