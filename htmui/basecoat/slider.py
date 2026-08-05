from htmy import ComponentType, PropertyValue, SafeStr, XBool, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/slider/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/range.min.js" defer></script>'
)


def slider(
    *,
    start_label: ComponentType | None = None,
    middle_label: ComponentType | None = None,
    end_label: ComponentType | None = None,
    disabled: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Range input styled as a slider, with optional labels.

    Arguments:
        start_label: Optional label shown at the start of a row above the slider.
        middle_label: Optional label shown in the middle of the row above the slider.
        end_label: Optional label shown at the end of the row above the slider.
        disabled: Whether the slider is disabled.
        class_: Extra CSS classes for the input element.
        **kwargs: Extra attributes for the input element.
    """
    if disabled:
        kwargs["disabled"] = XBool.true

    input_ = html.input_(type="range", class_=join_classes("input", class_), **kwargs)

    if start_label is None and middle_label is None and end_label is None:
        return input_

    return html.div(
        html.div(
            start_label if start_label is not None else html.label(),
            middle_label if middle_label is not None else html.label(),
            end_label if end_label is not None else html.label(),
            class_="flex items-center justify-between gap-2",
        ),
        input_,
        class_="grid w-full gap-1",
    )
