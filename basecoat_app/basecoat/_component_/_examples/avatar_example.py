from urllib.parse import quote

from htmy import ComponentType, html

from htmui.basecoat.avatar import avatar, avatar_group


def example() -> ComponentType:
    return html.div(
        html.h3("Basic:"),
        html.div(
            avatar(_img("SH", "#6366f1")),
            class_="flex items-center gap-2",
        ),
        html.h3("Sizes:"),
        html.div(
            avatar(_img("VN", "#10b981"), size="sm"),
            avatar(_img("PE", "#f43f5e")),
            avatar(_img("PJ", "#0ea5e9"), size="lg"),
            class_="flex items-center gap-2",
        ),
        html.h3("Badge:"),
        html.div(
            avatar(
                _img("VA", "#f97316"),
                html.span(class_="avatar-badge bg-green-600 dark:bg-green-800"),
            ),
            class_="flex items-center gap-2",
        ),
        html.h3("Group:"),
        avatar_group(
            avatar(_img("VJ", "#f59e0b")),
            avatar(_img("VP", "#ec4899")),
            avatar(_img("VA", "#8b5cf6")),
        ),
        html.h3("Group with count:"),
        avatar_group(
            avatar(_img("PJ", "#0ea5e9")),
            avatar(_img("SH", "#6366f1")),
            avatar(_img("PE", "#f43f5e")),
            avatar(_img("VN", "#10b981")),
            count="+3",
        ),
        class_="flex flex-col gap-2",
    )


def _img(initials: str, color: str) -> ComponentType:
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<circle cx="32" cy="32" r="32" fill="{color}"/>'
        f'<text x="32" y="32" dy=".35em" text-anchor="middle" '
        'font-family="system-ui, sans-serif" font-size="24" font-weight="600" fill="#fff">'
        f"{initials}</text></svg>"
    )
    return html.img(src=f"data:image/svg+xml,{quote(svg)}", alt=initials)
