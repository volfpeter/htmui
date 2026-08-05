from typing import Literal

from htmy import ComponentType, PropertyValue, XBool, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/switch/"

SwitchSize = Literal["sm"]


def switch(
    *,
    name: str,
    checked: bool = False,
    disabled: bool = False,
    invalid: bool = False,
    size: SwitchSize | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Checkbox input styled as a switch.

    Arguments:
        name: The name of the input.
        checked: Whether the switch is initially checked.
        disabled: Whether the switch is disabled.
        invalid: Whether to mark the switch as invalid.
        size: Optional size variant.
        class_: Extra CSS classes for the input element.
        **kwargs: Extra attributes for the input element.
    """
    if checked:
        kwargs["checked"] = XBool.true
    if disabled:
        kwargs["disabled"] = XBool.true
    if invalid:
        kwargs["aria_invalid"] = "true"
    if size is not None:
        kwargs["data_size"] = size

    return html.input_(
        type="checkbox",
        role="switch",
        name=name,
        class_=join_classes("input", class_),
        **kwargs,
    )
