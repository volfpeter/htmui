import json
from typing import Any, Literal

from htmy import ComponentType, PropertyValue, SafeStr, XBool, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/combobox/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/combobox.min.js" defer></script>'
)

dropdown_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="M8.25 15 12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9" /></svg>'
)
"""`chevron-up-down` icon from https://heroicons.com/."""


def option(
    *children: ComponentType,
    value: str | None = None,
    label: str | None = None,
    filter: str | None = None,
    force: bool = False,
    disabled: bool = False,
    keywords: str | None = None,
    selected: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Search option for `combobox`.

    Arguments:
        value: The value submitted by the hidden input.
        label: Optional label that overrides the option content in
            the displayed input when the `option` is selected.
        filter: Optional filter text.
        force: When `true`, the option always stays visible.
        disabled: Whether the option is disabled and non-selectable.
        keywords: Optional keywords for filtering.
        selected: Whether the option is initially selected.
        **kwargs: Other attributes passed directly to the element.
    """
    kwargs["role"] = "option"
    if value is not None:
        kwargs["data-value"] = value
    if label is not None:
        kwargs["data-label"] = label
    if keywords is not None:
        kwargs["data-keywords"] = keywords
    if filter is not None:
        kwargs["data-filter"] = filter
    if force:
        kwargs["data-force"] = "true"
    if disabled:
        kwargs["aria-disabled"] = "true"
    if selected:
        kwargs["aria-selected"] = "true"
    return html.div(*children, **kwargs)


def group(
    *items: ComponentType,
    heading: ComponentType,
    heading_id: str,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    `div` with `role="group"`, containing options with a linked heading.

    Arguments:
        heading: Group heading content.
        heading_id: Id of the heading element; also used as `aria-labelledby`.
        **kwargs: Other attributes passed through to the root element.
    """
    kwargs["role"] = "group"
    kwargs["aria-labelledby"] = heading_id
    return html.div(
        html.span(heading, role="heading", id=heading_id),
        *items,
        **kwargs,
    )


def combobox(  # noqa: C901
    *items: ComponentType,
    name: str,
    value: str | list[Any] | None = None,
    placeholder: str | None = None,
    disabled: bool = False,
    invalid: bool = False,
    empty_message: str | None = None,
    class_: str | None = None,
    multi: bool = False,
    auto_highlight: bool = False,
    close_on_select: bool = False,
    data_format: Literal["object"] | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Combobox component root.

    The component is input-first: the visible text input filters the list of
    options, while a hidden input stores the value submitted under `name`.

    Internal element IDs are derived from `name` automatically.

    Arguments:
        name: The name of the hidden input.
        value: The value of the combobox.
        placeholder: Placeholder text for the visible input.
        disabled: Disables the combobox.
        invalid: Mark the input as invalid for accessibility and validation.
        empty_message: Optional message shown when the filter matches nothing.
        class_: Additional classes for the root element.
        multi: Whether multi-selection is enabled.
        auto_highlight: Make the first visible option active when the list opens
            or filters, so Enter can select it without arrowing first.
        close_on_select: Whether to close the popover after selecting an option
            in multi-selection mode.
        data_format: Submitted value format. Use `"object"` to serialize selected
            values as `{ value, label }` objects.
        **kwargs: Extra attributes for the root element.
    """
    root_id = f"{name}-root"
    input_id = f"{root_id}-input"
    popover_id = f"{root_id}-popover"
    listbox_id = f"{root_id}-listbox"

    if multi and close_on_select:
        kwargs["data-close-on-select"] = "true"
    if auto_highlight:
        kwargs["data-auto-highlight"] = "true"
    if data_format is not None:
        kwargs["data-format"] = data_format

    input_attrs: dict[str, PropertyValue] = {
        "type": "text",
        "role": "combobox",
        "placeholder": placeholder,
        "autocomplete": "off",
        "autocorrect": "off",
        "spellcheck": "false",
        "aria-autocomplete": "list",
        "aria-expanded": "false",
        "aria-controls": listbox_id,
        "id": input_id,
    }
    if disabled:
        input_attrs["disabled"] = XBool.true
    if invalid:
        input_attrs["aria-invalid"] = "true"

    listbox_attrs: dict[str, PropertyValue] = {
        "role": "listbox",
        "id": listbox_id,
        "aria-labelledby": input_id,
        "aria-orientation": "vertical",
    }
    if multi:
        listbox_attrs["aria-multiselectable"] = "true"
    if empty_message is not None:
        listbox_attrs["data-empty"] = empty_message

    effective_value: str
    if value is None:
        effective_value = "" if not multi else "[]"
    elif isinstance(value, (list, tuple)):
        effective_value = json.dumps(list(value))
    else:
        effective_value = str(value)

    return html.div(
        html.input_(**input_attrs),
        dropdown_icon,
        html.div(
            html.div(*items, **listbox_attrs),
            id=popover_id,
            data_popover=XBool.true,
            aria_hidden="true",
        ),
        html.input_(type="hidden", name=name, value=effective_value),
        id=root_id,
        class_=join_classes("combobox", class_),
        **kwargs,
    )
