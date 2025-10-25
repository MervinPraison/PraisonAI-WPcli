"""SSH connection management for PraisonAIWP"""

import paramiko
from typing import Optional, Tuple
from praisonaiwp.utils.logger import get_logger
from praisonaiwp.utils.exceptions import SSHConnectionError

logger = get_logger(__name__)


class SSHManager:
    """Manages SSH connections to remote WordPress servers"""
    
    def __init__(
        self,
        hostname: str,
        username: str,
        key_file: str,
        port: int = 22,
        timeout: int = 30
    ):
        """
        Initialize SSH Manager
        
        Args:
            hostname: Server hostname or IP
            username: SSH username
            key_file: Path to SSH private key
            port: SSH port (default: 22)
            timeout: Connection timeout in seconds (default: 30)
        """
        self.hostname = hostname
        self.username = username
        self.key_file = key_file
        self.port = port
        self.timeout = timeout
        self.client: Optional[paramiko.SSHClient] = None
        
        logger.debug(f"Initialized SSHManager for {username}@{hostname}:{port}")
    
    def connect(self) -> "SSHManager":
        """
        Establish SSH connection
        
        Returns:
            Self for chaining
            
        Raises:
            SSHConnectionError: If connection fails
        """
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            logger.info(f"Connecting to {self.username}@{self.hostname}:{self.port}")
            
            self.client.connect(
                hostname=self.hostname,
                username=self.username,
                key_filename=self.key_file,
                port=self.port,
                timeout=self.timeout,
                look_for_keys=False,
                allow_agent=False
            )
            
            logger.info("SSH connection established successfully")
            return self
            
        except paramiko.AuthenticationException as e:
            logger.error(f"Authentication failed: {e}")
            raise SSHConnectionError(f"Authentication failed: {e}")
        except paramiko.SSHException as e:
            logger.error(f"SSH error: {e}")
            raise SSHConnectionError(f"SSH error: {e}")
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            raise SSHConnectionError(f"Connection failed: {e}")
    
    def execute(self, command: str) -> Tuple[str, str]:
        """
        Execute command on remote server
        
        Args:
            command: Command to execute
            
        Returns:
            Tuple of (stdout, stderr)
            
        Raises:
            SSHConnectionError: If not connected or execution fails
        """
        if not self.client:
            raise SSHConnectionError("Not connected. Call connect() first.")
        
        try:
            logger.debug(f"Executing command: {command}")
            
            stdin, stdout, stderr = self.client.exec_command(command)
            
            stdout_str = stdout.read().decode('utf-8')
            stderr_str = stderr.read().decode('utf-8')
            
            if stderr_str and 'Error:' in stderr_str:
                logger.warning(f"Command stderr: {stderr_str}")
            
            logger.debug(f"Command completed with {len(stdout_str)} bytes output")
            
            return stdout_str, stderr_str
            
        except Exception as e:
            logger.error(f"Command execution failed: {e}")
            raise SSHConnectionError(f"Command execution failed: {e}")
    
    def close(self):
        """Close SSH connection"""
        if self.client:
            self.client.close()
            logger.info("SSH connection closed")
            self.client = None
    
    def __enter__(self):
        """Context manager entry"""
        return self.connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
        return False
    
    def __del__(self):
        """Cleanup on deletion"""
        self.close()
