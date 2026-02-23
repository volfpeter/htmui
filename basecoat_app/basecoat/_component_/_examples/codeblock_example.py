import inspect

from htmy import ComponentType

from htmui.basecoat.codeblock import codeblock


def example() -> ComponentType:
    return codeblock(inspect.getsource(example), code_class="language-python")
