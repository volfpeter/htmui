from typing import Literal

from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/field/"

FieldOrientation = Literal["horizontal", "responsive"]


def fieldset(
    *children: ComponentType,
    title: ComponentType | None = None,
    subtitle: ComponentType | None = None,
    class_: str | None = None,
    title_class: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Fieldset that groups related fields.

    Arguments:
        *children: Fields and other content inside the fieldset.
        title: Optional title.
        subtitle: Optional description, shown after the title.
        class_: Extra CSS classes for the root element.
        title_class: Extra CSS classes for the title.
        **kwargs: Extra attributes for the root element.
    """
    return html.fieldset(
        html.legend(title, class_=title_class) if title is not None else None,
        subtitle,
        *children,
        class_=join_classes("fieldset", class_),
        **kwargs,
    )


def field(
    *children: ComponentType,
    orientation: FieldOrientation | None = None,
    invalid: bool = False,
    disabled: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Single field.

    Arguments:
        *children: Field content (label, control, description, etc.).
        orientation: Layout orientation.
        invalid: Whether to mark the field as invalid.
        disabled: Whether to mark the field as disabled.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    if orientation is not None:
        kwargs["data_orientation"] = orientation
    if invalid:
        kwargs["data_invalid"] = "true"
    if disabled:
        kwargs["data_disabled"] = "true"

    return html.div(*children, class_=join_classes("field", class_), role="group", **kwargs)


def field_separator(
    label: ComponentType | None = None,
    *,
    class_: str | None = None,
    label_class: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Separator between field groups.

    Arguments:
        label: Optional label rendered over the separator.
        class_: Extra CSS classes for the root element.
        label_class: Extra CSS classes for the label element.
        **kwargs: Extra attributes for the root element.
    """
    return html.div(
        html.hr(role="separator"),
        html.span(label, class_=label_class) if label is not None else None,
        class_=join_classes("field-separator", class_),
        **kwargs,
    )
