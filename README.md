# Alacritty Configuration

A personal Alacritty configuration with a custom palette and font settings.

## Compatibility

- `alacritty.toml` uses the TOML format supported by current Alacritty releases.
- The previous `alacritty.yml` file was migrated to TOML and removed.
- Install SauceCodePro Nerd Font; Alacritty will still start with the configured family unavailable, but it will fall back to another installed font.

## Installation

1. Install Alacritty and SauceCodePro Nerd Font.
2. Place `alacritty.toml` in the platform configuration directory:
   - Linux/BSD: `~/.config/alacritty/alacritty.toml`
   - macOS: `~/.config/alacritty/alacritty.toml`
   - Windows: `%APPDATA%\alacritty\alacritty.toml`
3. Restart Alacritty or rely on `live_config_reload = true` to apply changes.

You can also start Alacritty with this file explicitly:

```sh
alacritty --config-file ./alacritty.toml
```

## Validation

Run the included parser check:

```sh
python3 scripts/validate_toml.py
```

The script uses Python 3.11+ (`tomllib`); on older Python 3 versions, install `tomli` and run `python3 scripts/validate_toml.py`.

## Settings

The configuration preserves the previous palette, `SauceCodePro Nerd Font` family, size 10, 2 px window padding, 10,000-line scrollback, scroll multiplier 10, clipboard saving, semantic escape characters, glyph offsets, and live reload behavior.
