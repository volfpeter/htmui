from htmy import ComponentType, SafeStr, html

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/popover/"


js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/popover.min.js" defer></script>'
)


def popover(
    *children: ComponentType,
    id: str,
    button_content: ComponentType,
    button_class: str = "btn-outline",
    popover_class: str = "w-80",
) -> ComponentType:
    button_id = f"{id}-button"
    content_id = f"{id}-content"
    return html.div(
        html.button(
            button_content,
            id=button_id,
            class_=button_class,
            aria_controls=content_id,
            aria_expanded="false",
            type="button",
        ),
        html.div(
            *children,
            id=content_id,
            data_popover="",
            aria_hidden="true",
            clsss_=popover_class,
        ),
        id=id,
        class_="popover",
    )
