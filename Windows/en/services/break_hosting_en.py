import datetime
import json
import os
from time import sleep

date_write = datetime.datetime.now()

from en.credits.credits import credits_en
from files.ban.banners import ban_break_ip
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
except KeyboardInterrupt:
    from files.CCF import start_create_and_write_config
    start_create_and_write_config()

try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
    FWI = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
except FileNotFoundError:
    file_not_found_log()

def cl():
    os.system("cls")

def main():
    def start_break_hosting(break_hosting):
        global cl
        try:
            FWS.write(f'{user_usr}:StartCode "break_hosting" - ' + str(date_write) + '\n')
            FWS.close()
            cl()
            ban_break_ip()
            credits_en()
            print(Fore.YELLOW + 'Enter your domain. Example:' + Style.RESET_ALL, Fore.CYAN + 'google.com' + Style.RESET_ALL)
            ip_input_hosting = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
            FWI.write(f'{user_usr}:IntroducedCode "break_hosting" - {str(ip_input_hosting)} - ' + str(date_write) + '\n')
            FWI.close()
            getinfohosting = f'https://api.2ip.ua/hosting.json?site={str(ip_input_hosting)}'
            try:
                infoiphosting = urllib.request.urllopen( getinfohosting )
            except:
                print('[!] - Domain entered incorrectly - [!]')
                sleep(5)
                quit()
            infoiphosting = json.load( infoiphosting )
            try:
                print('Company >>> ', infoiphosting["name_ripe"])
            except KeyError:
                print('Company >>> Could not determine')
            try:
                print('Site >>> ', infoiphosting["site"])
            except KeyError:
                print('Site >>> Could not determine')
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
    def test_break_hosting(test_break_hosting):
        global cl
        print()
        cl()
    return test_break_hosting

def break_hosting():
    break_hostingg = main.start_break_hosting(break_hosting)
    break_hostingg

def test_break_hosting():
    my_test = main.test_break_hosting(test_break_hosting)
    my_test
