from __future__ import annotations

from htmy import ComponentType, PropertyValue, SafeStr, html
from htmy.utils import join, join_components

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/breadcrumb/"

chevron_right_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-4"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="m8.25 4.5 7.5 7.5-7.5 7.5" /></svg>'
)
"""`chevron-right` icon from https://heroicons.com/ with small adjustments."""


def breadcrumb(
    *children: ComponentType,
    separator: ComponentType = chevron_right_icon,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Breadcrumb navigation component.

    Arguments:
        *children: Breadcrumb items.
        separator: Separator to be inserted between items.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    return html.nav(
        html.ol(
            *join_components(
                tuple(html.li(child) for child in children if child is not None),
                html.li(separator, aria_hidden="true"),
            ),
        ),
        class_=join("breadcrumb", class_),
        **kwargs,
    )
