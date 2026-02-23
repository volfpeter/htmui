from __future__ import annotations

from typing import TYPE_CHECKING

from htmy import ComponentType, SafeStr, html
from htmy.utils import join

if TYPE_CHECKING:
    from typing import TypeAlias

    AccordionContent: TypeAlias = ComponentType
    AccordionSummary: TypeAlias = ComponentType
    AccordionItem: TypeAlias = tuple[AccordionSummary, AccordionContent]


__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/accordion/"


accordion_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-5 shrink-0 transition-transform duration-200 group-open:rotate-180">'
    '<path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>'
)
"""`chevron-down` icon from https://heroicons.com/ with additional styling."""


def summary_content(children: ComponentType) -> ComponentType:
    return html.h2(
        children,
        accordion_icon,
        class_=(
            "flex flex-1 items-start justify-between gap-4 py-4 "
            "text-left text-sm font-medium hover:underline"
        ),
    )


def summary(children: AccordionSummary, *, class_: str | None = None) -> ComponentType:
    return html.summary(
        summary_content(children),
        class_=join(
            (
                "w-full focus-visible:border-ring "
                "focus-visible:ring-ring/50 focus-visible:ring-[3px] "
                "transition-all outline-none rounded-md"
            ),
            class_,
        ),
    )


def accordion(
    *children: AccordionItem,
    content_class: str | None = None,
    item_class: str | None = None,
    root_class: str | None = None,
    summary_class: str | None = None,
) -> ComponentType:
    return html.section(
        *(
            html.details(
                summary(s, class_=summary_class),  # Summary
                html.section(c, class_=join("pb-4", content_class)),  # Content
                class_=join("group border-b last:border-b-0", item_class),
            )
            for s, c in children
        ),
        class_=join("accordion", root_class),
    )
