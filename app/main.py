from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request, Response
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from holm import App

app = FastAPI()

app.add_middleware(GZipMiddleware)


@app.middleware("http")
async def cache_control(_request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    response: Response = await call_next(_request)
    response.headers["cache-control"] = (
        "public, max-age=172800, s-maxage=172800, stale-while-revalidate=86400"
    )
    return response


app.mount("/static", StaticFiles(directory="static"), name="static")

App(app=app)
