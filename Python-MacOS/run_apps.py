import logging
import subprocess

# Constants go here
COMMAND = "open -a"
WORK_APP = frozenset(
    {
        "skype",
        "zalo",
        "messenger",
        "slack",
        "viber",
        "telegram\ desktop",
        "whatsapp",
        "spark",
        "docker",
        "line",
    }
)
HOME_APPS = frozenset({"zalo", "messenger", "viber", "telegram\ desktop", "spark"})
ENV = {"home": HOME_APPS, "work": WORK_APP}

logging.basicConfig(level=logging.INFO, format="%(message)s")


def run_apps() -> None:
    """Run your daily applications

    If you want to change you apps, just modify the constant applications name above

    Returns: None

    """

    apps = []

    # Let user picks which environment they want
    env = input(f"Choose your environment: {[env for env in ENV]}\n").lower().strip()

    if env in ENV:
        apps = ENV[env]  # Get the applications list
        logging.info("\nFinished fetching applications based on environment!")
    else:
        return print(
            f"Invalid environment: {env}.\n" f"Please enter the correct environments listed above"
        )

    # run() returns a CompletedProcess object if it was successful
    # errors in the created process are raised here too
    logging.info("Begin running applications\n")
    for app in apps:
        try:
            process = subprocess.run(
                f"{COMMAND} {app}",
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                universal_newlines=True,
            )
            logging.info(f"~> {process.args}\n")
        except subprocess.CalledProcessError as err:
            logging.warning(f"Error running {app}: {err.stderr}\n{app} may not be installed yet.\n")
    logging.info("\nFinished calling applications")


if __name__ == "__main__":
    run_apps()
