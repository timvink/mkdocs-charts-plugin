import os

from mkdocs.config import base, config_options
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin
from mkdocs.utils import copy_file

from mkdocs_charts_plugin.fences import fence_vegalite

HERE = os.path.dirname(os.path.abspath(__file__))


CUSTOM_FENCES = [{"name": "vegalite", "class": "vegalite", "format": fence_vegalite}]


def check_library(libnames, dependency):
    for lib in libnames:
        if dependency in str(lib):
            return True
    raise PluginError(
        f"[mkdocs_charts_plugin]: Missing 'extra_javascript' dependency for {dependency}. Please see setup instructions."
    )


class MkdocsMaterialOptions(base.Config):
    themes_light = config_options.ListOfItems(config_options.Type(str), default=["default"])
    themes_dark = config_options.ListOfItems(config_options.Type(str), default=["slate"])


class IntegrationsOptions(base.Config):
    mkdocs_material = config_options.SubConfig(MkdocsMaterialOptions)


class ChartsPlugin(BasePlugin):
    config_scheme = (
        ("data_path", config_options.Type(str, default="")),
        ("use_data_path", config_options.Type(bool, default=True)),
        ("vega_theme", config_options.Type(str, default="deprecated")),
        ("vega_theme_light", config_options.Type(str, default="default")),
        ("vega_theme_dark", config_options.Type(str, default="dark")),
        ("vega_renderer", config_options.Type(str, default="svg")),
        ("vega_width", config_options.Type(str, default="container")),
        ("fallback_width", config_options.Type(str, default="800")),
        ("integrations", config_options.SubConfig(IntegrationsOptions)),
    )

    def on_config(self, config, **kwargs):
        """
        Event trigger on config.
        See https://www.mkdocs.org/user-guide/plugins/#on_config.
        """
        if self.config.get("vega_theme") != "deprecated":
            raise PluginError(
                "[mkdocs_charts_plugin]: 'vega_theme' is deprecated and has been renamed to 'vega_theme_light'. Together with 'vega_theme_dark' this enables automatic theme switching. Please update your mkdocs.yml."
            )
    
        # Add pointer to mkdocs-charts-plugin.js
        # which is added to the output directory during on_post_build() event
        config["extra_javascript"] = ["js/mkdocs-charts-plugin.js"] + config["extra_javascript"]

        # Make sure custom fences are configured.
        parent_config = config.get("mdx_configs", {})
        if "pymdownx.superfences" not in parent_config:
            # If "superfences" was loaded through the "extra" plugin,
            # then its config will be in a different place
            parent_config = parent_config.get("pymdownx.extra", {})
        custom_fences = parent_config.get("pymdownx.superfences", {}).get("custom_fences", {})
        if not custom_fences:
            raise PluginError(
                "[mkdocs_charts_plugin]: You have not configured any custom fences, please see the setup instructions."
            )

        # Make sure javascript is configured
        libnames = config.get("extra_javascript", [])
        check_library(libnames, "vega")
        check_library(libnames, "vega-lite")
        check_library(libnames, "vega-embed")

    def on_post_page(self, output, page, config, **kwargs):
        """
        Insert plugin config as javascript variables into the page.
        """
        # Early return if not necessary
        if "vegalite" not in output:
            return output

        return self.add_javascript_variables(output, page, config)

    def on_post_build(self, config, **kwargs):
        """
        The post_build event does not alter any variables. Use this event to call post-build scripts.
        See https://www.mkdocs.org/user-guide/plugins/#on_post_build.
        """

        # Add mkdocs-charts-plugin.js
        js_output_base_path = os.path.join(config["site_dir"], "js")
        js_file_path = os.path.join(js_output_base_path, "mkdocs-charts-plugin.js")
        copy_file(
            os.path.join(os.path.join(HERE, "js"), "mkdocs-charts-plugin.js"),
            js_file_path,
        )

    def add_javascript_variables(self, html, page, config):
        """
        Each page might be in a different location.

        Determine path to root and add to html of page as a JS variable.
        """
        plugin_config = self.config.copy()

        # Find the path to the homepage
        docs_directory = config["docs_dir"]
        page_path = os.path.join(docs_directory, page.file.src_uri)
        path_to_homepage = os.path.relpath(docs_directory, os.path.dirname(page_path))

        if config.get("use_directory_urls"):
            path_to_homepage = os.path.join("..", path_to_homepage)
        plugin_config["path_to_homepage"] = path_to_homepage

        # ensure plugin config is string
        plugin_config["use_data_path"] = str(plugin_config["use_data_path"])

        # Config as javascript dictionary
        add_variables = f"""
        <script>
        var mkdocs_chart_plugin = {plugin_config}
        </script>
        """

        # insert into end of page
        idx = html.index("</body>")
        html = html[:idx] + add_variables + html[idx:]

        return html
