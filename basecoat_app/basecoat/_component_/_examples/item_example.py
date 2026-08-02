from htmy import ComponentType, html

from htmui.basecoat.button import button
from htmui.basecoat.item import item, item_link


def example() -> ComponentType:
    return html.div(
        item(
            html.section(
                html.h3("Default item"),
                html.p("A simple item with title and description."),
            ),
            html.aside(button("Action", variant="outline", size="sm")),
        ),
        item_link(
            html.section(
                html.h3("Outline link item"),
                html.p("Learn how to get started with our components."),
            ),
            href="#",
            variant="outline",
        ),
        item(
            html.section(
                html.h3("Small muted item"),
                html.p("A compact size for dense layouts."),
            ),
            variant="muted",
            size="sm",
        ),
        item(
            html.section(
                html.h3("Extra small outline item"),
                html.p("The most compact size available."),
            ),
            variant="outline",
            size="xs",
        ),
        class_="flex w-full max-w-md flex-col gap-6",
    )
