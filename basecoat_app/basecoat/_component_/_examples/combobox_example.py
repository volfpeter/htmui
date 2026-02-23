from htmy import ComponentType

from htmui.basecoat.combobox import combobox, option


def example() -> ComponentType:
    return combobox(
        option("Apple", value="apple"),
        option("Banana", value="banana", selected=True),
        option("Orange", value="orange", force=True),
        option("Strawberry", value="strawberry", keywords="fields forever"),
        option("Not an option", value="not-an-option", disabled=True),
        id="my-select-with-search",
        button_class="w-40",
    )
