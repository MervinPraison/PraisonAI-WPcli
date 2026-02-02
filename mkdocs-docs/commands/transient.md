# Transient Command

Manage WordPress transients.

## Quick Start

```bash
# Get transient
praisonaiwp transient get cache_key

# Set transient
praisonaiwp transient set cache_key "data" --expire 3600
```

## Subcommands

### get

Get transient value.

```bash
praisonaiwp transient get KEY [OPTIONS]
```

### set

Set transient with expiration.

```bash
praisonaiwp transient set KEY VALUE [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--expire INTEGER` | Expiration in seconds (default: 3600) |
| `--server TEXT` | Server name from config |

### delete

Delete transient.

```bash
praisonaiwp transient delete KEY [OPTIONS]
```

## Examples

```bash
# Get transient
praisonaiwp transient get cache_key

# Set transient (1 hour default)
praisonaiwp transient set cache_key "cached_data"

# Set with custom expiration (2 hours)
praisonaiwp transient set cache_key "data" --expire 7200

# Delete transient
praisonaiwp transient delete cache_key
```
