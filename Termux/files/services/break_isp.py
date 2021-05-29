#!/data/data/com.termux/files/usr/bin/python3
import datetime
import json
import os
from time import sleep

date_write = datetime.datetime.now()

from files.ban.banners import ban_break_ip
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

def start_isp():
    try:
        try:
            FRI = open('files/log/log.txt', 'a', encoding='utf-8')
            FRS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        FRS.write('root:StartCode "break_hosting" - ' + str(date_write) + '\n')
        FRS.close()
        cl()
        print(Fore.YELLOW + 'Введите IP-адрес' + Style.RESET_ALL)
        ip_input_isp = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        FRI.write('root:IntroducedCode "break_hosting" - ' + str(date_write) + '\n')
        FRI.close()
        getinfoipisp = f' https://api.2ip.ua/provider.json?ip={str(ip_input_isp)}'
        try:
            infoipisp = urllib.request.urlopen( getinfoipisp )
        except:
            print('[!] - IP-адрес введён неверно - [!]')
            sleep(5)
            quit()
        infoipisp = json.load( infoipisp )
        try:
            print('Провайдер >>> ', infoipisp["name_ripe"])
        except KeyError:
            print('Провайдер >>> Определить не удалось')
        try:
            print('Сайт провайдера >>> ', infoipisp["site"])
        except KeyError:
            print('Сайт провайдера >>> Определить не удалось')
        try:
            print('Начало диапозона IP-адерса ', infoipisp["ip_range_start"])
        except KeyError:
            print('Начало диапозона IP-адреса >>> Определить не удалось')
        try:
            print('Окончание диапозона IP-адреса >>> ', infoipisp["ip_range_end"])
        except KeyError:
            print('Окончание диапозона IP-адреса >>> Определить не удалось')
        try:
            print('IP-машрут >>> ', infoipisp["route"])
        except KeyError:
            print('IP-машрут >>> Определить не удалось')
        try:
            print('Маска >>> ', infoipisp["mask"])
        except KeyError:
            print('Маска >>> Определить не удалось')
        print()
        cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()

def test_isp():
    global cl
    print()
    cl()
