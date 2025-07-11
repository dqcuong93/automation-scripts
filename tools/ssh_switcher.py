#!/usr/bin/env python3
"""SSH Identity Switcher.

This script helps switch between different SSH identities by managing
the SSH agent's loaded keys.

Usage:
    ssh-switcher [OPTIONS] [IDENTITY]

    If IDENTITY is provided, switches to that identity.
    Otherwise, shows an interactive prompt to choose an identity.

Arguments:
    IDENTITY    Name of the SSH identity to switch to (optional)
               Available identities: cuong, vcs, gk, finsc_bitbucket

Options:
    -h, --help  Show this help message
    -l, --list  List available SSH identities

Examples:
    # Show help
    ssh-switcher --help

    # List available identities
    ssh-switcher --list

    # Switch to personal key
    ssh-switcher cuong

    # Switch to work key
    ssh-switcher vcs

    # Interactive mode (no arguments)
    ssh-switcher

Notes:
    - Requires ssh-agent to be running
    - SSH keys should be in ~/.ssh/ directory
    - Only one identity can be active at a time
    - Running with a new identity will remove all previously loaded keys
    - Use --list to see available identities and their status

Dependencies:
    click>=8.0.0

Environment:
    Requires ssh-agent to be running
    SSH keys should be in ~/.ssh/ directory
"""

import logging
import os
import subprocess
from pathlib import Path
from typing import Dict, Optional

import click

# SSH configurations
SSH_DIR = Path.home() / ".ssh"
SSH_IDENTITIES: Dict[str, str] = {
    "cuong": "personal",
    "gk": "cuong_gk",
    "finsc_bitbucket": "finsc_bitbucket",
}

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def verify_ssh_agent() -> None:
    """Verify that ssh-agent is running."""
    if not os.environ.get("SSH_AUTH_SOCK"):
        raise click.ClickException(
            "SSH agent is not running. Please start it with:\n" "  eval `ssh-agent -s`"
        )


def verify_ssh_key(identity: str) -> Path:
    """Verify that the SSH key exists.

    Args:
        identity: Name of the SSH identity to verify

    Returns:
        Path to the SSH key file

    Raises:
        click.ClickException: If the SSH key file doesn't exist
    """
    key_path = SSH_DIR / identity
    if not key_path.is_file():
        raise click.ClickException(
            f"SSH key not found: {key_path}\n" f"Please ensure the key exists in {SSH_DIR}"
        )
    return key_path


def run_ssh_command(cmd: list[str]) -> None:
    """Run an SSH-related command safely.

    Args:
        cmd: Command and arguments to run

    Raises:
        click.ClickException: If the command fails
    """
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stdout:
            logger.info(result.stdout)
    except subprocess.CalledProcessError as e:
        raise click.ClickException(f"SSH command failed: {e.stderr}")


def list_identities() -> None:
    """List all available SSH identities."""
    logger.info("\nAvailable SSH identities:")
    for alias, identity in SSH_IDENTITIES.items():
        key_path = SSH_DIR / identity
        status = "✓" if key_path.is_file() else "✗"
        logger.info(f"  {status} {alias}: {identity}")


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("identity", type=click.Choice(list(SSH_IDENTITIES.keys())), required=False)
@click.option("-l", "--list", is_flag=True, help="List available SSH identities")
def switch_ssh_key(identity: Optional[str], list: bool) -> None:
    """Switch between different SSH identities.

    If IDENTITY is provided, switches to that identity.
    Otherwise, shows an interactive prompt to choose an identity.

    Examples:
        # Switch to personal key
        ssh-switcher cuong

        # Switch to work key
        ssh-switcher vcs

        # List available identities
        ssh-switcher --list

        # Interactive mode
        ssh-switcher
    """
    try:
        verify_ssh_agent()

        if list:
            list_identities()
            return

        if not identity:
            list_identities()
            identity = click.prompt(
                "\nChoose an identity",
                type=click.Choice(list(SSH_IDENTITIES.keys())),
                show_choices=False,
            )

        key_file = verify_ssh_key(SSH_IDENTITIES[identity])

        # Remove all identities first
        run_ssh_command(["ssh-add", "-D"])

        # Add the new identity
        run_ssh_command(["ssh-add", str(key_file)])

        logger.info(f"\n✨ Successfully switched to SSH identity: {identity}")

    except click.ClickException as e:
        logger.error(str(e))
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    switch_ssh_key()
