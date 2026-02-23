from htmy import ComponentType, html

from htmui.basecoat.select import select


def example() -> ComponentType:
    return select(
        html.optgroup(
            html.option("Apple"),
            html.option("Banana", selected="true"),
            html.option("Orange"),
            html.option("Strawberry"),
            label="Fruits",
        ),
        button_class="w-40",
    )
