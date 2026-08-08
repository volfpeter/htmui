from htmy import ComponentType, html

from htmui.basecoat.table import table, table_container


def example() -> ComponentType:
    return table_container(
        table(
            html.caption("Upcoming sprint tasks."),
            html.thead(
                html.tr(
                    html.th("Task", class_="w-[100px]"),
                    html.th("Owner"),
                    html.th("Priority"),
                    html.th("Estimate", class_="text-end"),
                ),
            ),
            html.tbody(
                html.tr(
                    html.td("AUTH-12", class_="font-medium"),
                    html.td("Maya"),
                    html.td("High"),
                    html.td("5 pts", class_="text-end"),
                ),
                html.tr(
                    html.td("API-48", class_="font-medium"),
                    html.td("Jonah"),
                    html.td("Medium"),
                    html.td("3 pts", class_="text-end"),
                ),
                html.tr(
                    html.td("UI-07", class_="font-medium"),
                    html.td("Priya"),
                    html.td("Low"),
                    html.td("2 pts", class_="text-end"),
                ),
            ),
            html.tfoot(
                html.tr(
                    html.td("Total", colspan="3"),
                    html.td("10 pts", class_="text-end"),
                ),
            ),
        ),
    )
