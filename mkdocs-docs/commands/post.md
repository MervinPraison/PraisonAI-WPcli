# Post Command

Post utilities and management.

## Quick Start

```bash
# Delete a post
praisonaiwp post delete 123

# Check if post exists
praisonaiwp post exists 123
```

## Subcommands

### delete

Delete a post.

```bash
praisonaiwp post delete POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--force` | Force delete (skip trash) |
| `--server TEXT` | Server name from config |

### exists

Check if post exists.

```bash
praisonaiwp post exists POST_ID [OPTIONS]
```

## Examples

```bash
# Delete post (to trash)
praisonaiwp post delete 123

# Force delete (permanent)
praisonaiwp post delete 123 --force

# Check if post exists
praisonaiwp post exists 123
```
