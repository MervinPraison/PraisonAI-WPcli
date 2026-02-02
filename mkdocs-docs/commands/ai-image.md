# AI Image Command

Generate and optimize images for WordPress posts.

## Quick Start

```bash
# Generate an image
praisonaiwp ai image generate "AI technology concept"

# Generate alt text for media
praisonaiwp ai image alt-text --media-id 456
```

## Subcommands

### generate

Generate images using AI.

```bash
praisonaiwp ai image generate "PROMPT" [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--style TEXT` | Image style (photorealistic, artistic, cartoon) |
| `--size TEXT` | Image size (small, medium, large) |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### optimize

Optimize existing images.

```bash
praisonaiwp ai image optimize --media-id ID [OPTIONS]
```

### alt-text

Generate alt text for images.

```bash
praisonaiwp ai image alt-text --media-id ID [OPTIONS]
```

## Examples

```bash
# Generate photorealistic image
praisonaiwp ai image generate "AI technology" --style photorealistic

# Generate artistic image
praisonaiwp ai image generate "Future city" --style artistic --size large

# Generate alt text for media
praisonaiwp ai image alt-text --media-id 456

# Optimize image
praisonaiwp ai image optimize --media-id 456
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
