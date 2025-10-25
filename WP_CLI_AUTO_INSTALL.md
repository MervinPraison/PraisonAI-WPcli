# WP-CLI Auto-Installation Guide

PraisonAIWP can automatically detect your server's OS and install WP-CLI with a single command!

---

## 🚀 Quick Install

```bash
# Automatically detect OS and install WP-CLI
praisonaiwp install-wp-cli

# Skip confirmation prompts
praisonaiwp install-wp-cli -y

# Install with dependencies (curl, php)
praisonaiwp install-wp-cli --install-deps -y
```

**That's it!** PraisonAIWP will:
1. ✅ Detect your server's OS (Ubuntu, Debian, CentOS, etc.)
2. ✅ Download WP-CLI
3. ✅ Install it to the correct location
4. ✅ Verify it works
5. ✅ Update your config automatically

---

## Supported Operating Systems

✅ **Ubuntu** (18.04, 20.04, 22.04, 24.04)  
✅ **Debian** (9, 10, 11, 12)  
✅ **CentOS** (7, 8, 9)  
✅ **RHEL** (7, 8, 9)  
✅ **Fedora** (35+)  
✅ **Alpine Linux**  
✅ **macOS** (with Homebrew)  

---

## Installation Options

### Basic Installation

```bash
# Default: Install to /usr/local/bin/wp
praisonaiwp install-wp-cli
```

### Custom Installation Path

```bash
# Install to custom location
praisonaiwp install-wp-cli --install-path /usr/bin/wp
```

### Without Sudo

```bash
# Install to user directory (no sudo required)
praisonaiwp install-wp-cli --install-path ~/bin/wp --no-sudo
```

### With Dependencies

```bash
# Install curl and PHP if not present
praisonaiwp install-wp-cli --install-deps
```

### Specify PHP Binary

```bash
# For Plesk servers
praisonaiwp install-wp-cli --php-bin /opt/plesk/php/8.3/bin/php
```

### Different Server

```bash
# Install on staging server
praisonaiwp install-wp-cli --server staging
```

---

## How It Works

### 1. OS Detection

PraisonAIWP automatically detects:
- Operating system type (Ubuntu, CentOS, etc.)
- OS version
- Available package managers
- PHP installation

```bash
praisonaiwp install-wp-cli
```

Output:
```
Detecting remote OS...
✓ Detected: ubuntu 22.04
```

### 2. Check Existing Installation

Before installing, checks if WP-CLI is already present:

```
Checking if WP-CLI is already installed...
✓ WP-CLI is already installed at /usr/local/bin/wp
```

### 3. Installation Process

If not installed, automatically:

1. **Downloads WP-CLI**
   ```
   Downloading WP-CLI...
   ✓ WP-CLI downloaded
   ```

2. **Tests the download**
   ```
   Testing WP-CLI...
   ✓ WP-CLI test successful: WP-CLI 2.12.0
   ```

3. **Makes it executable**
   ```
   Making WP-CLI executable...
   ✓ WP-CLI is executable
   ```

4. **Installs to system path**
   ```
   Installing to /usr/local/bin/wp...
   ✓ WP-CLI installed to /usr/local/bin/wp
   ```

5. **Verifies installation**
   ```
   ✓ Installation successful: WP-CLI 2.12.0
   ```

### 4. Config Update

Automatically updates your PraisonAIWP config:

```
Updating config with WP-CLI path...
✓ Config updated
```

---

## Examples

### Example 1: Fresh Ubuntu Server

```bash
# Server has no WP-CLI
praisonaiwp install-wp-cli --install-deps -y
```

Output:
```
Installing WP-CLI on production

Detecting remote OS...
✓ Detected: ubuntu 22.04

Checking if WP-CLI is already installed...
WP-CLI not found at /usr/local/bin/wp

Installing WP-CLI...

Installing dependencies for ubuntu...
Updating package list...
Installing curl and php-cli...
✓ Dependencies installed

Downloading WP-CLI...
✓ WP-CLI downloaded

Testing WP-CLI...
✓ WP-CLI test successful: WP-CLI 2.12.0

Making WP-CLI executable...
✓ WP-CLI is executable

Installing to /usr/local/bin/wp...
✓ WP-CLI installed to /usr/local/bin/wp

✓ WP-CLI installed successfully!

You can now use PraisonAIWP commands!
```

### Example 2: Plesk Server

```bash
# Plesk server with custom PHP
praisonaiwp install-wp-cli \
  --php-bin /opt/plesk/php/8.3/bin/php \
  -y
```

### Example 3: Shared Hosting (No Sudo)

```bash
# Install to home directory
praisonaiwp install-wp-cli \
  --install-path ~/bin/wp \
  --no-sudo \
  -y
```

Then update your config:
```yaml
servers:
  production:
    wp_cli: /home/username/bin/wp
```

### Example 4: CentOS Server

```bash
praisonaiwp install-wp-cli --install-deps -y
```

Automatically uses `yum` for CentOS/RHEL.

---

## Programmatic Usage

You can also use the installer in your Python scripts:

```python
from praisonaiwp.core.ssh_manager import SSHManager
from praisonaiwp.core.wp_installer import WPCLIInstaller

# Connect to server
with SSHManager('hostname', 'user', '~/.ssh/id_rsa') as ssh:
    installer = WPCLIInstaller(ssh)
    
    # Auto-install
    success = installer.auto_install(
        install_path='/usr/local/bin/wp',
        use_sudo=True,
        install_deps=True
    )
    
    if success:
        print("✓ WP-CLI installed!")
```

### Just Detect OS

```python
installer = WPCLIInstaller(ssh)
os_type, os_version = installer.detect_os()
print(f"Detected: {os_type} {os_version}")
```

### Check if Installed

```python
if installer.check_wp_cli_installed('/usr/local/bin/wp'):
    print("WP-CLI is installed!")
else:
    print("WP-CLI not found")
```

### Install Dependencies Only

```python
installer.install_dependencies(use_sudo=True)
```

---

## Troubleshooting

### Permission Denied

```
Error: Permission denied installing to /usr/local/bin/wp
```

**Solution:**
```bash
# Use sudo (default)
praisonaiwp install-wp-cli

# Or install to user directory
praisonaiwp install-wp-cli --install-path ~/bin/wp --no-sudo
```

### curl Not Found

```
Error: curl: command not found
```

**Solution:**
```bash
# Install dependencies first
praisonaiwp install-wp-cli --install-deps
```

### PHP Not Found

```
Error: php: command not found
```

**Solution:**
```bash
# Install dependencies
praisonaiwp install-wp-cli --install-deps

# Or specify PHP path
praisonaiwp install-wp-cli --php-bin /opt/plesk/php/8.3/bin/php
```

### Already Installed

```
✓ WP-CLI is already installed at /usr/local/bin/wp
```

**This is good!** WP-CLI is already working. No action needed.

### Unknown OS

```
Detected: unknown unknown
```

**Solution:**

Manual installation:
```bash
# SSH to server
ssh user@hostname

# Download WP-CLI
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

# Make executable
chmod +x wp-cli.phar

# Move to path
sudo mv wp-cli.phar /usr/local/bin/wp

# Test
wp --version
```

---

## Manual Installation (Fallback)

If auto-install doesn't work, you can install manually:

### Ubuntu/Debian

```bash
ssh user@hostname

# Install dependencies
sudo apt-get update
sudo apt-get install -y curl php-cli php-mysql

# Download WP-CLI
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

# Test
php wp-cli.phar --version

# Install
chmod +x wp-cli.phar
sudo mv wp-cli.phar /usr/local/bin/wp

# Verify
wp --version
```

### CentOS/RHEL

```bash
ssh user@hostname

# Install dependencies
sudo yum install -y curl php-cli php-mysql

# Download WP-CLI
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

# Test
php wp-cli.phar --version

# Install
chmod +x wp-cli.phar
sudo mv wp-cli.phar /usr/local/bin/wp

# Verify
wp --version
```

---

## Benefits

✅ **One Command** - No manual steps  
✅ **OS Detection** - Works on any Linux distribution  
✅ **Safe** - Checks before installing  
✅ **Smart** - Auto-updates config  
✅ **Fast** - Completes in seconds  
✅ **Verified** - Tests installation before finishing  

---

## Command Reference

```bash
# Basic
praisonaiwp install-wp-cli

# With options
praisonaiwp install-wp-cli \
  --server production \
  --install-path /usr/local/bin/wp \
  --install-deps \
  --php-bin /usr/bin/php \
  --yes

# No sudo
praisonaiwp install-wp-cli --no-sudo --install-path ~/bin/wp
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--server` | Server name from config | `default` |
| `--install-path` | Installation path | `/usr/local/bin/wp` |
| `--no-sudo` | Don't use sudo | `false` |
| `--install-deps` | Install curl and PHP | `false` |
| `--php-bin` | PHP binary to test with | Auto-detect |
| `--yes`, `-y` | Skip confirmation | `false` |

---

## Summary

**Before PraisonAIWP:**
```bash
ssh user@hostname
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
php wp-cli.phar --version
chmod +x wp-cli.phar
sudo mv wp-cli.phar /usr/local/bin/wp
wp --version
exit
```

**With PraisonAIWP:**
```bash
praisonaiwp install-wp-cli -y
```

**That's it!** 🚀

---

**Auto-installation makes WP-CLI setup effortless!**
