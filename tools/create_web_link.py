#!/usr/bin/env python3
"""Web Link Creator.

This script creates cross-platform web shortcut (.html) files from URLs
provided by the user. The generated file is a minimal HTML page that
redirects to the target URL when opened in a browser, so it works the
same way on Windows, macOS, and Linux (unlike native shortcut formats
such as .url, .webloc, or .desktop, which are platform-specific).

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

    # This will create 'github.html' in the current directory

Notes:
    - Creates a cross-platform .html redirect file
    - Files are created in the current working directory
    - .html extension is automatically added to the filename
    - Existing files with the same name will be overwritten

Dependencies:
    click>=8.0.0

Environment:
    No special environment variables required
"""

import logging
from html import escape
from pathlib import Path

import click

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
def create_url_file() -> None:
    """Create a cross-platform web shortcut (.html redirect) file.

    The script will prompt for:
        1. URL to create shortcut for
        2. Name for the shortcut file
    """
    try:
        current_dir = Path.cwd()

        # Get user input
        url = click.prompt("Please copy the url here", type=str).strip()
        raw_filename = click.prompt("Please input your URL file name", type=str).strip()

        # Sanitize filename: strip any path components (e.g. "../", "/") to
        # prevent writing outside current_dir.
        filename = Path(raw_filename).name
        if not filename:
            raise click.ClickException("Invalid filename")

        # Create file
        escaped_url = escape(url, quote=True)
        html_content = (
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            f'<meta http-equiv="refresh" content="0;url={escaped_url}">\n'
            "</head>\n"
            "<body>\n"
            f'Redirecting to <a href="{escaped_url}">{escaped_url}</a>...\n'
            "</body>\n"
            "</html>\n"
        )
        file_path = current_dir / f"{filename}.html"
        file_path.write_text(html_content, encoding="utf-8")

        logger.info(f"\n✨ File '{filename}.html' created successfully at '{current_dir}'")

    except Exception as e:
        logger.error(f"Error creating URL file: {e}")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    create_url_file()
