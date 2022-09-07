import platform
import pyfiglet
from termcolor import colored, cprint
import inquirer
import time
import os

path_procfile = './Procfile'
path_runtime = './runtime.txt'
path_requirements = './requirements.txt'
python_version = platform.python_version()
current_dir = os.getcwd()
current_namedir = os.path.basename(os.getcwd())
procfile_config = f'web: gunicorn {current_namedir}.wsgi:application --log-file - --log-level debug\npython manage.py ' \
                  'collectstatic --noinput\nmanage.py migrate '
runtime_config = f'python-{python_version}'


def askNeeded():
    questions = [
        inquirer.Checkbox('file',
                          message="What file do you want to?",
                          choices=['Procfile', 'Runtime.txt'],
                          ),
    ]
    answers = inquirer.prompt(questions)
    return answers['file']


def checkExistingFiles(procfile, runtime):
    if os.path.isfile(procfile) and os.path.isfile(runtime):
        questions = [
            inquirer.Confirm('overwrite',
                             message="The file already exists. Would you like to overwrite it?", default=False),
        ]
        answers = inquirer.prompt(questions)
        return answers['overwrite']


def createProcfile(dir_path, config):
    try:
        with open(f'{dir_path}/Procfile', 'w') as f:
            f.write(config)
    except FileNotFoundError:
        print(f"The '{dir_path}' directory does not exist")


def createRuntime(dir_path, config):
    try:
        with open(f'{dir_path}/runtime.txt', 'w') as f:
            f.write(config)
    except FileNotFoundError:
        print(f"The '{dir_path}' directory does not exist")


# TODO: Create function for pip freeze

if __name__ == '__main__':
    intro_layout = pyfiglet.figlet_format("Django Tools")
    print(intro_layout)
    cprint("Welcome to django deploy tools ! Thanks for using my tools. =D", 'blue', attrs=['blink'])
    time.sleep(2)
    ask_file = askNeeded()
    ask_overwrite = checkExistingFiles(path_procfile, path_runtime)
    if 'Procfile' and 'Runtime.txt' in ask_file:
        if ask_overwrite:
            start = time.time()
            createProcfile(current_dir, procfile_config)
            createRuntime(current_dir, runtime_config)
            end = time.time()
            cprint('Overwriting in ', round((end - start) * 10 ** 3, 2), "ms")
        else:
            cprint('Good Bye', 'blue')
    else:
        cprint('Good Bye', 'blue')
