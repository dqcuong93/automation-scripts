import subprocess

def choose_ssh_file():
    '''This function will set the default ssh private key file to "cuong@vietnam-cloud.vn"
    Based on what user input ("cuong" or "vcs"), the program will set the correspondent ssh identity variable
    For now, this program is harded-code with 2 accepted ssh private key: "cuong" and "vcs".
    '''
    vcs_ssh_file = 'cuong@vietnam-cloud.vn'  # Default ssh file will be vcs
    personnal_ssh_file = 'dqcuong93@gmail.com'
    ssh_file = vcs_ssh_file

    while True:
        ssh_file_name = input("Choose your ssh file name: 'cuong' or 'vcs'\n--> ")  # Prompt input
        ssh_file_name = ssh_file_name.strip()  # Remove all whitespace

        if ssh_file_name not in ('cuong', 'vcs'):
            print('No SSH file found!')
            break
        else:
            if ssh_file_name == 'cuong': ssh_file = personnal_ssh_file

            command = f'ssh-add -D && ssh-add ~/.ssh/{ssh_file}'

            # run() returns a CompletedProcess object if it was successful
            # errors in the created process are raised here too
            process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            break

if __name__ == '__main__':
    choose_ssh_file()