from htmy import ComponentType, html

from htmui.basecoat import button, input_group


def example() -> ComponentType:
    return html.div(
        input_group.input_group(
            html.input_(type="text", placeholder="Jump to file..."),
            input_group.addon(html.kbd("⌘K", class_="kbd"), align="end"),
        ),
        input_group.input_group(
            html.input_(type="text", placeholder="Amount"),
            input_group.addon("$", align="start"),
            input_group.addon("per night", align="end"),
        ),
        input_group.input_group(
            html.textarea(placeholder="Notes for the team..."),
            html.footer(
                html.span("Pending"),
                button.button("Send", size="sm", class_="ml-auto"),
                data_align="end",
            ),
            vertical=True,
        ),
        class_="grid w-full max-w-sm gap-4",
    )
