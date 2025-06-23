import requests
from utils.utils import *

def main():
    cls()
    file = input(MAGENTA + "> In which file is (are) the proxie(s) ? Only put the file name (you need to put the file into the Multi-Tool directory in order to make it work) : ")
    file_path = f"./{file}"
    try:
        with open(file_path) as f:
            proxies = [line.strip() for line in f if line.strip()]
            if proxies:
                test_proxies(proxies)
            else:
                print(LRED + "> No proxies found in the file.")
    except FileNotFoundError:
        print(LRED + f"> File '{file}' not found. Please check the file name and try again.")

def test_proxies(proxies):
    working_proxies = 0
    non_working_proxies = 0
    for choice in proxies:
        try:
            rep = requests.get(
                "https://api.ipify.org",
                proxies={
                    "http": f"http://{choice}",
                    "https": f"http://{choice}",
                },
                timeout=5,
            )
            print(GREEN + f"> Proxy {choice} works : IP is {rep.text}")
            working_proxies += 1
        except requests.RequestException as e:
            print(LRED + f"> Proxy {choice} does not work or an error has been detected : {e}")
            non_working_proxies +=1
    total_proxies = working_proxies + non_working_proxies
    print(MAGENTA + f"\n> Proxy check is finished !\n> Total tested proxies = {total_proxies}\n{GREEN}> Working proxies : {working_proxies}\n{LRED}> Not working proxies : {non_working_proxies}")
    print(MAGENTA + "> Thanks for having used Multi-Tool !" + RESET)    
    