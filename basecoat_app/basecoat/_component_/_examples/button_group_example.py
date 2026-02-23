from htmy import ComponentType, html

from htmui.basecoat.button_group import button_group


def example() -> ComponentType:
    return html.div(
        html.h3("Horizontal button group:"),
        button_group(
            html.button("First", class_="btn"),
            html.button("Second", class_="btn"),
            html.button("Third", class_="btn"),
        ),
        html.h3("Vertical button group:"),
        html.div(
            button_group(
                html.button("First", class_="btn"),
                html.button("Second", class_="btn"),
                html.button("Third", class_="btn"),
                vertical=True,
            ),
            class_="flex justify-center",
        ),
        class_="flex flex-col gap-2",
    )
