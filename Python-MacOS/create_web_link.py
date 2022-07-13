"""Automatically create web link
Based on what user provided, program will create a web-link file.
"""

import os


def create_url_file():
    """Create a web-link file
    Create a web-link file from the specified link
    """

    current_directory_path = os.getcwd()  # Get current working directory
    url = input("Please copy the url here:\n--> ")

    file_name = input("Please input your URL file name:\n--> ")
    file_name = file_name + ".url"  # Append '.url' to the end of file name
    file_path = "/".join(
        [current_directory_path, file_name]
    )  # Join the current path and the file name together by '/'

    with open(file_path, "w", encoding="utf-8") as file:  # Create new file if not exist
        file.write(f"[InternetShortcut]\nURL={url}")


if __name__ == "__main__":
    create_url_file()
