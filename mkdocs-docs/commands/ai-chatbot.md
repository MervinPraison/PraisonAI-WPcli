# AI Chatbot Command

Deploy AI-powered chatbot to WordPress site.

## Quick Start

```bash
# Deploy chatbot
praisonaiwp ai chatbot deploy

# Get chatbot analytics
praisonaiwp ai chatbot analytics --days 30
```

## Subcommands

### deploy

Deploy chatbot to your WordPress site.

```bash
praisonaiwp ai chatbot deploy [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--widget-style TEXT` | Widget style (modern, classic, minimal) |
| `--position TEXT` | Widget position (bottom-right, bottom-left) |
| `--color TEXT` | Widget color |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### train

Train chatbot on your content.

```bash
praisonaiwp ai chatbot train [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--content-type TEXT` | Training content type |
| `--model TEXT` | AI model to use |

### analytics

Get chatbot analytics.

```bash
praisonaiwp ai chatbot analytics [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--days INTEGER` | Analytics period |

## Examples

```bash
# Deploy modern chatbot
praisonaiwp ai chatbot deploy --widget-style modern

# Deploy with custom positioning
praisonaiwp ai chatbot deploy --position bottom-left --color "#3b82f6"

# Train on posts
praisonaiwp ai chatbot train --content-type posts

# Get 30-day analytics
praisonaiwp ai chatbot analytics --days 30
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
