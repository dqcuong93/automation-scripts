import os

"""Automatically create web link
Based on what user provided, program will create a web-link file.
"""


def create_url_file():
    current_directory_path = os.getcwd()  # Get current working directory
    url = input("Please copy the url here:\n--> ")
    file_name = input("Please input your URL file name:\n--> ")
    file_name = file_name + ".url"  # Append '.url' to the end of file name
    file_path = "/".join(
        [current_directory_path, file_name]
    )  # Join the current path and the file name together by '/'
    f = open(file_path, "w")  # Create new file if not exist
    f.write(f"[InternetShortcut]\nURL={url}")


if __name__ == "__main__":
    create_url_file()
