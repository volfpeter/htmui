import json
from typing import Any, Literal

from htmy import ComponentType, PropertyValue, SafeStr, XBool, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/select/"


js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/select.min.js" defer></script>'
)


# `chevron-down` icon, matching the BasecoatUI reference markup.
_trigger_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
    'class="lucide lucide-chevron-down text-muted-foreground opacity-50 shrink-0">'
    '<path d="m6 9 6 6 6-6" /></svg>'
)


def option(
    *children: ComponentType,
    value: str | None = None,
    label: str | None = None,
    disabled: bool = False,
    selected: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    `div` with `role="option"` for `select`.

    Arguments:
        value: Maps to `data-value`.
        label: Optional `data-label` overriding the trigger/display text.
        disabled: Whether the option is disabled.
        selected: Whether the option is selected.
        **kwargs: Other attributes passed directly to the element.
    """
    kwargs["role"] = "option"
    if value is not None:
        kwargs["data-value"] = value
    if label is not None:
        kwargs["data-label"] = label
    if disabled:
        kwargs["aria-disabled"] = "true"
    if selected:
        kwargs["aria-selected"] = "true"
    return html.div(*children, **kwargs)


def separator(**kwargs: PropertyValue) -> ComponentType:
    """An `hr` separator between groups/options."""
    return html.hr(role="separator", **kwargs)


def group(
    *items: ComponentType,
    heading: ComponentType,
    heading_id: str,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    `div` with `role="group"`, containing options with a linked heading.

    Arguments:
        label: Group heading content.
        heading_id: Id of the heading span; also used as `aria-labelledby`.
        **kwargs: Other attributes passed through to the root element.
    """
    kwargs["role"] = "group"
    kwargs["aria-labelledby"] = heading_id
    return html.div(
        html.span(heading, role="heading", id=heading_id),
        *items,
        **kwargs,
    )


def select(  # noqa: C901
    *items: ComponentType,
    name: str,
    placeholder: str | None = None,
    multiple: bool = False,
    close_on_select: bool = False,
    format: Literal["object"] | None = None,
    value: str | list[Any] | None = None,
    disabled: bool = False,
    invalid: bool = False,
    trigger_class: str | None = None,
    listbox_class: str | None = None,
    popover_class: str | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Select component root.

    It contains a hidden input, which is submitted under `name`. Internal element IDs
    are derived from `name` automatically.

    Arguments:
        name: The name of the hidden input.
        placeholder: Text shown in the trigger when nothing is selected.
        multiple: Allow selecting multiple options.
        close_on_select: Whether to close the select after selecting an option.
            It only applies to the multi-select case.
        format: Value format submitted by the hidden input. Use `"object"` to
            send the full option object.
        value: Initially selected value. Pass a string for single select or
            a list for multiple select.
        disabled: Disable the trigger button.
        invalid: Mark the select as invalid for accessibility and validation.
        trigger_class: Additional classes for the trigger button.
        listbox_class: Additional classes for the listbox popup.
        popover_class: Additional classes for the popover wrapper.
        class_: Additional classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    id = f"{name}-root"
    trigger_id = f"{id}-trigger"
    popover_id = f"{id}-popover"
    listbox_id = f"{id}-listbox"

    root_attrs: dict[str, PropertyValue] = dict(kwargs)
    if placeholder is not None:
        root_attrs["data-placeholder"] = placeholder
    if multiple and close_on_select:
        root_attrs["data-close-on-select"] = "true"
    if format is not None:
        root_attrs["data-format"] = format

    trigger_attrs: dict[str, PropertyValue] = {
        "type": "button",
        "id": trigger_id,
        "aria-haspopup": "listbox",
        "aria-expanded": "false",
        "aria-controls": listbox_id,
    }
    if disabled:
        trigger_attrs["disabled"] = XBool.true
    if invalid:
        trigger_attrs["aria-invalid"] = "true"
    trigger_attrs["class"] = trigger_class

    popover_attrs: dict[str, PropertyValue] = {
        "id": popover_id,
        "data-popover": "",
        "aria-hidden": "true",
    }
    if popover_class:
        popover_attrs["class"] = popover_class

    listbox_attrs: dict[str, PropertyValue] = {
        "role": "listbox",
        "id": listbox_id,
        "aria-orientation": "vertical",
        "aria-labelledby": trigger_id,
    }
    if multiple:
        listbox_attrs["aria-multiselectable"] = "true"
    if listbox_class:
        listbox_attrs["class"] = listbox_class

    effective_value: str
    if value is None:
        effective_value = ""
    elif isinstance(value, (list, tuple)):
        effective_value = json.dumps(list(value))
    else:
        effective_value = str(value)

    return html.div(
        html.button(
            html.span(placeholder or "", class_="truncate"),
            _trigger_icon,
            **trigger_attrs,
        ),
        html.div(
            html.div(*items, **listbox_attrs),
            **popover_attrs,
        ),
        html.input_(
            type="hidden",
            name=name,
            value=effective_value,
        ),
        id=id,
        class_=join_classes("select", class_),
        **root_attrs,
    )
