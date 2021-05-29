import datetime
import json
import os
import time

date_write = datetime.datetime.now()

with open('Spider-Breaking\Termux\\files\config\config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_name_usr").get("root_input_usr")

try:
    FWT = open('files/log/test_log.txt', 'w', encoding='utf-8')
except FileNotFoundError:
    try:
        FWE = open('files/log/log.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        try:
            FWE1 = open('files/error.txt', 'a', encoding='utf-8')
            FWE1.write(f'{root_usr}:Error "FileNotFoundError - log.txt, test_log.txt" - ' + str(date_write) + '\n')
            FWE1.close()
            cl()
            print('Сохранено по пути files/error.txt')
            quit()
        except FileNotFoundError:
            FWE2 = open('files/error.txt', 'w', encoding='utf-8')
            FWE2.write(f'{root_usr}:Error "FileNotFoundError - log.txt, test_log.txt" - ' + str(date_write) + '\n')
            FWE2.close()
            cl()
            print('Сохранено по пути files/error.txt')
            quit()
    FWE.write(f'{root_usr}:Error "FileNotFoundError - test_log.txt" - ' + str(date_write) + '\n')
    FWE.close()
    cl()
    print('Сохранено по пути files/log/log.txt')
    quit()

red = '\033[31m'
green = '\033[32m'
reset = '\033[39m'

def cl():
    os.system("clear")

def start_test():
    try:
        FWS = open('files/log/log.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        try:
            FWE = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            try:
                FWE1 = open('files/error.txt', 'a', encoding='utf-8')
                FWE1.write(f'{root_usr}:Error "FileNotFoundError - log.txt, test_log.txt" - ' + str(date_write) + '\n')
                FWE1.close()
                cl()
                print('Сохранено по пути files/error.txt')
                quit()
            except FileNotFoundError:
                FWE2 = open('files/error.txt', 'w', encoding='utf-8')
                FWE2.write(f'{root_usr}:Error "FileNotFoundError - log.txt, test_log.txt" - ' + str(date_write) + '\n')
                FWE2.close()
                cl()
                print('Сохранено по пути files/error.txt')
                quit()
        FWE.write(f'{root_usr}:Error "FileNotFoundError - test_log.txt" - ' + str(date_write) + '\n')
        FWE.close()
        cl()
        print('Сохранено по пути files/log/log.txt')
        quit()
    FWS.write(f'{root_usr}:StartCode "test" - ' + str(date_write) + '\n')
    FWS.close()
    try:
        from files.main import test_main
        FWT.write(f'{root_usr}:FileCode "main" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "main" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.wrn.warn import test_warn
        FWT.write(f'{root_usr}:FileCode "warn" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "warn" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.break_cell import test_cell
        FWT.write(f'{root_usr}:FileCode "break_cell" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "break_cell" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.break_hosting import test_hosting
        FWT.write(f'{root_usr}:FileCode "break_hosting" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "break_hosting" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.break_ip import test_ip
        FWT.write(f'{root_usr}:FileCode "break_ip" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "break_ip" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.break_isp import test_isp
        FWT.write(f'{root_usr}:FileCode "break_isp" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "break_isp" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.break_mac import test_mac
        FWT.write(f'{root_usr}:FileCode "break_mac" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "break_mac" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.break_num_car import test_num_car
        FWT.write(f'{root_usr}:FileCode "break_num_car" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "break_num_car" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.break_num import test_num
        FWT.write(f'{root_usr}:FileCode "break_num" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "break_num" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.dos_wifi import test_dos_wifi
        FWT.write(f'{root_usr}:FileCode "dos_wifi" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "dos_wifi" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.search_nick import test_nick
        FWT.write(f'{root_usr}:FileCode "search_nick" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "search_nick" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.services import test_services
        FWT.write(f'{root_usr}:FileCode "services" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "services" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.services.sms_bomb import test_bomb
        FWT.write(f'{root_usr}:FileCode "sms_bomb" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "sms_bomb" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.help.help import test_help
        FWT.write(f'{root_usr}:FileCode "help" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "help" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.credits.credits import test_credits
        FWT.write(f'{root_usr}:FileCode "credits" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "credits" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from files.ban.banners import test_ban
        FWT.write(f'{root_usr}:FileCode "banners" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:FileCode "banners" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        from colorama import Fore, Style, Back
        FWT.write(f'\n{root_usr}:Component "Colorama" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:Component "Colorama" {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        import requests
        FWT.write(f'{root_usr}:Component "Requests" - {green}intalled{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:Component "Requests" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    try:
        import urllib3
        FWT.write(f'{root_usr}:Component "Urllib3" - {green}installed{reset} - ' + str(date_write) + '\n')
    except ImportError:
        FWT.write(f'{root_usr}:Component "Urllib3" - {red}not installed{reset} - ' + str(date_write) + '\n')
        pass
    FWT.close()

def read_test_log():
    FRT = open('files/log/test_log.txt')
    print(*FRT)
    time.sleep(15)
