import importlib.resources

from htmy import Snippet, Text

_content = Snippet(Text(importlib.resources.read_text(__package__, "page.html")))


def page() -> Snippet:
    return _content
