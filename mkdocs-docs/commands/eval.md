# Eval Command

Execute PHP code in WordPress context.

## Quick Start

```bash
# Execute PHP code
praisonaiwp eval "echo 'Hello World';"
```

## Usage

```bash
praisonaiwp eval "PHP_CODE" [OPTIONS]
praisonaiwp eval --file FILE [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--file TEXT` | PHP file to execute |
| `--server TEXT` | Server name from config |

## Examples

```bash
# Execute inline PHP
praisonaiwp eval "echo 'Hello World';"

# Execute PHP file
praisonaiwp eval --file script.php

# Get WordPress info
praisonaiwp eval "echo get_bloginfo('name');"
```
