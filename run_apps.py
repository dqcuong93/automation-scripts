import subprocess

apps = (
    'messages',
    'skype',
    'zalo',
    'messenger',
    'slack',
    'viber',
    'telegram',
    'whatsapp',
    'jira',
    'spark'
)

command = 'open -a'
commands = ''

for app in apps:
    commands += command + ' ' + app + '; '

# run() returns a CompletedProcess object if it was successful
# errors in the created process are raised here too
process = subprocess.run(commands, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout

output