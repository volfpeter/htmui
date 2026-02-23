from fastapi import HTTPException
from htmy import Component

from basecoat_app.component_docs import ComponentData, component_docs
from htmui.tailwind import centered

from ._examples import centered_example

tailwind_components: dict[str, ComponentData] = {
    "centered": {
        "title": "Centered",
        "code_example": centered_example,
        "component_impl": centered,
        "example": None,
    },
}


def metadata(component: str) -> dict[str, str]:
    data = tailwind_components.get(component)
    return {"title": "Not Found" if data is None else data["title"]}


def page(component: str) -> Component:
    data = tailwind_components.get(component)
    if data is None:
        raise HTTPException(404)

    return component_docs(
        data["code_example"],
        component_name=data["title"],
        impl=data["component_impl"],
        example=data["example"],
    )
