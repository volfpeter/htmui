"""htmui command-line interface."""

import ast
import shutil
import sys
from pathlib import Path
from typing import Annotated, Literal, TypeAlias

import typer

SOURCE_DIR = Path(__file__).parent / "basecoat"
UTILITIES = {"cdn", "typing"}
INIT_STEM = "__init__"

_Action: TypeAlias = Literal["new", "overwrite", "skip", "prompt"]

app = typer.Typer(name="htmui", no_args_is_help=True)


@app.command()
def init(
    src: Annotated[
        bool, typer.Option("--src", help="Install under src/<package>/ instead of <package>/.")
    ] = False,
    package: Annotated[
        str, typer.Option("-p", "--package", help="Target package directory name.")
    ] = "components",
    components: Annotated[
        list[str] | None, typer.Option("-c", "--component", help="Component to install (repeatable).")
    ] = None,
    force: Annotated[
        bool, typer.Option("-f", "--force", help="Overwrite existing files without asking.")
    ] = False,
    skip_existing: Annotated[
        bool, typer.Option("--skip-existing", help="Skip existing files without asking.")
    ] = False,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Show what would be done; write nothing.")
    ] = False,
) -> None:
    """
    Install basecoat components into the current project.

    Copies the selected components, or the full catalog if none are given, plus
    their dependencies and shared utilities. Existing `__init__.py` is never
    overwritten.
    """
    if force and skip_existing:
        typer.echo("Error: --force and --skip-existing are mutually exclusive.", err=True)
        raise typer.Exit(1)

    catalog = _selectable_catalog()
    catalog_set = set(catalog)

    requested = list(dict.fromkeys([] if components is None else components))
    unknown = [c for c in requested if c not in catalog_set]
    if len(unknown) > 0:
        typer.echo(f"Error: unknown component(s): {', '.join(unknown)}", err=True)
        typer.echo(f"Available components: {', '.join(catalog)}", err=True)
        raise typer.Exit(1)

    base = (Path.cwd() / "src" / package) if src else (Path.cwd() / package)
    if base.exists() and base.is_file():
        typer.echo(f"Error: {base} exists and is a file, not a directory.", err=True)
        raise typer.Exit(1)

    selection = requested if len(requested) > 0 else list(catalog)
    resolved, added = _resolve(selection, catalog_set)
    for dep, dependant in added:
        typer.echo(f"+ {dep} (dependency of {dependant})")

    plans = _plan_install(resolved, base, force=force, skip_existing=skip_existing)

    if dry_run:
        _print_plan(base, plans)
        raise typer.Exit(0)

    prompt_count = sum(1 for _s, _d, action in plans if action == "prompt")
    if prompt_count > 0:
        if not sys.stdin.isatty():
            typer.echo(
                f"Error: {prompt_count} existing file(s) in {base}; pass --force or --skip-existing.",
                err=True,
            )
            raise typer.Exit(1)
        choice: _Action = (
            "overwrite"
            if typer.confirm(f"Overwrite {prompt_count} existing file(s) in {base}?")
            else "skip"
        )
        plans = [(source, dest, choice if action == "prompt" else action) for source, dest, action in plans]

    installed, overwritten, skipped = _write_plans(plans, base)
    typer.echo(f"installed {installed}, overwritten {overwritten}, skipped {skipped} in {base}")


@app.command()
def version() -> None:
    """Print the htmui version and per-component versions."""
    from htmui import __version__ as htmui_version

    typer.echo(f"htmui {htmui_version}")
    for name, ver, framework, fw_ver in _component_versions():
        line = f"  {name} {ver}"
        if len(framework) > 0:
            line += f"  [{framework} {fw_ver}]" if len(fw_ver) > 0 else f"  [{framework}]"
        typer.echo(line)


def _selectable_catalog() -> list[str]:
    """Sorted installable component names, excluding `__init__` and utilities."""
    return sorted(
        p.stem for p in SOURCE_DIR.glob("*.py") if p.stem != INIT_STEM and p.stem not in UTILITIES
    )


def _sibling_imports(path: Path, catalog: set[str]) -> set[str]:
    """Relative-import modules from `path` that are in `catalog`."""
    tree = ast.parse(path.read_text(), filename=str(path))
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.level == 1 and node.module:
            out.add(node.module)
    return out & catalog


def _resolve(selection: list[str], catalog: set[str]) -> tuple[list[str], list[tuple[str, str]]]:
    """
    `selection` plus transitive relative-import dependencies within `catalog`.

    The second item is `(dependency, dependant)` for each name not already in
    `selection`.
    """
    added_log: list[tuple[str, str]] = []
    stack = list(selection)
    seen = set(selection)
    while stack:
        cur = stack.pop()
        for dep in _sibling_imports(SOURCE_DIR / f"{cur}.py", catalog):
            if dep not in seen:
                added_log.append((dep, cur))
                seen.add(dep)
                stack.append(dep)
    return sorted(seen), added_log


def _plan_install(
    resolved: list[str],
    base: Path,
    *,
    force: bool,
    skip_existing: bool,
) -> list[tuple[Path, Path, _Action]]:
    """
    Source, destination, and action for installing `resolved` into `base`.

    Always includes `__init__.py` and the utility modules. An existing
    `__init__.py` is skipped. Other existing files are overwritten if `force`,
    skipped if `skip_existing`, otherwise marked `prompt`.
    """
    plans: list[tuple[Path, Path, _Action]] = []
    for name in [INIT_STEM, *sorted(UTILITIES), *resolved]:
        source = SOURCE_DIR / f"{name}.py"
        dest = base / f"{name}.py"
        if dest.exists() and name == INIT_STEM:
            action: _Action = "skip"
        elif not dest.exists():
            action = "new"
        elif force:
            action = "overwrite"
        elif skip_existing:
            action = "skip"
        else:
            action = "prompt"
        plans.append((source, dest, action))
    return plans


def _action_line(dest: Path, action: _Action) -> str:
    name = dest.name
    if action == "skip" and dest.stem == INIT_STEM:
        return f"  skip      {name}  (existing __init__.py preserved)"
    if action == "new":
        return f"  new       {name}"
    if action == "overwrite":
        return f"  overwrite {name}"
    if action == "skip":
        return f"  skip      {name}"
    return f"  ask       {name}"


def _print_plan(base: Path, plans: list[tuple[Path, Path, _Action]]) -> None:
    """Print `plans` and a count summary for `base`."""
    typer.echo(f"Dry-run plan for {base}:")
    would_install = would_overwrite = would_skip = would_ask = 0
    for _source, dest, action in plans:
        typer.echo(_action_line(dest, action))
        if action == "new":
            would_install += 1
        elif action == "overwrite":
            would_overwrite += 1
        elif action == "prompt":
            would_ask += 1
        else:
            would_skip += 1
    typer.echo(
        f"would install {would_install}, overwrite {would_overwrite}, skip {would_skip}, ask {would_ask}"
    )


def _write_plans(plans: list[tuple[Path, Path, _Action]], base: Path) -> tuple[int, int, int]:
    """Write `plans` under `base`. Returns `(installed, overwritten, skipped)`."""
    base.mkdir(parents=True, exist_ok=True)
    installed = 0
    overwritten = 0
    skipped = 0
    for source, dest, action in plans:
        if action in ("new", "overwrite"):
            shutil.copyfile(source, dest)
            if action == "overwrite":
                overwritten += 1
            else:
                installed += 1
        else:
            skipped += 1
        typer.echo(_action_line(dest, action))
    return installed, overwritten, skipped


def _component_versions() -> list[tuple[str, str, str, str]]:
    """
    `(name, version, framework, framework_version)` for each module with `__version__`.

    Missing framework attributes are empty strings.
    """
    import importlib.util

    names = sorted(p.stem for p in SOURCE_DIR.glob("*.py") if p.stem != INIT_STEM)
    rows: list[tuple[str, str, str, str]] = []
    for name in names:
        path = SOURCE_DIR / f"{name}.py"
        spec = importlib.util.spec_from_file_location(f"htmui.basecoat.{name}", path)
        if spec is None or spec.loader is None:
            continue
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        ver = getattr(mod, "__version__", None)
        if ver is None:
            continue
        framework = getattr(mod, "__framework__", "")
        fw_ver = getattr(mod, "__framework_version__", "")
        rows.append((name, ver, framework, fw_ver))
    return rows


if __name__ == "__main__":
    app()
