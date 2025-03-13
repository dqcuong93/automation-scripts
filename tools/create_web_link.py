#!/usr/bin/env python3
"""Web Link Creator.

This script creates Windows-compatible web shortcut (.url) files
from URLs provided by the user.

Usage:
    create-web-link [OPTIONS]

Options:
    -h, --help  Show this help message

Examples:
    # Create a shortcut to GitHub
    create-web-link
    Please copy the url here:
    --> https://github.com
    Please input your URL file name:
    --> github

    # This will create 'github.url' in the current directory

Notes:
    - Creates Windows-compatible .url files
    - Files are created in the current working directory
    - .url extension is automatically added to the filename
    - Existing files with the same name will be overwritten

Dependencies:
    click>=8.0.0

Environment:
    No special environment variables required
"""

import logging
from pathlib import Path

import click

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
def create_url_file() -> None:
    """Create a Windows-compatible web shortcut (.url) file.

    The script will prompt for:
        1. URL to create shortcut for
        2. Name for the shortcut file
    """
    try:
        current_dir = Path.cwd()

        # Get user input
        url = click.prompt("Please copy the url here", type=str).strip()
        filename = click.prompt("Please input your URL file name", type=str).strip()

        # Create file
        file_path = current_dir / f"{filename}.url"
        file_path.write_text(f"[InternetShortcut]\nURL={url}", encoding="utf-8")

        logger.info(f"\n✨ File '{filename}.url' created successfully at '{current_dir}'")

    except Exception as e:
        logger.error(f"Error creating URL file: {e}")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    create_url_file()
