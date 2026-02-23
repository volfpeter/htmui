from htmy import SafeStr

_default_version = "11.11.1"


def theme(theme: str = "default", *, version: str = _default_version) -> SafeStr:
    return SafeStr(
        f'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/{version}/styles/{theme}.min.css">'
    )


def js(*, version: str = _default_version) -> SafeStr:
    return SafeStr(
        f'<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/{version}/highlight.min.js"></script>'
    )


def languages(*languages: str, version: str = _default_version) -> SafeStr:
    return SafeStr(
        "\n".join(
            (
                f'<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/{version}/languages/{lang}.min.js"></script>'
                for lang in languages
            )
        )
    )


class highlight_event:
    dom_content_loaded = "DOMContentLoaded"
    htmx_after_swap = "htmx:after:swap"
    htmx_v2_after_swap = "htmx:afterSwap"


def highlight_on_load(*events: str) -> SafeStr:
    return SafeStr(
        "\n".join(
            (
                "<script>",
                "const highlight = () => {",
                "  if (!window.hljs) return;",
                "  document",
                "  .querySelectorAll("
                "    'pre code:not([data-highlighted]), code.highlight:not([data-highlighted])'"
                ")",
                "  .forEach(el => window.hljs.highlightElement(el));",
                "};",
                "",
                "if (!window._hljsInit) {",
                "  window._hljsInit = true;",
                *(f"  document.addEventListener('{event}', highlight);" for event in events),
                "}",
                "</script>",
            )
        )
    )
