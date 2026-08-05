from __future__ import annotations

from typing import Literal

from htmy import (
    ComponentType,
    PropertyValue,
    SafeStr,
    Tag,
    XBool,
    as_component_sequence,
    html,
    join_classes,
)

from .button import ButtonSize, ButtonVariant
from .typing import HorizontalSide

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/sidebar/"


js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/sidebar.min.js" defer></script>'
)


SidebarItemVariant = Literal["default", "outline"]
"""Visual variant for menu items and submenu summaries."""

SidebarItemSize = Literal["default", "sm", "lg"]
"""Size for menu items and submenu summaries."""


menu_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" '
    'stroke-width="1.5" stroke="currentColor" class="size-6">'
    '<path stroke-linecap="round" stroke-linejoin="round" '
    'd="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/></svg>'
)
"""`bars-3` icon from https://heroicons.com/."""


def sidebar(
    *children: ComponentType,
    id: str,
    aria_label: str | None = None,
    header: ComponentType | None = None,
    footer: ComponentType | None = None,
    side: HorizontalSide = "left",
    initial_open: bool = True,
    initial_mobile_open: bool = False,
    class_: str | None = None,
    nav_class: str | None = None,
    section_class: str | None = "scrollbar-sm",
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Sidebar component.

    Arguments:
        *children: The content of the sidebar.
        id: The sidebar's ID.
        aria_label: Accessibility label for the sidebar's navigation component.
        header: Optional content at the top of the sidebar.
        footer: Optional content at the bottom of the sidebar.
        side: Side of the viewport the sidebar attaches to.
        initial_open: Whether the sidebar starts open on desktop. When `False`,
            the sidebar starts hidden and inert.
        initial_mobile_open: Whether the sidebar starts open below the
            mobile breakpoint.
        class_: Additional classes for the root element.
        nav_class: Additional classes for the nav element.
        section_class: Additional classes for the scrollable content section.
        **kwargs: Extra attributes for the root element.
    """
    if not initial_open:
        kwargs["data_initial_open"] = "false"
        kwargs["aria_hidden"] = "true"
        kwargs["inert"] = XBool.true

    if initial_mobile_open:
        kwargs["data_initial_mobile_open"] = "true"

    return html.aside(
        html.nav(
            None if header is None else html.header(*as_component_sequence(header)),
            html.section(*children, class_=section_class),
            None if footer is None else html.footer(*as_component_sequence(footer)),
            **({"aria_label": aria_label} if aria_label else {}),
            class_=nav_class,
        ),
        id=id,
        class_=join_classes("sidebar", class_),
        data_side=side,
        **kwargs,
    )


def sidebar_group(
    *children: ComponentType,
    label: ComponentType | None = None,
    label_id: str | None = None,
    group_class: str | None = None,
    list_class: str | None = None,
    heading_tag: str = "h3",
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Named navigation group inside the sidebar.

    Arguments:
        *children: The content of the sidebar group.
        label: Optional group heading content.
        label_id: Id of the heading element; also used as `aria-labelledby`.
        group_class: Additional classes for the group wrapper.
        list_class: Additional classes for the list element.
        heading_tag: Tag name for the heading element.
        **kwargs: Attributes passed directly to the group wrapper.
    """
    if label_id is not None:
        kwargs["aria_labelledby"] = label_id

    return html.div(
        None if label is None else Tag(heading_tag)(label, id=label_id),
        html.ul(*children, class_=list_class),
        class_=group_class,
        role="group",
        **kwargs,
    )


def sidebar_item(
    label: ComponentType,
    *,
    href: str | None = None,
    icon: ComponentType | None = None,
    current: bool = False,
    variant: SidebarItemVariant | None = None,
    size: SidebarItemSize | None = None,
    active: bool = False,
    disabled: bool = False,
    keep_mobile_open: bool = False,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Sidebar item.

    Arguments:
        label: The label of the item.
        href: Optional destination URL. When omitted, an action button is rendered.
        icon: Optional content rendered before the label.
        current: Whether this is the current page.
        variant: Visual variant of the item.
        size: The size of the item.
        active: Whether the item is in an active state.
        disabled: Whether the item is non-interactive.
        keep_mobile_open: Keep the mobile sidebar open when this item is
            clicked, instead of closing it.
       **kwargs: Attributes passed directly to the item.
    """
    if variant is not None:
        kwargs["data_variant"] = variant
    if size is not None:
        kwargs["data_size"] = size
    if active:
        kwargs["data_active"] = "true"
    if keep_mobile_open:
        kwargs["data_keep_mobile_sidebar_open"] = "true"

    if href is None:
        if disabled:
            kwargs["disabled"] = XBool.true

        return html.li(html.button(icon, html.span(label), type="button", **kwargs))

    if current:
        kwargs["aria_current"] = "page"
    if disabled:
        kwargs["aria_disabled"] = "true"
    return html.li(html.a(icon, html.span(label), href=href, **kwargs))


def submenu(
    *children: ComponentType,
    label: ComponentType,
    id: str | None = None,
    icon: ComponentType | None = None,
    open: bool = False,
    active: bool = False,
    variant: SidebarItemVariant | None = None,
    size: SidebarItemSize | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Sidebar submenu.

    Arguments:
        *children: Items wrapped by the submenu.
        label: Text label shown after the optional icon.
        icon: Optional content rendered before the label.
        open: Whether the submenu starts expanded.
        id: The ID of the element.
        variant: Visual variant for the summary control.
        size: Size for the summary control.
        active: Whether the summary control is in an active state.
        **kwargs: Attributes passed directly to the summary element.
    """
    content_id = None if id is None else f"{id}-content"
    if variant is not None:
        kwargs["data_variant"] = variant
    if size is not None:
        kwargs["data_size"] = size
    if active:
        kwargs["data_active"] = "true"
    if content_id is not None:
        kwargs["aria_controls"] = content_id

    details_props: dict[str, PropertyValue] = {}
    if id is not None:
        details_props["id"] = id
    if open:
        details_props["open"] = XBool.true

    return html.li(
        html.details(
            html.summary(
                icon,
                html.span(label),
                **kwargs,
            ),
            html.ul(*children, id=content_id),
            **details_props,
        )
    )


def sidebar_toggle(
    content: ComponentType = menu_icon,
    *,
    sidebar_id: str,
    class_: str | None = None,
    variant: ButtonVariant | None = None,
    size: ButtonSize | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Button that toggles the sidebar with the given ID.

    Arguments:
        content: Button content. Defaults to `menu_icon`.
        sidebar_id: Id of the sidebar to toggle.
        variant: Button variant.
        size: Button size.
        **kwargs: Other attributes passed directly to the button.
    """
    if class_ is not None:
        kwargs["class_"] = class_
    if variant is not None:
        kwargs["data_variant"] = variant
    if size is not None:
        kwargs["data_size"] = size
    return html.button(
        content,
        type="button",
        onclick=f"document.getElementById('{sidebar_id}')?.toggle()",
        **kwargs,
    )
