from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/spinner/"

spinner_path = SafeStr('<path d="M21 12a9 9 0 1 1-6.219-8.56" />')
"""Path for the `loader-circle` icon from https://lucide.dev."""


def spinner(
    *children: ComponentType,
    aria_label: str = "Loading",
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Animated spinner.

    Arguments:
        *children: SVG children (typically `<path>` elements).
            Defaults to `spinner_path`.
        aria_label: Accessible label for the spinner.
        class_: Extra CSS classes for the root SVG.
        **kwargs: Extra attributes for the SVG.
    """
    return html.svg(
        *(children if len(children) > 0 else (spinner_path,)),
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        role="status",
        aria_label=aria_label,
        class_=join_classes("animate-spin", class_),
        **kwargs,
    )
