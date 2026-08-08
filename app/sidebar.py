from htmy import ComponentType, SafeStr, html

from htmui.basecoat.sidebar import sidebar as sidebar_component
from htmui.basecoat.sidebar import sidebar_group, sidebar_item

from .basecoat._component_.page import basecoat_components
from .component_docs import ComponentData


def sidebar(path: str) -> ComponentType:
    return sidebar_component(
        _component_group(
            basecoat_components,
            id="basecoat-components-group",
            path=path,
            title=SafeStr("BasecoatUI"),
            url_prefix="/basecoat",
        ),
        header=html.a(SafeStr("htmui"), href="/", class_="font-semibold", hx_boost="true"),
        id="sidebar",
    )


def _component_group(
    components: dict[str, ComponentData],
    *,
    id: str,
    path: str,
    title: str,
    url_prefix: str,
) -> ComponentType:
    return sidebar_group(
        *(
            sidebar_item(
                comp_data["title"],
                href=href,
                current=(path == href),
                hx_boost="true",
            )
            for comp_path, comp_data in components.items()
            if (href := f"{url_prefix}/{comp_path}/")
        ),
        label=title,
        label_id=id,
        group_class="pt-2",
        list_class="flex flex-col gap-0.5",
    )
