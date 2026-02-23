from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/alert/"


def alert(
    *children: ComponentType,
    title: ComponentType,
    icon: ComponentType = None,
    class_: str | None = None,
    content_class: str | None = None,
    title_class: str | None = None,
    destructive: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    return html.div(
        icon,
        html.h2(title, class_=title_class),
        html.section(*children, class_=content_class) if len(children) > 0 else None,
        class_=join_classes("alert-destructive" if destructive else "alert", class_),
        **kwargs,
    )
