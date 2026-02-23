from __future__ import annotations

from typing import Literal

from htmy import ComponentType, Properties, SafeStr, as_component_sequence, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/sidebar/"


def js() -> SafeStr:
    return SafeStr(
        '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@0.3/dist/js/sidebar.min.js" defer></script>'
    )


Side = Literal["left", "right"]


def sidebar(
    *children: ComponentType,
    header: ComponentType | None = None,
    footer: ComponentType | None = None,
    root_class: str | None = None,
    nav_class: str | None = "p-2",
    nav_props: Properties | None = None,
    section_class: str | None = None,
    hidden: bool = False,
    side: Side = "left",
) -> ComponentType:
    return html.aside(
        html.nav(
            *as_component_sequence(header),
            html.section(*children, class_=join_classes("scrollbar", section_class)),
            *as_component_sequence(footer),
            **(nav_props or {"aria-label": "Sidebar navigation"}),
            class_=nav_class,
        ),
        class_=join_classes("sidebar", root_class),
        aria_hidden="true" if hidden else "false",
        data_side=side,
    )


menu_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
    'stroke-width="1.5" stroke="currentColor" class="size-6">'
    '<path stroke-linecap="round" stroke-linejoin="round" '
    'd="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/></svg>'
)
"""`bars-3` icon from https://heroicons.com/."""


def sidebar_toggle(content: ComponentType = None, class_: str | None = None) -> ComponentType:
    return html.button(
        menu_icon if content is None else content,
        type="button",
        onclick="document.dispatchEvent(new CustomEvent('basecoat:sidebar'))",
        **({"class_": class_} if class_ else {}),
    )
