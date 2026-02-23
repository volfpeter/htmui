from htmy import ComponentType, html

from htmui.basecoat.badge import badge


def example() -> ComponentType:
    return html.div(
        badge("Default"),
        badge("Destructive", variant="badge-destructive"),
        badge("Secondary", variant="badge-secondary"),
        badge("Outline", variant="badge-outline"),
        class_="flex gap-2",
    )
