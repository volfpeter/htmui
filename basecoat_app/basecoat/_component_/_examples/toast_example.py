from htmy import ComponentType, html

from htmui.basecoat.toast import toast, toaster


def example() -> ComponentType:
    return html.div(
        html.div(
            html.button(
                "Trigger notification.",
                class_="btn-outline",
                onclick="""document.dispatchEvent(new CustomEvent('basecoat:toast', {
                    detail: {
                      config: {
                        category: 'success',
                        title: 'Success',
                        description: 'Toast triggered by a button click.',
                        cancel: {
                          label: 'Dismiss'
                        }
                      }
                    }
                  }))""",
            ),
            class_="grow",
        ),
        toaster(
            toast(
                html.section(html.h2("Permanent toast."), html.p("No icons, no actions.")),
                category="success",
                duration=-1,
            ),
            align="center",
            class_="min-w-2xs md:min-w-sm",
            style="position: relative",  # Override fixed placement for this example.
        ),
        class_="flex flex-col items-center",
    )
