from fastapi import Request
from htmy import Component, ComponentType, SafeStr, html

from htmui.basecoat.sidebar import sidebar_toggle
from htmui.basecoat.theme_switcher import theme_switcher

from .head import head
from .sidebar import sidebar


def layout(children: ComponentType, request: Request) -> Component:
    """Root layout wrapping all pages."""
    return (
        html.DOCTYPE.html,
        html.html(
            head(),
            html.body(
                sidebar(request.url.path),
                html.div(
                    html.header(
                        sidebar_toggle(class_="btn-icon-ghost mr-auto"),
                        html.h1(
                            html.a(
                                "BasecoatUI",
                                href="https://basecoatui.com",
                                class_="font-semibold underline",
                                target="_blank",
                            ),
                            " components for ",
                            html.a(
                                "htmy",
                                href="https://volfpeter.github.io/htmy",
                                class_="font-semibold underline",
                                target="_blank",
                            ),
                            ".",
                        ),
                        theme_switcher(),
                        html.a(
                            github_icon,
                            href="https://github.com/volfpeter/htmui",
                            target="_blank",
                            class_="btn-icon size-8",
                            data_tooltip="GitHub repository",
                            data_side="bottom",
                            data_align="end",
                        ),
                        class_="w-full flex shrink-0 items-center p-4 gap-2 sticky top-0 z-10 "
                        "bg-background isolate border-b",
                    ),
                    html.main(
                        html.div(children, class_="mx-auto w-full flex-1 max-w-screen-md"),
                        class_=(
                            "w-full max-w-screen-lg p-4 md:p-6 xl:p-12 mx-auto relative flex gap-10 grow"
                        ),
                    ),
                    html.footer(
                        html.p(
                            "Built with ",
                            html.a(
                                "holm",
                                href="https://volfpeter.github.io/holm",
                                class_="font-semibold underline",
                                target="_blank",
                            ),
                            ", ",
                            html.a(
                                "htmy",
                                href="https://volfpeter.github.io/htmy",
                                class_="font-semibold underline",
                                target="_blank",
                            ),
                            ", ",
                            html.a(
                                "htmui",
                                href="https://github.com/volfpeter/htmui",
                                class_="font-semibold underline",
                                target="_blank",
                            ),
                            ", ",
                            html.a(
                                "BasecoatUI",
                                href="https://basecoatui.com",
                                class_="font-semibold underline",
                                target="_blank",
                            ),
                            ", and ",
                            html.a(
                                "FastAPI",
                                href="https://fastapi.tiangolo.com",
                                class_="font-semibold underline",
                                target="_blank",
                            ),
                            ".",
                        ),
                        class_="p-4 gap-2",
                    ),
                    class_="min-h-full flex flex-col",
                ),
                class_="h-screen v-screen",
            ),
        ),
    )


github_icon = SafeStr(
    '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 '
    "22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 "
    "1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 "
    '5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>'
)
"""`github` icon from https://lucide.dev/."""
