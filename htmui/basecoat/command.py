from typing import Any

from htmy import ComponentType, SafeStr, html

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/command/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/command.min.js" defer></script>'
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
    input_placeholder: str = "Search...",
    aria_label: str | None = "Command menu",
    no_results_message: str = "No results found",
) -> ComponentType:
    menu_id = f"{id}-menu"
    div_props: dict[str, Any] = {}
    if aria_label:
        div_props["aria-label"] = aria_label

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
            class_="scrollbar",
            role="menu",
            aria_orientation="vertical",
            data_empty=no_results_message,
        ),
        id=id,
        class_="command rounded-lg border shadow-md",
        **div_props,
    )


def command_dialog(
    *items: ComponentType,
    id: str,
    input_icon: ComponentType = None,
    input_placeholder: str = "Search...",
    aria_label: str | None = "Command menu",
    no_results_message: str = "No results found",
    onclick: str | None = "if (event.target === this) this.close()",
) -> ComponentType:
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
    )
