from htmy import ComponentType

from htmui.basecoat.pagination import pagination, pagination_item


def example() -> ComponentType:
    return pagination(
        pagination_item("1", url="#", class_="btn-ghost"),
        pagination_item("2", url="#", class_="btn-outline"),
        pagination_item("3", url="#", class_="btn-ghost"),
        next_url="#",
        previous_url="#",
    )
