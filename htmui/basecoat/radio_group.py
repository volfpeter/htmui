from htmy import ComponentType, XBool, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/radio-group/"


def radio_input(
    *children: ComponentType,
    name: str,
    value: str,
    checked: bool = False,
    class_: str | None = None,
    input_class: str | None = None,
) -> ComponentType:
    return html.label(
        html.input_(
            type="radio",
            name=name,
            value=value,
            class_=join_classes("input", input_class),
            checked=XBool.true if checked else None,
        ),
        *children,
        class_=join_classes("label", class_),
    )


def radio_group(*children: ComponentType, class_: str = "grid gap-2") -> ComponentType:
    return html.fieldset(*children, class_=class_)
