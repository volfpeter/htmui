from typing import Any

from htmy import ComponentType, html

from htmui.basecoat import chart


def example() -> ComponentType:
    return html.div(
        chart.chart(id="linux-market-share-chart", config=_chart_config),
        class_="w-full max-w-2xl",
    )


_chart_config: dict[str, Any] = {
    "type": "line",
    "labelKey": "year",
    "legend": True,
    "data": [
        {"year": "2016", "share": 1.2},
        {"year": "2017", "share": 1.4},
        {"year": "2018", "share": 1.3},
        {"year": "2019", "share": 1.6},
        {"year": "2020", "share": 1.8},
        {"year": "2021", "share": 1.5},
        {"year": "2022", "share": 2.0},
        {"year": "2023", "share": 3.0},
        {"year": "2024", "share": 4.5},
        {"year": "2025", "share": 6.5},
        {"year": "2026", "share": 9.0},
        {"year": "2027", "share": 11.5},
        {"year": "2028", "share": 13.5},
        {"year": "2029", "share": 15.5},
    ],
    "series": {
        "share": {
            "label": "Linux desktop market share",
            "color": "var(--chart-1)",
            "surface": "gradient",
            "dataset": {
                "borderWidth": 1.5,
                "tension": 0.35,
                "pointRadius": 0,
            },
        },
    },
}
