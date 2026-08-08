from htmy import ComponentType, html

from htmui.basecoat.select import group, option, select


def example() -> ComponentType:
    return html.div(
        select(
            group(
                option("Apple", value="apple"),
                option("Banana", value="banana", selected=True),
                option("Blueberry", value="blueberry"),
                option("Grapes", value="grapes"),
                option("Pineapple", value="pineapple"),
                heading="Fruits",
                heading_id="fruit-root-fruits",
            ),
            placeholder="Select a fruit",
            name="fruit",
            value="banana",
            trigger_class="w-[180px]",
        ),
        select(
            group(
                option("Apple", value="apple"),
                option("Banana", value="banana", selected=True),
                option("Blueberry", value="blueberry"),
                option("Grapes", value="grapes", selected=True),
                option("Pineapple", value="pineapple"),
                heading="Fruits",
                heading_id="fruits-multi-fruits",
            ),
            placeholder="Select fruits",
            name="fruits",
            multiple=True,
            value=["banana", "grapes"],
            trigger_class="w-[220px]",
        ),
        class_="flex flex-col gap-4",
    )
