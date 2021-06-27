import datetime
import json
import os

date_write = datetime.datetime.now()

def cl():
    os.system("cls")

from files.warn.warn import keyboard, file_not_found_log, file_not_found_work_proxy, i_e_colo
from files.ban.banners import started_ban, started_code
from en.credits.credits import credits_en
from en.services.break_cell_en import break_cell
from en.services.break_hosting_en import break_hosting
from en.services.break_ip_en import break_ip
from en.services.break_isp_en import break_isp
from en.services.break_mac_en import break_mac_en
from en.services.dos_wifi import dos_wifi

try:
    with open("Spider-Breaking\Windows\\files\config\config.json") as f:
        user_data = json.load(f)
    user_usr = user_data.get("user_name_usr").get("user_input_usr")
    user_menu_usr = user_data.get("user_menu").get("user_menu_usr")
except FileNotFoundError:
    from files.CCF import start_create_and_write_config
    start_create_and_write_config()

try:
    from colorama import Fore, Style, Back
except ImportError:
    i_e_colo()

try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt")
except FileNotFoundError:
    file_not_found_log()

def main():
    def start_main(mainn):
        global cl
        try:
            FWS.write(f'{user_usr}:StartCode "main_en" - ' + str(date_write) + '\n')
            FWS.close()
            cl()
            started_code()
            while True:
                cl()
                started_ban()
                credits_en()
                while True:
                    menu = input(Fore.RED + Style.BRIGHT + f'{user_menu_usr}> ' + Style.RESET_ALL + Style.NORMAL)
                    if str(menu) == "break_mac":
                        break_mac_en()
                    elif str(menu) == "break_isp":
                        break_isp()
                    elif str(menu) == "break_ip":
                        break_ip()
                    elif str(menu) == "break_cell":
                        break_cell()
                    elif str(menu) == "break_hosting":
                        break_hosting()
                    elif str(menu) == "dos_wifi":
                        dos_wifi()
                    elif str(menu) == "help":
                        FRH = open("Spider-Breaking\Windows\en\help.txt", "r", encoding="utf-8")
                        print(*FRH)
                        FRH.close()
                    else:
                        print(Fore.RED + Style.BRIGHT + 'Non-core commands' + Style.RESET_ALL + Style.NORMAL, f': {str(menu)}')
        except KeyboardInterrupt:
            keyboard()
