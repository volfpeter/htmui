from htmy import ComponentType, PropertyValue, SafeStr, XBool, html, join_classes

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/accordion/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/accordion.min.js" defer></script>'
)

accordion_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" '
    'stroke="currentColor">'
    '<path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" /></svg>'
)
"""`chevron-down` icon from https://heroicons.com/."""


def accordion_item(
    *content: ComponentType,
    summary: ComponentType,
    open: bool = False,
    disabled: bool = False,
    icon: ComponentType | None = accordion_icon,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Accordion item.

    Arguments:
        *content: The content of the accordion item.
        summary: The summary (trigger) of the item.
        open: Whether the item is open by default.
        disabled: Whether the item is disabled.
        icon: Optional trailing icon in the summary. Defaults to a chevron icon.
        class_: Extra CSS classes for the root component.
        **kwargs: Extra attributes for the root component.
    """
    if open:
        kwargs["open"] = XBool.true
    if disabled:
        kwargs["aria_disabled"] = "true"

    return html.details(
        html.summary(summary, icon),
        html.section(*content),
        class_=class_,
        **kwargs,
    )


def accordion(
    *children: ComponentType,
    multiple: bool = False,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Accordion root. Children are usually created with `accordion_item()`.

    Arguments:
        *children: Accordion items.
        multiple: Allow more than one item open at a time.
        class_: Extra CSS classes for the root component.
        **kwargs: Extra attributes for the root component.
    """
    if multiple:
        kwargs["data_multiple"] = ""

    return html.section(
        *children,
        class_=join_classes("accordion", class_),
        **kwargs,
    )
