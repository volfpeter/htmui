from htmy import ComponentType, html

from htmui.basecoat.combobox import combobox, option

options: list[ComponentType] = [
    option("Apple", value="apple"),
    option("Banana", value="banana", selected=True),
    option("Orange", value="orange", force=True),
    option("Strawberry", value="strawberry", keywords="fields forever"),
    option("Not an option", value="not-an-option", disabled=True),
]


def example() -> ComponentType:
    return html.div(
        html.p("Single selection"),
        combobox(
            *options,
            name="fruit",
            placeholder="Select a fruit",
            value="apple",
            class_="w-60",
        ),
        html.p("Multiple selection"),
        combobox(
            *options,
            name="fruits",
            value=["banana"],
            class_="w-60",
            multi=True,
        ),
        class_="flex flex-col gap-2",
    )
