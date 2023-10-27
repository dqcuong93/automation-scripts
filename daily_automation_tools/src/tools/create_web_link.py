"""Automatically create web link
Based on what user provided, program will create a web-link file.
"""

import logging
import os

logging.basicConfig(level=logging.INFO, format="%(message)s")


def create_url_file() -> None:
    """Create a web-link file based on the user provided URL

    Returns: None

    """

    current_directory_path = os.getcwd()  # Get current working directory
    url = input("Please copy the url here:\n--> ").strip()  # Get user provided url

    # Prompt user for filename, and append '.url' to the end of the filename
    file_name = input("Please input your URL file name:\n--> ").strip() + ".url"
    file_path = os.path.join(current_directory_path, file_name)

    with open(file_path, "w", encoding="utf-8") as file:  # Create new file if not exist
        file.write(f"[InternetShortcut]\nURL={url}")

    logging.info(f"\nFile '{file_name}' created successfully at '{current_directory_path}'.")
