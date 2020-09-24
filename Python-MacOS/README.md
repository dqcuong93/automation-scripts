# MacOS-automation-scripts 
Python automation scripts help your life easier.

This does most of your daily life works.

## GPG encryption
Encrypt your file by GPG (or GnuPG) with US Government standard `AES256`. 
Go to folder `encrypt_files_by_gpg` to see more detail.

## SSH key changing
File: `change_ssh_private_key.py`. 

This script will change the SSH private key file for you. Just call it and input your SSH file name.

## Applications auto run
File: `run_apps.py`. 

This script will help you runs your daily apps. Just call it and look at the result.

## Create web link file
File: `create-web-link.py`. 

This script will help you create a file link to a HTTP URL. The file should has ".url" suffix.

## Python automatic code formatting checked
File: `python-format-checking.py`.

This script will help you check your Python code format, using Black, Flake8 and Isort. Just call it and look at the result.

## How to run these scipts?
All these scipts are written in `Python` scripting language. To run, first you must have `Python 3` in your system, 
then use:
```zsh
python3 <your .py file>
```
For example:
```zsh
python3 run_apps.py
```

## Create aliases to run those scripts on Mac terminal
Create aliases in your ```.zshrc``` file on your Mac:
```zsh
alias <name-of-alias>="python3 path/to/your/file"
```
For example:
```zsh
# Create alias for these automation scripts
alias py=python3
alias run-apps-script="py ~/Projects/CodingBros/automation-scripts/Python-MacOS/run_apps.py"
alias change-ssh-key-script="py ~/Projects/CodingBros/automation-scripts/Python-MacOS/change_ssh_private_key.py"
alias create-web-link-script="py ~/Projects/CodingBros/automation-scripts/Python-MacOS/create-web-link.py"
alias code-check="py ~/Projects/CodingBros/automation-scripts/Python-MacOS/python-format-checking.py"
```
After setting up. To run, in your Mac terminal, run commands and enjoy :)
For example:
```zsh
run-apps-script
```

## Contributing
Author: Chris Dao (dqcuong93@gmail.com)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
