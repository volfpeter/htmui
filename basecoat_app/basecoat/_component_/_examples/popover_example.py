from htmy import ComponentType, html

from htmui.basecoat.popover import popover


def example() -> ComponentType:
    return popover(
        html.header(
            html.h4("Popover Title", class_="font-medium"),
            html.p("Popover description", class_="text-muted-foreground text-sm"),
            html.ul(
                html.li("Item 1"),
                html.li("Item 2"),
                html.li("Item 3"),
                class_="list-disc list-inside",
            ),
            class_="grid gap-1",
        ),
        button_content="Open popover",
        id="example-popover",
    )
