#!/data/data/com.termux/files/usr/bin/python3
import datetime
import json
import os
from time import sleep

date_write = datetime.datetime.now()

from files.ban.banners import ban_break_num
from files.credits.credits import ban_break_num_car
from files.wrn.warn import file_not_found_log, i_e_colo, keyboard

try:
    from colorama import Back, Style, Fore
except ImportError:
    i_e_colo()

def cl():
    os.system("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_break_num_car():
    global cl
    try:
        try:
            FWS = open('files/log/log.txt', 'a', encoding='utf-8')
            FWI = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        FWS.write(f'{root_usr}:StartCode "break_number_car" - ' + str(date_write) + '\n')
        FWS.close()
        cl()
        ban_break_num_car()
        credits()
        print(Fore.YELLOW + 'Введите номер авто' + Style.RESET_ALL)
        num_car_input = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        FWI.write(f'{root_usr}:IntroducedCode "break_number_car" - {str(num_car_input)} - ' + str(date_write) + '\n')
        FWI.close()
        print('Проверьте эти ссылки')
        print(f"\t https://авто-история.рф/num/{str(num_car_input)}/")
        print(f"\t https://www.230km.ru/{str(num_car_input)}.nomer")
        print(f"\t http://avto-nomer.ru/ru/gallery.php?fastsearch={str(num_car_input)}")
        cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()

def test_num_car():
    global cl
    print()
    cl()
