# Init Command

Initialize PraisonAIWP configuration.

## Quick Start

```bash
praisonaiwp init
```

## Usage

```bash
praisonaiwp init [OPTIONS]
```

## What It Does

1. Prompts for server hostname (or SSH config alias)
2. Prompts for SSH username
3. Prompts for SSH key path
4. Auto-detects WordPress installation path
5. Auto-detects PHP binary
6. Auto-detects WP-CLI path
7. Creates `~/.praisonaiwp/config.yaml`

## Examples

```bash
# Interactive configuration
praisonaiwp init
```

## Tips

- Use SSH config alias (e.g., `wp-prod`) for simplified connection
- Press Enter for WordPress path to auto-detect
- PHP binary is auto-detected, or specify for Plesk: `/opt/plesk/php/8.3/bin/php`
