"""Python conventions checking
This is a scripting file that will check and verify your code
for Python coding conventions.
"""

# Import required modules
import subprocess

try:
    import click
except ModuleNotFoundError:
    print(
        "\n~~~WARNING~~~\n"
        "Sorry! You must have required module(s) "
        "in your virtual environment in Python-MacOS folder\n"
        "Please be aware that I have left the requirements.txt for you!\n"
    )

MODULES = [
    "black",
    "isort",
    "flake8",
    "eradicate",
]


@click.command()
@click.argument("path-to-file", nargs=-1)
def code_checked(path_to_file):
    """Python code formatting check

    This program help you check your Python code format.
    You can check one or more files at a time.
    example: python3 python-format-checking.py <file_1> <file_2> | or a whole folder <folder_1>
    :param path_to_file: input your path to file here
    :return:
    """

    # Create list of command
    list_of_commands = "".join(
        [(module + " " + path + "; ") for module in MODULES for path in path_to_file]
    )

    print("Checking your code...")

    process = subprocess.run(
        list_of_commands,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        check=True,
    )
    print(f"\n{process.stdout}\n{process.stderr}")


if __name__ == "__main__":
    code_checked()  # pylint: disable=no-value-for-parameter
