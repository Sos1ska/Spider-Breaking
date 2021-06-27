import datetime
import json
import os

date_write = datetime.datetime.now()

from files.warn.warn import i_e_colo, file_not_found_log
try:
    from colorama import Fore, Style, Back
except ImportError:
    i_e_colo()

try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
except FileNotFoundError:
    file_not_found_log()

try:
    with open("Spider-Breaking\Windows\\files\config\config.json") as f:
        user_data = json.load(f)
    user_usr = user_data.get("user_name_usr").get("user_input_usr")
except FileNotFoundError:
    from files.CCF import start_create_and_write_config
    start_create_and_write_config()

def cl():
    os.system("cls")

def main():
    def credits_enn(credits_en):
        print('Our', Fore.BLUE + 'In contact with' + Style.RESET_ALL, 'links', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
        f'\t\t\thttps://vk.com/2pac_jdm\n'
        f'\t\t\thttps://vk.com/paket\n'
        f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
        print('Our mail', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
        print('Our Github links', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
        f'\t\t\thttps://github.com/Ki11sesh\n'
        f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
    
    def test_credits_en(test_credits_en):
        global cl
        print()
        cl()
    return test_credits_en

def test_credits_en():
    FWS.write(f'{user_usr}:Launched as a check - ' + str(date_write) + '\n')
    my_test = main.test_credits_en(test_credits_en)
    FWS.close()

def credits_en():
    credits = main.credits_enn(credits_en)
    credits
