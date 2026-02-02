# Network Command

WordPress multisite network management.

## Quick Start

```bash
# List network sites
praisonaiwp network site-list
```

## Subcommands

### site-list

List network sites.

```bash
praisonaiwp network site-list [OPTIONS]
```

### site-create

Create a network site.

```bash
praisonaiwp network site-create SLUG [OPTIONS]
```

### site-delete

Delete a network site.

```bash
praisonaiwp network site-delete SITE_ID [OPTIONS]
```

## Examples

```bash
# List sites
praisonaiwp network site-list

# Create site
praisonaiwp network site-create blog

# Delete site
praisonaiwp network site-delete 2
```
