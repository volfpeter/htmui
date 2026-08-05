from htmy import ComponentType, PropertyValue, XBool, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/radio-group/"


def radio_input(
    *children: ComponentType,
    name: str,
    value: str,
    description: ComponentType | None = None,
    checked: bool = False,
    disabled: bool = False,
    invalid: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Radio option, a horizontal field with input and label.

    Arguments:
        *children: Label content.
        name: The name of the input.
        value: Value submitted when this option is selected.
        description: Optional description shown under the label.
        checked: Whether the option is initially selected.
        disabled: Whether the option is disabled.
        invalid: Whether to mark the option as invalid.
        class_: Extra CSS classes for the field wrapper.
        **kwargs: Extra attributes for the input element.
    """
    input_id = f"{name}-{value}"

    if checked:
        kwargs["checked"] = XBool.true
    if disabled:
        kwargs["disabled"] = XBool.true
    if invalid:
        kwargs["aria_invalid"] = "true"

    label = html.label(*children, for_=input_id)
    content: ComponentType = html.section(label, html.p(description)) if description is not None else label

    field_attrs: dict[str, PropertyValue] = {
        "role": "group",
        "data_orientation": "horizontal",
    }
    if disabled:
        field_attrs["data_disabled"] = "true"
    if invalid:
        field_attrs["data_invalid"] = "true"

    return html.div(
        html.input_(
            type="radio",
            id=input_id,
            name=name,
            value=value,
            class_="input",
            **kwargs,
        ),
        content,
        class_=join_classes("field", class_),
        **field_attrs,
    )


def radio_group(
    *children: ComponentType,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Radio group container.

    Arguments:
        *children: The components in the group.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    return html.div(*children, class_=class_, role="radiogroup", data_slot="radio-group", **kwargs)
