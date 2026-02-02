# DB Command

Database operations.

## Quick Start

```bash
# Execute query
praisonaiwp db query "SELECT COUNT(*) FROM wp_posts"
```

## Subcommands

### query

Execute database queries.

```bash
praisonaiwp db query "SQL_QUERY" [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--server TEXT` | Server name from config |

## Examples

```bash
# Simple query
praisonaiwp db query "SELECT COUNT(*) FROM wp_posts"

# Query with conditions
praisonaiwp db query "SELECT * FROM wp_posts WHERE post_status = 'publish' LIMIT 5"

# Show tables
praisonaiwp db query "SHOW TABLES"

# Query on specific server
praisonaiwp db query "SHOW TABLES" --server production
```

## Security Note

!!! warning "SQL Injection"
    Be careful when executing raw SQL queries. Always sanitize user inputs and avoid exposing database credentials.
