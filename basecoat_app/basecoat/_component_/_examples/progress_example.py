from htmy import ComponentType, html

from htmui.basecoat.progress import progress


def example() -> ComponentType:
    return html.div(
        progress(
            start_label=html.label("Progress", class_="label"),
            end_label=html.output("66%", class_="label text-muted-foreground tabular-nums"),
            value=66,
            class_="w-full",
        ),
        progress(
            middle_label=html.label("Progress", class_="label"),
            value=40,
            class_="w-full",
        ),
        class_="grid w-full max-w-sm gap-4",
    )
