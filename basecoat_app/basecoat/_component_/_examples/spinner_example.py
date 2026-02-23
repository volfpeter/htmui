from htmy import ComponentType, html

from htmui.basecoat.spinner import spinner


def example() -> ComponentType:
    return html.div(
        spinner(),
        spinner("Spinner before the message.", class_="flex gap-2"),
        spinner("Spinner after the message.", class_="flex gap-2", position="after"),
        class_="flex flex-col items-center justify-center gap-2",
    )
