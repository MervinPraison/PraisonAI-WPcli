# AI Bulk Command

Perform bulk AI operations on multiple posts.

## Quick Start

```bash
# Bulk optimize posts
praisonaiwp ai bulk optimize --category "Technology"

# Bulk translate posts
praisonaiwp ai bulk translate --posts 1,2,3 --to es
```

## Subcommands

### process

Process bulk operations.

```bash
praisonaiwp ai bulk process [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--posts TEXT` | Post IDs or range (1,2,3 or 1-10) |
| `--category TEXT` | Process by category |
| `--status TEXT` | Filter by status |
| `--limit INTEGER` | Limit number of posts |
| `--operation TEXT` | Operation type (optimize, translate, summarize) |
| `--params TEXT` | Operation parameters (JSON) |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### optimize

Bulk optimize posts.

```bash
praisonaiwp ai bulk optimize [OPTIONS]
```

### translate

Bulk translate posts.

```bash
praisonaiwp ai bulk translate [OPTIONS]
```

## Examples

```bash
# Optimize all posts in category
praisonaiwp ai bulk optimize --category "Technology"

# Translate specific posts
praisonaiwp ai bulk translate --posts 1,2,3 --to es,fr

# Bulk summarize draft posts
praisonaiwp ai bulk process --status draft --operation summarize

# Process range of posts
praisonaiwp ai bulk process --posts 1-50 --operation optimize --limit 10
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
