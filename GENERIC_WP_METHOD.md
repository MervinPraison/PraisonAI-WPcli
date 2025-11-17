# Generic `wp()` Method - Direct WP-CLI Access

The `wp()` method provides direct access to **ANY** WP-CLI command without needing specific wrapper methods.

## Why Use `wp()`?

- ✅ **Universal**: Works with ALL WP-CLI commands (1000+ commands)
- ✅ **Simple**: Direct mapping to WP-CLI syntax
- ✅ **Flexible**: No waiting for new wrapper methods
- ✅ **Auto-parsing**: Automatically parses JSON output

## Basic Usage

```python
from praisonaiwp import WPClient

# Any WP-CLI command works!
client.wp('cache', 'flush')
client.wp('rewrite', 'flush')
client.wp('cron', 'event', 'list')
```

## With Options

```python
# Options become --key=value flags
posts = client.wp('post', 'list', status='publish', format='json')

# Boolean flags (use True)
user_id = client.wp('user', 'create', 'john', 'john@example.com', 
                    role='editor', porcelain=True)

# Underscores convert to hyphens
client.wp('search-replace', 'old', 'new', dry_run=True)
```

## Auto JSON Parsing

```python
# format='json' automatically parses the response
posts = client.wp('post', 'list', format='json')
for post in posts:
    print(post['ID'], post['post_title'])

# Without format='json', returns string
version = client.wp('core', 'version')  # Returns: "6.4.2"
```

## Real Examples

### Plugin Management
```python
# List all plugins
plugins = client.wp('plugin', 'list', format='json')

# Install and activate
client.wp('plugin', 'install', 'akismet')
client.wp('plugin', 'activate', 'akismet')

# Update all plugins
client.wp('plugin', 'update', '--all')
```

### Database Operations
```python
# Export database
client.wp('db', 'export', 'backup.sql')

# Optimize database
client.wp('db', 'optimize')

# List tables
tables = client.wp('db', 'tables', format='json')
```

### Theme Management
```python
# Install theme
client.wp('theme', 'install', 'twentytwentyfour')

# Activate theme
client.wp('theme', 'activate', 'twentytwentyfour')

# List themes
themes = client.wp('theme', 'list', status='active', format='json')
```

### Cron Management
```python
# List cron events
events = client.wp('cron', 'event', 'list', format='json')

# Run specific event
client.wp('cron', 'event', 'run', 'wp_version_check')

# Schedule new event
client.wp('cron', 'event', 'schedule', 'my_custom_hook', 
          '+1 hour', recurrence='hourly')
```

### Advanced Examples
```python
# Export content
client.wp('export', author='admin', start_date='2024-01-01')

# Import content
client.wp('import', 'content.xml', authors='create')

# Regenerate thumbnails
client.wp('media', 'regenerate', '--yes')

# Update core
client.wp('core', 'update')

# Verify checksums
client.wp('core', 'verify-checksums')
```

## Convenience Methods vs `wp()`

### Both approaches work:

**Convenience method** (with IDE autocomplete):
```python
user_id = client.create_user('john', 'john@example.com', role='editor')
```

**Generic method** (more flexible):
```python
user_id = client.wp('user', 'create', 'john', 'john@example.com', 
                    role='editor', porcelain=True)
```

### When to use each:

| Use Convenience Methods | Use `wp()` Method |
|------------------------|-------------------|
| Common operations | New/experimental commands |
| Need IDE autocomplete | Quick prototyping |
| Want type hints | Custom WP-CLI packages |
| Prefer documentation | Maximum flexibility |

## Tips & Tricks

### 1. Underscore to Hyphen Conversion
```python
# Python uses underscores, WP-CLI uses hyphens
client.wp('search-replace', 'old', 'new', dry_run=True)
# Becomes: wp search-replace old new --dry-run
```

### 2. Boolean Flags
```python
# Use True for flags without values
client.wp('post', 'delete', 123, force=True)
# Becomes: wp post delete 123 --force
```

### 3. Escaping Special Characters
```python
# Single quotes are automatically escaped
client.wp('post', 'create', title="It's a test", content="Quote: 'hello'")
```

### 4. Multiple Values
```python
# Pass lists or comma-separated strings
client.wp('post', 'list', post__in='1,2,3', format='json')
```

## Error Handling

```python
from praisonaiwp.utils.exceptions import WPCLIError

try:
    client.wp('plugin', 'activate', 'nonexistent-plugin')
except WPCLIError as e:
    print(f"Command failed: {e}")
```

## Complete Example

```python
from praisonaiwp import SSHManager, WPClient

# Connect
ssh = SSHManager('example.com', 'username')
client = WPClient(ssh, '/var/www/html')

# Use any WP-CLI command
version = client.wp('core', 'version')
print(f"WordPress {version}")

# List all posts
posts = client.wp('post', 'list', post_type='post', format='json')
print(f"Found {len(posts)} posts")

# Flush cache
client.wp('cache', 'flush')

# Export database
client.wp('db', 'export', '/tmp/backup.sql')

# Done!
ssh.close()
```

## Discover Available Commands

```python
# Get WP-CLI help
help_text = client.wp('help')

# Get help for specific command
help_text = client.wp('help', 'post', 'create')

# List all commands
commands = client.wp('cli', 'cmd-dump')
```

## Summary

The `wp()` method gives you **unlimited access** to WP-CLI's full power:
- 1000+ built-in commands
- Custom WP-CLI packages
- Future WP-CLI features (no code updates needed)
- Direct, intuitive syntax

**You're not limited to our wrapper methods anymore!** 🚀
