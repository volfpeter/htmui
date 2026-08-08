from htmy import ComponentType, SafeStr, html

from htmui.basecoat.button import button
from htmui.basecoat.spinner import spinner

_plus_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
    'stroke-linejoin="round" class="lucide lucide-plus">'
    '<path d="M5 12h14" /><path d="M12 5v14" /></svg>'
)
"""`plus` icon from https://lucide.dev."""

_branch_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" data-icon="inline-start" width="24" height="24" '
    'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
    'stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-git-branch">'
    '<path d="M15 6a9 9 0 0 0-9 9V3" />'
    '<circle cx="18" cy="6" r="3" /><circle cx="6" cy="18" r="3" /></svg>'
)
"""`git-branch` icon from https://lucide.dev, with inline-start icon spacing."""


def example() -> ComponentType:
    return html.div(
        html.h3("Variants:"),
        html.div(
            button("Primary"),
            button("Secondary", variant="secondary"),
            button("Outline", variant="outline"),
            button("Ghost", variant="ghost"),
            button("Link", variant="link"),
            button("Destructive", variant="destructive"),
            class_="flex flex-wrap items-center gap-2",
        ),
        html.h3("Sizes:"),
        html.div(
            button("Extra small", variant="outline", size="xs"),
            button("Small", variant="outline", size="sm"),
            button("Large", variant="outline", size="lg"),
            class_="flex flex-wrap items-center gap-2",
        ),
        html.h3("Icons:"),
        html.div(
            button(_branch_icon, "New branch", variant="outline", size="sm"),
            button(_plus_icon, variant="outline", size="icon", aria_label="Add"),
            button(spinner(data_icon="inline-start"), "Generating", disabled=True),
            class_="flex flex-wrap items-center gap-2",
        ),
        class_="flex flex-col gap-2",
    )
