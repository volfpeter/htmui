from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from htmy import html
from htmy.utils import join

if TYPE_CHECKING:
    from htmy import ComponentType, PropertyValue


__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/badge/"

BadgeVariant = Literal["badge", "badge-secondary", "badge-destructive", "badge-outline"]


def badge(
    *children: ComponentType,
    variant: BadgeVariant = "badge",
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    return html.span(
        *children,
        class_=join(variant, class_),
        **kwargs,
    )
