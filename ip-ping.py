import pyfiglet
import subprocess
print("\033[1;31;36m_____________________________________________________________________________")
print("\033[94m")
print(pyfiglet.figlet_format("Website Ip Ping |"))
print("\033[1;31;36m_____________________________________________________________________________")


print("")
print("\033[92m      #########################################################")
print("\033[92m       | \033[95m Author : 𝙲𝚊𝚙𝚝𝚊𝚒𝚗 𝚇𝚃")
print("\033[92m       | \033[95m Tool   : Website Ip Ping")
print("\033[92m       | \033[95m Github : https://github.com/Captain-XT/ip-ping.git")
print("\033[92m       |\033[95m  Coder  : Mr.CxtHacker        \033[37mv1.1")
print("\033[92m      #########################################################")
print("\033[1;31;36m______________________________________________________________________________")
print("\033[0;31;40m______________________________________________________________________________")
print("\033[1;31;36m______________________________________________________________________________")
print("\033[1;32;40m                  [+]Enter Ip Or Website Name[+]")
print()
x = input("\033[1;34;40m>>> \033[37m")
subprocess.call("ping "+ x ,shell=True)
