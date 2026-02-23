from htmy import ComponentSequence, ComponentType, html

from htmui.basecoat.command import command, command_dialog, search_icon
from htmui.unstyled import menu


def example() -> ComponentType:
    return html.div(
        html.button(
            "Open command dialog",
            html.kbd(
                "⌘+K",
                class_="kbd",
            ),
            class_="btn-outline",
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
        menu.group(
            menu.menu_item(html.span("Commit")),
            menu.menu_item(html.span("Pull")),
            menu.menu_item(html.span("Push")),
            id="command-group-1",
            label="Git",
        ),
        menu.group(
            menu.menu_item(html.span("Review")),
            menu.menu_item(html.span("Approve"), disabled=True),
            menu.menu_item(html.span("Comment")),
            id="command-group-2",
            label="Actions",
        ),
    )
