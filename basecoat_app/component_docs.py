import inspect
from typing import Any, Protocol, TypedDict

from htmy import ComponentType, SafeStr, html

from htmui.basecoat.codeblock import codeblock
from htmui.tailwind.centered import centered


class Example(Protocol):
    def example(self) -> ComponentType: ...


class ComponentData(TypedDict):
    title: str
    code_example: Example
    component_impl: Any
    example: ComponentType


def component_docs(
    code_example: Example, *, component_name: str, impl: Any, example: ComponentType = None
) -> ComponentType:
    framework_docs: ComponentType = None
    if (framework := getattr(impl, "__framework__", None)) and (
        framework_url := getattr(impl, "__framework_url__", None)
    ):
        framework_docs = html.p(
            SafeStr("For more details, see the "),
            html.a(
                SafeStr(f"{framework} documentation"),
                href=str(framework_url),
                class_="font-semibold underline",
                target="_blank",
            ),
            ".",
        )
    return html.div(
        html.h1(component_name, class_="text-3xl font-bold"),
        html.h2(SafeStr("Example:"), class_="text-2xl font-bold"),
        centered(example or code_example.example(), class_="border rounded-xl p-4"),
        html.hr(),
        html.h2(SafeStr("Code example:"), class_="text-2xl font-bold"),
        codeblock(inspect.getsource(code_example), code_class="language-python"),  # type: ignore[arg-type]
        html.hr(),
        html.h2(SafeStr("Component implementation:"), class_="text-2xl font-bold"),
        framework_docs,
        codeblock(inspect.getsource(impl), code_class="language-python"),
        class_="flex flex-col gap-4",
    )
