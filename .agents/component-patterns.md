# htmui component patterns

Detailed conventions for `htmui/basecoat/*.py` and their demo examples. Read existing
implementations (`select.py`, `dropdown_menu.py`, `combobox.py`, `menu.py`) when
something here is unclear — they are the canonical examples.

## Module shape

Every component module starts with:

```python
from htmy import ComponentType, PropertyValue, SafeStr, html, join_classes

__version__ = "0.1.0"
__framework__ = "BasecoatUI"
__framework_version__ = "<major>"            # major version of the checked-out basecoat lib
__framework_url__ = "https://basecoatui.com/components/<name>/"
```

`component_docs.py` reads `__framework__`/`__framework_url__` to link out from the demo
page, so keep them accurate.

If the component needs a per-component JS bundle, expose it as a module-level `SafeStr`:

```python
js = SafeStr('<script src="https://cdn.jsdelivr.net/npm/basecoat-css@1/dist/js/<name>.min.js" defer></script>')
```

Pin to the major version (`@1`), not a patch version, matching the checked-out
`basecoat/package.json` major. Use the shared `htmui/basecoat/cdn.py` for app-wide
assets, not per-component.

## Components are functions, not classes

One function per logical piece, all returning `ComponentType`. Expose sub-parts the
user composes (e.g. `select()` + `option()` + `group()` + `separator`). The root
function takes children positionally:

```python
def select(*items: ComponentType, name: str, ..., **kwargs: PropertyValue) -> ComponentType:
```

## `**kwargs` pass-through

- `**kwargs: PropertyValue` is the last parameter. It passes user attrs straight to a
  specific element — don't build intermediate dicts for it.
- For component-managed attrs derived from named params, assign directly
  (`kwargs["data-..."] = ...`) so the helper's value wins over any user value. The
  user edits the helper if they truly need to override.
- Trivial attrs can be set inline on the element.

## Class extension

Use `join_classes("basecoat-root-class", class_)` on the root so users pass extra
classes via `class_`. Component-managed classes (`btn`, `select`, ...) go in the join;
don't drop the base class.

## Types

- Shared cross-component types belong in `htmui/basecoat/typing.py`
  (`Align`, `Side`, `ButtonVariant`, `ButtonSize`). A helper rendering a plain `btn`
  reuses `ButtonVariant`/`ButtonSize`.
- Component-scoped variant/size scopes (e.g. sidebar items) live in the component's
  own module.
- Before defining a `Literal[...]`, grep `basecoat/src/css/components/*.css` and the
  mdx `HTML structure` block for the documented `data-*` values. Don't invent them.

## Icons

htmui can't rely on lucide being available, so icons are inlined as module-level
`SafeStr` string literals, usually from [heroicons](https://heroicons.com). Copy the
SVG verbatim. If an icon already exists in the module, don't redefine it. If you need
a new/uncertain icon, ask the user for the content rather than inventing markup.

## Form components

Prefer `name` as the primary public identifier (it's what the form submits). Derive
internal element ids from it when needed. Don't expose a separate `id` argument for
form internals.

## Accessibility

Don't default `aria-label` or other a11y attrs unless the component needs them to
function. Default to `None` and emit only when provided.

## Docstrings

Describe behavior from the user's point of view, never the produced DOM/HTML. Match
`select.py`/`dropdown_menu.py`: an `Arguments:` section listing each parameter in
order, ending with:

```
    **kwargs: Extra attributes for the root element.
```

## Scope: cover general use-cases, not everything

Don't implement every Basecoat option or attribute. Cover the common path; let
`**kwargs` carry rare configs. Users copy components into their codebase and adapt —
keep the helper lean.

Trivial Basecoat components (single class, no required structure or extra JS) may be
omitted from htmui and rendered directly with `htmy` primitives, e.g.
`html.input_(class_="input")`. App-specific helpers that use Basecoat classes (e.g.
`codeblock`) can still live in `htmui/basecoat/`.

One htmui component may cover multiple Basecoat components (e.g. `dialog` also serves
`alert-dialog`). When deciding coverage, flag it to the user.

## Demo examples

`basecoat_app/basecoat/_component_/_examples/<name>_example.py` defines an
`example()` function returning `ComponentType` showing real, idiomatic usage. Check
the existing example before changing a component's public API — the example is the
demonstrated contract. The catalog in
`basecoat_app/basecoat/_component_/page.py` maps each slug to its implementation and
example; keep it in sync when adding/removing components.
