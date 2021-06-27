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
    from colorama import Fore, Style, Back
except ImportError:
    i_e_colo()
try:
    import urllib, requests
except ImportError:
    i_e_url_requ()
try:
    import urllib3
except ImportError:
    i_e_url3()

try:
    with open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8") as f:
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
    def start_break_isp(break_isp):
        global cl
        try:
            FWS.write(f'{user_usr}:StartCode "break_isp" - ' + str(date_write) + '\n')
            FWS.close()
            cl()
            ban_break_ip()
            credits_en()
            print(Fore.YELLOW + 'Enter the IP Address' + Style.RESET_ALL)
            isp_input = input(Fore.RED + Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
            FWI.write(f'{user_usr}:IntoducedCode "break_isp" - {str(isp_input)} - ' + str(date_write) + '\n')
            FWI.close()
            getinfoisp = f'https://api.2ip.ua/provider.json?ip={str(isp_input)}'
            try:
                infoisp = urllib.urlopen( getinfoisp )
            except:
                print('[!] - The IP address is entered incorrectly - [!]')
                sleep(5)
                quit()
            infoisp = json.load( infoisp )
            try:
                print('ISP >>> ', infoisp["name_ripe"])
            except KeyError:
                print('ISP >>> Could not determine')
            try:
                print('Site ISP >>> ', infoisp["site"])
            except KeyError:
                print('Site ISP >>> Could not determine')
            try:
                print('Start of IP address range >>> ', infoisp["ip_range_start"])
            except KeyError:
                print('Start of IP address range >>> Could not determine')
            try:
                print('End of IP address range >>> ', infoisp["ip_range_end"])
            except KeyError:
                print('End of IP address range >>> Coule not determine')
            try:
                print('IP Route >>> ', infoisp["route"])
            except KeyError:
                print('IP Route >>> Could not determine')
            try:
                print('Mask >>> ', infoisp["mask"])
            except KeyError:
                print('Mask >>> Could not determine')
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
    def test_break_isp(test_break_isp):
        global cl
        print()
        cl()
    return test_break_isp

def break_isp():
    break_ispp = main.start_break_isp(break_isp)
    break_ispp

def test_break_isp():
    my_test = main.test_break_isp(test_break_isp)
    my_test