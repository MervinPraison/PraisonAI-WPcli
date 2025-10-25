"""WordPress CLI client for PraisonAIWP"""

import json
from typing import Any, Optional, Dict, List
from praisonaiwp.core.ssh_manager import SSHManager
from praisonaiwp.utils.logger import get_logger
from praisonaiwp.utils.exceptions import WPCLIError

logger = get_logger(__name__)


class WPClient:
    """WordPress CLI operations wrapper"""
    
    def __init__(
        self,
        ssh: SSHManager,
        wp_path: str,
        php_bin: str = 'php',
        wp_cli: str = '/usr/local/bin/wp'
    ):
        """
        Initialize WP Client
        
        Args:
            ssh: SSH Manager instance
            wp_path: WordPress installation path
            php_bin: PHP binary path (default: 'php')
            wp_cli: WP-CLI binary path (default: '/usr/local/bin/wp')
        """
        self.ssh = ssh
        self.wp_path = wp_path
        self.php_bin = php_bin
        self.wp_cli = wp_cli
        
        logger.debug(f"Initialized WPClient for {wp_path}")
    
    def _execute_wp(self, command: str) -> str:
        """
        Execute WP-CLI command
        
        Args:
            command: WP-CLI command (without 'wp' prefix)
            
        Returns:
            Command output
            
        Raises:
            WPCLIError: If command fails
        """
        full_cmd = f"cd {self.wp_path} && {self.php_bin} {self.wp_cli} {command}"
        
        logger.debug(f"Executing WP-CLI: {command}")
        
        stdout, stderr = self.ssh.execute(full_cmd)
        
        if stderr and 'Error:' in stderr:
            logger.error(f"WP-CLI error: {stderr}")
            raise WPCLIError(f"WP-CLI error: {stderr}")
        
        return stdout.strip()
    
    def get_post(self, post_id: int, field: Optional[str] = None) -> Any:
        """
        Get post data
        
        Args:
            post_id: Post ID
            field: Specific field to retrieve (optional)
            
        Returns:
            Post data (dict if no field specified, str if field specified)
        """
        cmd = f"post get {post_id}"
        
        if field:
            cmd += f" --field={field}"
            result = self._execute_wp(cmd)
            return result
        else:
            cmd += " --format=json"
            result = self._execute_wp(cmd)
            return json.loads(result)
    
    def create_post(self, **kwargs) -> int:
        """
        Create a new post
        
        Args:
            **kwargs: Post fields (post_title, post_content, post_status, etc.)
            
        Returns:
            Created post ID
        """
        args = []
        for key, value in kwargs.items():
            # Escape single quotes in value
            escaped_value = str(value).replace("'", "'\\''")
            args.append(f"--{key}='{escaped_value}'")
        
        cmd = f"post create {' '.join(args)} --porcelain"
        result = self._execute_wp(cmd)
        
        post_id = int(result.strip())
        logger.info(f"Created post ID: {post_id}")
        
        return post_id
    
    def update_post(self, post_id: int, **kwargs) -> bool:
        """
        Update an existing post
        
        Args:
            post_id: Post ID to update
            **kwargs: Fields to update
            
        Returns:
            True if successful
        """
        args = []
        for key, value in kwargs.items():
            # Escape single quotes in value
            escaped_value = str(value).replace("'", "'\\''")
            args.append(f"--{key}='{escaped_value}'")
        
        cmd = f"post update {post_id} {' '.join(args)}"
        self._execute_wp(cmd)
        
        logger.info(f"Updated post ID: {post_id}")
        return True
    
    def list_posts(
        self,
        post_type: str = 'post',
        **filters
    ) -> List[Dict[str, Any]]:
        """
        List posts with filters
        
        Args:
            post_type: Post type (default: 'post')
            **filters: Additional filters (post_status, etc.)
            
        Returns:
            List of post dictionaries
        """
        args = [f"--post_type={post_type}", "--format=json"]
        
        for key, value in filters.items():
            args.append(f"--{key}={value}")
        
        cmd = f"post list {' '.join(args)}"
        result = self._execute_wp(cmd)
        
        return json.loads(result)
    
    def db_query(self, query: str) -> str:
        """
        Execute database query
        
        Args:
            query: SQL query
            
        Returns:
            Query result
        """
        # Escape query for shell
        escaped_query = query.replace('"', '\\"').replace('$', '\\$')
        cmd = f'db query "{escaped_query}"'
        
        return self._execute_wp(cmd)
    
    def search_replace(
        self,
        old: str,
        new: str,
        tables: Optional[List[str]] = None,
        dry_run: bool = False
    ) -> str:
        """
        Search and replace in database
        
        Args:
            old: Text to find
            new: Replacement text
            tables: Tables to search (optional)
            dry_run: Preview changes without applying
            
        Returns:
            Command output
        """
        cmd = f"search-replace '{old}' '{new}'"
        
        if tables:
            cmd += f" {' '.join(tables)}"
        
        if dry_run:
            cmd += " --dry-run"
        
        return self._execute_wp(cmd)
