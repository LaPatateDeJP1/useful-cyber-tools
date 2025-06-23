import hashlib
import os
import sys
import subprocess
from colorama import Fore
from getpass import getpass
import pyperclip
from utils.utils import *

# On Arch Linux, pyperclip doesn't work as it should. I prefer using this function instead.c
# Windows : use pyperclip | Linux : use this function
def copy_to_clipboard(text):
    if sys.platform == 'win32':
        pyperclip.copy(text)
        print(MAGENTA + f"> Hash has been copied to the clipboard.")
    elif sys.platform == 'linux':
        try:
            subprocess.run(["wl-copy"], input=text.encode("utf-8"))
            print(MAGENTA + f"> Hash has been copied to the clipboard.")  
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + "> A system error makes it unable to copy your hash. It might be caused by your OS (you're probably on Linux which makes it hard for Python to use the clipboard)." + RESET)
            return
    
def hash_pswd():
    cls()
    password = getpass(MAGENTA + "> Type your password : ")

    # Hashing the password and showing it to the user 
    hashed = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    print(MAGENTA + "> SHA256's hashed password : " + hashed + RESET)

    # Using clipboard for quicker interactions 
    clip = input(MAGENTA + "> Do you want to copy it into your clipboard ? (Y/N) : ")

    if clip == "Y":
        copy_to_clipboard(hashed)
    else:
        print(MAGENTA + f"> Hash '{hashed}' has not been copied to the clipboard.")
    
    # Goodbye and exit
    print(MAGENTA + "> Thanks for having used our Multi-Tool !" + RESET)
    exit()
    