# AI Optimizer Command

Optimize WordPress content for SEO, readability, and engagement.

## Quick Start

```bash
# Optimize a post for SEO
praisonaiwp ai optimize post 123 --seo

# Optimize for readability and apply changes
praisonaiwp ai optimize post 123 --readability --apply
```

## Subcommands

### post

Optimize an existing WordPress post.

```bash
praisonaiwp ai optimize post POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--seo` | Enable SEO optimization |
| `--readability` | Improve readability |
| `--engagement` | Optimize for engagement |
| `--apply` | Apply optimizations directly to the post |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |
| `--verbose` | Show detailed output |

### content

Optimize custom content.

```bash
praisonaiwp ai optimize content "Your content here" [OPTIONS]
```

## Examples

```bash
# SEO optimization
praisonaiwp ai optimize post 123 --seo

# Full optimization
praisonaiwp ai optimize post 123 --seo --readability --engagement

# Optimize and apply changes
praisonaiwp ai optimize post 123 --seo --readability --apply

# Preview without applying
praisonaiwp ai optimize post 123 --seo --verbose
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
