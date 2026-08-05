from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/alert/"


def alert(
    *children: ComponentType,
    title: ComponentType,
    icon: ComponentType = None,
    footer: ComponentType | None = None,
    class_: str | None = None,
    content_class: str | None = None,
    title_class: str | None = None,
    destructive: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Alert component with optional icon, description, and action region.

    Arguments:
        *children: Optional content below the title.
        title: Alert title.
        icon: Optional icon.
        footer: Optional footer, typically an `html.footer(...)`.
        class_: Extra CSS classes for the root element.
        content_class: Extra CSS classes for the description section.
        title_class: Extra CSS classes for the title.
        destructive: Whether to use the destructive variant.
        **kwargs: Extra attributes for the root element.
    """
    if destructive:
        kwargs["data_variant"] = "destructive"

    return html.div(
        icon,
        html.h2(title, class_=title_class),
        html.section(*children, class_=content_class) if len(children) > 0 else None,
        footer,
        class_=join_classes("alert", class_),
        **kwargs,
    )
