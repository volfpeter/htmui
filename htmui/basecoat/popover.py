from typing import Literal, TypeAlias

from htmy import ComponentType, Properties, SafeStr, html, join_classes

from .button import ButtonVariant

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/popover/"


js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/popover.min.js" defer></script>'
)

PopoverAlign: TypeAlias = Literal["start", "center", "end"]
PopoverSide: TypeAlias = Literal["top", "bottom", "left", "right", "inline-start", "inline-end"]


def popover(
    *children: ComponentType,
    id: str,
    button_content: ComponentType,
    button_class: str | None = None,
    button_variant: ButtonVariant | None = "outline",
    popover_align: PopoverAlign | None = None,
    popover_class: str = "w-80",
    popover_side: PopoverSide | None = None,
) -> ComponentType:
    button_id = f"{id}-button"
    content_id = f"{id}-content"
    popover_props: Properties = {}
    if popover_align is not None:
        popover_props["data_align"] = popover_align
    if popover_side is not None:
        popover_props["data_side"] = popover_side

    return html.div(
        html.button(
            button_content,
            id=button_id,
            class_=join_classes("btn", button_class),
            **({"data_variant": button_variant} if button_variant else {}),
            aria_controls=content_id,
            aria_expanded="false",
            type="button",
        ),
        html.div(
            *children,
            id=content_id,
            data_popover="",
            aria_hidden="true",
            class_=popover_class,
            **popover_props,
        ),
        id=id,
        class_="popover",
    )
