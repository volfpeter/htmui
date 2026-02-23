from htmy import ComponentType, PropertyValue, html
from htmy.utils import join

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "0.3"
__framework_url__ = "https://basecoatui.com/components/card/"


def card(*children: ComponentType, class_: str | None = None, **kwargs: PropertyValue) -> ComponentType:
    return html.div(*children, class_=join("card", class_), **kwargs)
