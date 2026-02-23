from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/select/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/select.min.js" defer></script>'
)


def select(*children: ComponentType, class_: str | None = None, **kwargs: PropertyValue) -> ComponentType:
    return html.select(*children, class_=join_classes("select", class_), **kwargs)
