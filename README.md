# automation-scripts

PyThon automation scripts help your life easier

## EDX-scripts

Automatically run EDX code by script

Fetch those files to your local machine then run it in your bash/zsh command line interface.

## MacOS-scripts

### GPG encryption
Encrypt your file by GPG (or GnuPG) with US Government standard `AES256`. 
Go to folder `encrypt_files_by_gpg` to have a better look at it.

### SSH key changing
File: `change_ssh_private_key.py`. 

This script will change the SSH private key file for you. Just call it and input your SSH file name.

### Applications auto run
File: `run_apps.py`. 

This script will help you runs your daily apps. Just call it and look at the result.

### How to run these scipts?
All these scipts are written in `Python` scripting language. To run, first you must have `Python 3` in your system, 
then use:
```zsh
python3 <your .py file>
```
For example:
```zsh
python3 run_apps.py
```

### Create aliases to run those scripts on Mac terminal
Create aliases in your ```.zshrc``` file on your Mac:
```zsh
alias <name-of-alias>="python3 path/to/your/file"
```
For example:
```zsh
alias run-apps-script="python3 /Users/chrisdao/Projects/CodingBros/automation-scripts/MacOS/run_apps.py"
alias change-ssh-key-script="python3 /Users/chrisdao/Projects/CodingBros/automation-scripts/MacOS/change_ssh_private_key.py"
```
After setting up. To run, in your Mac terminal, run this command and enjoy :)
```zsh
run-apps-script
```

## Contributing

Author: Chris Dao (dqcuong93@gmail.com)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate
