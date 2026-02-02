# Widget Command

Manage WordPress widgets.

## Quick Start

```bash
# List widgets
praisonaiwp widget list
```

## Subcommands

### list

List widgets.

```bash
praisonaiwp widget list [OPTIONS]
```

### add

Add widget.

```bash
praisonaiwp widget add WIDGET [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--title TEXT` | Widget title |
| `--sidebar TEXT` | Sidebar ID |

### update

Update widget.

```bash
praisonaiwp widget update ID [OPTIONS]
```

### delete

Delete widget.

```bash
praisonaiwp widget delete ID [OPTIONS]
```

## Examples

```bash
# List widgets
praisonaiwp widget list

# Add text widget
praisonaiwp widget add text --title "My Widget" --sidebar sidebar-1
```
