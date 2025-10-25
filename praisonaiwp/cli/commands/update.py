"""Update command - Update WordPress posts"""

import click
from praisonaiwp.core.config import Config
from praisonaiwp.core.ssh_manager import SSHManager
from praisonaiwp.core.wp_client import WPClient
from praisonaiwp.editors.content_editor import ContentEditor
from praisonaiwp.utils.logger import get_logger
from rich.console import Console
from rich.prompt import Confirm

console = Console()
logger = get_logger(__name__)


@click.command()
@click.argument('post_id', type=int)
@click.argument('find_text', required=False)
@click.argument('replace_text', required=False)
@click.option('--line', type=int, help='Update specific line number')
@click.option('--nth', type=int, help='Update nth occurrence')
@click.option('--preview', is_flag=True, help='Preview changes without applying')
@click.option('--server', default=None, help='Server name from config')
def update_command(post_id, find_text, replace_text, line, nth, preview, server):
    """
    Update WordPress post content
    
    Examples:
    
        # Update all occurrences
        praisonaiwp update 123 "old text" "new text"
        
        # Update specific line
        praisonaiwp update 123 "old text" "new text" --line 10
        
        # Update 2nd occurrence
        praisonaiwp update 123 "old text" "new text" --nth 2
        
        # Preview changes
        praisonaiwp update 123 "old text" "new text" --preview
    """
    
    try:
        # Load configuration
        config = Config()
        server_config = config.get_server(server)
        
        # Validate inputs
        if not find_text or not replace_text:
            console.print("[red]Error: Both find_text and replace_text are required[/red]")
            raise click.Abort()
        
        console.print(f"\n[yellow]Fetching post {post_id}...[/yellow]")
        
        with SSHManager(
            server_config['hostname'],
            server_config['username'],
            server_config['key_file'],
            server_config.get('port', 22)
        ) as ssh:
            
            wp = WPClient(
                ssh,
                server_config['wp_path'],
                server_config.get('php_bin', 'php'),
                server_config.get('wp_cli', '/usr/local/bin/wp')
            )
            
            # Get current content
            try:
                post_data = wp.get_post(post_id)
                current_content = wp.get_post(post_id, field='post_content')
            except Exception as e:
                console.print(f"[red]Error: Post {post_id} not found[/red]")
                raise click.Abort()
            
            # Apply replacement based on options
            editor = ContentEditor()
            
            if line:
                console.print(f"[cyan]Replacing at line {line}...[/cyan]")
                new_content = editor.replace_at_line(current_content, line, find_text, replace_text)
            elif nth:
                console.print(f"[cyan]Replacing occurrence #{nth}...[/cyan]")
                new_content = editor.replace_nth_occurrence(current_content, find_text, replace_text, nth)
            else:
                console.print("[cyan]Replacing all occurrences...[/cyan]")
                new_content = current_content.replace(find_text, replace_text)
            
            # Show preview
            changes = _show_preview(current_content, new_content)
            
            if not changes:
                console.print("[yellow]No changes to apply[/yellow]")
                return
            
            if preview:
                console.print("\n[yellow]Preview mode - no changes applied[/yellow]")
                return
            
            # Confirm changes
            if not Confirm.ask("\n[bold]Apply these changes?[/bold]", default=True):
                console.print("[yellow]Update cancelled[/yellow]")
                return
            
            # Apply changes
            console.print("\n[yellow]Updating post...[/yellow]")
            wp.update_post(post_id, post_content=new_content)
            
            console.print(f"[green]✓ Post {post_id} updated successfully[/green]")
            console.print(f"Title: {post_data.get('post_title', 'N/A')}\n")
    
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        logger.error(f"Update command failed: {e}")
        raise click.Abort()


def _show_preview(old_content, new_content):
    """Show preview of changes"""
    
    old_lines = old_content.split('\n')
    new_lines = new_content.split('\n')
    
    changes = []
    for i, (old_line, new_line) in enumerate(zip(old_lines, new_lines), 1):
        if old_line != new_line:
            changes.append((i, old_line, new_line))
    
    if changes:
        console.print(f"\n[bold cyan]Changes to be made: {len(changes)}[/bold cyan]\n")
        
        for line_num, old_line, new_line in changes[:5]:  # Show first 5 changes
            console.print(f"[bold]Line {line_num}:[/bold]")
            console.print(f"  [red]- {old_line.strip()}[/red]")
            console.print(f"  [green]+ {new_line.strip()}[/green]\n")
        
        if len(changes) > 5:
            console.print(f"[dim]... and {len(changes) - 5} more changes[/dim]\n")
    
    return changes
