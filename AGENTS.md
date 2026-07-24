# Agent notes for htmui

## Repo structure

- `htmui/`: htmy component library
  - `basecoat/`: BasecoatUI component implementations (Python helpers)
  - `tailwind/`: Tailwind-specific helpers
  - `unstyled/`: Unstyled primitives (e.g. `menu`)
- `basecoat_app/`: Demo/docs application
  - `basecoat/_component_/`: Pages and examples for each implemented component
  - `basecoat/_component_/_examples/`: Example code rendered on each page
  - `basecoat/_component_/page.py`: Sidebar/source-of-truth for implemented components

The BasecoatUI repo may be checked out to `basecoat/`, its structure:

- `site/src/docs/components/*.mdx`: Component documentation
- `src/css/components/`: Component CSS
- `src/js/`: Component JavaScript
- `src/templates/{jinja,nunjucks}/`: Reference template macros

## Basecoat to htmui mapping policy

- `htmui.basecoat` modules produce the HTML/CSS/JS markup documented in BasecoatUI
- One htmui component may cover multiple Basecoat components (e.g. `dialog` also serves alert-dialog)
- Trivial Basecoat components - single class, no required structure or extra JS - may be omitted from htmui and rendered directly with `htmy` primitives, eg. `html.input_(class_="input")`
- App-specific utilities that happen to use Basecoat classes (e.g. `codeblock`) can live in `htmui/basecoat/` even if they are not Basecoat components

## Component discovery

- Basecoat component list if checked out: `basecoat/site/src/docs/components/*.mdx`
- Implemented htmui components: `htmui/basecoat/*.py`
- Live component catalog: `basecoat_app/basecoat/_component_/page.py`
- Examples show real usage and should be checked before changing APIs

## API and docstring conventions

- Docstrings should describe behavior from the user's point of view, not the
  implementation detail (e.g. what an attribute does for the user, not which
  HTML attribute it sets).
- For form components, prefer `name` as the primary public identifier. Derive
  internal element ids from `name` (e.g. `{name}-root`) instead of exposing a
  separate `id` argument. The user cares about the submitted form data, not
  internal ids.

## Key learnings

- Basecoat v1 uses root class + data attributes (`class="btn" data-variant="outline"`), not the old composed classes (`btn-outline`). Legacy aliases are only in the optional compat stylesheet
- CSS style packs are standalone bundles (`vega.css`, `nova.css`, etc.); do not layer them on top of each other
- JavaScript is split into `basecoat.min.js` runtime + per-component scripts (or `all.min.js`). Component methods (`sidebar.toggle()`, `toaster.toast()`, `window.basecoat.theme.*`) replaced the old `basecoat:*` custom events
- Some documented "components" are patterns, not CSS components: Spinner, Pagination, Scroll Area
- The checked-out `basecoat/` repo is the best source of truth for markup and API changes; docs often include template-macro hints
