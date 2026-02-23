from htmy import ComponentType, html

from htmui.basecoat import dialog


def example() -> ComponentType:
    return html.div(
        dialog.show_dialog_button("Show dialog", dialog_id="example-alert-dialog"),
        dialog.dialog(
            html.p("This is an example alert dialog."),
            html.p(
                "It has no ",
                html.code("onclick"),
                " handler, so it cannot be closed by clicking on the backdrop.",
            ),
            id="example-alert-dialog",
            alert=True,
            title="Alert dialog",
            actions=html.button("Close", class_="btn", onclick=dialog.handle_close_button_click.close),
        ),
    )
