# System Command

WordPress system operations.

## Quick Start

```bash
# Flush cache
praisonaiwp system cache-flush

# Get WordPress version
praisonaiwp system version
```

## Subcommands

### cache-flush

Clear WordPress cache.

```bash
praisonaiwp system cache-flush [OPTIONS]
```

### cache-type

Get cache type.

```bash
praisonaiwp system cache-type [OPTIONS]
```

### version

Get WordPress version.

```bash
praisonaiwp system version [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--detailed` | Show detailed version info |

### check-install

Check WordPress installation.

```bash
praisonaiwp system check-install [OPTIONS]
```

## Examples

```bash
# Clear cache
praisonaiwp system cache-flush

# Get cache type
praisonaiwp system cache-type

# Get WordPress version
praisonaiwp system version

# Get detailed version info
praisonaiwp system version --detailed

# Check installation
praisonaiwp system check-install
```
