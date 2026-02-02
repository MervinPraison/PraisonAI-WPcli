# Menu Command

Manage WordPress navigation menus.

## Quick Start

```bash
# List menus
praisonaiwp menu list

# Create a menu
praisonaiwp menu create "Main Menu"
```

## Subcommands

### list

List all menus.

```bash
praisonaiwp menu list [OPTIONS]
```

### create

Create a new menu.

```bash
praisonaiwp menu create NAME [OPTIONS]
```

### delete

Delete a menu.

```bash
praisonaiwp menu delete MENU_ID
```

### add-item

Add an item to a menu.

```bash
praisonaiwp menu add-item MENU_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--title TEXT` | Menu item title |
| `--url TEXT` | Menu item URL |
| `--parent INTEGER` | Parent menu item ID |
| `--order INTEGER` | Menu item order |

## Examples

```bash
# List all menus
praisonaiwp menu list

# Create menu
praisonaiwp menu create "Main Menu"

# Delete menu
praisonaiwp menu delete 123

# Add menu item
praisonaiwp menu add-item 123 --title "Home" --url "https://example.com"

# Add nested menu item
praisonaiwp menu add-item 123 --title "About" --url "https://example.com/about" --parent 456 --order 2
```
