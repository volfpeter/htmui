from __future__ import annotations

from htmy import ComponentType, PropertyValue, SafeStr, html
from htmy.utils import join, join_components

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
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
    return html.ol(
        *join_components(
            tuple(
                html.li(
                    child,
                    class_="inline-flex items-center gap-1.5",
                )
                for child in children
                if child is not None
            ),
            separator,
        ),
        class_=join(
            "text-muted-foreground flex flex-wrap items-center gap-1.5 text-sm break-words sm:gap-2.5",
            class_,
        ),
        **kwargs,
    )
