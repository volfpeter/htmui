import json
from typing import Any, Protocol

from htmy import ComponentType, Fragment, PropertyValue, SafeStr, html

__version__ = "0.2.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/chart/"

js = SafeStr(
    '<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/chart.min.js" defer></script>'
)

chart_js = SafeStr('<script src="https://cdn.jsdelivr.net/npm/chart.js/dist/chart.umd.min.js"></script>')
"""Chart.js CDN script."""


class ChartInitScriptFactory(Protocol):
    """
    Callable protocol for building a chart initialization script element
    from a canvas ID and a chart config.
    """

    def __call__(self, id: str, config: dict[str, Any], /) -> ComponentType:
        """
        Returns the script element that initializes the chart for
        the given ID with the given chart config.
        """
        ...


class handle_chart_init:
    @staticmethod
    def default(id: str, config: dict[str, Any], /) -> ComponentType:
        """
        Default `ChartInitScriptFactory` which initializes the chart once
        the Basecoat runtime is ready.
        """
        config_json = json.dumps(config, separators=(",", ":")).replace("</", "<\\/")
        return html.script(
            SafeStr(
                f"""(() => {{
  const canvas = document.getElementById({json.dumps(id)});
  if (!canvas) return;
  const init = () => window.basecoat?.chart?.(canvas, {config_json});
  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", init, {{ once: true }});
  }} else {{
    init();
  }}
}})();"""
            )
        )


def chart(
    *,
    id: str,
    config: dict[str, Any] | None = None,
    class_: str | None = None,
    script: ChartInitScriptFactory | None = handle_chart_init.default,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Chart.js canvas themed with Basecoat defaults.

    Arguments:
        id: Canvas element ID.
        config: Optional JSON-serializable config for `basecoat.chart()`.
            See the Basecoat Chart documentation for details.
        class_: Extra CSS classes for the canvas element.
        script: Optional callback that receives the canvas ID and `config` and
            returns the initialization script element. Defaults to
            `handle_chart_init.default`.
        **kwargs: Extra attributes for the canvas element.
    """
    canvas = html.canvas(
        id=id,
        class_=class_,
        **kwargs,
    )
    if config is None or script is None:
        return canvas

    return Fragment(canvas, script(id, config))
