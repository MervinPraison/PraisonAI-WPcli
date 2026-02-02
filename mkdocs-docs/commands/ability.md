# Ability Command

Manage user capabilities and permissions.

## Quick Start

```bash
# List user capabilities
praisonaiwp ability list USER_ID
```

## Usage

```bash
praisonaiwp ability list USER_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--server TEXT` | Server name from config |

## Examples

```bash
# List capabilities for user
praisonaiwp ability list 1

# List on specific server
praisonaiwp ability list 1 --server production
```
