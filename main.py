import requests
import time
import random
import string
from pystyle import Colorate, Colors, Write, Center
import json
f = open( "config.json" , "rb" )
json_data = json.loads(f.read())
headers = {
    'Authorization': json_data["Token"]
}
def run():


    N = 8
    K = 4
    E = 12
    print(Colorate.Vertical(Colors.blue_to_purple, (Center.XCenter(
    """
          _________      .__             .___           
         /   _____/ ____ |  |   ____   __| _/_______  __
         \_____  \ /  _ \|  |  /  _ \ / __ |/ __ \  \/ /
         /        (  <_> )  |_(  <_> ) /_/ \  ___/\   / 
        /_______  /\____/|____/\____/\____ |\___  >\_/  
                  \/                        \/    \/   
        1: Generated Userchecker
    """
    )), 1))
    inp = input("Number :")
    if inp == "1":
        while True:
            res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
            url = requests.get(
            f"https://scriptblox.com/api/user/username?name={res}", headers=headers).json()
            taken = url["taken"]
            print(Colorate.Vertical(Colors.blue_to_purple, (Center.XCenter(
            f"""
            ╔═╗┌─┐┌┐┌┌─┐┬─┐┌┬┐┌─┐┌┬┐  ╦ ╦┌─┐┌─┐┬─┐
            ║ ╦├┤ │││├─┤├┬┘ │ ├┤  ││  ║ ║└─┐├┤ ├┬┘
            ╚═╝└─┘┘└┘┴ ┴┴└─ ┴ └─┘─┴┘  ╚═╝└─┘└─┘┴└─
            Name: {res}  Taken: {taken} 
            """
            )), 1))
            time.sleep(0.1)
run()
