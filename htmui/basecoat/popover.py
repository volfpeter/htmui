from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

from .button import ButtonVariant
from .typing import Align, Side

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/popover/"


js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/popover.min.js" defer></script>'
)


def popover(
    *children: ComponentType,
    id: str,
    button_content: ComponentType,
    button_class: str | None = None,
    button_variant: ButtonVariant | None = "outline",
    class_: str | None = None,
    popover_align: Align | None = None,
    popover_class: str | None = "w-72",
    popover_side: Side | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Popover with a trigger button and inline-positioned content.

    Arguments:
        *children: Popover content.
        id: Root element ID.
        button_content: Trigger button content.
        button_class: Extra CSS classes for the trigger button.
        button_variant: Trigger button variant.
        class_: Extra CSS classes for the root element.
        popover_align: Popover content alignment.
        popover_class: CSS classes for the popover content.
        popover_side: Preferred popover side.
        **kwargs: Extra attributes for the root element.
    """
    trigger_id = f"{id}-trigger"
    content_id = f"{id}-popover"

    return html.div(
        html.button(
            button_content,
            id=trigger_id,
            type="button",
            aria_controls=content_id,
            aria_expanded="false",
            class_=join_classes("btn", button_class),
            data_variant=button_variant,
        ),
        html.div(
            *children,
            id=content_id,
            data_popover="",
            aria_hidden="true",
            class_=popover_class,
            data_align=popover_align,
            data_side=popover_side,
        ),
        id=id,
        class_=join_classes("popover", class_),
        **kwargs,
    )
