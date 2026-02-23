from typing import Literal

from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/toast/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/toast.min.js" defer></script>'
)


def toaster(
    *children: ComponentType,
    class_: str | None = None,
    align: Literal["start", "center", "end"] | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """Toast container."""
    kwargs["id"] = "toaster"
    if align is not None:
        kwargs["data-align"] = align

    return html.div(*children, class_=join_classes("toaster", class_), **kwargs)


def toast(
    *children: ComponentType,
    category: Literal["success", "info", "warning", "error"] | None = None,
    class_: str | None = None,
    duration: int | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    if category is not None:
        kwargs["data-category"] = category
    if duration is not None:
        kwargs["data-duration"] = duration

    return html.div(
        html.div(*children, class_="toast-content"),
        class_=join_classes("toast", class_),
        role="status",
        aria_atomic="true",
        aria_hidden="false",
        **kwargs,
    )
