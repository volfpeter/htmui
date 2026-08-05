from htmy import ComponentType, html

from htmui.basecoat.badge import badge


def example() -> ComponentType:
    return html.div(
        badge("Default"),
        badge("Destructive", variant="destructive"),
        badge("Secondary", variant="secondary"),
        badge("Outline", variant="outline"),
        badge("Ghost", variant="ghost"),
        class_="flex gap-2",
    )
