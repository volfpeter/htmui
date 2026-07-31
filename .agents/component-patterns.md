# htmui component patterns

Conventions for `htmui/basecoat/*.py`. Canonical examples: `select.py`, `alert.py`,
`card.py`, `breadcrumb.py`, `toast.py`.

Components and helpers are vendored into apps, small and correct beats exhaustive.

## Module shape

```python
from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "<major>"  # basecoat package major, include minor if component introduced in minor version
__framework_url__ = "https://basecoatui.com/components/<name>/"
```

Per-component JS (major pin only):

```python
js = SafeStr('<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/<name>.min.js" defer></script>')
```

App-wide assets live in `cdn.py`, not per component.

## Functions

Flat functions returning `ComponentType`, children positional:

```python
def select(*items: ComponentType, name: str, ..., **kwargs: PropertyValue) -> ComponentType:
```

Sub-helpers only for non-obvious markup (`option`, hidden input, joined separators).
Do not wrap plain tags (`header`, `section`, `footer`, `a`) — callers use `html.*`.

## `**kwargs`

- Last param; pass straight through to the owned element.
- Component-managed attrs: `kwargs["data_variant"] = ...` so the helper wins.
- No named param that only forwards one optional attr (`aria_label`, one-off `data-*`).

## Classes

`join_classes("alert", class_)` (or `htmy.utils.join`) on the root. Keep the Basecoat
root class; don't re-state layout utilities Basecoat CSS already applies.

## Types

- Shared only in `typing.py`: `Align`, `Side`.
- Everything else is local (`CardSize`, `SidebarItemSize`, `ButtonVariant` and
  `ButtonSize` in `button.py`).
- `data-size` / `data-variant` sets differ per component — grep that component's CSS/mdx.
- One non-default yes/no token → `bool` (`destructive=True`). Size token → local
  `Literal["sm"] | None`. No global `Size`/`Variant`.

## Icons

Inline heroicons as module-level `SafeStr`. Don't invent SVGs — ask. Don't add
docs-only attrs on defaults (`data-rtl-flip`).

## Forms

`name` is the public id (form submit). Derive internal ids from it; no separate `id`
arg for internals.

## Accessibility

Emit a11y attrs only when required for behavior, or when the caller passes them via
kwargs. No default `aria-label` strings; no `aria_label=` hint params.

## Docstrings

One short user-POV line + `Arguments:` in param order, ending with
`**kwargs: Extra attributes for the root element.` No DOM tours. See `alert.py`.

## Scope

Common path only. Skip polish and every docs demo. Trivial single-class components
may be omitted (`html.input_(class_="input")`). One helper may cover multiple Basecoat
components — confirm with the user first.

## Examples

`basecoat_app/.../_examples/<name>_example.py` → `example()`. Don't edit unless the
change breaks it or a required API must be shown. Catalog: `page.py`.
