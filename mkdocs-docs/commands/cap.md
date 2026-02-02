# Cap Command

Role capability management.

## Quick Start

```bash
# Add capability to role
praisonaiwp cap add editor edit_others_posts
```

## Usage

```bash
praisonaiwp cap [SUBCOMMAND] ROLE CAPABILITY [OPTIONS]
```

**Subcommands:**

| Subcommand | Description |
|------------|-------------|
| `add` | Add capability to role |
| `remove` | Remove capability from role |
| `list` | List role capabilities |

## Examples

```bash
# Add capability
praisonaiwp cap add editor manage_options

# Remove capability
praisonaiwp cap remove author publish_posts

# List capabilities
praisonaiwp cap list administrator
```
