from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

from .typing import Align, ButtonVariant, Side

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/dropdown-menu/"


js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/dropdown-menu.min.js" defer></script>'
)


def dropdown_menu(
    *items: ComponentType,
    id: str,
    button_content: ComponentType,
    button_class: str | None = None,
    button_variant: ButtonVariant | None = "outline",
    class_: str | None = None,
    popover_class: str | None = None,
    popover_align: Align | None = None,
    popover_side: Side | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    menu_id = f"{id}-menu"
    button_id = f"{menu_id}-button"

    return html.div(
        html.button(
            button_content,
            type="button",
            id=button_id,
            aria_controls=menu_id,
            aria_expanded="false",
            aria_haspopup="menu",
            class_=join_classes("btn", button_class),
            **({"data_variant": button_variant} if button_variant else {}),
        ),
        html.div(
            html.div(
                *items,
                id=menu_id,
                role="menu",
                aria_labelledby=button_id,
            ),
            data_popover="",
            aria_hidden="true",
            class_="min-w-56" if popover_class is None else popover_class,
            data_align=popover_align,
            data_side=popover_side,
        ),
        class_=join_classes("dropdown-menu", class_),
        id=id,
        **kwargs,
    )
