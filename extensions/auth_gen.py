import random
import time
from utils.utils import *
from colorama import Fore, Style


# This time I didn't do a copy/paste as Linux isn't my best friend, even if on windows it works with pyperclip3.
# It is way simpler like this but maybe I'll try to use eMail with socket lib to make the thing more realistic and useful (with an API maybe or smth like that)...

def main():
    cls()
    # Little header
    print(MAGENTA + START)
    print('|' + "AUTH GENERATOR".center(50) + '|')
    print(MID)
    print ('|' + "I will upgrade it very soon !".center(50) + '|')
    print(END + RESET + "\n")

    # Generation of the password
    characthers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    auth = ''.join(random.choice(characthers) for _ in range(6))
    print(MAGENTA + f"> Generated code : {auth}")
    time.sleep(3)
    print("> Thanks for having used Multi-Tool !" + RESET) 
    exit()