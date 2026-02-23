from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/combobox/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/select.min.js" defer></script>'
)
"""Combobox uses the same JavaScript as the `select` component."""


dropdown_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="M8.25 15 12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9" /></svg>'
)
"""`chevron-up-down` icon from https://heroicons.com/."""


def combobox(
    *children: ComponentType,
    id: str,
    button_class: str = "btn-outline",
    button_label: str = "",
    button_icon: ComponentType = dropdown_icon,
    class_: str | None = None,
    search_placeholder: str = "Search...",
) -> ComponentType:
    button_id = f"{id}-button"
    listbox_id = f"{id}-listbox"
    return html.div(
        html.button(
            html.span(button_label),
            button_icon,
            class_=join_classes("btn-outline justify-between", button_class),
            id=button_id,
            type="button",
            aria_haspopup="listbox",
            aria_expanded="false",
            aria_controls=listbox_id,
        ),
        html.div(
            html.header(
                html.input_(
                    type="text",
                    value="",
                    placeholder=search_placeholder,
                    autocomplete="off",
                    autocorrect="off",
                    spellcheck="false",
                    aria_autocomplete="list",
                    role="combobox",
                    aria_expanded="false",
                    aria_controls=listbox_id,
                    aria_labelledby=button_id,
                )
            ),
            html.div(
                *children,
                role="listbox",
                id=listbox_id,
                aria_orientation="vertical",
                aria_labelledby=button_id,
            ),
            id=f"{id}-popover",
            data_popover="",
            aria_hidden="true",
        ),
        html.input_(type="hidden", name=f"select-{id}-value", value=""),
        class_=join_classes("select", class_),
        id=id,
    )


def option(
    *children: ComponentType,
    value: str,
    disabled: bool = False,
    force: bool = False,
    keywords: str | None = None,
    selected: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    """Search option component for `select_with_search`."""
    kwargs["role"] = "option"
    kwargs["data-value"] = value
    if disabled:
        kwargs["aria-disabled"] = "true"
    if force:
        kwargs["data-force"] = "true"
    if keywords:
        kwargs["data-keywords"] = keywords
    if selected:
        kwargs["aria-selected"] = "true"
    return html.div(*children, **kwargs)
