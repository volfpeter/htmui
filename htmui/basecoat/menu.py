from typing import Literal, TypeAlias

from htmy import ComponentType, Properties, PropertyValue, SafeStr, html

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/menu/"


MenuItemKind: TypeAlias = Literal["item", "checkbox", "radio"]
ShortcutKind: TypeAlias = Literal["kbd", "command"]

check_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="size-5">'
    '<path fill-rule="evenodd" d="M16.704 4.153a.75.75 0 0 1 .143 1.052l-8 10.5a.75.75 0 0 1-1.127.075l-4.5-4.5a.75.75 0 0 1 1.06-1.06l3.894 3.893 7.48-9.817a.75.75 0 0 1 1.05-.143Z" clip-rule="evenodd" />'
    "</svg>"
)
"""`check` icon from https://heroicons.com."""

_kind_has_indicator: set[MenuItemKind] = {"checkbox", "radio"}

_kind_to_role: dict[MenuItemKind, str] = {
    "item": "menuitem",
    "checkbox": "menuitemcheckbox",
    "radio": "menuitemradio",
}


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


def menu_item(  # noqa: C901
    *children: ComponentType,
    kind: MenuItemKind = "item",
    class_: str | None = None,
    disabled: bool = False,
    checked: bool | None = None,
    destructive: bool = False,
    filter: str | None = None,
    force: bool = False,
    keep_open: bool = False,
    keywords: str | None = None,
    shortcut: str | None = None,
    shortcut_kind: ShortcutKind = "kbd",
    indicator: ComponentType | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Menu item.

    Works inside `command`, `dropdown_menu`, or other `role="menu"` components.
    """
    role = _kind_to_role[kind]

    if disabled:
        kwargs["aria_disabled"] = "true"

    if checked is not None:
        kwargs["aria_checked"] = "true" if checked else "false"
    elif kind in _kind_has_indicator:
        kwargs["aria_checked"] = "false"

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

    indicator_comp: ComponentType | None = indicator
    if indicator_comp is None and kind in _kind_has_indicator:
        indicator_comp = check_icon

    shortcut_comp: ComponentType | None = None
    if shortcut is not None:
        if shortcut_kind == "command":
            shortcut_comp = html.span(shortcut, data_shortcut="")
        else:
            shortcut_comp = html.kbd(shortcut)

    return html.div(
        None if indicator_comp is None else html.span(indicator_comp, data_indicator=""),
        *children,
        shortcut_comp,
        role=role,
        **kwargs,
    )
