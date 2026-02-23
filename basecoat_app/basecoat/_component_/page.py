from fastapi import HTTPException
from htmy import Component, html

from basecoat_app.component_docs import ComponentData, component_docs
from htmui.basecoat import (
    accordion,
    alert,
    badge,
    breadcrumb,
    button_group,
    card,
    codeblock,
    combobox,
    command,
    dialog,
    dropdown_menu,
    field,
    pagination,
    popover,
    radio_group,
    select,
    sidebar,
    spinner,
    tabs,
    theme_switcher,
    toast,
)

from ._examples import (
    accordion_example,
    alert_dialog_example,
    alert_example,
    badge_example,
    breadcrumb_example,
    button_group_example,
    card_example,
    codeblock_example,
    combobox_example,
    command_example,
    dialog_example,
    dropdown_menu_example,
    field_example,
    pagination_example,
    popover_example,
    radio_group_example,
    select_example,
    sidebar_example,
    spinner_example,
    tabs_example,
    theme_switcher_example,
    toast_example,
)

basecoat_components: dict[str, ComponentData] = {
    "accordion": {
        "title": "Accordion",
        "code_example": accordion_example,
        "component_impl": accordion,
        "example": None,
    },
    "alert": {
        "title": "Alert",
        "code_example": alert_example,
        "component_impl": alert,
        "example": None,
    },
    "alert-dialog": {
        "title": "Alert Dialog",
        "code_example": alert_dialog_example,
        "component_impl": dialog,
        "example": None,
    },
    "badge": {
        "title": "Badge",
        "code_example": badge_example,
        "component_impl": badge,
        "example": None,
    },
    "breadcrumb": {
        "title": "Breadcrumb",
        "code_example": breadcrumb_example,
        "component_impl": breadcrumb,
        "example": None,
    },
    "button-group": {
        "title": "Button Group",
        "code_example": button_group_example,
        "component_impl": button_group,
        "example": None,
    },
    "card": {
        "title": "Card",
        "code_example": card_example,
        "component_impl": card,
        "example": None,
    },
    "codeblock": {
        "title": "Code Block",
        "code_example": codeblock_example,
        "component_impl": codeblock,
        "example": None,
    },
    "combobox": {
        "title": "Combobox",
        "code_example": combobox_example,
        "component_impl": combobox,
        "example": None,
    },
    "command": {
        "title": "Command",
        "code_example": command_example,
        "component_impl": command,
        "example": None,
    },
    "dialog": {
        "title": "Dialog",
        "code_example": dialog_example,
        "component_impl": dialog,
        "example": None,
    },
    "dropdown-menu": {
        "title": "Dropdown Menu",
        "code_example": dropdown_menu_example,
        "component_impl": dropdown_menu,
        "example": None,
    },
    "field": {
        "title": "Field",
        "code_example": field_example,
        "component_impl": field,
        "example": None,
    },
    "pagination": {
        "title": "Pagination",
        "code_example": pagination_example,
        "component_impl": pagination,
        "example": None,
    },
    "popover": {
        "title": "Popover",
        "code_example": popover_example,
        "component_impl": popover,
        "example": None,
    },
    "radio-group": {
        "title": "Radio Group",
        "code_example": radio_group_example,
        "component_impl": radio_group,
        "example": None,
    },
    "select": {
        "title": "Select",
        "code_example": select_example,
        "component_impl": select,
        "example": None,
    },
    "sidebar": {
        "title": "Sidebar",
        "code_example": sidebar_example,
        "component_impl": sidebar,
        "example": html.p("See the sidebar of the page."),
    },
    "spinner": {
        "title": "Spinner",
        "code_example": spinner_example,
        "component_impl": spinner,
        "example": None,
    },
    "tabs": {
        "title": "Tabs",
        "code_example": tabs_example,
        "component_impl": tabs,
        "example": None,
    },
    "theme-switcher": {
        "title": "Theme Switcher",
        "code_example": theme_switcher_example,
        "component_impl": theme_switcher,
        "example": None,
    },
    "toast": {
        "title": "Toast",
        "code_example": toast_example,
        "component_impl": toast,
        "example": None,
    },
}


def metadata(component: str) -> dict[str, str]:
    data = basecoat_components.get(component)
    return {"title": "Not Found" if data is None else data["title"]}


def page(component: str) -> Component:
    data = basecoat_components.get(component)
    if data is None:
        raise HTTPException(404)

    return component_docs(
        data["code_example"],
        component_name=data["title"],
        impl=data["component_impl"],
        example=data["example"],
    )
