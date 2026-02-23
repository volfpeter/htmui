from collections.abc import Iterable
from typing import Literal

from htmy import ComponentType, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/spinner/"

spinner_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" role="status" '
    'aria-label="Loading" class="animate-spin"><path d="M21 12a9 9 0 1 1-6.219-8.56" /></svg>'
)
"""`loader-circle` icon from https://ludice.dev."""


def spinner(
    *children: ComponentType,
    class_: str | None = "flex shrink-0 items-center justify-center",
    svg_class: Iterable[str] | None = None,
    position: Literal["before", "after"] = "before",
) -> ComponentType:
    """
    Returns a `div` that wraps an animated spinner icon.

    Arguments:
        *children: Child items to display in the wrapper `div` next to the spinner.
        class_: The CSS class for the div that wraps the spinner icon.
        svg_class: CSS classes to apply to the icon through its wrapper `div`. Each of these CSS
            classes will be prefixed with `[&_svg]` automatically when applied to the `div`.
        position: Where to place the spinner relative to `children`.
    """
    svg_class = " ".join(f"[&_svg]:{c}" for c in svg_class) if svg_class else None
    children = (spinner_icon, *children) if position == "before" else (*children, spinner_icon)
    return html.div(*children, class_=join_classes(class_, svg_class))
