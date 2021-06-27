import datetime
import json
import os
from time import sleep

date_write = datetime.datetime.now()

from files.warn.warn import i_e_colo, i_e_url_requ, i_e_url3, keyboard, file_not_found_log
from files.ban.banners import ban_break_mac
from en.credits.credits import credits_en

try:
    from colorama import Fore, Style, Back
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
    FWI = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
except FileNotFoundError:
    file_not_found_log()

def cl():
    os.system("cls")

def main():
    global cl
    def start_break_mac_en(break_mac_en):
        global cl
        try:
            cl()
            FWS.write(f'{user_usr}:StartCode "break_mac" - ' + str(date_write) + '\n')
            FWS.close()
            ban_break_mac()
            credits_en()
            print(Fore.YELLOW + 'Enter the MAC Address. Example:' + Style.RESET_ALL, Fore.CYAN + '00:30:48:5a:58:65' + Style.RESET_ALL)
            mac_input = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL +  Style.NORMAL)
            FWI.write(f'{user_usr}:InroducedCode "break_mac" - {str(mac_input)} - ' + str(date_write) + '\n')
            FWI.close()
            getinfomac = f'https://api.2ip.ua/mac.json?mac={str(mac_input)}'
            try:
                infomac = urllib.request.urlopen( getinfomac )
            except:
                print('[!] - MAC-Address entered incorrectly - [!]')
                sleep(5)
                quit()
            infomac = json.load( infomac )
            try:
                print('Country >>> ', infomac["country"])
            except KeyError:
                print('Country >>> Could not determine')
            try:
                print('Company >>> ', infomac["company"])
            except KeyError:
                print('Company >>> Could not determine')
            try:
                print('Address >>> ', infomac["address"])
            except KeyError:
                print('Address >>> Could not determine')
            try:
                print('Date the MAC address was created >>> ', infomac["date_created"])
            except KeyError:
                print('Date the MAC address was created >>> Could not determine')
            try:
                print('MAC address update date >>> ', infomac["date_updated"])
            except KeyError:
                print('MAC address update date >>> Could not determine')
            print()
            cont_input = input(Fore.GREEN + 'Press [ENTER] to continue: ' + Style.RESET_ALL)
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
    def test_break_mac(test_break_mac):
        global cl
        print()
        cl()

def break_mac_en():
    break_mac = main.start_break_mac_en(break_mac_en)
    break_mac

def test_break_mac():
    my_test = main.test_break_mac(test_break_mac)
    my_test