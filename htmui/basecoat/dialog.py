from typing import Literal

from htmy import Component, ComponentType, PropertyValue, SafeStr, as_component_sequence, html, join_classes

from .typing import ButtonSize, ButtonVariant

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/dialog/"

AlertDialogSize = Literal["sm"]


class handle_click:
    close: str = "if (event.target === this) this.close()"
    delete: str = "if (event.target === this) this.delete()"


class handle_close_button_click:
    close: str = "this.closest('dialog').close()"
    delete: str = "this.closest('dialog').delete()"


close_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
    'stroke-width="1.5" stroke="currentColor" class="size-5">'
    '<path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />'
    "</svg>"
)
"""`x-mark` icon from https://heroicons.com/."""


def close_button(
    icon: ComponentType = close_icon,
    *,
    onclick: str = handle_close_button_click.close,
    aria_label: str = "Close dialog",
    class_: str | None = None,
    size: ButtonSize | None = "icon-sm",
    variant: ButtonVariant | None = "ghost",
    **kwargs: PropertyValue,
) -> ComponentType:
    """Close button for dialogs."""
    if variant is not None:
        kwargs["data_variant"] = variant
    if size is not None:
        kwargs["data_size"] = size
    return html.button(
        icon,
        type="button",
        class_=join_classes("btn", class_),
        onclick=onclick,
        aria_label=aria_label,
        **kwargs,
    )


def dialog(
    *children: ComponentType,
    id: str,
    title: ComponentType,
    description: ComponentType | None = None,
    footer: Component | None = None,
    close_button: ComponentType | None = close_button(),  # noqa: B008
    figure: ComponentType | None = None,
    alert: bool = False,
    size: AlertDialogSize | None = None,
    class_: str | None = None,
    content_class: str | None = None,
    onclick: str = handle_click.close,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Dialog or alert-dialog modal.

    Arguments:
        *children: Dialog body content.
        id: Dialog element id.
        title: Dialog title.
        description: Optional description shown under the title.
        footer: Optional footer content, e.g. action buttons.
        close_button: Optional close button.
        figure: Optional media to show in a `figure` in the header.
        alert: Whether this is an alert dialog.
        size: Dialog size.
        class_: Extra CSS classes for the root `dialog` element.
        content_class: Extra CSS classes for the inner content.
        onclick: Click handler for the root `dialog` element. Ignored for alert dialogs.
        **kwargs: Extra attributes for the `dialog` element.
    """
    title_id = f"{id}-title"
    description_id = f"{id}-description"
    kwargs["aria_labelledby"] = title_id
    if not alert:
        kwargs["onclick"] = onclick
    if size is not None:
        kwargs["data_size"] = size
    if description is not None:
        kwargs["aria_describedby"] = description_id

    return html.dialog(
        html.div(
            html.header(
                html.figure(figure) if figure is not None else None,
                html.h2(title, id=title_id),
                html.p(description, id=description_id) if description is not None else None,
            ),
            html.section(*children) if len(children) > 0 else None,
            html.footer(*as_component_sequence(footer)) if footer else None,
            close_button,
            class_=content_class,
        ),
        id=id,
        class_=join_classes("alert-dialog" if alert else "dialog", class_),
        **kwargs,
    )


def show_dialog_button(
    title: ComponentType,
    *,
    dialog_id: str,
    class_: str | None = None,
    variant: ButtonVariant | None = "outline",
    **kwargs: PropertyValue,
) -> ComponentType:
    """Button that opens a dialog with `showModal()`."""
    if variant is not None:
        kwargs["data_variant"] = variant
    return html.button(
        title,
        class_=join_classes("btn", class_),
        type="button",
        onclick=f"document.getElementById('{dialog_id}').showModal()",
        **kwargs,
    )
