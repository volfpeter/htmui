from htmy import ComponentType, html

from htmui.basecoat.field import field, fieldset


def example() -> ComponentType:
    return html.form(
        fieldset(
            field(
                html.label("Title", for_="title-input"),
                html.input_(id="title-input", type="text", required=""),
            ),
            field(
                html.label("Description", for_="description-input"),
                html.textarea(id="description-input"),
            ),
            title="New Issue",
            subtitle=html.p("Fill out the form to create a new issue."),
        ),
        class_="w-full max-w-md space-y-4",
    )
