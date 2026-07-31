from htmy import ComponentType, html

from htmui.basecoat import dialog


def example() -> ComponentType:
    return html.div(
        dialog.show_dialog_button("Show dialog", dialog_id="example-dialog"),
        dialog.dialog(
            html.p("This is an example dialog."),
            html.p("It contains multiple paragraphs."),
            id="example-dialog",
            title="Example dialog",
            description="This is an example dialog description.",
            footer=html.button("Close", class_="btn", onclick=dialog.handle_close_button_click.close),
        ),
    )
