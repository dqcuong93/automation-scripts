# Automation Scripts

Automation scripts help your life easier, it does most of your daily work.

## System Requirements

- MacOS (tested on Catalina 10.15.6 and above)
- Python 3.8+
- ZSH shell

## Available Tools

1. `create-web-link`: Create web links
2. `format-check`: Check Python code formatting
3. `ssh-switcher`: Switch between SSH identities

## Installation and Usage

1. Clone repository:

```bash
git clone https://github.com/dqcuong93/automation-scripts.git
cd automation-scripts
```

2. Create bin directory and add to PATH:

```bash
mkdir -p ~/.bin
echo 'export PATH="$HOME/.bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

> **Why `~/.bin` and PATH?**
>
> - `~/.bin` is a common convention in Unix-like systems for storing user-specific executable files
> - Adding it to PATH allows you to run these scripts from anywhere without specifying the full path
> - This keeps your scripts organized and easily accessible while following Unix best practices

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create symbolic links for scripts:

```bash
ln -sf "$(pwd)/tools/create_web_link.py" ~/.bin/create-web-link
ln -sf "$(pwd)/tools/format_checker.py" ~/.bin/format-check
ln -sf "$(pwd)/tools/ssh_switcher.py" ~/.bin/ssh-switcher
```

5. Make scripts executable:

```bash
chmod +x ~/.bin/create-web-link ~/.bin/format-check ~/.bin/ssh-switcher
```

After installation, you can use these commands from anywhere in your terminal:

### Create Web Links (`create-web-link`)

Create web links for various services.

```bash
create-web-link --help  # Show help
create-web-link jira    # Create Jira ticket link
```

### Format Checker (`format-check`)

Check Python code formatting using various tools:

- black: Code formatting
- isort: Import sorting
- flake8: Style guide enforcement
- mypy: Type checking
- bandit: Security checks

```bash
format-check --help     # Show help
format-check file.py    # Check single file
format-check dir/       # Check directory
```

### SSH Identity Switcher (`ssh-switcher`)

Switch between different SSH identities easily.

```bash
ssh-switcher --help      # Show help
ssh-switcher --list      # List available identities
ssh-switcher personal    # Switch to personal key
ssh-switcher            # Interactive mode
```

## Updates

To update to the latest version:

```bash
cd automation-scripts  # or wherever you cloned the repo
git pull
pip install -r requirements-dev.txt  # Update dependencies
```

## Uninstallation

1. Remove symbolic links:

```bash
rm ~/bin/create-web-link ~/bin/format-check ~/bin/ssh-switcher
```

2. Remove repository (optional):

```bash
# From repository root
cd ..
rm -rf automation-scripts
```

3. Remove PATH from ~/.zshrc (optional):
   - Open ~/.zshrc in your editor
   - Remove the line: `export PATH="$HOME/bin:$PATH"`
   - Run: `source ~/.zshrc`

4. Remove bin directory (optional):
   - Only if no other scripts are using it:
   
   ```bash
   rm -rf ~/bin
   ```

## Contributing

Author: Chris Dao <dqcuong93@gmail.com>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
