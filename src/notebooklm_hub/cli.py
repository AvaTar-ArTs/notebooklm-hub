"""NotebookLM Hub command line interface."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .release import build_release


def doctor(root: Path) -> dict[str, bool]:
    return {
        "research": (root / "research").exists(),
        "provenance": (root / "provenance").exists(),
        "runtime": (root / "src" / "notebooklm_hub").exists(),
        "tests": (root / "tests").exists(),
        "publisher": (root / "packages" / "publisher").exists(),
        "skills": (root / "packages" / "skills").exists(),
        "workflow": (root / "docs" / "HUB_WORKFLOW.md").exists(),
        "checkpoints": (root / "checkpoints").exists(),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="notebooklm-hub")
    sub = parser.add_subparsers(dest="command", required=True)

    doctor_parser = sub.add_parser("doctor", help="audit Hub repository structure")
    doctor_parser.add_argument("--root", default=".")
    doctor_parser.add_argument("--json", action="store_true")

    release_parser = sub.add_parser("release", help="build full and component ZIP releases")
    release_parser.add_argument("--root", default=".")
    release_parser.add_argument("--out", default="dist")
    release_parser.add_argument("--version", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "doctor":
        result = doctor(Path(args.root).resolve())
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            for name, present in result.items():
                print(f"{'OK' if present else 'MISSING':7} {name}")
        return 0
    if args.command == "release":
        manifest = build_release(args.root, args.out, version=args.version)
        print(json.dumps(manifest, indent=2, sort_keys=True))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
