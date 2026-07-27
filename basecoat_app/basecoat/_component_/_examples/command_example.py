from htmy import ComponentSequence, ComponentType, html

from htmui.basecoat.command import command, command_dialog, command_item, search_icon
from htmui.basecoat.menu import menu_item_group, menu_separator


def example() -> ComponentType:
    return html.div(
        html.button(
            "Open command dialog",
            html.kbd(
                "⌘+K",
                class_="kbd",
            ),
            class_="btn",
            data_variant="outline",
            type="button",
            onclick="document.getElementById('command-dialog-example').showModal()",
        ),
        command_dialog(*command_menu(), id="command-dialog-example", input_icon=search_icon),
        html.hr(),
        command(*command_menu(), id="command-example", input_icon=search_icon),
        class_="flex flex-col gap-4",
    )


def command_menu() -> ComponentSequence:
    return (
        menu_item_group(
            command_item(html.span("Commit"), filter="Commit"),
            command_item(html.span("Pull"), filter="Pull"),
            command_item(html.span("Push"), filter="Push"),
            id="command-group-1",
            label="Git",
        ),
        menu_separator(),
        menu_item_group(
            command_item(html.span("Review"), filter="Review"),
            command_item(html.span("Approve"), filter="Approve", disabled=True),
            command_item(html.span("Comment"), filter="Comment"),
            id="command-group-2",
            label="Actions",
        ),
    )
