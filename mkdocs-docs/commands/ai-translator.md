# AI Translator Command

Translate WordPress content to multiple languages using AI.

## Quick Start

```bash
# Translate a post to Spanish and French
praisonaiwp ai translate post 123 --to es,fr

# Create new translated posts
praisonaiwp ai translate post 123 --to de --create-new
```

## Subcommands

### post

Translate an existing WordPress post.

```bash
praisonaiwp ai translate post POST_ID [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--to TEXT` | Target languages (comma-separated codes) |
| `--from TEXT` | Source language (auto-detect if not specified) |
| `--preserve-formatting` | Preserve HTML formatting |
| `--create-new` | Create new posts for translations |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |
| `--verbose` | Show detailed output |

### content

Translate custom content.

```bash
praisonaiwp ai translate content "Your text" --to es,fr
```

## Supported Languages

Common language codes: `en` (English), `es` (Spanish), `fr` (French), `de` (German), `it` (Italian), `pt` (Portuguese), `zh` (Chinese), `ja` (Japanese), `ko` (Korean), `ar` (Arabic), `ru` (Russian), `hi` (Hindi), and 20+ more.

## Examples

```bash
# Translate to multiple languages
praisonaiwp ai translate post 123 --to es,fr,de

# Create new posts for each translation
praisonaiwp ai translate post 123 --to es,fr --create-new

# Preserve HTML formatting
praisonaiwp ai translate post 123 --to de --preserve-formatting
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
