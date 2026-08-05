from typing import Literal, TypeAlias

from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/item/"

ItemVariant: TypeAlias = Literal["outline", "muted"]

ItemSize: TypeAlias = Literal["xs", "sm"]


def item(
    *children: ComponentType,
    variant: ItemVariant | None = None,
    size: ItemSize | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Item row.

    Arguments:
        *children: Item content.
        variant: Item variant.
        size: Item size.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    if variant is not None:
        kwargs["data_variant"] = variant
    if size is not None:
        kwargs["data_size"] = size

    return html.article(
        *children,
        class_=join_classes("item", class_),
        **kwargs,
    )


def item_link(
    *children: ComponentType,
    href: str,
    variant: ItemVariant | None = None,
    size: ItemSize | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Link-styled item row.

    Arguments:
        *children: Item content.
        href: Destination URL.
        variant: Item variant.
        size: Item size.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    if variant is not None:
        kwargs["data_variant"] = variant
    if size is not None:
        kwargs["data_size"] = size

    return html.a(
        *children,
        href=href,
        class_=join_classes("item", class_),
        **kwargs,
    )


def item_group(
    *children: ComponentType,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Group of related items.

    Arguments:
        *children: The contained items.
        class_: Extra CSS classes for the group.
        **kwargs: Extra attributes for the root element.
    """
    return html.div(
        *children,
        class_=join_classes("item-group", class_),
        role="list",
        **kwargs,
    )
