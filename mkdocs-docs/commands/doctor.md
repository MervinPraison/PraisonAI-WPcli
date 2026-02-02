# Doctor Command

The `doctor` command checks your PraisonAIWP configuration and connectivity. It's the first command to run when troubleshooting or setting up a new environment.

## Quick Start

```bash
praisonaiwp doctor
```

## What It Shows

1. **Configuration File Location** - Where your config is stored (`~/.praisonaiwp/config.yaml`)
2. **Default Server** - Which WordPress site is used by default
3. **All Configured Servers** - Table of all servers with their websites and transport types
4. **Connection Test** - Optional connectivity verification
5. **Quick Reference Tips** - Common commands to get started

## Example Output

```
╭──────────────────────────────────────╮
│ PraisonAIWP Doctor                   │
│ Configuration and connectivity check │
╰──────────────────────────────────────╯

Configuration File:
  📁 /Users/you/.praisonaiwp/config.yaml
  ✓ Config file exists

Default Server: default
  🌐 Website: https://your-site.com
  🔌 Transport: ssh
  🖥️  Hostname: your-host

Configured Servers: (3 total)
┏━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Name      ┃ Website                ┃ Transport  ┃ Default ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━┩
│ default   │ https://your-site.com  │ ssh        │ ✓       │
│ staging   │ https://staging.com    │ ssh        │         │
│ k8s       │ https://k8s-site.com   │ kubernetes │         │
└───────────┴────────────────────────┴────────────┴─────────┘

╭─────────────────────────── Tips ───────────────────────────╮
│ • Config: ~/.praisonaiwp/config.yaml                       │
│ • Default site: https://your-site.com                      │
│ • List posts: praisonaiwp list --server default            │
│ • Create post: praisonaiwp create "Title" --content "HTML" │
╰────────────────────────────────────────────────────────────╯
```

## Options

| Option | Description |
|--------|-------------|
| `--server NAME` | Test connection to a specific server |
| `--verbose, -v` | Show detailed configuration and full settings |

## Examples

### Basic Check
```bash
praisonaiwp doctor
```

### Test Specific Server Connection
```bash
praisonaiwp doctor --server staging
```

### Verbose Mode
```bash
praisonaiwp doctor --verbose
```

## Troubleshooting

### Config Not Found
If you see "Config file not found", run:
```bash
praisonaiwp init
```

### Connection Failed
1. Verify SSH key is correct in config
2. Check hostname resolves
3. Ensure WP-CLI is installed on remote server

## For AI Agents

!!! info "Agent Discovery"
    When working with praisonaiwp, always run `doctor` first to understand:
    
    - Which website is the default target
    - Available servers and their URLs
    - Whether the configuration is valid
    
    **Development Location**: `~/crawler/praisonaiwp`
    
    **Run with**: `cd ~/crawler/praisonaiwp && uv run praisonaiwp doctor`
