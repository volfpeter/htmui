from htmy import ComponentType, html

from htmui.basecoat.radio_group import radio_group, radio_input


def example() -> ComponentType:
    return html.div(
        radio_group(
            radio_input(
                "Default",
                name="density",
                value="default",
                description="Standard spacing for most use cases.",
            ),
            radio_input(
                "Comfortable",
                name="density",
                value="comfortable",
                checked=True,
                description="More space between elements.",
            ),
            radio_input(
                "Compact",
                name="density",
                value="compact",
                description="Minimal spacing for dense layouts.",
            ),
            aria_label="View density",
        ),
        radio_group(
            radio_input("Email only", name="notify", value="email", invalid=True),
            radio_input("SMS only", name="notify", value="sms", invalid=True),
            radio_input(
                "Both",
                name="notify",
                value="both",
                checked=True,
                disabled=True,
            ),
            aria_label="Notification preferences",
        ),
        class_="flex flex-col gap-6",
    )
