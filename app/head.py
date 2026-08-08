from holm import Metadata
from htmy import ComponentType, Context, SafeStr, component, html

from htmui.basecoat import cdn as basecoat_cdn
from htmui.basecoat import chart as basecoat_chart
from htmui.basecoat import codeblock, theme_switcher
from htmui.basecoat import init_on_htmx_history_restore as basecoat_init

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
        basecoat_chart.chart_js,
        basecoat_chart.js,
        basecoat_init,
        theme_switcher.js,
        codeblock.highlightjs_js(),
        codeblock.highlightjs_languages("python"),
        codeblock.highlightjs_on_load(
            codeblock.highlightjs_events.dom_content_loaded,
            codeblock.highlightjs_events.htmx_after_swap,
        ),
    )
