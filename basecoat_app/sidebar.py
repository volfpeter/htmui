from htmy import ComponentType, SafeStr, html

from htmui.basecoat.sidebar import sidebar as sidebar_component

from .basecoat._component_.page import basecoat_components
from .component_docs import ComponentData
from .tailwind._component_.page import tailwind_components
from .unstyled._component_.page import unstyled_components


def sidebar(path: str) -> ComponentType:
    return sidebar_component(
        _component_group(
            basecoat_components,
            id="basecoat-components-group",
            path=path,
            title=SafeStr("BasecoatUI"),
            url_prefix="/basecoat",
        ),
        _component_group(
            tailwind_components,
            id="tailwind-components-group",
            path=path,
            title=SafeStr("TailwindCSS"),
            url_prefix="/tailwind",
        ),
        _component_group(
            unstyled_components,
            id="unstyled-components-group",
            path=path,
            title=SafeStr("Unstyled"),
            url_prefix="/unstyled",
        ),
        header=html.header(html.a(SafeStr("htmui"), href="/", hx_boost="true"), class_="font-semibold"),
    )


def _component_group(
    components: dict[str, ComponentData],
    *,
    id: str,
    path: str,
    title: str,
    url_prefix: str,
) -> ComponentType:
    return html.div(
        html.h3(title, id=id, class_="pt-2"),
        html.ul(
            *(
                html.li(
                    html.a(
                        comp_data["title"],
                        href=href,
                        hx_boost="true",
                        **({"aria-current": "page"} if path == href else {}),
                    )
                )
                for comp_path, comp_data in components.items()
                if (href := f"{url_prefix}/{comp_path}/")
            ),
            class_="flex flex-col gap-0.5",
        ),
        class_="group",
        aria_labelledby=id,
    )
