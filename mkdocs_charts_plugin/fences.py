from pymdownx.superfences import _escape

from mkdocs.exceptions import PluginError

from mkdocs_charts_plugin.utils import _validateJSON


def fence_vegalite(source, language, class_name, options, md, **kwargs):
    """
    Inspired by https://github.com/facelessuser/pymdown-extensions/blob/8ee5b5caec8f9373e025f50064585fb9d9b71f86/pymdownx/superfences.py#L146
    """  # noqa

    if not _validateJSON(source):
        raise PluginError(f"Your vegalite syntax is not valid JSON. Fix {source}")

    classes = kwargs["classes"]
    id_value = kwargs["id_value"]
    attrs = kwargs["attrs"]

    if class_name:
        classes.insert(0, class_name)

    id_value = ' id="{}"'.format(id_value) if id_value else ""
    classes = ' class="{}"'.format(" ".join(classes)) if classes else ""
    attrs = (
        " " + " ".join('{k}="{v}"'.format(k=k, v=v) for k, v in attrs.items())
        if attrs
        else ""
    )

    return f"<vegachart style='width: 100%' {id_value}{classes}{attrs}>{_escape(source)}</vegachart>"
