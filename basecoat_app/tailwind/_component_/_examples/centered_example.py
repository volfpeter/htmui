from htmy import ComponentType, html

from htmui.tailwind.centered import centered


def example() -> ComponentType:
    return centered(html.h3("Nice to see you!", class_="text-lg font-bold"))
