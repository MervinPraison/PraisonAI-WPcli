# AI Moderator Command

AI-powered comment moderation and response generation.

## Quick Start

```bash
# Moderate pending comments
praisonaiwp ai moderate comments

# Auto-approve safe comments
praisonaiwp ai moderate comments --auto-approve
```

## Subcommands

### comments

Moderate WordPress comments.

```bash
praisonaiwp ai moderate comments [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--post-id INTEGER` | Moderate comments for specific post |
| `--auto-approve` | Auto-approve safe comments |
| `--spam-detection` | Enable spam detection |
| `--sentiment-analysis` | Analyze comment sentiment |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### analyze

Analyze comment patterns.

```bash
praisonaiwp ai moderate analyze [OPTIONS]
```

### respond

Generate AI responses to comments.

```bash
praisonaiwp ai moderate respond [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--generate-responses` | Generate AI responses |
| `--tone TEXT` | Response tone (friendly, professional) |

## Examples

```bash
# Moderate all pending comments
praisonaiwp ai moderate comments

# Moderate comments on specific post
praisonaiwp ai moderate comments --post-id 123

# Full moderation with spam detection
praisonaiwp ai moderate comments --spam-detection --sentiment-analysis

# Auto-approve and respond
praisonaiwp ai moderate comments --auto-approve --generate-responses
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
