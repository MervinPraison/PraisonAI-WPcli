# AI Workflow Command

Create and manage automated content workflows.

## Quick Start

```bash
# Create a workflow
praisonaiwp ai workflow create "Content Pipeline"

# List workflows
praisonaiwp ai workflow list
```

## Subcommands

### create

Create a new workflow.

```bash
praisonaiwp ai workflow create "NAME" [OPTIONS]
```

**Options:**

| Option | Description |
|--------|-------------|
| `--description TEXT` | Workflow description |
| `--trigger TEXT` | Workflow trigger (schedule, manual, event) |
| `--server TEXT` | Server name from config |
| `--json` | Output in JSON format |

### list

List all workflows.

```bash
praisonaiwp ai workflow list [OPTIONS]
```

### run

Run a workflow.

```bash
praisonaiwp ai workflow run --workflow-id ID [OPTIONS]
```

## Examples

```bash
# Create scheduled workflow
praisonaiwp ai workflow create "Daily Content" --trigger schedule

# Create manual workflow
praisonaiwp ai workflow create "Review Pipeline" --trigger manual

# List all workflows
praisonaiwp ai workflow list

# Run specific workflow
praisonaiwp ai workflow run --workflow-id wf-123
```

## Requirements

- AI features: `pip install praisonaiwp[ai]`
- OpenAI API key: `export OPENAI_API_KEY="sk-..."`
