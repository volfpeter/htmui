from htmy import ComponentType, html, join_classes

__version__ = "0.1.0"
__framework__ = "TailwindCSS"
__framework_version__ = "4"
__framework_url__ = "https://tailwindcss.com"


def centered(*children: ComponentType, class_: str | None = None) -> ComponentType:
    return html.div(
        *children,
        class_=join_classes("flex flex-col items-center justify-center", class_),
    )
