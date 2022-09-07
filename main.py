import re
from pprint import pprint
from termcolor import colored, cprint
import inquirer
import time
import os


def checkExistingFiles():
    path_procfile = './Procfile'
    path_runtime = './runtime.txt'
    path_requirements = './requirements.txt'
    if os.path.isfile(path_procfile) and os.path.isfile(path_runtime):
        value = input('The file already exists. Would you like to overwrite it?')
        if value == 'y':
            start = time.time()
            print(10 + 5)
            end = time.time()
            print('Overwriting in ', round((end - start) * 10 ** 3, 2), "ms")
        else:
            print('Good Bye!')


# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# questions = [
#   inquirer.Text('name', message="What's your name"),
#   inquirer.Text('surname', message="What's your surname"),
#   inquirer.Text('phone', message="What's your phone number",
#                 validate=lambda _, x: re.match('\+?\d[\d ]+\d', x),
#                 )
# ]
# answers = inquirer.prompt(questions)
# print(answers)
if __name__ == '__main__':
    checkExistingFiles()
