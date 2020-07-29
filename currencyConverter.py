import requests as req
import socket , time
from colorama import Fore , init
init()
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
lred = Fore.LIGHTRED_EX
lcyan = Fore.LIGHTCYAN_EX

banner = """
█▀▀ █░█ █▀█ █▀█ █▀▀ █▄░█ █▀▀ █▄█   █▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ ▀█▀ █▀▀ █▀█
█▄▄ █▄█ █▀▄ █▀▄ ██▄ █░▀█ █▄▄ ░█░   █▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ░█░ ██▄ █▀▄"""
cred = """
     [+] Made By GH0STH4CK3R        [+] www.currency.me.uk
------------------------------------------------------------------------     """
print(green + banner)
print(lgreen + cred)

try:
    ip = socket.gethostbyname("www.google.com") 
    print(lgreen + "[+] Internet : Active\n")   
except Exception as e:
    print(lred + "[-] Internet : Not Available \nExitting in 5 seconds")  
    time.sleep(5)
    exit()
try:
    ip = socket.gethostbyname("www.currency.me.uk") 
    print(lgreen + "[+] Host : Available\n")   
except Exception as e:
    print(lred + "[-] Host : Not Available \nExitting in 5 seconds")  
    time.sleep(5)
    exit()

url = "https://www.currency.me.uk/remote/ER-CCCS2-AJAX.php?"

print(lcyan + "Example : USD  (US Dollar) , GBP (GreatBritain Pound) , LKR (SriLankan Rupee) ")

print(lgreen + "")
C_from = input("Enter currency , Convert FROM : ")
C_to = input("\nEnter currency , Convert TO : ")
val = input("\nEnter value to convert : ")

if C_from.isnumeric()  or C_to.isnumeric() :
    print(lred + "\nInput only Currency short names (ex: USD )")
    input("\nExit >")
    exit()
elif val.isalpha() :
    print(lred + "\nInput only numeric values (ex: 10 )")
    input("\nExit >")
    exit()
else:    
    para = {"ConvertTo": C_to,"ConvertFrom": C_from,"amount": val} 

    res = req.get(url , params=para)

    if res.status_code == 200 :
        print(lcyan + "")
        print(C_to,":",res.text)
    else:
        print(lred + "Connection Error",res.status_code)

print(lred + "")
input("Exit >")
