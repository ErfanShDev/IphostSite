import socket
import time
from colorama import Fore,init

init()

print(Fore.RED +" [*] Id Telgram Me :" + Fore.WHITE + "  @ERFAN_0909")
slppr = time.sleep(1)
print(Fore.RED +" [*] Id GitHub Me :" + Fore.WHITE + "   ErfanShDev")
slppr = time.sleep(1)
print(Fore.RED +" [*] Language Programer :" + Fore.WHITE + " Python" + "\n")



slp6 = time.sleep(5)

host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)

print (Fore.RED + " [*] Host Name: " + Fore.LIGHTCYAN_EX + "{0}".format(host_name))
print (Fore.RED + " [*] IP Address: " + Fore.LIGHTCYAN_EX +"{0}".format(ip_addr) + "\n\n")

hosts = ['www.google.com', 'www.github.com']
for i in hosts:
    print (Fore.RED + " Site Target: "+ Fore.WHITE + "{0}".format((i)) + Fore.RED +" And IP Address: " + Fore.RED + " [*] " + Fore.WHITE+ "{1}".format(i, socket.gethostbyname(i)) + Fore.RED + " [*]" + "\n")
