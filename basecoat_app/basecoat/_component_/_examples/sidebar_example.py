from htmy import ComponentType, html

from htmui.basecoat.separator import separator
from htmui.basecoat.sidebar import (
    sidebar,
    sidebar_group,
    sidebar_item,
    sidebar_toggle,
    submenu,
)

_sidebar_id = "sidebar"

_hrefs = {
    "Dashboard": "/",
    "Settings": "/settings/",
    "Profile": "/profile/",
}


def example(current_path: str = "/dashboard/") -> ComponentType:
    return html.div(
        sidebar_toggle("Toggle sidebar", sidebar_id=_sidebar_id),
        sidebar(
            sidebar_group(
                *(
                    sidebar_item(name, href=href, current=current_path == href)
                    for name, href in _hrefs.items()
                ),
                label="Pages",
                label_id="sidebar-pages-group-label",
            ),
            separator,
            sidebar_group(
                submenu(
                    sidebar_item("General", href="#account/general"),
                    sidebar_item("Team", href="#account/team"),
                    sidebar_item("Billing", href="#account/billing"),
                    label="Account",
                    id=f"{_sidebar_id}-account",
                ),
                label="Settings",
                label_id="sidebar-settings-group-label",
            ),
            id=_sidebar_id,
        ),
        class_="relative",
    )
