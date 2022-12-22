import subprocess

# Constants go here
COMMAND = "open -a"
WORK_APP = (
    "messages",
    "skype",
    "zalo",
    "messenger",
    "slack",
    "viber",
    "telegram\ desktop",
    "whatsapp",
    "spark",
    "mail",
    "docker",
)
HOME_APPS = (
    "messages",
    "skype",
    "zalo",
    "messenger",
    "viber",
    "telegram\ desktop",
    "whatsapp",
)
ENV = {"home": HOME_APPS, "work": WORK_APP}


def run_apps() -> None:
    """Run your daily applications

    If you want to change you apps, just modify the constant applications name above

    Returns: None

    """

    apps = []

    # Let user picks which environment they want
    env = input(f"Choose your environment: {[env for env in ENV]}\n")
    env = env.lower().strip()  # Remove whitespace

    if env in ENV:  # Check if user input the exits environment or not
        apps = ENV[env]  # Get the applications list
        print("\nFinished fetching applications based on environment!")
    else:
        return print("Please enter the correct environments listed above!")

    # run() returns a CompletedProcess object if it was successful
    # errors in the created process are raised here too
    print("Begin running applications\n")
    for app in apps:
        try:
            process = subprocess.run(
                f"{COMMAND} {app}",
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                universal_newlines=True,
            )
        except Exception:
            print(f"{app} may not be installed yet.")
        print(f"\n~> {process.args}")
    print("\n\nFinished calling applications")


if __name__ == "__main__":
    run_apps()
