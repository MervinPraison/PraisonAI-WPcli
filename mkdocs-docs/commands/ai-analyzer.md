# AI Analyzer Command

Analyze content performance and provide AI-driven insights.

## Quick Start

```bash
# Analyze post performance
praisonaiwp ai analyze performance 123

# Predict performance
praisonaiwp ai analyze predict 123
```

## Subcommands

### performance

Analyze content performance.

```bash
praisonaiwp ai analyze performance POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--metrics TEXT` | Metrics to analyze (views, engagement, seo) |
| `--timeframe TEXT` | Analysis timeframe |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### predict

Predict content performance.

```bash
praisonaiwp ai analyze predict POST_ID [OPTIONS]
```

### compare

Compare performance across posts.

```bash
praisonaiwp ai analyze compare [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--days INTEGER` | Comparison period |

## Examples

```bash
# Basic performance analysis
praisonaiwp ai analyze performance 123

# Analyze specific metrics
praisonaiwp ai analyze performance 123 --metrics views,engagement

# Predict post performance
praisonaiwp ai analyze predict 123

# Compare performance over 30 days
praisonaiwp ai analyze compare --days 30
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
