from htmy import ComponentType, html

from htmui.basecoat.tabs import tab_button, tab_panel, tabs


def example() -> ComponentType:
    panel_1_id = "example-panel-1"
    button_1_id = f"{panel_1_id}-button"
    panel_2_id = "example-panel-2"
    button_2_id = f"{panel_2_id}-button"
    return html.div(
        tabs(
            tab_panel(
                html.div(
                    html.header(html.h2("First panel"), html.p("First panel content.")),
                    class_="card",
                ),
                id=panel_1_id,
                button_id=button_1_id,
                selected=True,
                class_="w-80",
            ),
            tab_panel(
                html.div(
                    html.header(html.h2("Second panel"), html.p("Second panel content.")),
                    class_="card",
                ),
                id=panel_2_id,
                button_id=button_2_id,
                class_="w-80",
            ),
            buttons=(
                tab_button(
                    "First",
                    id=button_1_id,
                    panel_id=panel_1_id,
                    selected=True,
                ),
                tab_button(
                    "Second",
                    id=button_2_id,
                    panel_id=panel_2_id,
                ),
            ),
        )
    )
