from typing import Literal

from htmy import ComponentType, Fragment, PropertyValue, SafeStr, html, join_classes

from .typing import Align

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/toast/"

ToastCategory = Literal["success", "info", "warning", "error"]

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/toast.min.js" defer></script>'
)


def toaster(
    *children: ComponentType,
    id: str,
    class_: str | None = None,
    align: Align | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Toast container.

    Arguments:
        *children: Initial toasts rendered inside the container.
        id: The unique identifier of the component.
        class_: Extra CSS classes for the container.
        align: Horizontal alignment of the toaster.
        **kwargs: Extra attributes for the root element.
    """
    if align is not None:
        kwargs["data-align"] = align

    return html.div(*children, class_=join_classes("toaster", class_), id=id, **kwargs)


def toast(
    *children: ComponentType,
    category: ToastCategory | None = None,
    class_: str | None = None,
    duration: int | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Toast item.

    Arguments:
        *children: Toast content. Use `toast_content()` for the standard toast layout.
        category: Semantic category that controls styling.
        class_: Optional CSS classes for the toast.
        duration: Timeout in milliseconds. Use `-1` to keep the toast open.
        **kwargs: Extra attributes for the root element.
    """
    if category is not None:
        kwargs["data-category"] = category
    if duration is not None:
        kwargs["data-duration"] = duration

    return html.div(
        html.div(*children, class_="toast-content"),
        class_=join_classes("toast", class_),
        role="alert" if category == "error" else "status",
        aria_atomic="true",
        aria_hidden="false",
        **kwargs,
    )


def toast_content(
    description: ComponentType,
    *,
    title: ComponentType | None = None,
    icon: ComponentType | None = None,
    footer: ComponentType | None = None,
) -> ComponentType:
    """
    Standard toast content layout.

    Arguments:
        description: Toast description.
        title: Optional toast title.
        icon: Optional icon.
        footer: Optional footer element, typically an `html.footer(...)`.
    """
    return Fragment(
        icon,
        html.section(
            None if title is None else html.h2(title),
            html.p(description),
        ),
        footer,
    )
