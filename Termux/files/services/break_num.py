 #!/data/data/com.termux/files/usr/bin/python3import datetime
import json
import os
from time import sleep

date_write = datetime.datetime.now()

from files.ban.banners import ban_break_num
from files.credits.credits import credits
from files.wrn.warn import (file_not_found_log, i_e_colo, i_e_url3,
                            i_e_url_requ, keyboard)

try:
    from colorama import Back, Fore, Style
except ImportError:
    i_e_colo()
try:
    import urllib
except ImportError:
    i_e_url_requ()
try:
    import urllib3
except ImportError:
    i_e_url3()

def cl():
    os.system("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")

def start_num():
    global cl
    try:
        try:
            FWI = open('files/log/log.txt', 'a', encoding='utf-8')
            FWS = open('files/log/log.txt', 'a', encoding='utf-8')
        except FileNotFoundError:
            file_not_found_log()
        FWS.write(f'{root_usr}:StartCode "break_num" - ' + str(date_write) + '\n')
        FWS.close()
        print(Fore.YELLOW + 'Введите номер телефона Пример:' + Style.RESET_ALL, Fore.CYAN + '+79515200611' + Style.RESET_ALL)
        number_input = input(Fore.RED +  Style.BRIGHT + '> ' + Style.RESET_ALL + Style.NORMAL)
        FWI.write(f'{root_usr}:IntroducedCode "break_num" - {str(number_input)} - ' + str(date_write) + '\n')
        FWI.close()
        getinfonum = f'https://htmlweb.ru/geo/api.php?json&telcod={str(number_input)}'
        try:
            infoNumber = urllib.request.urlopen( getinfonum )
        except:
            print('[!] - Номер введён неверно - [!]')
            sleep(5)
            quit()
        infoNumber = json.load( infoNumber )
        try:
            print(f"Страна >>> ", infoNumber["country"]["fullname"])
        except KeyError:
            print(f"Cтрана >>> Не удалось определить")
        try:
            print(f"Столица >>> ", infoNumber["capital"]["name"])
        except KeyError:
            print(f"Столица >>> Не удалось определить")
        try:
            print(f"Широта столицы >>> ", infoNumber["capital"]["latitude"])
        except KeyError:
            print(f"Широта столицы >>> Не удалось определить")
        try:
            print(f"Долгота столицы >>> ", infoNumber["capital"]["longitude"])
        except KeyError:
            print(f"Долгота столицы >>> Не удалось определить")
        try:
            print(f"Тип времени >>> +", infoNumber["capital"]["time_zone"])
        except KeyError:
            print(f"Тип времени >>> Не удалось определить")
        try:
            print(f"Код номера >>> ", infoNumber["country"]["country_code3"])
        except KeyError:
            print(f"Код номера >>> Не удалось опеределить")
        try:
            print(f"MCC номера >>> ", infoNumber["country"]["mcc"])
        except KeyError:
            print(f"MCC номера >>> Не удалось оперделить")
        try:
            print(f"Регион >>> ", infoNumber["region"]["name"])
        except KeyError:
            print(f"Регион >>> Не удалось определить")
        try:
            print(f"Округ >>> ", infoNumber["region"]["okrug"])
        except KeyError:
            print(f"Округ >>> Не удалось определить")
        try:
            print(f"Код региона >>> ", infoNumber["region"]["autocod"])
        except KeyError:
            print(f"Код региона >>> Не удалось определить")
        try:
            print(f"Город >>> ", infoNumber["0"]["name"])
        except KeyError:
            print(f"Город >>> Не удалось определить")
        try:
            print(f"Широта города >>> ", infoNumber["0"]["latitude"])
        except KeyError:
            print(f"Широта города >>> Не удалось определить")
        try:
            print(f"Долгота города >>> ", infoNumber["0"]["longitude"])
        except KeyError:
            print(f"Долгота города >>> Не удалось определить")
        try:
            print(f"Oper_id >>> ", infoNumber["0"]["oper_id"])
        except KeyError:
            print(f"Oper_id >>> Не удалось определить")
        try:
            print(f"Радиус номеров телефонов >>> ", infoNumber["0"]["def"])
        except KeyError:
            print(f"Радиус номеров телефоно >>> Не удалось определить")
        try:
            print(f"Рабочесть телефона >>> ", infoNumber["0"]["mobile"])
        except KeyError:
            print(f"Рабочесть телефона >>> Не удалось определить")
        try:
            print(f"Оператор >>> ", infoNumber["0"]["oper"])
        except KeyError:
            print(f"Оператор >>> Не удалось определить")
        print('\n')
        print(f"https://api.whatsapp.com/send?phone={str(number_input)}&text=You,%20are&20hacked%20by%20by%20the%20Cool-Hackers - Поиск номера в", Fore.GREEN + "WhatsApp" + Style.RESET_ALL) 
        print(f"https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - Поиск номера в", Fore.BLUE + "Facebook" + Style.RESET_ALL)
        print(f"https://linkedin.com/checkpoint/rp/request-password-reset-submit - Поиск номера в Linkedin")
        print(f"https://viber://add?number={str(number_input)} - Поиск номера в", Fore.MAGENTA + "Viber" + Style.RESET_ALL)
        print(f"https://skype:{str(number_input)}?call - Звонок через", Fore.BLUE + "Skype" + Style.RESET_ALL)
        print(f"tel:{str(number_input)} - Простой звонок")
        print()
        cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()

def test_num():
    global cl
    print()
    cl()
