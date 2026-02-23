from htmy import ComponentSequence, ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/tabs/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/tabs.min.js" defer></script>'
)


def tab_button(
    *children: ComponentType,
    id: str,
    panel_id: str,
    selected: bool = False,
    class_: str | None = None,
) -> ComponentType:
    return html.button(
        *children,
        type="button",
        role="tab",
        id=id,
        aria_controls=panel_id,
        aria_selected="true" if selected else "false",
        tabindex="0",
        class_=class_,
    )


def tab_panel(
    *children: ComponentType,
    id: str,
    button_id: str,
    selected: bool = False,
    class_: str | None = None,
) -> ComponentType:
    return html.div(
        *children,
        role="tabpanel",
        id=id,
        aria_labelledby=button_id,
        tabindex="-1",
        aria_selected="true" if selected else "false",
        hidden=None if selected else "",
        class_=class_,
    )


def tabs(
    *panels: ComponentType,
    buttons: ComponentSequence,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    return html.div(
        html.nav(*buttons, role="tablist", aria_orientation="horizontal", class_="w-full"),
        *panels,
        class_=join_classes("tabs w-full", class_),
        **kwargs,
    )
