from htmy import ComponentType, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/pagination/"

chevron_left_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="M15.75 19.5 8.25 12l7.5-7.5" /></svg>'
)
"""`chevron-left` icon from https://heroicons.com/."""

chevron_right_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor" class="size-5"><path stroke-linecap="round" stroke-linejoin="round" '
    'd="m8.25 4.5 7.5 7.5-7.5 7.5" /></svg>'
)
"""`chevron-right` icon from https://heroicons.com/."""


def pagination_item(
    *content: ComponentType,
    url: str,
    class_: str | None = None,
    selected: bool = False,
) -> ComponentType:
    return html.li(
        html.a(
            *content,
            href=url,
            class_=join_classes("btn-outline" if selected else "btn-ghost", class_),
        )
    )


def pagination(
    *items: ComponentType,
    next_content: ComponentType = SafeStr("Next"),  # noqa: B008
    next_url: str,
    previous_content: ComponentType = SafeStr("Previous"),  # noqa: B008
    previous_url: str,
) -> ComponentType:
    return html.nav(
        html.ul(
            None
            if previous_content is None
            else pagination_item(chevron_left_icon, previous_content, url=previous_url),
            *items,
            None
            if next_content is None
            else pagination_item(chevron_right_icon, next_content, url=next_url),
            class_="flex flex-row items-center gap-1",
        ),
        role="navigation",
        aria_label="pagination",
        class_="mx-auto flex w-full justify-center",
    )
