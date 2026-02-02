# Getting Started

Welcome to PraisonAIWP - AI-powered WordPress content management via WP-CLI over SSH.

## Quick Reference

| What | Command |
|------|---------|
| Check setup | `praisonaiwp doctor` |
| List posts | `praisonaiwp list` |
| Create post | `praisonaiwp create "Title" --content "<p>HTML</p>"` |
| Update post | `praisonaiwp update 123 --post-content "<p>New</p>"` |
| Append to post | `praisonaiwp update 123 --append "<h2>New Section</h2>"` |
| Find text | `praisonaiwp find "keyword"` |

## Configuration

Config file: `~/.praisonaiwp/config.yaml`

Run `praisonaiwp doctor` to see your current configuration and default server.

## Development Setup

For local development:

```bash
cd ~/crawler/praisonaiwp
uv run praisonaiwp --help
```

## Features

- **Multi-server support** - SSH and Kubernetes transports
- **Gutenberg-native** - Auto-converts HTML to Gutenberg blocks
- **AI integration** - AI-powered content generation
- **Duplicate detection** - Find similar posts
- **Backup & restore** - Database management
- **MCP server** - Model Context Protocol support

See the [Commands](../commands/index.md) section for full documentation.
