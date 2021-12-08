#!/usr/bin/python3
import os
import time
import sys

os.system("clear")
print("This tool will install the best tools for termux.")
print("@GamingOS")

choice = input("\033[93mDo you want to install the best tools for termux? [y/n] ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system("apt update && apt upgrade -y")
print("Please wait,this may take some time")
print("First, please allow the storage permission")
os.system("termux-setup-storage")

print("1)sqlmap")
os.system("mkdir Tools")
os.system("cd Tools")
os.system("apt install git -y")
os.system("apt install python -y")
os.system("git clone https://github.com/sqlmapproject/sqlmap")

print("2)nmap")
os.system("pkg install nmap -y")

print("3)setoolkit")
os.system("pkg install curl -y")
os.system("curl -LO https://raw.githubusercontent.com/Hax4us/master/setoolkit.sh")
os.system("cd setoolkit")
os.system("bash setoolkit.sh")

print("4)Tool-X")
os.system("git clone https://github.com/Rajkumrdusad/Tool-X.git")
os.system("bash install.aex")

print("5)zphisher")
os.system("pkg install php openssh -y")
os.system("git clone https://github.com/htr-tech/zphisher.git")
os.system("cd zphisher")
os.system("bash zphisher.sh")

print("6)fsociety")
os.system("git clone https://github.com/Manisso/fsociety.git")

print("7)Hydra")
os.system("git clone https://github.com/isuruwa/T-HYDRA")
os.system("cd T-HYDRA/Files")
os.system("bash thyins.sh")

print("8)seeker")
os.system("git clone https://github.com/thewhiteh4t/seeker.git")
os.system("cd seeker")
os.system("pip3 install requests")

print("9)EasY_HACk")
os.system("git clone https://github.com/sabri-zaki/EasY_HaCk")
os.system("cd EasY_HACk")
os.system("bash install.sh")

print("Done! Exiting...")
os.system("exit") 

