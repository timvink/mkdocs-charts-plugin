from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


class ChartsPlugin(BasePlugin):

    config_scheme = (("data_path", config_options.Type(str, default=".")),)

    def on_config(self, config):
        """

        See https://www.mkdocs.org/user-guide/plugins/#on_config
        Args:
            config

        Returns:
            Config
        """
        pass
