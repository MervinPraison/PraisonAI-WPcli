# Rewrite Command

Manage WordPress rewrite rules.

## Quick Start

```bash
# List rewrite rules
praisonaiwp rewrite list

# Flush rewrite rules
praisonaiwp rewrite flush
```

## Subcommands

### list

List rewrite rules.

```bash
praisonaiwp rewrite list [OPTIONS]
```

### flush

Flush rewrite rules.

```bash
praisonaiwp rewrite flush [OPTIONS]
```

### structure

Set permalink structure.

```bash
praisonaiwp rewrite structure STRUCTURE [OPTIONS]
```

## Examples

```bash
# List rules
praisonaiwp rewrite list

# Flush rules
praisonaiwp rewrite flush

# Set structure
praisonaiwp rewrite structure "/%postname%/"
```
