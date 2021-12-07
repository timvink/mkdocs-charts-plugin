from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


class ChartsPlugin(BasePlugin):

    config_scheme = (
        ("data_path", config_options.Type(str, default=".")),
        ("use_data_path", config_options.Type(bool, default=True)),
        ("vega_theme", config_options.Type(str, default="default")),
        ("vega_renderer", config_options.Type(str, default="svg")),
        ("vega_width", config_options.Type(str, default="container")),
        ("fallback_width", config_options.Type(str, default="800")),
    )

    def on_post_page(self, output, page, config, **kwargs):

        # save plugin config to javascript
        self.config["use_data_path"] = str(self.config["use_data_path"])

        add_variables = f"""
        <script>
        var mkdocs_chart_plugin = {self.config}
        </script>
        """

        # insert into end of page
        idx = output.index("</body>")
        output = output[:idx] + add_variables + output[idx:]

        return output

    # plan:
    # traverse upwards untill you find the `mkdocs.yml` file
    # read that,
    # find the directory of the docs_dir
    # parse the json, get the schema url, look in the docs_dir, read the JSON
    # return the source
    # import os
    # print(os.getcwd())
    # from pathlib import Path
    # import json
    # schema = json.loads(Path("docs/assets/charts/schemaone.json").read_text())
