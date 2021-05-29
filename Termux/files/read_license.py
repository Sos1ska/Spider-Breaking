#!/data/data/com.termux/files/usr/bin/python3
import datetime
import time
import json
import os

date_write = datetime.datetime.now()

from files.wrn.warn import file_not_found_log, i_e_colo, keyboard

try:
    from colorama import Back, Fore, Style
except ImportError:
    i_e_colo()

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_menu_usr = root_data.get("root_menu").get("root_menu_usr")
root_usr = root_data.get("root_menu").get("root_menu_usr")

def cl():
    os.system("clear")

def read_license():
    global cl
    try:
        try:
            FWS = open('files/log/log.txt', 'a', encoding='utf-8')
            FWA = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        FWS.write(f'{root_usr}:StartCode "read_license" - ' + str(date_write) + '\n')
        FWS.close()
        print(Fore.YELLOW + 'Вы хотите прочитать лицензию?' + Style.RESET_ALL)
        while True:
            read = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
            if str(read) == "y":
                FWA.write(f'{root_usr}:Answer "read_license" - "{str(read)}" - ' + str(date_write) + '\n')
                os.system("cat /data/data/com.termux/files/Sos1ska/.Termux/files/licenses/license")
                time.sleep(120)
            elif str(read) == "n":
                FWA.write(f'{root_usr}:Answer "read_license" - "{str(read)}" - ' + str(date_write) + '\n')
                cl()
            else:
                print(Fore.RED + Style.BRIGHT + 'Неккоретный ответ' + Style.RESET_ALL + Style.NORMAL, f': {str(read)}')
            FWA.close()
    except KeyboardInterrupt:
        keyboard()
