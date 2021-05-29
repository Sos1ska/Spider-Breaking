import datetime
import json
import os
from time import sleep

date_write = datetime.datetime.now()

from files.ban.banners import ban_break_mac
from files.credits.credits import credits
from files.wrn.warn import (file_not_found_log, i_e_colo, i_e_url3,
                            i_e_url_requ, keyboard)

try:
    from colorama import Back, Fore, Style
except ImportError:
    i_e_colo()
try:
    import urllib
except ImportError:
    i_e_url_requ()
try:
    import urllib3
except ImportError:
    i_e_url3()

def cl():
    os.system("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_mac():
    global cl
    try:
        try:
            FRI = open('files/log/log.txt', 'a', encoding='utf-8')
            FRS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        FRS.write(f'{root_usr}:StartCode "break_mac" - ' + str(date_write) + '\n')
        FRS.close()
        print(Fore.YELLOW + 'Введите MAC-адрес. Пример:' + Style.RESET_ALL, Fore.CYAN + '00:30:48:5a:58:65' + Style.RESET_ALL)
        ip_input_mac = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        FRI.write(f'{root_usr}:IntroducedCode "break_mac" - {str(ip_input_mac)} - ' + str(date_write) + '\n')
        FRI.close()
        getinfomac = f'https://api.2ip.ua/mac.json?mac={str(ip_input_mac)}'
        try:
            infoipmac = urllib.request.urlopen( getinfomac )
        except:
            print('[!] - MAC-адрес введён неверно - [!]')
            sleep(5)
            quit()
            infoipmac = json.load( infoipmac )
        try:
            print('Страна >>> ', infoipmac["country"])
        except KeyError:
            print('Страна >>> Определить не удалось')
        try:
            print('Компания >>> ', infoipmac["company"])
        except KeyError:
            print('Компания >>> Определить не удалось')
        try:
            print('Адрес >>> ', infoipmac["address"])
        except KeyError:
            print('Адрес >>> Определить не удалось')
        try:
            print('Дата создание MAC-адреса >>> ', infoipmac["date_created"])
        except KeyError:
            print('Дата создание MAC-адреса >>> Определить не удалось')
        try:
            print('Дата обновления MAC-адреса >>> ', infoipmac["date_updated"])
        except KeyError:
            print('Дата обновления MAC-адреса >>> Определить не удалось')
        print()
        cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()

def test_mac():
    global cl
    print()
    cl()
