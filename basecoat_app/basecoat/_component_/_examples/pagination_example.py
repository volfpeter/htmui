from htmy import ComponentType

from htmui.basecoat.pagination import pagination, pagination_item


def example() -> ComponentType:
    return pagination(
        pagination_item("1", url="#"),
        pagination_item("2", url="#", selected=True),
        pagination_item("3", url="#"),
        next_url="#",
        previous_url="#",
    )
