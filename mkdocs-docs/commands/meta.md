# Meta Command

Manage post and user metadata.

## Quick Start

```bash
# Get post meta
praisonaiwp meta post get 123 views

# Set user meta
praisonaiwp meta user set 1 nickname "Admin"
```

## Subcommands

### post get

Get post meta value.

```bash
praisonaiwp meta post get POST_ID KEY
```

### post set

Set post meta value.

```bash
praisonaiwp meta post set POST_ID KEY VALUE
```

### post update

Update post meta value.

```bash
praisonaiwp meta post update POST_ID KEY VALUE
```

### post delete

Delete post meta value.

```bash
praisonaiwp meta post delete POST_ID KEY
```

### user get

Get user meta value.

```bash
praisonaiwp meta user get USER_ID KEY
```

### user set

Set user meta value.

```bash
praisonaiwp meta user set USER_ID KEY VALUE
```

### user update

Update user meta value.

```bash
praisonaiwp meta user update USER_ID KEY VALUE
```

### user delete

Delete user meta value.

```bash
praisonaiwp meta user delete USER_ID KEY
```

## Examples

```bash
# Post metadata
praisonaiwp meta post get 123 views
praisonaiwp meta post set 123 views 1000
praisonaiwp meta post update 123 views 1500
praisonaiwp meta post delete 123 views

# User metadata
praisonaiwp meta user get 1 nickname
praisonaiwp meta user set 1 nickname "Admin"
praisonaiwp meta user update 1 nickname "SuperAdmin"
praisonaiwp meta user delete 1 custom_field
```
