from htmy import ComponentType, Properties, PropertyValue, html


def group(
    *items: ComponentType, id: str, label: str, label_props: Properties | None = None
) -> ComponentType:
    label_id = f"{id}-label"
    return html.div(
        html.span(label, id=label_id, role="heading", **(label_props or {})),
        *items,
        id=id,
        role="group",
        aria_labelledby=label_id,
    )


def separator() -> ComponentType:
    return html.hr(role="separator")


def menu_item(*children: ComponentType, disabled: bool = False, **kwargs: PropertyValue) -> ComponentType:
    if disabled:
        kwargs["aria-disabled"] = "true"

    return html.div(*children, role="menuitem", **kwargs)
