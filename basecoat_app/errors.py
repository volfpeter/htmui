from fastapi import Request
from fastapi.responses import RedirectResponse
from holm.fastapi import FastAPIErrorHandler
from holm.typing import ErrorHandlerMapping


def make_redirect_handler(error_type: str) -> FastAPIErrorHandler:
    async def handler(_request: Request, _err: Exception) -> RedirectResponse:
        return RedirectResponse(url=f"/e/{error_type}", status_code=302)

    return handler


handlers: ErrorHandlerMapping = {
    400: make_redirect_handler("bad-request"),
    404: make_redirect_handler("not-found"),
    500: make_redirect_handler("server-error"),
    Exception: make_redirect_handler("server-error"),
}
