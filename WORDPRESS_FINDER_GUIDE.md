# WordPress Auto-Detection Guide

PraisonAIWP can automatically find WordPress installations on your server!

---

## 🚀 Quick Find

```bash
# Automatically find WordPress installations
praisonaiwp find-wordpress

# Interactively select from multiple installations
praisonaiwp find-wordpress --interactive

# Find and update config automatically
praisonaiwp find-wordpress --update-config
```

---

## How It Works

### 1. **Multiple Search Strategies**

PraisonAIWP uses several methods to find WordPress:

#### **Method 1: Search for wp-config.php**
Searches common directories for `wp-config.php`:
- `/var/www/`
- `/home/*/public_html`
- `/usr/share/nginx/`
- `/opt/`
- `/srv/`

#### **Method 2: Check Common Paths**
Checks known WordPress locations:
- `/var/www/html`
- `/var/www/html/wordpress`
- `/var/www/wordpress`
- `/var/www/vhosts/*/httpdocs`
- `/home/*/public_html`
- `/home/*/www`
- `/usr/share/nginx/html`
- And more...

#### **Method 3: Verification**
Verifies each found path has:
- ✅ `wp-config.php` (configuration)
- ✅ `wp-content/` (themes, plugins)
- ✅ `wp-includes/` (core files)
- ✅ WordPress version (from version.php)

---

## Usage Examples

### Example 1: Find All Installations

```bash
praisonaiwp find-wordpress
```

**Output:**
```
Finding WordPress installations on production

Searching for WordPress installations...
This may take a moment...

✓ Found 2 WordPress installation(s)

┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ Path                                      ┃ Version ┃ Components              ┃
┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1 │ /var/www/html                             │ 6.4.2   │ config, content, includes│
│ 2 │ /var/www/vhosts/example.com/httpdocs      │ 6.3.1   │ config, content, includes│
└───┴───────────────────────────────────────────┴─────────┴─────────────────────────┘

Use --interactive to select installation
Use --update-config to save to configuration
```

### Example 2: Interactive Selection

```bash
praisonaiwp find-wordpress --interactive
```

**Output:**
```
Finding WordPress installations on production

✓ Found 2 WordPress installation(s)

Multiple WordPress installations found:

┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━┓
┃ # ┃ Path                                      ┃ Version ┃ Status    ┃
┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━┩
│ 1 │ /var/www/html                             │ 6.4.2   │ ✓ Valid   │
│ 2 │ /var/www/vhosts/example.com/httpdocs      │ 6.3.1   │ ✓ Valid   │
└───┴───────────────────────────────────────────┴─────────┴───────────┘

Select WordPress installation [1]: 1

Selected: /var/www/html
```

### Example 3: Find and Update Config

```bash
praisonaiwp find-wordpress --update-config
```

**Output:**
```
Finding WordPress installations on production

✓ Found 1 WordPress installation(s)

┏━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ Path          ┃ Version ┃ Components              ┃
┡━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1 │ /var/www/html │ 6.4.2   │ config, content, includes│
└───┴───────────────┴─────────┴─────────────────────────┘

Updating config with: /var/www/html
✓ Config updated
```

### Example 4: Different Server

```bash
praisonaiwp find-wordpress --server staging --interactive
```

---

## Integration with Init

The `init` command can also auto-detect WordPress:

```bash
praisonaiwp init
```

**During setup:**
```
WordPress installation path [/var/www/html]: 
  (Press Enter to auto-detect)

Searching for WordPress...
✓ Found: /var/www/html (WordPress 6.4.2)
```

---

## Programmatic Usage

Use the finder in your Python scripts:

```python
from praisonaiwp.core.ssh_manager import SSHManager
from praisonaiwp.core.wp_finder import WordPressFinder

with SSHManager('hostname', 'user', '~/.ssh/id_rsa') as ssh:
    finder = WordPressFinder(ssh)
    
    # Find all installations
    installations = finder.find_all()
    
    for install in installations:
        print(f"Found: {install['path']} (v{install['version']})")
    
    # Find best installation (auto-select)
    best_path = finder.find_best()
    print(f"Best installation: {best_path}")
    
    # Verify specific path
    is_valid, info = finder.verify_wordpress('/var/www/html')
    if is_valid:
        print(f"Valid WordPress at /var/www/html")
        print(f"Version: {info['version']}")
```

---

## Search Locations

### Standard Locations
- `/var/www/html`
- `/var/www/html/wordpress`
- `/var/www/wordpress`
- `/usr/share/nginx/html`
- `/usr/share/nginx/html/wordpress`
- `/opt/wordpress`
- `/srv/www/wordpress`

### Plesk/cPanel Hosting
- `/var/www/vhosts/*/httpdocs`
- `/var/www/vhosts/*/public_html`
- `/home/*/public_html`
- `/home/*/www`
- `/home/*/htdocs`

### Custom Locations
If WordPress is in a custom location, you can:
1. Specify manually: `praisonaiwp init --wp-path /custom/path`
2. Add to search: The finder will still try to locate it

---

## Verification Process

For each found path, PraisonAIWP checks:

### 1. **Core Files**
```bash
✓ wp-config.php exists
✓ wp-content/ directory exists
✓ wp-includes/ directory exists
```

### 2. **WordPress Version**
```bash
✓ Reads version from wp-includes/version.php
✓ Displays version: 6.4.2
```

### 3. **Validity**
```bash
✓ All components present
✓ Valid WordPress installation
```

---

## No WordPress Found?

If no installations are found:

```
✗ No WordPress installations found

Searched locations:
  • /var/www/html
  • /var/www/vhosts/*/httpdocs
  • /home/*/public_html
  • And other common paths

Specify path manually with --wp-path option
```

**Solutions:**

1. **Specify manually:**
   ```bash
   praisonaiwp init --wp-path /custom/wordpress/path
   ```

2. **Check permissions:**
   ```bash
   # Make sure SSH user can access WordPress directory
   ls -la /var/www/html
   ```

3. **Verify WordPress is installed:**
   ```bash
   ssh user@server "ls /var/www/html/wp-config.php"
   ```

---

## Multiple Installations

If multiple WordPress installations are found:

### Option 1: Interactive Selection
```bash
praisonaiwp find-wordpress --interactive
```

Select the one you want to use.

### Option 2: Specify Manually
```bash
praisonaiwp init --wp-path /var/www/vhosts/example.com/httpdocs
```

### Option 3: Use Best Match
The finder automatically selects the most likely installation:
- Prioritizes `/var/www/html`
- Then `/var/www/wordpress`
- Then first valid installation found

---

## Command Options

```bash
praisonaiwp find-wordpress [OPTIONS]
```

### Options

| Option | Description |
|--------|-------------|
| `--server NAME` | Server to search (default: `default`) |
| `--interactive`, `-i` | Interactively select from multiple installations |
| `--update-config` | Update config file with found path |

---

## Benefits

✅ **No manual searching** - Automatic detection  
✅ **Multiple strategies** - Finds WordPress anywhere  
✅ **Verification** - Ensures valid installation  
✅ **Version detection** - Shows WordPress version  
✅ **Interactive selection** - Choose from multiple installations  
✅ **Auto-configuration** - Updates config automatically  

---

## Summary

**Before:**
```bash
ssh user@server
find / -name "wp-config.php" 2>/dev/null
# Manually check each path
# Update config manually
```

**Now:**
```bash
praisonaiwp find-wordpress --interactive --update-config
```

**That's it!** WordPress path automatically detected and configured! 🚀

---

**Auto-detection makes WordPress setup effortless!**
