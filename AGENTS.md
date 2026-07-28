# htmui

`htmui` is an `htmy` component library that wraps [BasecoatUI](https://basecoatui.com).
Each component is a thin Python helper that reproduces Basecoat's documented
HTML/CSS/JS so users get server-rendered markup that Basecoat's runtime enhances.

## Repo layout

- `htmui/` — the component library
  - `basecoat/` — BasecoatUI component implementations (`select.py`, `dialog.py`, ...).
    Wrapper components live here, grouped by target framework. Apps copy these files
    into their own codebase and adapt as needed.
  - `tailwind/`, `unstyled/` — other, framework-agnostic helpers.
  - `basecoat/typing.py` — shared types only (`Align`, `Side`, `ButtonVariant`,
    `ButtonSize`). Component-scoped types live in their own module.
- `basecoat/` — the checked-out BasecoatUI source. The source of truth for markup
  and APIs:
  - `site/src/docs/components/*.mdx` — component docs (the `<Preview>` block holds the
    canonical DOM).
  - `src/css/components/*.css` — defines allowed `data-*` values.
  - `src/templates/{jinja,nunjucks}/` — reference template macros, useful for naming
    and argument intent.
- `basecoat_app/` — demo/docs app rendering every component.
  - `basecoat/_component_/page.py` — catalog mapping slug → implementation + example.
  - `basecoat/_component_/_examples/` — one `*_example.py` per component showing real
    usage. Check the example before changing a component's public API.

## Conventions

- Basecoat uses root class + `data-*` attributes (`class="btn" data-variant="outline"`),
  not composed classes like `btn-outline`. Don't invent `data-*` values — grep the
  Basecoat source.
- Components are flat functions returning `htmy` `ComponentType`, not classes. Match
  the style of existing components (see `select.py`, `dropdown_menu.py`).
- Don't implement every Basecoat option. Cover general use-cases; `**kwargs` passes
  rare configs straight to the element. Users copy and modify components freely.
- Run lint/types before finishing:

  ```
  uv run poe check        # ruff format --check, ruff check, mypy (strict)
  uv run poe check --fix  # also auto-fix
  uv run poe basecoat-dev # serve the demo app
  ```

- When something about a component's structure isn't clear, read existing
  implementations — they set the patterns. See `.agents/component-patterns.md` for
  the detailed conventions.

## Debugging

You don't need to verify every change, but when output looks wrong or you want to
inspect rendered markup, run an inline renderer:

```
uv run python -c "from htmy import render; from htmui.basecoat import select; ..."
```

Import the component(s), build the tree, and print the rendered string. This is a
debugging tool — use it when needed, not as a required step.
