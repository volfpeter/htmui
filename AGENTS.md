# htmui

`htmui` is an `htmy` component library that wraps [BasecoatUI](https://basecoatui.com).
Each component is a thin Python helper that reproduces Basecoat's documented
HTML/CSS/JS so users get server-rendered markup that Basecoat's runtime enhances.

Users copy helpers into their apps and adapt them — keep APIs lean.

## Repo layout

- `htmui/` — the component library
  - `basecoat/` — BasecoatUI wrappers (`select.py`, `dialog.py`, …). Apps copy these
    files and adapt as needed.
  - `tailwind/`, `unstyled/` — framework-agnostic helpers.
  - `basecoat/typing.py` — shared types only (e.g. `Align`, `Side`). Component-scoped
    types stay in their module (`ButtonVariant`, `ButtonSize` live in `button.py`).
- `basecoat/` — checked-out BasecoatUI source (source of truth):
  - `site/src/docs/components/*.mdx` — docs; `<Preview>` is the canonical DOM.
  - `src/css/components/*.css`, `src/css/styles/*.css` — allowed `data-*` values
    (per component, not global).
  - `src/templates/{jinja,nunjucks}/` — reference macros (naming/intent; may be absent).
- `basecoat_app/` — demo app
  - `basecoat/_component_/page.py` — slug → impl + example.
  - `basecoat/_component_/_examples/` — one `*_example.py` per component. Check it
    before changing a public API.

## Conventions

- Root class + `data-*` (`class="btn" data-variant="outline"`), not `btn-outline`.
  Grep Basecoat for **that** component — don't invent values.
- Flat functions returning `htmy` `ComponentType`. Match existing modules
  (`select.py`, `alert.py`, `card.py`).
- Cover general use-cases; `**kwargs` for the rest. API/layout/docstring/example
  rules: `.agents/component-patterns.md`.
- Create/upgrade a component: `.agents/skills/basecoat-to-htmui`.
- Before finishing:

  ```
  uv run poe check        # ruff format --check, ruff check, mypy (strict)
  uv run poe check --fix  # also auto-fix
  uv run poe basecoat-dev # serve the demo app
  ```

## Debugging

Optional. To inspect markup, render with `htmy.renderer.Renderer` (async) and print
the string. Not a required step.
