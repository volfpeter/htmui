from htmy import ComponentType, html

from htmui.basecoat import dialog


def example() -> ComponentType:
    return html.div(
        dialog.show_dialog_button("Show dialog", dialog_id="example-alert-dialog"),
        dialog.dialog(
            id="example-alert-dialog",
            title="Alert dialog",
            description=(
                "This is an example alert dialog. It cannot be closed by clicking on the backdrop."
            ),
            footer=html.button("Close", class_="btn", onclick=dialog.handle_close_button_click.close),
            close_button=None,
            alert=True,
        ),
    )
