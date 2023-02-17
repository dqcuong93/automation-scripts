import logging
import subprocess
from shlex import quote as shlex_quote

SSH_FILE_PATH = "~/.ssh/"

logging.basicConfig(level=logging.INFO, format="%(message)s")


def set_ssh_private_key() -> None:
    """This function sets the ssh private key file automatically.

    Based on what user input ("cuong" or "vcs", etc.),
    the program will set the correspondent ssh identity variable.

    For now, this program accepts 3 ssh private key: "cuong", "vcs" and "gk".

    Returns: None

    """

    # Dictionary of existing ssh files
    ssh_files = {
        "cuong": "dqcuong93@gmail.com",
        "vcs": "cuong@vietnam-cloud.vn",
        "gk": "cuong.dao@goldenkey-software.com",
    }

    while True:
        # Prompt input and remove all whitespace
        ssh_file_name = input(f"Choose your ssh file name in {list(ssh_files)=}:\n--> ").strip()

        if ssh_file_name in ssh_files:
            ssh_file = ssh_files[ssh_file_name]  # Get value of key

            # shlex_quote lets you plug the security hole
            commands = ["ssh-add", "-D", "&&", "ssh-add", f"{SSH_FILE_PATH}{shlex_quote(ssh_file)}"]
            command_str = " ".join(commands).strip()

            logging.info(f"Executing command: {command_str}\n")

            # run() returns a CompletedProcess object if it was successful
            # Errors in the created process are raised here too
            try:
                subprocess.run(
                    command_str,
                    shell=True,
                    check=True,
                    stdout=subprocess.PIPE,
                    universal_newlines=True,
                )
                logging.info(f"\nSuccessfully added SSH file of {ssh_file_name} with {ssh_file}")
            except subprocess.CalledProcessError as err:
                logging.warning(f"ERROR: {err}")
            else:
                break
        else:
            logging.warning("No SSH file found!!\n")


if __name__ == "__main__":
    set_ssh_private_key()
