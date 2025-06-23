import socket 
import requests
from utils.utils import * 

def search_ip():
    cls()

    # Get Local IP Address
    hostname = socket.gethostname()
    localip = socket.gethostbyname(hostname)

    # Get Public IP Address
    req = requests.get("https://api.ipify.org")
    publicip = req.text

    print(MAGENTA + f"> Your Local IP is '{localip}'")
    print(MAGENTA + f"> Your Public IP is '{publicip}'" + RESET)
    exit()




