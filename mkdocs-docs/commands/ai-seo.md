# AI SEO Command

Comprehensive SEO analysis and optimization.

## Quick Start

```bash
# Perform SEO audit
praisonaiwp ai seo audit 123

# Analyze keywords
praisonaiwp ai seo keywords 123
```

## Subcommands

### audit

Perform SEO audit on a post.

```bash
praisonaiwp ai seo audit POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--depth TEXT` | Audit depth (basic, comprehensive) |
| `--focus-keyword TEXT` | Focus keyword for analysis |
| `--competitors` | Analyze competitors |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### keywords

Analyze keywords for a post.

```bash
praisonaiwp ai seo keywords POST_ID [OPTIONS]
```

### meta

Analyze meta tags.

```bash
praisonaiwp ai seo meta POST_ID [OPTIONS]
```

## Examples

```bash
# Basic SEO audit
praisonaiwp ai seo audit 123

# Comprehensive audit with focus keyword
praisonaiwp ai seo audit 123 --depth comprehensive --focus-keyword "AI trends"

# Keyword analysis
praisonaiwp ai seo keywords 123

# Meta tag analysis
praisonaiwp ai seo meta 123

# Competitor analysis
praisonaiwp ai seo audit 123 --competitors
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
