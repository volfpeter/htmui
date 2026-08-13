import asyncio
import re
from pathlib import Path

from htmy import Renderer, html, md
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
        page_html = await Renderer().render(
            # Wrap markdown so the app's prose list styling (list-disc/decimal) is
            # scoped to documentation content only and never reaches component
            # <ul>/<ol> implementations elsewhere.
            html.div(md.MD(readme), data_markdown="")
        )

        with open(app_path / "page.html", "w") as file:
            file.write(_add_heading_ids(page_html))

    asyncio.run(task())


def _add_heading_ids(content: str) -> str:
    """Add GitHub-style heading ids so in-page anchors work."""

    def repl(match: re.Match[str]) -> str:
        level, inner = match.group(1), match.group(2)
        slug = _slug(inner)
        if slug == "":
            return match.group(0)
        return f'<h{level} id="{slug}">{inner}</h{level}>'

    return re.compile(r"<h([1-6])>(.*?)</h\1>", flags=re.DOTALL).sub(repl, content)


def _slug(text: str) -> str:
    cleaned = re.compile(r"<[^>]+>").sub("", text).strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", cleaned).strip("-")


if __name__ == "__main__":
    app()
