#!/data/data/com.termux/files/usr/bin/python3
import datetime
import json
import os
from time import sleep

date_write = datetime.datetime.now()

from files.ban.banners import ban_break_ip
from files.credtis.credits import credits
from files.wrn.warn import (file_not_found_log, i_e_colo, i_e_url3,
                            i_e_url_requ, keyboard)

try:
    from colorama import Back, Fore, Style
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
    os.systema("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_hosting():
    global cl
    try:
        try:
            FRI = open('files/log/log.txt', 'a', encoding='utf-8')
            FRS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        cl()
        ban_break_ip()
        credits()
        FRS.write(f'{root_usr}:StartCode "break_hosting" - ' + str(date_write) + '\n')
        FRS.close()
        print(Fore.YELLOW + 'Введите домен. Пример:' + Style.RESET_ALL, Fore.CYAN + 'google.com' + Style.RESET_ALL)
        ip_input_hosting = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        FRI.write(f'{root_usr}:IntroducedCode "break_hosting" - {str(ip_input_hosting)} - ' + str(date_write) + '\n')
        FRI.close()
        getinfohosting = f'https://api.2ip.ua/hosting.json?site={str(ip_input_hosting)}'
        try:
            infoiphosting = urllib.request.uelopen( getinfohosting )
        except:
            print('[!] - Домен введён неверно - [!]')
            sleep(5)
            quit()
        infoiphosting = json.load( infoiphosting )
        try:
            print('Компания >>> ', infoiphosting["name_ripe"])
        except KeyError:
            print('Компания >>> Определить не удалось')
        try:
            print('Сайт >>> ', infoiphosting["site"])
        except KeyError:
            print('Сайт >>> Определить не удалось')
        print()
        cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()

def test_hosting():
    global cl
    print()
    cl()
