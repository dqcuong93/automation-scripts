# Automation Scripts

Automation scripts help your life easier, it does most of your daily work.

## System Requirements

- MacOS (tested on Catalina 10.15.6 and above)
- Python 3.8+
- ZSH shell

## Available Tools

1. `create-web-link`: Create web links
1. `python-format-check`: Check Python code formatting
1. `run-apps`: Run applications
1. `change-ssh-key`: Change SSH private key

## Installation and Usage

1. Clone repository:

```bash
git clone https://github.com/dqcuong93/automation-scripts.git
cd automation-scripts
```

1. Create bin directory and add to PATH:

```bash
mkdir -p ~/bin
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

> **Why `~/bin` and PATH?**
>
> - `~/bin` is a common convention in Unix-like systems for storing user-specific executable files
> - Adding it to PATH allows you to run these scripts from anywhere without specifying the full path
> - This keeps your scripts organized and easily accessible while following Unix best practices
>

1. Create symbolic links for scripts:

```bash
ln -sf "$(pwd)/tools/create_web_link.py" ~/bin/create-web-link
ln -sf "$(pwd)/tools/python_format_checking.py" ~/bin/python-format-check
ln -sf "$(pwd)/tools/run_apps.py" ~/bin/run-apps
ln -sf "$(pwd)/tools/change_ssh_private_key.py" ~/bin/change-ssh-key
```

1. Make scripts executable:

```bash
chmod +x ~/bin/create-web-link ~/bin/python-format-check ~/bin/run-apps ~/bin/change-ssh-key
```

1. Install required dependencies:

```bash
pip install click prompt_toolkit
```

After installation, you can use these commands from anywhere in your terminal:

- `create-web-link`: Create web links
- `python-format-check`: Check Python code formatting
- `run-apps`: Run applications
- `change-ssh-key`: Change SSH private key

## Updates

To update to the latest version:

```bash
cd automation-scripts  # or wherever you cloned the repo
git pull
```

## Uninstallation

```bash
rm ~/bin/create-web-link ~/bin/python-format-check ~/bin/run-apps ~/bin/change-ssh-key
```

## Contributing

Author: Chris Dao <dqcuong93@gmail.com>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
