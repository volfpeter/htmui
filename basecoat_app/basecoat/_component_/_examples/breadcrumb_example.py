from htmy import ComponentType

from htmui.basecoat.breadcrumb import breadcrumb


def example() -> ComponentType:
    return breadcrumb("First", "Second", "Third")
