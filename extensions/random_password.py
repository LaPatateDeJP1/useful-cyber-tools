import random 
from colorama import Fore
import sys
import os
import pyperclip
import subprocess
from utils.utils import *

# On Arch Linux, pyperclip doesn't work as it should. I prefer using this function instead
# Windows : use pyperclip | Linux : use this function
def copy_to_clipboard(text):
    if sys.platform.startswith == 'win':
        pyperclip.copy(text)
        print(MAGENTA + f"> Password has been copied to the clipboard.")
    elif sys.platform == 'linux':
        try:
            subprocess.run(["wl-copy"], input=text.encode("utf-8"))
            print(MAGENTA + f"> Password has been copied to the clipboard.")  
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + "> A system error makes it unable to copy your hash. It might be caused by your OS (you're probably on Linux which makes it hard for Python to use the clipboard)." + RESET)
            return
        
def pswd():
    cls()
    try:
        lenght = int(input(MAGENTA + "> What lenght should the password be ? "))
    except ValueError:
        print("> Please choose a valid number." + RESET)
        return
    # Generation of the password
    asciic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789(){}[]/\\*@!?.$"
    password = ''.join(random.choice(asciic) for _ in range(lenght))
    print("> Generated password : " + password)

    # Using clipboard for quicker interactions 
    clip = input(MAGENTA + "> Do you want to copy it into your clipboard ? (Y/N) : ")

    if clip == "Y":
        copy_to_clipboard(password)
    else:
        print(MAGENTA + f"> Password '{password}' has not been copied to the clipboard.")
    
    # Goodbye and exit
    print(MAGENTA + "> Thanks for having used our Multi-Tool !" + RESET)
    exit()
