# Role Command

Manage WordPress user roles.

## Quick Start

```bash
# List roles
praisonaiwp role list
```

## Subcommands

### list

List all roles.

```bash
praisonaiwp role list [OPTIONS]
```

### get

Get role details.

```bash
praisonaiwp role get ROLE [OPTIONS]
```

### create

Create a new role.

```bash
praisonaiwp role create ROLE "DISPLAY_NAME" [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--capabilities TEXT` | Comma-separated capabilities |

### delete

Delete a role.

```bash
praisonaiwp role delete ROLE [OPTIONS]
```

## Examples

```bash
# List roles
praisonaiwp role list

# Get role info
praisonaiwp role get editor

# Create role
praisonaiwp role create moderator "Moderator" --capabilities "edit_posts,moderate_comments"

# Delete role
praisonaiwp role delete custom_role
```
