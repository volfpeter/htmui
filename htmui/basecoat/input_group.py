from typing import Literal, TypeAlias

from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/input-group/"

AddonAlign: TypeAlias = Literal["start", "end"]


def addon(
    *children: ComponentType,
    align: AddonAlign,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Addon positioned at the start or end of an input group.

    Arguments:
        *children: Addon content.
        align: On which side of the input the addon should be displayed.
        class_: Extra CSS classes for the addon.
        **kwargs: Extra attributes for the addon.
    """
    return html.span(*children, class_=class_, data_align=align, **kwargs)


def input_group(
    *children: ComponentType,
    vertical: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Container that display controls and addons as an input group.

    Arguments:
        *children: Controls and addons contained by the group.
        vertical: Whether to use a vertical layout.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    if vertical:
        kwargs["data_orientation"] = "vertical"

    return html.div(*children, class_=join_classes("input-group", class_), **kwargs)
