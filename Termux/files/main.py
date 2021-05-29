import datetime
import json
import os

from files.ban.banners import started_ban, started_code
from files.credits.credits import credits
from files.help.help import help_menu
from files.read_license import read_license
from files.services.break_cell import start_cell
from files.services.break_hosting import start_hosting
from files.services.break_ip import start_ip
from files.services.break_isp import start_isp
from files.services.break_mac import start_mac
from files.services.break_num import start_num
from files.services.break_num_car import start_num_car
from files.services.dos_wifi import start_dos_wifi
from files.services.search_nick import start_nick
from files.services.sms_bomb import start_bomb
from files.services.weeman_master.weeman import main
from files.services.update import update
from files.wrn.warn import (file_not_found_log, i_e_colo, i_e_url3,
                            i_e_url_requ, keyboard)

try:
    from colorama import Back, Fore, Style
except ImportError:
    i_e_colo()
try:
    import requests
except ImportError:
    i_e_url_requ()

date_write = datetime.datetime.now()

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_menu_usr = root_data.get("root_menu").get("root_menu_usr")
root_usr = root_data.get("root_menu").get("root_menu_usr")

def test_main():
    print()
    os.system("clear")

def cl():
    os.system("clear")

def start_main():
    global cl
    try:
        try:
            FWS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        FWS.write(f'{root_usr}:StartCode "main" - ' + str(date_write) + '\n')
        FWS.close()
        cl()
        read_license()
        cl()
        started_code()
        while True:
            cl()
            started_ban()
            credits()
            while True:
                menu = input(Fore.RED + Style.BRIGHT + f'{root_menu_usr}> ' + Style.RESET_ALL + Style.NORMAL)
                if str(menu) == "break_num":
                    start_num()
                elif str(menu) == "break_num_car":
                    start_num_car()
                elif str(menu) == "break_hosting":
                    start_hosting
                elif str(menu) == "dos-wifi":
                    start_dos_wifi()
                elif str(menu) == "break_ip":
                    start_ip()
                elif str(menu) == "break_isp":
                    start_isp()
                elif str(menu) == "break_mac":
                    start_mac()
                elif str(menu) == "search_nick":
                    start_nick()
                elif str(menu) == "sms-bomb":
                    start_bomb()
                elif str(menu) == "help":
                    help_menu()
                elif str(menu) == "fishing":
                    main()
                elif str(menu) == "update":
                    update()
                else:
                    print(Fore.RED + Style.BRIGHT + 'Неккоретная команды' + Style.RESET_ALL + Style.NORMAL, f': {str(menu)}')
    except KeyboardInterrupt:
        keyboard()
