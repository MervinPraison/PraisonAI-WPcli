# AI Curator Command

Curate and suggest related content automatically.

## Quick Start

```bash
# Find related content
praisonaiwp ai curate related 123

# Get content suggestions
praisonaiwp ai curate suggest --category "Technology"
```

## Subcommands

### related

Find content related to a specific post.

```bash
praisonaiwp ai curate related POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--count INTEGER` | Number of suggestions (default: 5) |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### suggest

Suggest new content ideas.

```bash
praisonaiwp ai curate suggest [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--category TEXT` | Filter by category |
| `--count INTEGER` | Number of suggestions |

### trending

Get trending topics.

```bash
praisonaiwp ai curate trending [OPTIONS]
```

## Examples

```bash
# Find 5 related posts
praisonaiwp ai curate related 123 --count 5

# Suggest content for category
praisonaiwp ai curate suggest --category "AI" --count 10

# Get trending topics
praisonaiwp ai curate trending
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
