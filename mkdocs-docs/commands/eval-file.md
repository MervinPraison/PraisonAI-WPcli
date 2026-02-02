# Eval-File Command

Execute PHP files in WordPress context.

## Quick Start

```bash
# Execute PHP file
praisonaiwp eval-file script.php
```

## Usage

```bash
praisonaiwp eval-file FILE [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--server TEXT` | Server name from config |

## Examples

```bash
# Execute PHP file
praisonaiwp eval-file script.php

# Execute on specific server
praisonaiwp eval-file script.php --server production
```
