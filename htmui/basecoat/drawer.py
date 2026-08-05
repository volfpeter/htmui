from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

from .typing import Side

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/drawer/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/drawer.min.js" defer></script>'
)


def drawer(
    *children: ComponentType,
    id: str,
    title: ComponentType | None = None,
    description: ComponentType | None = None,
    footer: ComponentType | None = None,
    side: Side | None = None,
    class_: str | None = None,
    content_class: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Drawer component.

    Arguments:
        *children: Drawer body content.
        id: Drawer element ID.
        title: Optional title.
        description: Optional description shown under the title.
        footer: Optional footer. Should be an `html.footer()` when provided.
        side: On which side the drawer should appear.
        class_: Extra CSS classes for the root element.
        content_class: Extra CSS classes for the inner content.
        **kwargs: Extra attributes for the root element.
    """
    title_id = f"{id}-title"
    description_id = f"{id}-description"
    if title is not None:
        kwargs["aria_labelledby"] = title_id
    if description is not None:
        kwargs["aria_describedby"] = description_id
    if side is not None:
        kwargs["data_side"] = side

    header = None
    if title is not None or description is not None:
        header = html.header(
            html.h2(title, id=title_id) if title is not None else None,
            html.p(description, id=description_id) if description is not None else None,
        )

    return html.dialog(
        html.article(
            header,
            html.section(*children) if len(children) > 0 else None,
            footer,
            class_=content_class,
        ),
        id=id,
        class_=join_classes("drawer", class_),
        **kwargs,
    )
