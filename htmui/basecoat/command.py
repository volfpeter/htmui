from typing import Any

from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

from .menu import menu_item

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/command/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/command.min.js" defer></script>'
)


search_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-6"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" /></svg>'
)
"""`magnifying-glass` icon from https://heroicons.com/."""


def command(
    *items: ComponentType,
    id: str,
    input_icon: ComponentType = None,
    input_placeholder: str = "Type a command or search...",
    aria_label: str | None = "Command menu",
    no_results_message: str = "No results found.",
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """Basecoat v1 command menu.

    Items should be created with `menu_item(..., filter=..., keywords=...)` from
    `htmui.basecoat.menu`. The `filter` text is required for the command JavaScript
    to match the item while typing.
    """
    menu_id = f"{id}-menu"
    root_props: dict[str, Any] = {"id": id}
    if aria_label is not None:
        root_props["aria_label"] = aria_label

    return html.div(
        html.header(
            input_icon,
            html.input_(
                type="text",
                id=f"{id}-input",
                role="combobox",
                autocomplete="off",
                autocorrect="off",
                placeholder=input_placeholder,
                spellcheck="false",
                aria_autocomplete="list",
                aria_expanded="true",
                aria_controls=menu_id,
            ),
        ),
        html.div(
            *items,
            id=menu_id,
            role="menu",
            aria_orientation="vertical",
            data_empty=no_results_message,
        ),
        class_=join_classes("command", class_),
        **root_props,
        **kwargs,
    )


def command_item(
    *children: ComponentType,
    filter: str,
    keywords: str | None = None,
    shortcut: str | None = None,
    indicator: ComponentType | None = None,
    disabled: bool = False,
    force: bool = False,
    keep_open: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """Basecoat v1 command item (`filter` is required for the command JS to match it)."""
    return menu_item(
        *children,
        filter=filter,
        keywords=keywords,
        shortcut=shortcut,
        shortcut_kind="command",
        indicator=indicator,
        disabled=disabled,
        force=force,
        keep_open=keep_open,
        class_=class_,
        **kwargs,  # type: ignore[arg-type]
    )


def command_dialog(
    *items: ComponentType,
    id: str,
    input_icon: ComponentType = None,
    input_placeholder: str = "Type a command or search...",
    aria_label: str | None = "Command menu",
    no_results_message: str = "No results found.",
    onclick: str | None = "if (event.target === this) this.close()",
    **kwargs: PropertyValue,
) -> ComponentType:
    """Basecoat v1 command palette wrapped in `<dialog class="command-dialog">`."""
    return html.dialog(
        command(
            *items,
            id=f"{id}-command",
            input_icon=input_icon,
            input_placeholder=input_placeholder,
            aria_label=None,
            no_results_message=no_results_message,
        ),
        id=id,
        class_="command-dialog",
        aria_label=aria_label,
        onclick=onclick,
        **kwargs,
    )
