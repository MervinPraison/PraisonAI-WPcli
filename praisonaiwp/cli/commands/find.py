"""Find command - Search for text in WordPress posts"""

import click
from praisonaiwp.core.config import Config
from praisonaiwp.core.ssh_manager import SSHManager
from praisonaiwp.core.wp_client import WPClient
from praisonaiwp.editors.content_editor import ContentEditor
from praisonaiwp.utils.logger import get_logger
from rich.console import Console
from rich.table import Table

console = Console()
logger = get_logger(__name__)


@click.command()
@click.argument('pattern')
@click.argument('post_id', type=int, required=False)
@click.option('--type', 'post_type', default='post', help='Post type to search')
@click.option('--server', default=None, help='Server name from config')
def find_command(pattern, post_id, post_type, server):
    """
    Search for text in WordPress posts
    
    Examples:
    
        # Find in specific post
        praisonaiwp find "search text" 123
        
        # Find across all posts
        praisonaiwp find "search text"
        
        # Find in pages
        praisonaiwp find "search text" --type page
    """
    
    try:
        # Load configuration
        config = Config()
        server_config = config.get_server(server)
        
        console.print(f"\n[yellow]Searching for: '{pattern}'...[/yellow]\n")
        
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
            
            editor = ContentEditor()
            
            if post_id:
                # Search in specific post
                _search_in_post(wp, editor, post_id, pattern)
            else:
                # Search across all posts
                _search_all_posts(wp, editor, post_type, pattern)
    
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        logger.error(f"Find command failed: {e}")
        raise click.Abort()


def _search_in_post(wp, editor, post_id, pattern):
    """Search in a specific post"""
    
    try:
        post_data = wp.get_post(post_id)
        content = wp.get_post(post_id, field='post_content')
        
        occurrences = editor.find_occurrences(content, pattern)
        
        if occurrences:
            console.print(f"[green]Found {len(occurrences)} occurrence(s) in post {post_id}[/green]")
            console.print(f"[bold]Title:[/bold] {post_data.get('post_title', 'N/A')}\n")
            
            for line_num, line_content in occurrences:
                console.print(f"[cyan]Line {line_num}:[/cyan] {line_content}")
        else:
            console.print(f"[yellow]No occurrences found in post {post_id}[/yellow]")
    
    except Exception as e:
        console.print(f"[red]Error: Post {post_id} not found[/red]")


def _search_all_posts(wp, editor, post_type, pattern):
    """Search across all posts using database query"""
    
    console.print(f"[cyan]Searching {post_type}s in database...[/cyan]\n")
    
    # Use WP-CLI db query for fast server-side search
    query = f"""
        SELECT ID, post_title 
        FROM wp_posts 
        WHERE post_type = '{post_type}' 
        AND post_status = 'publish' 
        AND post_content LIKE '%{pattern}%'
        ORDER BY post_date DESC
    """
    
    try:
        result = wp.db_query(query)
        
        # Parse results
        import json
        
        if not result or result.strip() == '' or result == '[]':
            console.print(f"[yellow]No occurrences found[/yellow]")
            return
        
        posts = json.loads(result) if isinstance(result, str) else result
        
        if not posts:
            console.print(f"[yellow]No occurrences found[/yellow]")
            return
        
        console.print(f"[green]Found in {len(posts)} {post_type}(s):[/green]\n")
        
        # Show results with line details for first few posts
        for i, post in enumerate(posts[:10]):  # Limit to first 10 for performance
            post_id = post['ID']
            title = post['post_title']
            
            console.print(f"[bold cyan]Post {post_id}:[/bold cyan] {title}")
            
            # Get detailed occurrences only for displayed posts
            try:
                content = wp.get_post(post_id, field='post_content')
                occurrences = editor.find_occurrences(content, pattern)
                
                for line_num, line_content in occurrences[:3]:  # Show first 3
                    console.print(f"  Line {line_num}: {line_content[:80]}...")
                if len(occurrences) > 3:
                    console.print(f"  [dim]... and {len(occurrences) - 3} more[/dim]")
            except Exception as e:
                logger.warning(f"Failed to get details for post {post_id}: {e}")
            
            console.print()
        
        if len(posts) > 10:
            console.print(f"[dim]... and {len(posts) - 10} more posts[/dim]")
    
    except Exception as e:
        logger.error(f"Database search failed: {e}")
        console.print(f"[yellow]Falling back to slower search method...[/yellow]\n")
        _search_all_posts_fallback(wp, editor, post_type, pattern)


def _search_all_posts_fallback(wp, editor, post_type, pattern):
    """Fallback: Search across all posts (slower method)"""
    
    # Get all posts
    posts = wp.list_posts(post_type=post_type, post_status='publish')
    
    if not posts:
        console.print(f"[yellow]No {post_type}s found[/yellow]")
        return
    
    console.print(f"[cyan]Searching {len(posts)} {post_type}s...[/cyan]\n")
    
    results = []
    
    for post in posts:
        post_id = post['ID']
        try:
            content = wp.get_post(post_id, field='post_content')
            occurrences = editor.find_occurrences(content, pattern)
            
            if occurrences:
                results.append({
                    'id': post_id,
                    'title': post['post_title'],
                    'occurrences': occurrences
                })
        except Exception as e:
            logger.warning(f"Failed to search post {post_id}: {e}")
    
    if results:
        console.print(f"[green]Found in {len(results)} {post_type}(s):[/green]\n")
        
        for result in results:
            console.print(f"[bold cyan]Post {result['id']}:[/bold cyan] {result['title']}")
            for line_num, line_content in result['occurrences'][:3]:  # Show first 3
                console.print(f"  Line {line_num}: {line_content[:80]}...")
            if len(result['occurrences']) > 3:
                console.print(f"  [dim]... and {len(result['occurrences']) - 3} more[/dim]")
            console.print()
    else:
        console.print(f"[yellow]No occurrences found[/yellow]")
