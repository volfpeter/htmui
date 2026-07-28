from typing import Literal, TypeAlias

Align: TypeAlias = Literal["start", "center", "end"]

Side: TypeAlias = Literal["top", "bottom", "left", "right", "inline-start", "inline-end"]

ButtonVariant: TypeAlias = Literal["outline", "secondary", "ghost", "destructive", "link"]

ButtonSize: TypeAlias = Literal["xs", "sm", "default", "lg", "icon", "icon-xs", "icon-sm", "icon-lg"]
