import subprocess

# Constant go here
COMMAND = "open -a"
APPS_NAME = (
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
)


def run_apps():
    """Run your daily applications
    If you want to change you apps, just modify the constant APPS_NAME above
    """

    # run() returns a CompletedProcess object if it was successful
    # errors in the created process are raised here too
    for app in APPS_NAME:
        try:
            process = subprocess.run(
                f"{COMMAND} {app}",
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                universal_newlines=True,
            )
        except Exception:
            return print(
                f"""
                Error when opening application(s)
                Error report: {Exception}
                """
            )
        print(f"Running command ==> {process.args}")
    print("Finished calling applications")


if __name__ == "__main__":
    run_apps()
