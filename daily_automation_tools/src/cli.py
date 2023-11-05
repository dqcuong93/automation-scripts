def display_menu():
    tools = {
        1: "Run daily applications",
        2: "Format Python code",
        3: "Create web link",
        4: "Change ssh private key",
        5: "Exit",
    }
    print(
        "\n=== Automation tools that help you easily run your daily tasks ===\n\n"
        "Choose a tool from the menu below:"
    )
    for number, name in tools.items():
        print(f"{number}. {name}")


def format_checking():
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import PathCompleter
    from tools import python_format_checking

    completer = PathCompleter(expanduser=True)
    file_paths = []

    while True:
        path = prompt("Enter file path (press Enter TWICE to finish): ", completer=completer)
        if path.strip() == "":
            break
        file_paths.append(path)

    python_format_checking.code_checked(file_paths)


def script_called(choice):
    import sys

    from tools import change_ssh_private_key, create_web_link, run_apps

    if choice not in list(range(1, 6)):
        sys.exit("No valid choice, exiting!")
    else:
        match choice:
            case 1:
                run_apps.run_apps()
            case 2:
                format_checking()
            case 3:
                create_web_link.create_url_file()
            case 4:
                change_ssh_private_key.set_ssh_private_key()
            case 5:
                sys.exit("Exiting!")


def choices_selection():
    import sys

    while True:
        display_menu()
        choice = input("\nSelect NUMBER: ")
        try:
            choice = int(choice)
        except ValueError:
            sys.exit("No valid choice, exiting!")
        else:
            script_called(choice=choice)


def main():
    try:
        choices_selection()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)
