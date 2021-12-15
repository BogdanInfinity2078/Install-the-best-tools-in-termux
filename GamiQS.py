#!/usr/bin/python3
import os
import time
import sys

os.system("clear")
print("\u001b[32m+-----------------------------------------------+")
print("\u001b[32m+ This tool will install the best tools for     +")
print("\u001b[32m+ termux.                                       +")
print("+-----------------------------------------------+")
print("\u001b[32m+ Maded by GamingOS | Version 4.0 (Stable)      +")
print("\u001b[32m+-----------------------------------------------+")
print("\u001b[32m+ Package 1: sqlmap     Package 6: fsociety     +")
print("\u001b[32m+ Package 2: nmap       Package 7: Hydra        +")
print("\u001b[32m+ Package 3: setoolkit  Package 8: seeker       +")
print("\u001b[32m+ Package 4: Tool-X     Package 9: EasY_HACk    +")
print("\u001b[32m+ Package 5: zphisher                           +")
print("+-----------------------------------------------+")

choice = input("\u001b[34mDo you want to install the best tools for termux? (y/n) ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system("apt update && apt upgrade -y")
print("\u001b[36m---------------------------------------")
print("\u001b[36mPlease wait,this may take some time")
print("\u001b[36m---------------------------------------")

print("\u001b[36m---------------------------------------")
print("\u001b[36mFirst, please allow the storage permission")
print("\u001b[36m---------------------------------------")
os.system("termux-setup-storage")

print(" \u001b[34m--------------------------------------")
print("1)sqlmap")
print(" \u001b[34m--------------------------------------")
os.system("apt install git -y")
os.system("apt install python -y")
os.system("git clone https://github.com/sqlmapproject/sqlmap")

print("\u001b[34m---------------------------------------")
print("2)nmap")
print("\u001b[34m---------------------------------------")
os.system("pkg install nmap -y")

print("\u001b[34m---------------------------------------")
print("3)setoolkit")
print("\u001b[34m---------------------------------------")
os.system("pkg install curl -y")
os.system("curl -LO https://raw.githubusercontent.com/Hax4us/master/setoolkit.sh")

print("\u001b[34m---------------------------------------")
print("4)Tool-X")
print("\u001b[34m---------------------------------------")
os.system("git clone https://github.com/Rajkumrdusad/Tool-X.git")

print("\u001b[34m---------------------------------------")
print("5)zphisher")
print("\u001b[34m---------------------------------------")
os.system("pkg install php openssh -y")
os.system("git clone https://github.com/htr-tech/zphisher.git")

print("\u001b[34m---------------------------------------")
print("6)fsociety")
print("\u001b[34m---------------------------------------")
os.system("git clone https://github.com/Manisso/fsociety.git")

print("\u001b[34m---------------------------------------")
print("7)Hydra")
print("\u001b[34m---------------------------------------")
os.system("git clone https://github.com/isuruwa/T-HYDRA")

print("\u001b[34m---------------------------------------")
print("8)seeker")
print("\u001b[34m---------------------------------------")
os.system("git clone https://github.com/thewhiteh4t/seeker.git")
os.system("pip3 install requests")

print("\u001b[34m---------------------------------------")
print("9)EasY_HACk")
print("\u001b[34m---------------------------------------")
os.system("git clone https://github.com/sabri-zaki/EasY_HaCk")

print("\u001b[34mDone! Exiting...")
os.system("exit") 

