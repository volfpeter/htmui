---
name: basecoat-to-htmui
description: Create or update the htmui implementation of a Basecoat component.
---

# Skill: Basecoat to htmui

Convert or upgrade a BasecoatUI component into `htmui/basecoat/`. User supplies the
`.mdx` under `basecoat/site/src/docs/components/`.

Follow `AGENTS.md` and `.agents/component-patterns.md` for API shape — this skill is
**workflow only**.

## Workflow

For upgrades: **summarize the plan and flag API decisions before editing**, unless
the user already said to implement.

1. Read the `.mdx` (`<Preview>` + HTML structure = markup source of truth).
2. Grep allowed `data-*` in `basecoat/src/css/components/<name>.css` and
   `basecoat/src/css/styles/*.css`. Per-component values only.
3. Skim `basecoat/src/templates/{jinja,nunjucks}/` if a macro exists (naming hints).
4. **Upgrade path:** diff current helper vs v1. If already compatible, say so and stop.
   Otherwise fix real gaps only (root class, structure, `data-*`, JS API). Bump
   `__framework_version__` to `basecoat/package.json` major. Touch JS/CSS tags only if
   bundle path changed (`@1` major pin). Keep icons unless markup must change; ask
   before inventing SVGs.
5. **Coverage:** trivial one-class components → omit (use `html.*`). Multi-component
   mapping (e.g. dialog/alert-dialog) → confirm with user. Common path only; demos
   (RTL, custom colors, nested widgets) are out of scope unless asked.
6. Implement per `.agents/component-patterns.md`.
7. **Examples:** edit only if broken by the change or a new required API must appear.
   Sync `page.py` only when adding/removing catalog entries.
8. `uv run poe check`.

## Notes

- No required render verification; use `Renderer` from `AGENTS.md` if markup looks wrong.
- When unsure if a value needs a named param → kwargs; mention it in the plan.
