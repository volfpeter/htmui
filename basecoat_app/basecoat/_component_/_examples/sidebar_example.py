from htmy import ComponentType, html

from htmui.basecoat.sidebar import sidebar, sidebar_toggle

_sidebar_id = "sidebar"


def example(current_path: str = "/dashboard") -> ComponentType:
    return html.div(
        sidebar_toggle("Toggle sidebar", sidebar_id=_sidebar_id),
        sidebar(
            html.div(
                html.h3("Pages", id="sidebar-pages-group-title"),
                html.ul(
                    *(
                        html.li(
                            html.a(
                                page.title(),
                                href=href,
                                hx_boost="true",
                                **({"aria-current": "page"} if current_path == href else {}),
                            )
                        )
                        for page in ("dashboard", "settings", "profile")
                        if (href := f"/{page}/")
                    )
                ),
                class_="group",
                aria_labelledby="sidebar-pages-group-title",
            ),
            id=_sidebar_id,
        ),
        class_="relative",
    )
