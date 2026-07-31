from typing import Literal, TypeAlias

from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/button/"

ButtonVariant: TypeAlias = Literal["outline", "secondary", "ghost", "destructive", "link"]

ButtonSize: TypeAlias = Literal["xs", "sm", "default", "lg", "icon", "icon-xs", "icon-sm", "icon-lg"]


def button(
    *children: ComponentType,
    variant: ButtonVariant | None = None,
    size: ButtonSize | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Button component.

    Arguments:
        *children: Button content.
        variant: Button variant.
        size: Button size.
        class_: Extra CSS classes for the button.
        **kwargs: Extra attributes for the button.
    """
    if variant is not None:
        kwargs["data_variant"] = variant
    if size is not None:
        kwargs["data_size"] = size
    return html.button(*children, class_=join_classes("btn", class_), type_="button", **kwargs)
