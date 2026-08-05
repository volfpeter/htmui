from htmy import ComponentType, html

from htmui.basecoat import slider


def example() -> ComponentType:
    return html.div(
        slider.slider(
            start_label=html.label("0", class_="label"),
            middle_label=html.output("6", class_="label text-muted-foreground"),
            end_label=html.label("11", class_="label"),
            min=0,
            max=11,
            value=6,
            oninput="this.previousElementSibling.querySelector('output').value = this.value",
            class_="w-full",
        ),
        slider.slider(
            middle_label=html.label("Rating", class_="label"),
            min=0,
            max=10,
            value=8,
            class_="w-full",
        ),
        slider.slider(min=0, max=100, value=50, disabled=True, class_="w-full"),
        class_="grid w-full max-w-sm gap-4",
    )
