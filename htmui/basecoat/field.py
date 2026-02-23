from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/field/"


def fieldset(
    *children: ComponentType,
    title: ComponentType,
    subtitle: ComponentType = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    return html.fieldset(
        html.legend(title),
        subtitle,
        *children,
        class_=join_classes("fieldset", class_),
        **kwargs,
    )


def field(
    *children: ComponentType,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    return html.div(*children, class_=join_classes("field", class_), role="group", **kwargs)
