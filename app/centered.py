from htmy import ComponentType, html, join_classes


def centered(*children: ComponentType, class_: str | None = None) -> ComponentType:
    return html.div(
        *children,
        class_=join_classes("flex flex-col items-center justify-center", class_),
    )
