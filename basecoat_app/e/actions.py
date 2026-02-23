from typing import Literal

from holm import action
from htmy import Component, html

from htmui.tailwind.centered import centered

_messages: dict[str | None, dict[Literal["title", "message"], str]] = {
    "not-found": {
        "title": "Not Found",
        "message": "The page you are looking was not found.",
    },
    "server-error": {
        "title": "Server Error",
        "message": "An unexpected error has occurred on the server.",
    },
    "bad-request": {
        "title": "Bad Request",
        "message": "The request was malformed or invalid.",
    },
}


def metadata(error_code: str | None = None) -> dict[str, str]:
    msg = _messages.get(error_code, _messages["bad-request"])
    return {"title": msg["title"]}


@action.get("/", use_layout=True, metadata=metadata)
@action.get("/{error_code}", use_layout=True, metadata=metadata)
def page(error_code: str | None = None) -> Component:
    msg = _messages.get(error_code, _messages["bad-request"])
    return centered(
        html.h2(msg["title"], class_="text-2xl font-bold"),
        html.p(msg["message"]),
        class_="gap-4",
    )
