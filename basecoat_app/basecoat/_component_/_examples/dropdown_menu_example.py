from htmy import ComponentType, html

from htmui.basecoat.dropdown_menu import dropdown_menu
from htmui.basecoat.menu import menu_item, menu_item_group, menu_separator


def example() -> ComponentType:
    return dropdown_menu(
        menu_item_group(
            menu_item(html.span("Commit")),
            menu_item(html.span("Pull")),
            menu_item(html.span("Push")),
            id="dropdown-group-1",
            label="Git",
            label_props={"class": "font-semibold"},
        ),
        menu_separator(),
        menu_item_group(
            menu_item(html.span("Review")),
            menu_item(html.span("Approve"), disabled=True),
            menu_item(html.span("Comment")),
            id="dropdown-group-2",
            label="Actions",
            label_props={"class": "font-semibold"},
        ),
        button_content="Dropdown menu",
        id="dropdown-example",
    )
