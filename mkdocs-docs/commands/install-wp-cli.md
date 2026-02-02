# Install WP-CLI Command

Install WP-CLI on remote server.

## Quick Start

```bash
# Install with confirmation
praisonaiwp install-wp-cli

# Auto-install
praisonaiwp install-wp-cli -y
```

## Usage

```bash
praisonaiwp install-wp-cli [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `-y, --yes` | Skip confirmation prompts |
| `--install-deps` | Install dependencies (curl, php) |
| `--install-path TEXT` | Custom installation path (default: /usr/local/bin/wp) |
| `--php-bin TEXT` | Custom PHP binary path |
| `--server TEXT` | Server name from config |

## Examples

```bash
# Auto-install
praisonaiwp install-wp-cli -y

# Install with dependencies
praisonaiwp install-wp-cli --install-deps -y

# Custom path
praisonaiwp install-wp-cli --install-path /usr/bin/wp -y

# For Plesk servers
praisonaiwp install-wp-cli --php-bin /opt/plesk/php/8.3/bin/php -y
```

## Supported OS

- Ubuntu, Debian, CentOS, RHEL, Fedora, Alpine Linux, macOS
