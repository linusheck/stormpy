#!/usr/bin/env python3
"""Generate a Markdown inventory of stormpy's public module namespaces.

For this inventory, a public name is any name in a selected module's namespace
that does not begin with an underscore. This intentionally records accidental
exports (for example, imported helper names) as well as deliberate API.

The script inventories module-level names only. It does not enumerate methods,
properties, or other members of exported classes.

Run from a stormpy checkout with stormpy available in the active environment:

    python resources/scripts/public_api_inventory.py \
        --output stormpy-public-api.md

For Google Sheets review, generate a ``.csv`` file, edit the Decision,
Target / group, and Notes columns, download it as CSV, and pass that file back
with ``--review-csv`` when generating a fresh Markdown inventory.

Use ``--recommend`` to prefill blank decisions. Existing decisions loaded with
``--review-csv`` always take precedence over generated recommendations.

Use --module to replace the default module list, or --add-module to extend it.
Optional modules that cannot be imported are recorded instead of aborting the
inventory. Unexpected import failures make the command fail.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import enum
import importlib
import importlib.machinery
import inspect
import io
import pathlib
import platform
import sys
import types
from dataclasses import dataclass
from typing import Any, Iterable, Sequence

DEFAULT_MODULES = (
    "stormpy",
    "stormpy.storage",
    "stormpy.logic",
    "stormpy.utility",
    "stormpy.utility.multiobjective_plotting",
    "stormpy.simulator",
    "stormpy.dft",
    "stormpy.dft.modules",
    "stormpy.dft.simulator",
    "stormpy.gspn",
    "stormpy.pars",
    "stormpy.pomdp",
    "stormpy.info",
    "stormpy.exceptions",
    "stormpy.examples",
    "stormpy.examples.files",
    "stormpy.pycarl",
    "stormpy.pycarl.formula",
    "stormpy.pycarl.cln",
    "stormpy.pycarl.cln.formula",
    "stormpy.pycarl.gmp",
    "stormpy.pycarl.gmp.formula",
    "stormpy.pycarl.convert",
    "stormpy.pycarl.parse",
)

OPTIONAL_MODULE_PREFIXES = {
    "stormpy.utility.multiobjective_plotting": "plot dependencies",
    "stormpy.dft": "DFT",
    "stormpy.gspn": "GSPN",
    "stormpy.pars": "PARS",
    "stormpy.pomdp": "POMDP",
}

REVIEW_DECISIONS = ("KEEP", "ALIAS", "CONSOLIDATE", "DEPRECATE", "PRIVATE")

GENERIC_TYPE_TOKENS = (
    "RationalInterval",
    "ExactInterval",
    "Parametric",
    "Interval",
    "Exact",
    "Double",
    "RatFunc",
    "_ratinterval",
    "_parametric",
    "_interval",
    "_exact",
    "_double",
    "_ratfunc",
)

CSV_FIELDS = (
    "Module",
    "Public import path",
    "Kind",
    "Defined by",
    "Layer",
    "Decision",
    "Target / group",
    "Notes",
)


@dataclass(frozen=True)
class Entry:
    public_path: str
    kind: str
    defined_by: str
    layer: str


@dataclass(frozen=True)
class ImportFailure:
    module: str
    reason: str
    expected: bool


@dataclass(frozen=True)
class Review:
    decision: str = ""
    target: str = ""
    notes: str = ""


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=pathlib.Path, help="write the inventory to this file instead of stdout")
    parser.add_argument(
        "--format",
        choices=("markdown", "csv"),
        help="output format; inferred from an .md or .csv output suffix when omitted",
    )
    parser.add_argument(
        "--review-csv",
        type=pathlib.Path,
        help="carry review fields forward from a previously generated CSV",
    )
    parser.add_argument(
        "--recommend",
        action="store_true",
        help="prefill blank review fields using the documented conservative recommendations",
    )
    parser.add_argument(
        "--module",
        action="append",
        dest="modules",
        metavar="MODULE",
        help="module to inventory; may be repeated and replaces the default list",
    )
    parser.add_argument(
        "--add-module",
        action="append",
        default=[],
        metavar="MODULE",
        help="module to add to the default or --module list; may be repeated",
    )
    parser.add_argument("--no-timestamp", action="store_true", help="omit the generation timestamp for stable diffs")
    return parser.parse_args(argv)


def optional_component(module_name: str) -> str | None:
    for prefix, component in OPTIONAL_MODULE_PREFIXES.items():
        if module_name == prefix or module_name.startswith(prefix + "."):
            return component
    return None


def import_inventories(module_names: Iterable[str]) -> tuple[dict[str, list[Entry]], list[ImportFailure]]:
    inventories = {}
    failures = []
    for module_name in module_names:
        try:
            module = importlib.import_module(module_name)
        except ImportError as error:
            failures.append(ImportFailure(module_name, str(error), optional_component(module_name) is not None))
        else:
            # Snapshot immediately: importing later child modules mutates their
            # parent package by attaching the child as an attribute.
            inventories[module_name] = inventory([module])[module_name]
    return inventories, failures


def object_kind(value: Any) -> str:
    if inspect.ismodule(value):
        return "module"
    if inspect.isclass(value):
        try:
            if issubclass(value, enum.Enum):
                return "enum"
        except TypeError:
            pass
        return "class"
    if inspect.isroutine(value):
        return "function"
    return "constant"


def defining_module(value: Any) -> str:
    if inspect.ismodule(value):
        return value.__name__
    origin = getattr(value, "__module__", None)
    if origin:
        return origin
    return type(value).__module__


def implementation_layer(origin: str) -> str:
    if not origin.startswith("stormpy"):
        return "external"
    try:
        origin_module = importlib.import_module(origin)
    except ImportError:
        return "unknown"
    module_file = getattr(origin_module, "__file__", "") or ""
    if any(module_file.endswith(suffix) for suffix in importlib.machinery.EXTENSION_SUFFIXES):
        return "C++ binding"
    return "Python"


def inventory(modules: Iterable[types.ModuleType]) -> dict[str, list[Entry]]:
    result = {}
    for module in modules:
        entries = []
        for name, value in vars(module).items():
            if name.startswith("_"):
                continue
            origin = defining_module(value)
            entries.append(Entry(f"{module.__name__}.{name}", object_kind(value), origin, implementation_layer(origin)))
        result[module.__name__] = sorted(entries, key=lambda entry: entry.public_path.casefold())
    return result


def load_reviews(path: pathlib.Path) -> dict[str, Review]:
    reviews = {}
    with path.open(newline="", encoding="utf-8-sig") as review_file:
        reader = csv.DictReader(review_file)
        missing_fields = set(CSV_FIELDS) - set(reader.fieldnames or ())
        if missing_fields:
            raise ValueError(f"review CSV is missing column(s): {', '.join(sorted(missing_fields))}")
        for line_number, row in enumerate(reader, start=2):
            public_path = (row["Public import path"] or "").strip()
            if not public_path:
                raise ValueError(f"review CSV line {line_number} has no public import path")
            if public_path in reviews:
                raise ValueError(f"review CSV contains duplicate public import path: {public_path}")
            decision = (row["Decision"] or "").strip().upper()
            if decision and decision not in REVIEW_DECISIONS:
                allowed = ", ".join(REVIEW_DECISIONS)
                raise ValueError(f"invalid decision {decision!r} for {public_path}; expected one of: {allowed}")
            reviews[public_path] = Review(
                decision=decision,
                target=(row["Target / group"] or "").strip(),
                notes=(row["Notes"] or "").strip(),
            )
    return reviews


def generic_name(name: str) -> str:
    generic = name
    for token in GENERIC_TYPE_TOKENS:
        generic = generic.replace(token, "")
    return generic.strip("_")


def generic_families(inventories: dict[str, list[Entry]]) -> dict[str, str]:
    """Map clear C++ value-type specializations to a proposed generic path."""
    families: dict[tuple[str, str], list[Entry]] = {}
    for module_name, entries in inventories.items():
        for entry in entries:
            if entry.layer != "C++ binding" or entry.kind not in {"class", "function"}:
                continue
            name = entry.public_path.rsplit(".", 1)[1]
            base = generic_name(name)
            if base and base != name:
                families.setdefault((module_name, base), []).append(entry)

    result = {}
    for (module_name, base), entries in families.items():
        target = f"{module_name}.{base}"
        for entry in entries:
            if entry.public_path != target:
                result[entry.public_path] = target
    return result


def recommended_reviews(inventories: dict[str, list[Entry]], existing: dict[str, Review]) -> dict[str, Review]:
    """Fill blank decisions using conservative, reproducible API heuristics."""
    recommendations = dict(existing)
    all_entries = [entry for entries in inventories.values() for entry in entries]
    all_paths = {entry.public_path for entry in all_entries}
    generic_targets = generic_families(inventories)
    deprecated_names = {"StateValuation", "StateValuationsBuilder", "StateValuationTransformer"}
    helper_modules = {"stormpy", "os", "np", "storm_error", "cln_converter", "gmp_converter"}

    for entry in all_entries:
        if recommendations.get(entry.public_path, Review()).decision:
            continue
        module_name, name = entry.public_path.rsplit(".", 1)

        domain_target = None
        if module_name == "stormpy":
            for domain in ("stormpy.storage", "stormpy.logic"):
                candidate = f"{domain}.{name}"
                if candidate in all_paths:
                    domain_target = candidate
                    break

        if domain_target:
            review = Review(
                "ALIAS",
                domain_target,
                "Prefer the domain-oriented import; retain this flattened path during migration.",
            )
        elif name in deprecated_names:
            review = Review("DEPRECATE", notes="Already deprecated or retained as a legacy compatibility shim.")
        elif entry.public_path in generic_targets:
            review = Review(
                "CONSOLIDATE",
                generic_targets[entry.public_path],
                "Value-type specialization; expose one Python dispatcher or facade.",
            )
        elif entry.kind == "module" and (name in helper_modules or entry.public_path in {"stormpy.cln", "stormpy.gmp"}):
            target = "stormpy.pycarl." + name if entry.public_path in {"stormpy.cln", "stormpy.gmp"} else ""
            review = Review("PRIVATE", target, "Imported implementation/helper module; do not expose as API.")
        elif entry.layer == "external" and entry.kind != "constant":
            review = Review("PRIVATE", notes="Accidentally imported external helper; not stormpy API.")
        else:
            review = Review("KEEP")
        recommendations[entry.public_path] = review
    return recommendations


def escape_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def build_configuration() -> list[tuple[str, Any]]:
    import stormpy

    configuration: list[tuple[str, Any]] = [
        ("stormpy version", getattr(stormpy, "__version__", "unknown")),
        ("Python version", platform.python_version()),
    ]
    try:
        from stormpy.info import _config

        configuration.append(("Storm version", getattr(_config, "STORM_VERSION", "unknown")))
        for name in sorted(name for name in vars(_config) if name.startswith("STORM_WITH_")):
            configuration.append((name, getattr(_config, name)))
    except ImportError as error:
        configuration.append(("Storm configuration", f"unavailable: {error}"))
    return configuration


def render_markdown(inventories: dict[str, list[Entry]], failures: Sequence[ImportFailure], reviews: dict[str, Review], include_timestamp: bool) -> str:
    total = sum(len(entries) for entries in inventories.values())
    lines = [
        "# stormpy public namespace inventory",
        "",
        (
            "This is a mechanical inventory of every module-level name that does not begin with `_` "
            "in the modules listed below. Inclusion does not mean that a name was intentionally public, "
            "documented, or covered by a compatibility guarantee. Class members are not included."
        ),
        "",
        f"**Total entries:** {total}",
    ]
    if include_timestamp:
        timestamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
        lines.append(f"**Generated:** {timestamp}")
    lines.extend(["", "## Build configuration", "", "| Setting | Value |", "|---|---|"])
    for name, value in build_configuration():
        lines.append(f"| {escape_cell(name)} | {escape_cell(value)} |")

    lines.extend(
        [
            "",
            "## Review labels",
            "",
            "- **KEEP**: retain the public path as-is.",
            "- **ALIAS**: retain it temporarily as an alias to the API named in Target / group.",
            "- **CONSOLIDATE**: combine related specializations under the generic API named in Target / group.",
            "- **DEPRECATE**: begin a deprecation cycle without a direct replacement.",
            "- **PRIVATE**: remove it from the supported public API.",
            "",
            "Decision, Target / group, and Notes are the team-editable fields.",
        ]
    )

    if failures:
        lines.extend(["", "## Modules not inventoried", "", "| Module | Expected optional failure | Reason |", "|---|---|---|"])
        for failure in failures:
            lines.append(f"| `{failure.module}` | {'yes' if failure.expected else 'no'} | {escape_cell(failure.reason)} |")

    for module_name, entries in inventories.items():
        component = optional_component(module_name)
        suffix = f" (optional: {component})" if component else ""
        lines.extend(
            [
                "",
                f"## `{module_name}`{suffix}",
                "",
                f"{len(entries)} entries.",
                "",
                "| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |",
                "|---|---|---|---|---|---|---|",
            ]
        )
        for entry in entries:
            review = reviews.get(entry.public_path, Review())
            lines.append(
                f"| {escape_cell(review.decision)} | `{entry.public_path}` | {entry.kind} | `{entry.defined_by}` | "
                f"{entry.layer} | {escape_cell(review.target)} | {escape_cell(review.notes)} |"
            )

    current_paths = {entry.public_path for entries in inventories.values() for entry in entries}
    stale_paths = sorted(set(reviews) - current_paths)
    if stale_paths:
        lines.extend(
            [
                "",
                "## Reviewed paths no longer present",
                "",
                "These paths existed in the review CSV but not in the current runtime inventory:",
                "",
            ]
        )
        lines.extend(f"- `{path}`" for path in stale_paths)
    return "\n".join(lines) + "\n"


def render_csv(inventories: dict[str, list[Entry]], reviews: dict[str, Review]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for module_name, entries in inventories.items():
        for entry in entries:
            review = reviews.get(entry.public_path, Review())
            writer.writerow(
                {
                    "Module": module_name,
                    "Public import path": entry.public_path,
                    "Kind": entry.kind,
                    "Defined by": entry.defined_by,
                    "Layer": entry.layer,
                    "Decision": review.decision,
                    "Target / group": review.target,
                    "Notes": review.notes,
                }
            )
    return output.getvalue()


def output_format(requested_format: str | None, output: pathlib.Path | None) -> str:
    if requested_format:
        return requested_format
    if output and output.suffix.lower() == ".csv":
        return "csv"
    return "markdown"


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    requested_modules = args.modules if args.modules is not None else list(DEFAULT_MODULES)
    module_names = list(dict.fromkeys([*requested_modules, *args.add_module]))
    inventories, failures = import_inventories(module_names)
    try:
        reviews = load_reviews(args.review_csv) if args.review_csv else {}
    except (OSError, ValueError) as error:
        print(f"Failed to read review CSV: {error}", file=sys.stderr)
        return 2
    if args.recommend:
        reviews = recommended_reviews(inventories, reviews)

    selected_format = output_format(args.format, args.output)
    if selected_format == "csv":
        rendered_output = render_csv(inventories, reviews)
    else:
        rendered_output = render_markdown(inventories, failures, reviews, include_timestamp=not args.no_timestamp)

    if args.output:
        args.output.write_text(rendered_output, encoding="utf-8")
    else:
        sys.stdout.write(rendered_output)

    unexpected_failures = [failure for failure in failures if not failure.expected]
    if unexpected_failures:
        print(
            "Failed to import required module(s): " + ", ".join(failure.module for failure in unexpected_failures),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
