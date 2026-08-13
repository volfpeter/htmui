![Linters](https://github.com/volfpeter/htmui/actions/workflows/linters.yml/badge.svg)

**Source code**: [https://github.com/volfpeter/htmui](https://github.com/volfpeter/htmui)

**Live demo**: [https://htmui.vercel.app](https://htmui.vercel.app)

# htmui

Python UI components for [htmy](https://volfpeter.github.io/htmy/), wrapping [BasecoatUI](https://basecoatui.com/) and [Tailwind CSS](https://tailwindcss.com/).

`htmui` is designed with hypermedia applications, and specifically [HTMX](https://htmx.org/), in mind. Components reproduce Basecoat's documented markup so Basecoat's runtime can enhance them.

`htmy` and `holm` have built-in Jinja support. If you use another templating engine, converting the components is straightforward, because `htmy` mimics HTML.

## Key features

- **Vendored**: copy the components you need into your project and adapt them.
- **`htmui init` CLI** that copies selected components, their dependencies, and shared utilities.
- **BasecoatUI** components as typed `htmy` functions: buttons, dialogs, sidebars, forms, and more.
- Extra helpers such as `codeblock` that are not part of Basecoat.
- Works anywhere `htmy` works, including [holm](https://volfpeter.github.io/holm/).

## Prerequisites

You need [htmy](https://volfpeter.github.io/htmy/) in your project:

```bash
pip install htmy
```

For the best developer experience, it is recommended to use [holm](https://volfpeter.github.io/holm/). It brings built-in `htmy` and HTMX support, and is built around FastAPI.

The copied components also need [BasecoatUI](https://basecoatui.com/) and [Tailwind CSS](https://tailwindcss.com/) on the page. CDN snippets are included (see [Assets](#assets)).

## Usage

`htmui` is designed to be vendored. You do not install it as a runtime dependency. Instead, you copy the components you need into your project and adjust them.

```bash
uvx htmui init
```

This copies the full catalog into `./components`. Use `-c` to copy only the components you need. Dependencies are included automatically:

```bash
uvx htmui init -c dialog -c select
```

Useful options:

```bash
uvx htmui init --src                  # install into src/components/
uvx htmui init -p ui                  # install into ./ui
uvx htmui init -c dialog --dry-run    # print the plan, write nothing
uvx htmui init --force                # overwrite existing files
uvx htmui init --skip-existing        # keep existing files
uvx htmui version                     # package and per-component versions
```

You can also copy files from `htmui/basecoat/` by hand.

### Example

After `htmui init`:

```python
from htmy import ComponentType, html

from components.alert import alert
from components.button import button


def saved() -> ComponentType:
    return html.div(
        alert("Your changes have been saved.", title="Saved"),
        button("Continue"),
    )
```

Every component has a live example and its Python source in the sidebar.

## Assets

You can add the CDN snippets from `cdn` to your document head:

```python
from htmy import ComponentType, html

from components import cdn


def head() -> ComponentType:
    return html.head(
        cdn.css,
        cdn.tailwind_css,
        cdn.js,
    )
```

Some Basecoat classes may not work with the Tailwind CDN setup, so a local JS/CSS setup is recommended for production. The [demo application](https://github.com/volfpeter/htmui/tree/main/app) shows one such setup.

`codeblock` includes optional [Highlight.js](https://highlightjs.org/) helpers for syntax highlighting.

## Related projects

- [htmy](https://volfpeter.github.io/htmy/): async Python server-side rendering.
- [holm](https://volfpeter.github.io/holm/): Next.js-like developer experience on FastAPI, `htmy`, and FastHX.
- [FastHX](https://volfpeter.github.io/fasthx/): HTMX rendering for FastAPI.
- [BasecoatUI](https://basecoatui.com/): the design system these components wrap.

## Support

Consider supporting the project through [sponsoring](https://buymeacoffee.com/volfpeter), or reach out for [consulting](https://www.volfp.com/contact?subject=Consulting%20-%20htmui) so you can get the most out of the library.

## Development

Python:

- `uv` for project and dependency management.
- `poethepoet` for tasks. Run `uv run poe` to see them.
- `mypy` for static analysis.
- `ruff` for formatting and linting.

JavaScript:

- `npm` for the demo app's Tailwind and Basecoat tooling.

To get started:

```bash
uv sync
npm install
honcho start
```

`honcho start` runs the demo app and the Tailwind watcher together. You can also run `uv run poe dev` and `uv run poe build-dev-css --watch` separately.

The index page of the demo is generated from this README (`uv run poe build-content`).

## License

The package is open-sourced under the conditions of the [MIT license](https://choosealicense.com/licenses/mit/).

## Credits

This project wouldn't exist without the components and documentation of [BasecoatUI](https://basecoatui.com/).
