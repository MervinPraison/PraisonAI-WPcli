# Comment Command

Manage WordPress comments.

## Quick Start

```bash
# List comments
praisonaiwp comment list

# Approve a comment
praisonaiwp comment approve 456
```

## Subcommands

### list

List comments with filters.

```bash
praisonaiwp comment list [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--post-id INTEGER` | Filter by post ID |
| `--status TEXT` | Filter by status (approve, pending, spam, trash) |
| `--server TEXT` | Server name from config |

### get

Get comment details.

```bash
praisonaiwp comment get COMMENT_ID
```

### create

Create a new comment.

```bash
praisonaiwp comment create POST_ID "CONTENT" [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--author TEXT` | Comment author name |
| `--email TEXT` | Author email |

### update

Update an existing comment.

```bash
praisonaiwp comment update COMMENT_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--content TEXT` | New comment content |

### delete

Delete a comment.

```bash
praisonaiwp comment delete COMMENT_ID
```

### approve

Approve a comment.

```bash
praisonaiwp comment approve COMMENT_ID
```

### unapprove

Unapprove a comment.

```bash
praisonaiwp comment unapprove COMMENT_ID
```

## Examples

```bash
# List all comments
praisonaiwp comment list

# List comments for specific post
praisonaiwp comment list --post-id 123

# List pending comments
praisonaiwp comment list --status pending

# Get comment details
praisonaiwp comment get 456

# Create comment
praisonaiwp comment create 123 "Great post!" --author "John"

# Approve/unapprove comments
praisonaiwp comment approve 456
praisonaiwp comment unapprove 456

# Delete comment
praisonaiwp comment delete 456
```
