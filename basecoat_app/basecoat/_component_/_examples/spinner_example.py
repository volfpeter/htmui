from htmy import ComponentType, html

from htmui.basecoat.spinner import spinner


def example() -> ComponentType:
    return html.div(
        spinner(),
        html.div(spinner(), "Loading...", class_="flex items-center gap-2"),
        class_="flex flex-col items-center justify-center gap-4",
    )
