# Remove the background

# Library
from rembg import remove
from pyfiglet import figlet_format
from termcolor2 import colored
from PIL import Image

# Intro
print(colored(figlet_format('Remove The Background Picture'), color='cyan'))
print(colored('===========================================================', color='blue'))

# Value Input
name_file = input('Please Enter Name Picture ===> ')
name_out = input('Please Enter Name For Output [Format == .png] ===> ')

# Start Remove Background
img = Image.open(f'{name_file}')
output = remove(img)
output.save(f'{name_out}')

# A Message As Job Completion
print('                                                 ')
print(colored('=========================================', color='yellow'))
print(colored(figlet_format('Done'), color='green'))

# Finish
# Create By Moein Heshmati