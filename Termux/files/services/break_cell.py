import datetime
import json
import os

from files.credits.credits import credits
from files.wrn.warn import file_not_found_log, i_e_colo, keyboard

date_write = datetime.datetime.now()

def test_break_cell():
    global cl
    print()
    cl()

def cl():
    os.system("clear")

try:
    from colorama import Back, Style, Fore
except ImportError:
    i_e_colo()

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_cell():
    global cl
    try:
        try:
            FWS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        cl()
        credits()
        FWS.write(f'{root_usr}:StartCode "break_cell" - ' + str(date_write) + '\n')
        FWS.close()
        credits()
        latitude_tower_input = input(Fore.YELLOW + Style.BRIGHT + "Введите широту: " + Style.RESET_ALL + Style.NORMAL)
        longitude_tower_input = input(Fore.YELLOW + Style.BRIGHT + "Введите долготу: " + Style.RESET_ALL + Style.NORMAL)
        print(f"https://opencellid.org/#zoom=13&lat={str(latitude_tower_input)}&lon={str(longitude_tower_input)}")
        print()
        cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()
