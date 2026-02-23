import asyncio
from pathlib import Path

from htmy import Renderer, md
from typer import Typer

app = Typer(name="CLI for the Basecoat app.")

app_path = Path(__file__).parent


@app.command()
def ping() -> None:
    # Until there are multiple commands.
    print("pong")


@app.command()
def build_static_content() -> None:
    """
    Regenerates the static content of the app.
    """

    async def task() -> None:
        # -- Generate the index page from the README.md file.
        readme = app_path.parent / "README.md"
        page_html = await Renderer().render(md.MD(readme))

        with open(app_path / "page.html", "w") as file:
            file.write(page_html)

    asyncio.run(task())


if __name__ == "__main__":
    app()
