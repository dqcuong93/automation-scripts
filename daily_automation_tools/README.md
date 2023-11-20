# MacOS-automation-scripts 
Python automation scripts help your life easier.

This does most of your daily life works.

## GPG encryption
Encrypt your file by GPG (or GnuPG) with US Government standard `AES256`. 
Go to folder `encrypt_files_by_gpg` to see more detail.

## How to create packaging for distribution?
First, update version in `setup.py`

`pip install wheel`

`python setup.py bdist_wheel`

Move `.whl` file into same directory as **setup.py**

## How to install daily_automation_tools package?
Install the file daily_automations_tools-2.0.0-py3-none-any.whl package by using pip:
`pip install daily_automations_tools-2.0.0-py3-none-any.whl`

## How to use
From terminal run `daily_automation_tools` then choose tool **NUMBER** you want from the menu

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
Use like: `code-format python_format_checking.py` .zshrc file has to be setup first.

This script will help you check your Python code format, using Black, Flake8 and Isort. Just call it and look at the result.

## Contributing
Author: Chris Dao (dqcuong93@gmail.com)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
