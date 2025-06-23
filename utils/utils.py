# Ahhhh imports
import os
from colorama import Fore

# Color shortcuts
RED = Fore.RED
LRED = Fore.LIGHTRED_EX
BLUE = Fore.BLUE
LBLUE = Fore.LIGHTBLUE_EX
CYAN = Fore.CYAN
GREEN = Fore.GREEN
LGREEN = Fore.LIGHTGREEN_EX
MAGENTA = Fore.MAGENTA
RESET = Fore.RESET

# Aesthetic shortcuts (ends and beginnings, middle and inputs)
START = '╭' + '─' * 50 + '╮'
MID = '|' + '―' * 50 + '|'
END = '╰' + '―' * 50 + '╯'

PINPUT = "> Multi-Tool #"

# Basic commands that makes life easier 
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')