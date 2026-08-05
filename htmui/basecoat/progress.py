from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/progress/"


def progress(
    *,
    value: int,
    min: int = 0,
    max: int = 100,
    start_label: ComponentType | None = None,
    middle_label: ComponentType | None = None,
    end_label: ComponentType | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Progress bar component, with optional labels.

    Arguments:
        value: Current value, clamped to the `[min, max]` interval.
        min: Minimum value.
        max: Maximum value.
        start_label: Optional label shown at the start of a row above the bar.
        middle_label: Optional label shown in the middle of the row above the bar.
        end_label: Optional label shown at the end of the row above the bar.
        class_: Extra CSS classes for the root element.
        **kwargs: Extra attributes for the root element.
    """
    value = min if value < min else max if value > max else value
    pct = (value - min) / (max - min) * 100 if max != min else 0
    bar = html.div(
        html.span(style=f"width: {pct:.4g}%"),
        role="progressbar",
        aria_valuenow=value,
        aria_valuemin=min,
        aria_valuemax=max,
        class_=join_classes("progress", class_),
        **kwargs,
    )

    if start_label is None and middle_label is None and end_label is None:
        return bar

    return html.div(
        html.div(
            start_label if start_label is not None else html.label(),
            middle_label if middle_label is not None else html.label(),
            end_label if end_label is not None else html.label(),
            class_="flex items-center justify-between gap-2",
        ),
        bar,
        class_="grid w-full gap-1",
    )
