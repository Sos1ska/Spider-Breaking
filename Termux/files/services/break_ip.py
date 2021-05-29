#!/data/data/com.termux/files/usr/bin/python3
import datetime
import json
import os
from time import sleep
date_write = datetime.datetime.now()

from files.ban.banners import ban_break_ip
from files.credits.credtis import credits
from files.wrn.warn import (file_not_found_log, i_e_colo, i_e_url3,
                            i_e_url_requ, keyboard)

try:
    from colorama import Back, Style, Fore
except ImportError:
    i_e_colo()
try:
    import urllib3
except ImportError:
    i_e_url3()
try:
    import requests
except ImportError:
    i_e_url_requ()

def cl():
    os.system("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_ip():
    global cl
    try:
        try:
            FRI = open('files/log/log.txt', 'a', encoding='utf-8')
            FRS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        FRS.write('{root_usr}:StartCode "break_ip" - ' + str(date_write) + '\n')
        FRS.close()
        cl()
        ban_break_ip()
        credits()
        print(Fore.YELLOW + Style.BRIGHT + 'Введите IP-адрес' + Style.RESET_ALL + Style.NORMAL)
        ip_input = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        FRI.write(f'{root_usr}:IntroducedCode "break_ip" - {str(ip_input)} - ' + str(date_write) + '\n')
        FRI.close()
        getinfoip = f'https://ipinfo.io/{str(ip_input)}/json'
        try:
            infoIp = urllib.request.urlopen( getinfoip )
        except:
            print('[!] - IP-адрес введён не верно - [!]')
            sleep(5)
            quit()
        infoIp = json.load( infoIp )
        try:
            print('Страна >>> ', infoIp["country"])
        except KeyError:
            print('Страна >>> Определить не удалось')
        try:
            print('Город >>> ', infoIp["city"])
        except KeyError:
            print('Город >>> Определить не удалось')
        try:
            print('Широта и долгота города >>> ', infoIp["loc"])
        except KeyError:
            print('Широта и долгота города >>> Определить не удалось')
        try:
            print('Название сети >>> ', infoIp["hostname"])
        except KeyError:
            print('Название сети >>> Определить не удалось')
        try:
            print('Провайдер >>> ', infoIp["org"])
        except KeyError:
            print('Провайдер >>> Определить не удалось')
        print()
        cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()

def test_ip():
    global cl
    print()
    cl()
