from htmy import ComponentType, html

from htmui.basecoat.alert import alert


def example() -> ComponentType:
    return html.div(
        alert("This is a default alert.", title="Default"),
        alert(
            "This is a destructive alert.",
            title="Important!",
            destructive=True,
        ),
        alert(
            "Enable it under your profile settings to get started.",
            title="Dark mode is now available",
            footer=html.footer(
                html.button("Enable", type="button", class_="btn", data_size="xs"),
            ),
        ),
        alert(
            "This alert has a custom styling.",
            title_class="text-green-500 underline",
            content_class="text-green-300",
            title="Make it green",
        ),
        class_="flex flex-col gap-2",
    )
