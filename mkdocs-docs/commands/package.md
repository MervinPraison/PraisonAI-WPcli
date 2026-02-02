# Package Command

WP-CLI package management.

## Quick Start

```bash
# List packages
praisonaiwp package list
```

## Usage

```bash
praisonaiwp package [SUBCOMMAND] [OPTIONS]
```

**Subcommands:**

| Subcommand | Description |
|------------|-------------|
| `list` | List installed packages |
| `install` | Install a package |
| `uninstall` | Uninstall a package |

## Examples

```bash
# List packages
praisonaiwp package list

# Install package
praisonaiwp package install wp-cli/doctor-command
```
