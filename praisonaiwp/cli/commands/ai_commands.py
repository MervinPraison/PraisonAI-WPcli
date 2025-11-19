"""AI-powered content generation commands"""
import click

from praisonaiwp.ai import AI_AVAILABLE
from praisonaiwp.core.config import Config
from praisonaiwp.core.ssh_manager import SSHManager


@click.group()
def ai():
    """AI-powered content generation commands"""
    pass


@ai.command()
@click.argument('topic')
@click.option('--title', help='Post title (defaults to topic)')
@click.option('--status', default='draft', help='Post status (draft/publish)')
@click.option('--auto-publish', is_flag=True, help='Automatically publish to WordPress')
@click.option('--verbose', is_flag=True, help='Verbose output')
@click.option('--server', help='Server name from config')
def generate(topic, title, status, auto_publish, verbose, server):
    """Generate content using AI

    Examples:
        praisonaiwp ai generate "AI Trends 2025"
        praisonaiwp ai generate "AI Trends" --title "The Future of AI" --auto-publish
        praisonaiwp ai generate "AI" --status publish --auto-publish --verbose
    """
    # Check if AI is available
    if not AI_AVAILABLE:
        click.echo(click.style(
            "Error: AI features not available. "
            "Install with: pip install 'praisonaiwp[ai]'",
            fg='red'
        ))
        raise click.Abort()

    # Load config
    config = Config()
    if not config.exists():
        click.echo(click.style(
            "Error: Configuration not found. Run 'praisonaiwp init' first.",
            fg='red'
        ))
        raise click.Abort()

    # Import here to avoid import errors when AI not installed
    from praisonaiwp.ai.integration import PraisonAIWPIntegration
    from praisonaiwp.core.wp_client import WPClient

    try:
        # Get server config
        server_config = config.get_server(server)

        # Create SSH manager and WP client
        ssh_manager = SSHManager(
            hostname=server_config.get('hostname') or server_config.get('ssh_host'),
            username=server_config.get('username') or server_config.get('ssh_user'),
            key_file=server_config.get('key_file') or server_config.get('ssh_key'),
            port=server_config.get('port', 22)
        )

        wp_client = WPClient(
            ssh=ssh_manager,
            wp_path=server_config.get('wp_path', '/var/www/html'),
            php_bin=server_config.get('php_bin', 'php'),
            wp_cli=server_config.get('wp_cli', '/usr/local/bin/wp'),
            verify_installation=False  # Skip verification for AI commands
        )

        # Create integration
        integration = PraisonAIWPIntegration(
            wp_client,
            status=status,
            verbose=1 if verbose else 0
        )

        # Show progress
        click.echo(f"Generating content about: {topic}")
        if verbose:
            click.echo(f"Model: gpt-4o-mini")
            click.echo(f"Status: {status}")

        # Generate content
        result = integration.generate(
            topic=topic,
            title=title,
            auto_publish=auto_publish
        )

        # Show result
        click.echo("\n" + "="*50)
        click.echo(click.style("Generated Content:", fg='green', bold=True))
        click.echo("="*50)
        click.echo(result['content'])

        if result.get('post_id'):
            click.echo("\n" + "="*50)
            click.echo(click.style(
                f"✓ Published to WordPress! Post ID: {result['post_id']}",
                fg='green',
                bold=True
            ))
        else:
            click.echo("\n" + click.style(
                "Content generated (not published). Use --auto-publish to publish.",
                fg='yellow'
            ))

    except Exception as e:
        click.echo(click.style(f"Error: {str(e)}", fg='red'))
        if verbose:
            import traceback
            traceback.print_exc()
        raise click.Abort()
