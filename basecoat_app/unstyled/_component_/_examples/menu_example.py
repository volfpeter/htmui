from htmy import ComponentType, html

from htmui.unstyled import menu


def example() -> ComponentType:
    return html.div(
        html.p("Menu with custom TailwindCSS styles:"),
        html.div(
            menu.group(
                menu.menu_item(html.span("Commit"), data_label="commit"),
                menu.menu_item(html.span("Pull"), data_label="pull"),
                menu.menu_item(html.span("Push"), data_label="push"),
                id="command-group-1",
                label="Git",
                label_props={"class": "font-semibold"},
            ),
            menu.separator(),
            menu.group(
                menu.menu_item(html.span("Review"), data_label="review"),
                menu.menu_item(html.span("Approve"), data_label="approve", disabled=True),
                menu.menu_item(html.span("Comment"), data_label="comment"),
                id="command-group-2",
                label="Actions",
                label_props={"class": "font-semibold"},
            ),
            id="menu-example",
            class_="flex flex-col gap-2 p-2 bg-popover rounded",
        ),
        class_="flex flex-col gap-2",
    )
