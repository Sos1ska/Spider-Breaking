import datetime
import json
import os
import webbrowser

date_write = datetime.datetime.now()

from en.credits.credits import credits_en
from files.warn.warn import (file_not_found_log, i_e_colo, i_e_url3,
                             i_e_url_requ, keyboard)

try:
    from colorama import Back, Fore, Style
except ImportError:
    i_e_colo()
try:
    import urllib

    import requests
except ImportError:
    i_e_url_requ()
try:
    import urllib3
except ImportError:
    i_e_url3()

try:
    with open("Spider-Breaking\Windows\\files\config\config.json") as f:
        user_data = json.load(f)
    user_usr = user_data.get("user_name_usr").get("user_input_usr")
except FileNotFoundError:
    from files.CCF import start_create_and_write_config
    start_create_and_write_config()

try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
except FileNotFoundError:
    file_not_found_log()

def cl():
    os.system("cls")

def main():
    def start_break_cell(break_cell):
        global cl
        try:
            FWS.write(f'{user_usr}:StartCode "break_cell" - ' + str(date_write) + '\n')
            FWS.close()
            cl()
            credits_en()
            latitude_tower_input = input(Fore.YELLOW + Style.BRIGHT + 'Введите широту: ' + Style.RESET_ALL + Style.NORMAL)
            longitude_tower_input = input(Fore.YELLOW + Style.BRIGHT + 'Введите долготу: ' + Style.RESET_ALL + Style.NORMAL)
            webbrowser.open("https://opencellid.org/#zoom=13&lat={str(latitude_tower_input)}&lon={str(longitude_tower_input)}")
            print()
            cont_input = input(Fore.YELLOW + 'Press [ENTER] to continue: ' + Style.RESET_ALL)
            if str(cont_input) == "0":
                quit()
            elif str(cont_input) == "quit":
                quit()
            elif str(cont_input) == "quit()":
                quit()
            elif str(cont_input) == "exit":
                quit()
            elif str(cont_input) == "exit()":
                quit()
        except KeyboardInterrupt:
            keyboard()
    
    def test_break_cell_en(test_break_cell_en):
        global cl
        print()
        cl()
    return test_break_cell_en

def break_cell():
    break_celll = main.start_break_cell(break_cell)
    break_celll

def test_break_cell_en():
    my_test = main.test_break_cell_en(test_break_cell_en)
    my_test
