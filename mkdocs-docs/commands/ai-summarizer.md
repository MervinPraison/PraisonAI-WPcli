# AI Summarizer Command

Generate summaries, excerpts, and social media content from WordPress posts.

## Quick Start

```bash
# Summarize a post
praisonaiwp ai summarize post 123

# Generate social media content
praisonaiwp ai summarize post 123 --social twitter,linkedin
```

## Subcommands

### post

Generate summaries and social media content for a post.

```bash
praisonaiwp ai summarize post POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--excerpt` | Generate post excerpt |
| `--social TEXT` | Generate social posts (twitter, linkedin, facebook) |
| `--tldr` | Generate TL;DR summary |
| `--length TEXT` | Summary length (short, medium, long) |
| `--hashtags` | Include hashtags in social posts |
| `--tone TEXT` | Content tone (professional, casual, academic) |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |
| `--verbose` | Show detailed output |

### keywords

Extract keywords from a post.

```bash
praisonaiwp ai summarize keywords POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--count INTEGER` | Number of keywords to extract |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### meta

Generate meta description and SEO meta tags.

```bash
praisonaiwp ai summarize meta POST_ID [OPTIONS]
```

## Examples

```bash
# Generate excerpt for a post
praisonaiwp ai summarize post 123 --excerpt

# Generate Twitter and LinkedIn posts
praisonaiwp ai summarize post 123 --social twitter,linkedin --hashtags

# Extract 10 keywords
praisonaiwp ai summarize keywords 123 --count 10

# Generate meta description
praisonaiwp ai summarize meta 123
```

## Requirements

- AI features installed: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
