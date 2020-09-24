import subprocess

try:
    import click
except ModuleNotFoundError:
    print(
        "\n~~~WARNING~~~\n"
        "Sorry! You must have Click module in your virtual environment in Python-MacOS folder\n"
        "Please be aware that I have left the requirements.txt for you!\n"
    )

MODULES = [
    "black",
    "isort",
    "flake8",
]


@click.command()
@click.argument("path-to-file", nargs=-1)
def code_checked(path_to_file):
    """Python check code formatting"""

    # Create list of command
    list_of_commands = "".join(
        [(module + " " + path + "; ") for module in MODULES for path in path_to_file]
    )

    print("Checking your code!...")

    process = subprocess.run(
        list_of_commands,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    print(f"\n{process.stdout}\n{process.stderr}")


if __name__ == "__main__":
    code_checked()
