from htmy import ComponentType, html

from htmui.basecoat.dropdown_menu import dropdown_menu
from htmui.basecoat.menu import menu_item, menu_item_group
from htmui.basecoat.separator import separator


def example() -> ComponentType:
    return dropdown_menu(
        menu_item_group(
            menu_item(html.span("Commit"), shortcut="⌘+K"),
            menu_item(html.span("Pull"), shortcut="⇧⌘P"),
            menu_item(html.span("Push"), shortcut="⇧⌘K"),
            id="dropdown-group-1",
            label="Git",
            label_props={"class": "font-semibold"},
        ),
        separator,
        menu_item_group(
            menu_item(html.span("Approve"), kind="radio", checked=True, shortcut="⌘+A"),
            menu_item(html.span("Comment"), kind="radio", disabled=True, shortcut="⌘+/"),
            menu_item(html.span("Reject"), kind="radio", shortcut="⌘+R"),
            id="dropdown-group-2",
            label="Review",
            label_props={"class": "font-semibold"},
        ),
        button_content="Dropdown menu",
        id="dropdown-example",
    )
