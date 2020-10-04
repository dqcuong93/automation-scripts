import subprocess


def choose_ssh_file():
    """This function will set the ssh private key file automatically.
    Based on what user input ("cuong" or "vcs"),
    the program will set the correspondent ssh identity variable.
    For now, this program accepts 2 ssh private key: "cuong" and "vcs".
    """

    existing_ssh_file = {
        "cuong": "dqcuong93@gmail.com",
        "vcs": "cuong@vietnam-cloud.vn",
    }

    while True:
        ssh_file_name = input(
            f"Choose your ssh file name {list(existing_ssh_file)}:\n--> "
        )  # Prompt input
        ssh_file_name = ssh_file_name.strip()  # Remove all whitespace

        if ssh_file_name in existing_ssh_file:  # Check if SSH file name exist
            ssh_file = existing_ssh_file[ssh_file_name]  # Get value of key

            command = f"ssh-add -D && ssh-add ~/.ssh/{ssh_file}"

            # run() returns a CompletedProcess object if it was successful
            # errors in the created process are raised here too
            subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                universal_newlines=True,
            )
            break
        else:
            print("No SSH file found! Exit!")
            break


if __name__ == "__main__":
    choose_ssh_file()
