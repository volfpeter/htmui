from typing import Literal

from htmy import ComponentType, PropertyValue, html
from htmy.utils import join

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/card/"

CardSize = Literal["sm"]


def card(
    *children: ComponentType,
    class_: str | None = None,
    size: CardSize | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Card container.

    Arguments:
        *children: Card content.
        class_: Extra CSS classes for the root element.
        size: Optional denser layout size.
        **kwargs: Extra attributes for the root element.
    """
    if size is not None:
        kwargs["data_size"] = size

    return html.div(*children, class_=join("card", class_), **kwargs)
