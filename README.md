# htmui

`htmui` is a Python library that implements complex UI components using `htmy`.

It is designed with hypermedia applications, and specifically HTMX in mind.

What if you are using Jinja or similar templating engines instead of `htmy`? Converting the components from `htmy` to your templating engine of choice is straightforward, because of how `htmy` mimics HTML.

## Prerequisites

You need to have [htmy](https://volfpeter.github.io/htmy/){:target="\_blank"} installed in your project to be able to use `htmui` components.

You can do it with a simple `pip install htmy`.

For the best developer experience, it is recommended to use [holm](https://volfpeter.github.io/holm/){:target="\_blank"} as your application framework. It brings built-in `htmy` (and thus `htmui`) and HTMX support, and is built around FastAPI.

## How to use

`htmui` is designed to be "vendored". You don't install either the library or its components. Instead you copy the components you need into your project and adjust them to fit your requirements.

## UI framework integrations

### BasecoatUI

[BasecoatUI](https://basecoatui.com/){:target="\_blank"} components and utilities are in the `htmui/basecoat` package.

These components require [BasecoatUI](https://basecoatui.com/){:target="\_blank"} and [TailwindCSS](https://tailwindcss.com/){:target="\_blank"} to be installed. While TailwindCSS fully works from a CDN, some BasecoatUI classes do not, so a full local JS setup is recommended.

Most of the BasecoatUI components are implemented, except trivial ones that only require a single CSS class name.

There are also extra components like `codeblock`, that use BasecoatUI to a degree, but are not in BasecoatUI.

### Highlight.js

[Highlight.js](https://highlightjs.org/){:target="\_blank"} components and utilities are in the `htmui/highlightjs.py` module.

### TailwindCSS

[TailwindCSS](https://tailwindcss.com/){:target="\_blank"} components and utilities are in the `htmui/tailwind` package.

There are a couple of simple utility components that use TailwindCSS classes. The goal of these components is to complement TailwindCSS-based UI libraries.

### Unstyled

General components and utilities are in the `htmui/unstyled` package.

Similarly minimal as the TailwindCSS components, the goal is to complement TailwindCSS-based UI libraries.

## Development

### Tools

Python:

- `uv` for project and dependency management.
- `poethepoet` for running tasks. Run `uv run poe` to see all available tasks.
- `mypy` for static code analysis.
- `ruff` is used for formatting and linting.

JavaScript:

- `npm` for managing JavaScript dependencies for example applications.

Other:

- `honcho` for running applications that require multiple processes, like a Python application and the TailwindCSS CLI.

To get started, run `uv sync` and `npm install`.

## Applications

### Basecoat

Just run `honcho start`. This will spin up `basecoat_app` and the corresponding TailwindCSS CLI that generates the application's CSS file.

## License

The package is open-sourced under the conditions of the [MIT license](https://choosealicense.com/licenses/mit/){:target="\_blank"}.

## Credits

This project wouldn't exist without the JavaScript components and excellent documentation of [BasecoatUI](https://basecoatui.com/){:target="\_blank"}.
