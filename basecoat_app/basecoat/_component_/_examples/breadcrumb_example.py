from htmy import ComponentType, html

from htmui.basecoat.breadcrumb import breadcrumb


def example() -> ComponentType:
    return breadcrumb(
        html.a("Home", href="#"),
        html.a("Components", href="#"),
        html.span("Breadcrumb", aria_current="page"),
    )
