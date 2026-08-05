from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/table/"


def table(
    *children: ComponentType,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Table component.

    Arguments:
        *children: Table content.
        class_: Extra CSS classes for the table.
        **kwargs: Extra attributes for the table element.
    """
    return html.table(*children, class_=join_classes("table", class_), **kwargs)


def table_container(
    *children: ComponentType,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Horizontally scrollable wrapper for wide tables.

    Arguments:
        *children: Container content, usually a single `table`.
        class_: Extra CSS classes for the container.
        **kwargs: Extra attributes for the container.
    """
    return html.div(*children, class_=join_classes("table-container", class_), **kwargs)
