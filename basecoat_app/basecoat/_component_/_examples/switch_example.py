from htmy import ComponentType, html

from htmui.basecoat import field, switch


def example() -> ComponentType:
    return html.div(
        field.field(
            switch.switch(name="notifications", id="switch-notifications"),
            html.label("Notifications", for_="switch-notifications"),
            orientation="horizontal",
        ),
        field.field(
            switch.switch(name="offline-sync", id="switch-offline", disabled=True),
            html.label("Offline sync", for_="switch-offline"),
            orientation="horizontal",
            disabled=True,
        ),
        field.field(
            switch.switch(name="compact-mode", id="switch-compact", size="sm"),
            html.label("Compact mode", for_="switch-compact"),
            orientation="horizontal",
        ),
        class_="grid w-full max-w-sm gap-4",
    )
