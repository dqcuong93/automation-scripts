import subprocess

import click

APPS = [
    "black",
    "isort",
    "flake8",
]


@click.command()
@click.argument("path-to-file")
def code_checked(path_to_file):
    """Python check code formatting"""

    list_of_commands = ""
    print("Running:")
    for a in APPS:
        list_of_commands += " ".join([a, path_to_file, "; "])
        print(f"~> {a + ' ' + path_to_file}")

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
