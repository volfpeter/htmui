---
name: basecoat-to-htmui
description: Create or update the htmui implementation of a Basecoat component.
---

# Skill: Basecoat to htmui

Convert a BasecoatUI component (from its `.mdx` doc) into an `htmui/basecoat/` wrapper,
or upgrade an existing wrapper to a new Basecoat version. The user supplies the path to
the component's `.mdx` file under `basecoat/site/src/docs/components/`.

Follow documented htmui component patterns (`.agents/component-patterns.md`) for module
shape, functions, kwargs handling, types, docstrings, icons, and scope.

## Workflow

Run through this checklist:

- [ ] Read the user-provided `.mdx` fully. The `<Preview>` block holds the canonical DOM; the `HTML structure` `<dl>` documents each element and its `data-*`/`aria-*` attributes. These are the source of truth for markup.
- [ ] Cross-check allowed `data-*` values against `basecoat/src/css/components/<name>.css` — don't invent variants/sizes/sides.
- [ ] Read `basecoat/src/templates/{jinja,nunjucks}/` for the matching macro to infer intended argument naming and grouping.
- [ ] Decide coverage: - Trivial component (single class, no required structure or JS)? Omit it — render with an `htmy` primitive and tell the user. - Multiple Basecoat components map to one htmui component? Confirm coverage with the user (e.g. `dialog` also serves `alert-dialog`). - Don't implement every documented option — cover general use-cases; let `**kwargs` carry rare configs.
- [ ] If upgrading an existing `htmui/basecoat/<name>.py`: - Diff old mdx vs new mdx (or old vs new `HTML structure`) to spot added/removed attributes, renamed `data-*`, structural changes. - Update `__framework_version__` to the major version of the checked-out `basecoat/package.json` and `__framework_url__` if the slug changed. - JS/CSS asset tags use the major version (`@1`), not a patch pin. Only touch them if the bundle name or path actually changed. - Preserve existing icons unless their markup changed; if a new/changed icon is uncertain, ask the user for the SVG content — don't invent it.
- [ ] Implement/patch the component following `.agents/component-patterns.md`: module header, flat functions, `**kwargs` pass-through with component-managed attrs assigned via `kwargs[...] = ...`, `join_classes(...)` for class extension, component-scoped types local / shared types in `typing.py`, user-POV docstrings with an `Arguments:` block.
- [ ] Add or update `basecoat_app/basecoat/_component_/_examples/<name>_example.py` (`example()` returning `ComponentType`) showing idiomatic usage, and keep the catalog in `basecoat_app/basecoat/_component_/page.py` in sync (slug → impl + example).
- [ ] Run `uv run poe check`. Fix lint/type issues. (Not required, but cheap.)

## Notes

- No automated render verification is required. When output looks wrong or you want to
  inspect markup, render inline: `uv run python -c "from htmy import render; ..."`.
- Flag any non-trivial coverage or API decision to the user before committing to it.
