from htmy import ComponentType, html

from htmui.basecoat import button, dialog, drawer


def example() -> ComponentType:
    return html.div(
        html.div(
            dialog.show_dialog_button("Open left", dialog_id="example-drawer-left"),
            dialog.show_dialog_button("Open right", dialog_id="example-drawer-right"),
            class_="flex flex-wrap gap-2",
        ),
        drawer.drawer(
            html.p("Left-side drawer content."),
            id="example-drawer-left",
            title="Left drawer",
            description="Anchored to the left edge of the viewport.",
            footer=_drawer_footer(),
            side="left",
        ),
        drawer.drawer(
            html.p("Right-side drawer content."),
            id="example-drawer-right",
            title="Right drawer",
            description="Anchored to the right edge of the viewport.",
            footer=_drawer_footer(),
            side="right",
        ),
    )


def _drawer_footer() -> ComponentType:
    return html.footer(
        button.button("Submit", onclick=dialog.handle_close_button_click.close),
        button.button(
            "Cancel",
            variant="outline",
            onclick=dialog.handle_close_button_click.close,
        ),
    )
