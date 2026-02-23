from htmy import Component, ComponentType, PropertyValue, SafeStr, as_component_sequence, html

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/dialog/"


class handle_click:
    close: str = "if (event.target === this) this.close()"
    delete: str = "if (event.target === this) this.delete()"


def dialog(
    *children: ComponentType,
    id: str,
    title: str,
    actions: Component = None,
    close_button: ComponentType = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    title_id = f"{id}-title"
    return html.dialog(
        html.div(
            html.header(html.h2(title, id=title_id)),
            html.section(*children) if children else None,
            html.footer(*as_component_sequence(actions)) if actions else None,
            close_button if close_button else None,
        ),
        id=id,
        class_="dialog w-full sm:max-w-[425px] max-h-[612px]",
        aria_labelledby=title_id,
        **kwargs,
    )


class handle_close_button_click:
    close: str = "this.closest('dialog').close()"
    delete: str = "this.closest('dialog').delete()"


close_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
    'stroke-width="1.5" stroke="currentColor" class="size-6">'
    '<path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />'
    "</svg>"
)
"""`x-mark` icon from https://heroicons.com/."""


def close_button(
    icon: ComponentType = close_icon,
    *,
    onclick: str = handle_close_button_click.close,
    aria_label: str = "Close dialog",
) -> ComponentType:
    return html.button(
        icon,
        class_="cursor-pointer",
        type="button",
        onclick=onclick,
        aria_label=aria_label,
    )


def show_dialog_button(
    title: ComponentType, *, dialog_id: str, class_: str = "btn-outline"
) -> ComponentType:
    return html.button(
        title,
        class_=class_,
        type="button",
        onclick=f"document.getElementById('{dialog_id}').showModal()",
    )
