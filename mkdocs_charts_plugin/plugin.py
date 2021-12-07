import os

from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


class ChartsPlugin(BasePlugin):

    config_scheme = (
        ("data_path", config_options.Type(str, default="")),
        ("use_data_path", config_options.Type(bool, default=True)),
        ("vega_theme", config_options.Type(str, default="default")),
        ("vega_renderer", config_options.Type(str, default="svg")),
        ("vega_width", config_options.Type(str, default="container")),
        ("fallback_width", config_options.Type(str, default="800")),
    )

    def on_page_content(self, html, page, config, files, **kwargs):
        """
        Store reference to homepage
        """
        if page.file.src_path == "index.md":
            self.homepage = page.file

    def on_post_page(self, output, page, config, **kwargs):
        """
        Insert plugin config as javascript variables into the page.
        """
        # Find path to homepage
        path_to_homepage = self.homepage.url_relative_to(page.file)
        path_to_homepage = os.path.dirname(path_to_homepage)
        if config.get("use_directory_urls"):
            path_to_homepage = os.path.join("..", path_to_homepage)
        self.config["path_to_homepage"] = path_to_homepage

        # ensure plugin config is string
        self.config["use_data_path"] = str(self.config["use_data_path"])

        # Config as javascript dictionary
        add_variables = f"""
        <script>
        var mkdocs_chart_plugin = {self.config}
        </script>
        """

        # insert into end of page
        idx = output.index("</body>")
        output = output[:idx] + add_variables + output[idx:]

        return output
