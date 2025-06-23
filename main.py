# Files imports
from utils.utils import *
from extensions import hash_passwd, random_password, auth_gen, my_ip, proxies

def menu():
    # Header of the Multi-Tool
    print(MAGENTA + START)
    print('|' + MAGENTA + "MULTI-TOOL".center(50) + '|')
    print(MAGENTA + MID + Fore.RESET)

    # Multi-Tool's body
    print(MAGENTA + '|' + "1. Generate a random password".center(50) + '|')
    print(MAGENTA + '|' + "2. Hash a password (SHA256)".center(50) + '|')
    print(MAGENTA + '|' + "3. Authentification code (Beta version)".center(50) + '|')
    print(MAGENTA + '|' + "4. Check my IP (useful for next options)".center(50) + '|')
    print(MAGENTA + '|' + "5. Simple HTTP/S proxy checker".center(50) + '|')
    print(MID)

    # Footer and input of the Multi-Tool
    print(MAGENTA + '|' + "2025 LaPatateDeJP, MIT Licence.".center(50)  + '|')
    print(END)
    choice = input(f"\n{PINPUT} {RESET}")

    # Choices
    if choice == '1':
        random_password.pswd()
    elif choice == '2':
        hash_passwd.hash_pswd()
    elif choice == '3':
        auth_gen.main()
    elif choice == '4':
        my_ip.search_ip()
    elif choice == '5':
        proxies.main()
    else:
        print(MAGENTA + 'Good bye !' + RESET)

menu()