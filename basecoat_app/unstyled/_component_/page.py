from fastapi import HTTPException
from htmy import Component

from basecoat_app.component_docs import ComponentData, component_docs
from htmui.unstyled import menu

from ._examples import menu_example

unstyled_components: dict[str, ComponentData] = {
    "menu": {
        "title": "Menu",
        "code_example": menu_example,
        "component_impl": menu,
        "example": None,
    }
}


def metadata(component: str) -> dict[str, str]:
    data = unstyled_components.get(component)
    return {"title": "Not Found" if data is None else data["title"]}


def page(component: str) -> Component:
    data = unstyled_components.get(component)
    if data is None:
        raise HTTPException(404)

    return component_docs(
        data["code_example"],
        component_name=data["title"],
        impl=data["component_impl"],
        example=data["example"],
    )
