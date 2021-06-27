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
except FileNotFoundError:
    from files.CCF import start_create_and_write_config
    start_create_and_write_config

try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
    FWI = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
except FileNotFoundError:
    file_not_found_log()

def cl():
    os.system("cls")

def main():
    def start_break_ip(break_ip):
        global cl
        try:
            FWS.write(f'{user_usr}:StartCode "break_ip" - ' + str(date_write) + '\n')
            FWS.close()
            cl()
            ban_break_ip()
            credits_en()
            print(Fore.YELLOW + 'Enter the IP Address' + Style.RESET_ALL)
            ip_input = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
            FWI.write(f'{user_usr}:IntroducedCode "break_ip" - {str(ip_input)} - ' + str(date_write) + '\n')
            FWI.close()
            getinfoip = f'https://ipinfo.io/{str(ip_input)}/json'
            try:
                infoip = urllib.request.urlopen( getinfoip )
            except:
                print('[!] - The IP address is entered incorrectly - [!]')
                sleep(5)
                quit()
            infoip = json.load( infoip )
            try:
                print('Country >>> ', infoip["country"])
            except KeyError:
                print('Country >>> Could not determine')
            try:
                print('City >>> ', infoip["city"])
            except KeyError:
                print('City >>> Could not determine')
            try:
                print('Latitude and longitude of the city >>> ', infoip["loc"])
            except KeyError:
                print('Latitude and longitude of the city >>> Could not determine')
            try:
                print('Network name >>> ', infoip["hostname"])
            except KeyError:
                print('Network name >>> Could not determine')
            try:
                print('ISP >>> ', infoip["org"])
            except KeyError:
                print('ISP >>> Could not determine')
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
    def test_break_ip(test_break_ip):
        global cl
        print()
        cl()
    return test_break_ip

def break_ip():
    break_ipp = main.start_break_ip(break_ip)
    break_ipp

def test_break_ip():
    my_test = main.test_break_ip(test_break_ip)
    my_test
