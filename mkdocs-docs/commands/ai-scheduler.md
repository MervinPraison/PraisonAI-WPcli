# AI Scheduler Command

Intelligent content scheduling and analytics for WordPress.

## Quick Start

```bash
# Analyze scheduling patterns
praisonaiwp ai schedule analyze --days 30

# Get optimal posting times
praisonaiwp ai schedule suggest
```

## Subcommands

### analyze

Analyze content scheduling patterns.

```bash
praisonaiwp ai schedule analyze [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--days INTEGER` | Analysis period in days |
| `--category TEXT` | Filter by category |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### suggest

Suggest optimal posting times.

```bash
praisonaiwp ai schedule suggest [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--timezone TEXT` | Timezone for scheduling |
| `--category TEXT` | Filter by category |

### calendar

Generate a content calendar.

```bash
praisonaiwp ai schedule calendar [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--frequency TEXT` | Posting frequency (daily, weekly, monthly) |
| `--days INTEGER` | Calendar period |

## Examples

```bash
# Analyze last 30 days
praisonaiwp ai schedule analyze --days 30

# Suggest times for specific category
praisonaiwp ai schedule suggest --category "Technology"

# Generate weekly content calendar
praisonaiwp ai schedule calendar --frequency weekly --days 14
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
