import subprocess

# Constant go here
COMMAND = "open -a "
APPS_NAME = (
    "messages",
    "skype",
    "zalo",
    "messenger",
    "twitter",
    "slack",
    "viber",
    "telegram",
    "whatsapp",
    "jira",
    "spark",
    # "mail",
)


def run_apps():
    list_of_commands = ""

    # Create list of commands
    for a in APPS_NAME:
        list_of_commands += COMMAND + a + ";"

    # run() returns a CompletedProcess object if it was successful
    # errors in the created process are raised here too
    process = subprocess.run(
        list_of_commands,
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    print(process)


if __name__ == "__main__":
    run_apps()
