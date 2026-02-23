from htmy import ComponentType

from htmui.basecoat.radio_group import radio_group, radio_input


def example() -> ComponentType:
    return radio_group(
        radio_input("Option 1", name="choice", value="option-1"),
        radio_input("Option 2", name="choice", value="option-2", checked=True),
        radio_input("Option 3", name="choice", value="option-3"),
    )
