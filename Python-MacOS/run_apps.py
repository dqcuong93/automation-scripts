import subprocess

# Constant go here
COMMAND = "open -a"
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
)


def run_apps():
    """Run your daily applications
    If you want to change you apps, just modify the constant APPS_NAME above
    """
    list_of_commands = ""

    # Create list of commands
    for a in APPS_NAME:
        list_of_commands += " ".join([COMMAND, a, ";"])

    # run() returns a CompletedProcess object if it was successful
    # errors in the created process are raised here too
    try:
        process = subprocess.run(
            list_of_commands,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
    except Exception:
        return print(f"Error when opening application(s)")
    else:
        return print(f"Commands run: {process.args.split(' ;')}")


if __name__ == "__main__":
    run_apps()
