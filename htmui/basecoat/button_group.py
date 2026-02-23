from htmy import ComponentType, PropertyValue, html
from htmy.utils import join

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/button-group/"


def button_group(
    *children: ComponentType,
    class_: str = "",
    vertical: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    if "role" not in kwargs:
        kwargs["role"] = "group"

    if vertical:
        kwargs["data-orientation"] = "vertical"

    return html.div(*children, class_=join("button-group", class_), **kwargs)
