from typing import Literal, TypeAlias

from htmy import ComponentSequence, ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/tabs/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/tabs.min.js" defer></script>'
)

Orientation: TypeAlias = Literal["horizontal", "vertical"]

TabsVariant: TypeAlias = Literal["line"]


def tab_button(
    *children: ComponentType,
    id: str,
    panel_id: str,
    selected: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Tab button.

    Arguments:
        *children: Button content.
        id: Button ID.
        panel_id: The ID of the controlled tab panel.
        selected: Whether this tab is active.
        class_: Extra CSS classes for the button.
        **kwargs: Extra attributes for the button.
    """
    return html.button(
        *children,
        type="button",
        role="tab",
        id=id,
        aria_controls=panel_id,
        aria_selected="true" if selected else "false",
        tabindex="0" if selected else "-1",
        class_=class_,
        **kwargs,
    )


def tab_panel(
    *children: ComponentType,
    id: str,
    button_id: str,
    selected: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Tab panel.

    Arguments:
        *children: Panel content.
        id: Panel ID.
        button_id: The ID of the button that controls this tab panel.
        selected: Whether this panel is active.
        class_: Extra CSS classes for the panel.
        **kwargs: Extra attributes for the panel.
    """
    if not selected:
        kwargs["hidden"] = ""

    return html.div(
        *children,
        role="tabpanel",
        id=id,
        aria_labelledby=button_id,
        tabindex="-1",
        aria_selected="true" if selected else "false",
        class_=class_,
        **kwargs,
    )


def tabs(
    *panels: ComponentType,
    buttons: ComponentSequence,
    orientation: Orientation = "horizontal",
    variant: TabsVariant | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Tabs root with a tablist and panels.

    Arguments:
        *panels: Tab panels.
        buttons: Sequence of tab buttons.
        orientation: Tablist orientation.
        variant: Optional tablist style.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    return html.div(
        html.nav(*buttons, role="tablist", aria_orientation=orientation, data_variant=variant),
        *panels,
        class_=join_classes("tabs", class_),
        **kwargs,
    )
