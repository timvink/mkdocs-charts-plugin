// Function copied from https://github.com/koaning/justcharts/blob/main/justcharts.js
async function parseSchema(viewdiv){
    let url = viewdiv.attributes['schema-url'].textContent;
    var resp = await fetch(url);
    var schema = await resp.json();
    return schema
}

// Function copied from https://github.com/koaning/justcharts/blob/main/justcharts.js
function parseInlineSchema(viewdiv){
    let inline = JSON.parse(viewdiv.textContent);
    
    let baseSchema = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    }

    let schema = Object.assign({}, baseSchema, inline)
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

    // mkdocs-material uses 'md-content
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


// Adapted from 
// https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#uml-diagram-example
//  https://github.com/koaning/justcharts/blob/main/justcharts.js
const chartplugin = className => {

  
    // Find all of our vegalite sources and render them.
    const blocks = document.querySelectorAll('vegachart');
    const surrogate = document.querySelector("div.md-content")

    for (let i = 0; i < blocks.length; i++) {

      const block = blocks[i]

      // get the vegalite JSON
      var schema = parseInlineSchema(block);

      // If width is not set at all, set to 'container'
      // Note we inserted <vegachart style='width: 100%'>..
      // So 'container' will use 100% width
      if (!('width' in schema)) {
          schema.width = "container"
      }

      // charts widths are screwed in tabbed-content (thinks its zero width)
      // we need to set an explicit, absolute width
      // is chart in tabbed-content?
      if (classnameInParents(block, "tabbed-content")) {
        var chart_width = schema.width || '';
        if (isNaN(chart_width)) {
            schema.width = findProperChartWidth(block);
        }
      }

      console.log(schema)
      
      // Render the chart into the (hidden) temp
      vegaEmbed(block, schema, {actions: false, "theme": "default", "renderer": "svg"});

    }
  }
  
  // This should be run on document load
  document.addEventListener("DOMContentLoaded", () => {chartplugin("vegalite")})