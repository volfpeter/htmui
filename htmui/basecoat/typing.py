from typing import Literal, Protocol, TypeAlias

from htmy import PropertyValue

Align: TypeAlias = Literal["start", "center", "end"]

HorizontalSide: TypeAlias = Literal["left", "right"]

Side: TypeAlias = HorizontalSide | Literal["top", "bottom"]

InlineSide: TypeAlias = Literal["inline-start", "inline-end"]

FloatingSide: TypeAlias = Side | InlineSide


class IdToProperty(Protocol):
    """Callable protocol for building a property value from an HTML element ID."""

    def __call__(self, id: str, /) -> PropertyValue:
        """Returns the property value for the given ID."""
        ...
