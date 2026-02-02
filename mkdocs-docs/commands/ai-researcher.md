# AI Researcher Command

Research topics and generate comprehensive content with citations.

## Quick Start

```bash
# Research a topic
praisonaiwp ai research topic "Machine Learning"

# Generate content outline
praisonaiwp ai research outline "AI Trends 2025"
```

## Subcommands

### topic

Research a topic comprehensively.

```bash
praisonaiwp ai research topic "TOPIC" [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--depth TEXT` | Research depth (basic, comprehensive, detailed) |
| `--sources INTEGER` | Number of sources to include |
| `--format TEXT` | Output format (markdown, html, plain) |
| `--citations` | Include citations |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### citations

Generate citations for content.

```bash
praisonaiwp ai research citations POST_ID
```

### outline

Create a content outline.

```bash
praisonaiwp ai research outline "TOPIC" [OPTIONS]
```

## Examples

```bash
# Basic research
praisonaiwp ai research topic "Machine Learning"

# Comprehensive research with citations
praisonaiwp ai research topic "AI Ethics" --depth comprehensive --citations

# Create detailed outline
praisonaiwp ai research outline "AI Trends 2025" --depth detailed

# Generate citations for existing post
praisonaiwp ai research citations 123
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
