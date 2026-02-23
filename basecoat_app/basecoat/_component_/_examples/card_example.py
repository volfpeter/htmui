from htmy import ComponentType, html

from htmui.basecoat.card import card


def example() -> ComponentType:
    return card(
        html.header(html.h2("Card title")),
        html.section(html.p("Card content")),
        html.footer(html.p("Card footer")),
        class_="w-sm",
    )
