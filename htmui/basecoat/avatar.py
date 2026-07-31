from typing import Literal, TypeAlias

from htmy import ComponentType, PropertyValue, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "1"
__framework_url__ = "https://basecoatui.com/components/avatar/"

AvatarSize: TypeAlias = Literal["sm", "lg"]


def avatar(
    *children: ComponentType,
    size: AvatarSize | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Avatar component.

    Arguments:
        *children: Avatar content.
        size: Avatar size.
        class_: Extra CSS classes for the avatar.
        **kwargs: Extra attributes for the avatar.
    """
    if size is not None:
        kwargs["data_size"] = size

    return html.span(*children, class_=join_classes("avatar", class_), **kwargs)


def avatar_group(
    *children: ComponentType,
    count: ComponentType | str | None = None,
    class_: str | None = None,
    **kwargs: PropertyValue,
) -> ComponentType:
    """
    Group of overlapping avatars with an optional trailing count indicator.

    Arguments:
        *children: Avatar components.
        count: Content of the trailing `data-count` indicator.
        class_: Extra CSS classes for the group.
        **kwargs: Extra attributes for the root element.
    """
    if count is not None:
        children = (*children, html.span(count, data_count=""))

    return html.div(*children, class_=join_classes("avatar-group", class_), **kwargs)
