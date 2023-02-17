"""Python conventions checking
This is a scripting file that will check and verify your code
for Python coding conventions.
"""

import logging
import subprocess

import click

MODULES = [
    "black",
    "isort",
    "flake8",
    "eradicate",
]

logging.basicConfig(level=logging.INFO, format="%(message)s")


def check_dependencies():
    try:
        import click
    except ModuleNotFoundError:
        logging.warning(
            "\n~~~WARNING~~~\n"
            "Sorry! You must have required module(s) "
            "in your Python virtual environment\n"
            "Please be aware that I have left the requirements.txt for you!\n"
        )


@click.command()
@click.argument("file_paths", nargs=-1, type=click.Path(exists=True))
def code_checked(file_paths: any) -> None:
    """Python code formatting check

    This program help you check your Python code format.
    You can check one or more files at a time.
    example: python3 python-format-checking.py <file_1> <file_2> | or a whole folder <folder_1>

    Args:
        file_paths: your path to file here

    Returns: None

    """

    check_dependencies()

    command_list = [f"{module} {file_path}" for module in MODULES for file_path in file_paths]

    command_str = ";".join(command_list)

    logging.info("Checking your code...")

    try:
        process = subprocess.run(
            command_str,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=True,
        )
        logging.info(f"\n{process.stdout}\n{process.stderr}")
    except subprocess.CalledProcessError as err:
        logging.error(err)


if __name__ == "__main__":
    code_checked()  # pylint: disable=no-value-for-parameter
