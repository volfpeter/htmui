from holm import Metadata
from htmy import ComponentType, Context, SafeStr, component, html

from htmui import highlightjs
from htmui.basecoat import cdn as basecoat_cdn
from htmui.basecoat import init_on_htmx_history_restore as basecoat_init
from htmui.basecoat import theme_switcher

from .settings import settings


@component.context_only
def head(ctx: Context) -> ComponentType:
    metadata = Metadata.from_context(ctx)
    title = "htmui"
    if (subtitle := metadata.get("title")) is not None:
        title = f"{subtitle} | {title}"

    return html.head(
        html.title(title),
        html.meta(charset="utf-8"),
        html.meta(name="viewport", content="width=device-width, initial-scale=1"),
        html.link(id="favicon", rel="icon", href="/static/favicon.ico"),
        SafeStr(  # HTMX
            '<script src="https://cdn.jsdelivr.net/npm/htmx.org@4.0.0-alpha7/dist/htmx.min.js"></script>'
        ),
        html.link(rel="stylesheet", href=f"/static/{settings.css_file}"),
        basecoat_cdn.js,
        basecoat_init,
        theme_switcher.js,
        highlightjs.js(),
        highlightjs.languages("python"),
        highlightjs.highlight_on_load(
            highlightjs.highlight_event.dom_content_loaded,
            highlightjs.highlight_event.htmx_after_swap,
        ),
    )
