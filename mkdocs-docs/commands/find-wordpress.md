# Find WordPress Command

Find WordPress installations on server.

## Quick Start

```bash
# Find installations
praisonaiwp find-wordpress
```

## Usage

```bash
praisonaiwp find-wordpress [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--interactive` | Interactive selection from multiple installations |
| `--update-config` | Auto-update config with selected installation |
| `--server TEXT` | Server name from config |

## Examples

```bash
# Find all installations
praisonaiwp find-wordpress

# Interactive selection
praisonaiwp find-wordpress --interactive

# Find and update config
praisonaiwp find-wordpress --update-config
```
