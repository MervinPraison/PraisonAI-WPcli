# Plugin Command

Manage WordPress plugins.

## Quick Start

```bash
# List all plugins
praisonaiwp plugin list

# Activate a plugin
praisonaiwp plugin activate akismet
```

## Subcommands

### list

List installed plugins.

```bash
praisonaiwp plugin list [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--status [all\|active\|inactive]` | Filter by status (default: all) |
| `--server TEXT` | Server name from config |

### update

Update plugin(s).

```bash
praisonaiwp plugin update [PLUGIN] [OPTIONS]
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `PLUGIN` | Plugin slug or "all" (default: all) |

### activate

Activate a plugin.

```bash
praisonaiwp plugin activate PLUGIN [OPTIONS]
```

### deactivate

Deactivate a plugin.

```bash
praisonaiwp plugin deactivate PLUGIN [OPTIONS]
```

### install

Install a plugin.

```bash
praisonaiwp plugin install PLUGIN [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--version TEXT` | Specific version to install |
| `--force` | Force installation |

### delete

Delete a plugin.

```bash
praisonaiwp plugin delete PLUGIN [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--no-deactivate` | Skip deactivation before delete |

## Examples

```bash
# List all plugins
praisonaiwp plugin list

# List active plugins only
praisonaiwp plugin list --status active

# Update all plugins
praisonaiwp plugin update

# Update specific plugin
praisonaiwp plugin update akismet

# Install plugin
praisonaiwp plugin install jetpack

# Activate/deactivate plugins
praisonaiwp plugin activate akismet
praisonaiwp plugin deactivate hello-dolly
```
