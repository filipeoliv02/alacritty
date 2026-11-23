#!/usr/bin/env python3
"""Validate the repository's Alacritty TOML configuration."""

from pathlib import Path
import sys

try:
    import tomllib
except ModuleNotFoundError:
    try:
        import tomli as tomllib
    except ModuleNotFoundError:
        print("error: Python 3.11+ or the 'tomli' package is required", file=sys.stderr)
        raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "alacritty.toml"


def main() -> int:
    try:
        with CONFIG.open("rb") as fh:
            data = tomllib.load(fh)
    except FileNotFoundError:
        print(f"error: missing {CONFIG}", file=sys.stderr)
        return 1
    except tomllib.TOMLDecodeError as exc:
        print(f"error: invalid TOML in {CONFIG}: {exc}", file=sys.stderr)
        return 1

    required = (("font", "size"), ("window", "padding"), ("scrolling", "history"),
                ("selection", "save_to_clipboard"), ("colors", "primary"),
                ("colors", "normal"), ("colors", "bright"))
    missing = [".".join(parts) for parts in required
               if not isinstance(data.get(parts[0]), dict)
               or parts[1] not in data[parts[0]]]
    if missing:
        print("error: missing required configuration: " + ", ".join(missing), file=sys.stderr)
        return 1

    print(f"validated {CONFIG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
