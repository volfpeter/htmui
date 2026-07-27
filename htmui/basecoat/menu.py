from typing import Literal

from htmy import ComponentType, Properties, PropertyValue, html

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/menu/"


def menu(
    *items: ComponentType,
    id: str,
    aria_labelledby: str | None = None,
    aria_label: str | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """Menu list wrapper."""
    if aria_labelledby is not None:
        kwargs["aria_labelledby"] = aria_labelledby
    if aria_label is not None:
        kwargs["aria_label"] = aria_label
    return html.div(*items, id=id, class_=class_, role="menu", **kwargs)


def menu_item_group(
    *items: ComponentType,
    id: str,
    label: str,
    label_props: Properties | None = None,
) -> ComponentType:
    """Menu item group with a heading."""
    label_id = f"{id}-label"
    return html.div(
        html.div(label, id=label_id, role="heading", **(label_props or {})),
        *items,
        id=id,
        role="group",
        aria_labelledby=label_id,
    )


def menu_separator() -> ComponentType:
    """Menu item separator."""
    return html.hr(role="separator")


def menu_item(  # noqa: C901
    *children: ComponentType,
    class_: str | None = None,
    disabled: bool = False,
    checked: bool | None = None,
    destructive: bool = False,
    filter: str | None = None,
    keywords: str | None = None,
    shortcut: str | None = None,
    shortcut_kind: Literal["kbd", "command"] = "kbd",
    indicator: ComponentType | None = None,
    force: bool = False,
    keep_open: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Menu item.

    Works inside `command`, `dropdown_menu`, or other `role="menu"` components.
    """
    if disabled:
        kwargs["aria_disabled"] = "true"
    if checked is not None:
        kwargs["aria_checked"] = "true" if checked else "false"
    if destructive:
        kwargs["data_variant"] = "destructive"
    if filter is not None:
        kwargs["data_filter"] = filter
    if keywords is not None:
        kwargs["data_keywords"] = keywords
    if force:
        kwargs["data_force"] = ""
    if keep_open:
        kwargs["data_keep_command_open"] = ""
    if class_ is not None:
        kwargs["class_"] = class_

    shortcut_comp: ComponentType | None = None
    if shortcut is not None:
        if shortcut_kind == "command":
            shortcut_comp = html.span(shortcut, data_shortcut="")
        else:
            shortcut_comp = html.kbd(shortcut)

    return html.div(
        None if indicator is None else html.span(indicator, data_indicator=""),
        *children,
        shortcut_comp,
        role="menuitem",
        **kwargs,
    )
