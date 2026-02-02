# Cron Command

Manage WordPress cron jobs.

## Quick Start

```bash
# List cron events
praisonaiwp cron list

# Run cron event
praisonaiwp cron run my_hook
```

## Subcommands

### list

List scheduled cron events.

```bash
praisonaiwp cron list [OPTIONS]
```

### run

Run a cron event.

```bash
praisonaiwp cron run HOOK [OPTIONS]
```

### test

Test cron system.

```bash
praisonaiwp cron test [OPTIONS]
```

### event schedule

Schedule a cron event.

```bash
praisonaiwp cron event schedule HOOK [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--recurrence TEXT` | Recurrence (hourly, daily, weekly) |
| `--hook_code TEXT` | PHP code to execute |

### event delete

Delete a cron event.

```bash
praisonaiwp cron event delete HOOK [OPTIONS]
```

## Examples

```bash
# List cron events
praisonaiwp cron list

# Run specific event
praisonaiwp cron run wp_version_check

# Test cron system
praisonaiwp cron test

# Schedule hourly event
praisonaiwp cron event schedule my_hook --recurrence hourly
```
