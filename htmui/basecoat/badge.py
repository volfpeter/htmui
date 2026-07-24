from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from htmy import html
from htmy.utils import join

if TYPE_CHECKING:
    from htmy import ComponentType, PropertyValue


__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/badge/"

BadgeVariant = Literal["secondary", "destructive", "outline", "ghost"]


def badge(
    *children: ComponentType,
    variant: BadgeVariant | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    if variant is not None:
        kwargs["data_variant"] = variant
    return html.span(
        *children,
        class_=join("badge", class_),
        **kwargs,
    )
