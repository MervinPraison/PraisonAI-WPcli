# Config Command

Manage PraisonAIWP and WordPress configuration.

## Quick Start

```bash
# Get config value
praisonaiwp config get DB_NAME

# List config
praisonaiwp config list
```

## Subcommands

### get

Get configuration value.

```bash
praisonaiwp config get KEY [OPTIONS]
```

### set

Set configuration value.

```bash
praisonaiwp config set KEY VALUE [OPTIONS]
```

### list

List all configuration.

```bash
praisonaiwp config list [OPTIONS]
```

### path

Show configuration file path.

```bash
praisonaiwp config path [OPTIONS]
```

## Examples

```bash
# Get database name
praisonaiwp config get DB_NAME

# Set site URL
praisonaiwp config set SITE_URL "https://example.com"

# List all config
praisonaiwp config list

# Show config path
praisonaiwp config path
```
