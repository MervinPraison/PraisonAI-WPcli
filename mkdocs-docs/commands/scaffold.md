# Scaffold Command

Generate WordPress code structures.

## Quick Start

```bash
# Generate post type
praisonaiwp scaffold post-type book
```

## Subcommands

### post-type

Generate custom post type.

```bash
praisonaiwp scaffold post-type NAME [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--label TEXT` | Post type label |
| `--public` | Public post type |
| `--supports TEXT` | Supported features |

### taxonomy

Generate taxonomy.

```bash
praisonaiwp scaffold taxonomy NAME [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--label TEXT` | Taxonomy label |
| `--hierarchical` | Hierarchical taxonomy |
| `--post_types TEXT` | Associated post types |

### plugin

Generate plugin.

```bash
praisonaiwp scaffold plugin NAME [OPTIONS]
```

### theme

Generate theme.

```bash
praisonaiwp scaffold theme NAME [OPTIONS]
```

### child-theme

Generate child theme.

```bash
praisonaiwp scaffold child-theme PARENT NAME [OPTIONS]
```

## Examples

```bash
# Generate post type
praisonaiwp scaffold post-type book --label "Books" --public

# Generate taxonomy
praisonaiwp scaffold taxonomy genre --label "Genres" --hierarchical

# Generate plugin
praisonaiwp scaffold plugin my-plugin --plugin_name "My Plugin"

# Generate child theme
praisonaiwp scaffold child-theme twentytwentyfour my-child
```
