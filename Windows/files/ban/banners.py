import datetime
import json
import os
import random
from time import sleep

date_write = datetime.datetime.now()

from files.warn.warn import i_e_colo, file_not_found_log

with open('Spider-Breaking\Windows\\files\config\config.json') as f:
    user_data = json.load(f)
user_usr = user_data.get("user_name_usr").get("user_input_usr")

try:
    from colorama import Fore, Style, Back
except ImportError:
    i_e_colo

try:
    FWT = open('Spider-Breaking\Windows\\files\log\log.txt', 'a', encoding='utf-8')
except FileNotFoundError:
    file_not_found_log()

def cl():
      os.system("cls")

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
Version 4.0 ''',
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
Version 4.0 ''',
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
Version 4.0 ''',
'''
░░░░░░░  ░░░░░░  ░░░░░░░ ░░ ░░   ░░ ░░░░░░░  ░░░░░  ░░   ░░  ░░░░░   ░░░░░░ ░░   ░░ ░░░░░░░ ░░░░░░  ░░░░░░░
▒▒      ▒▒    ▒▒ ▒▒      ▒▒ ▒▒  ▒▒  ▒▒      ▒▒   ▒▒ ▒▒   ▒▒ ▒▒   ▒▒ ▒▒      ▒▒  ▒▒  ▒▒      ▒▒   ▒▒ ▒▒
▒▒▒▒▒▒▒ ▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒      ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒▒▒
     ▓▓ ▓▓    ▓▓      ▓▓ ▓▓ ▓▓  ▓▓       ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ ▓▓      ▓▓  ▓▓  ▓▓      ▓▓   ▓▓      ▓▓
███████  ██████  ███████ ██ ██   ██ ███████ ██   ██ ██   ██ ██   ██  ██████ ██   ██ ███████ ██   ██ ███████
Version 4.0 ''',
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
Version 4.0 ''']



ban_ip = ['''
 BBBB              k        III PPPP 
 B   B             k k       I  P   P
 BBBB  rrr eee  aa kk        I  PPPP 
 B   B r   e e a a k k       I  P    
 BBBB  r   ee  aaa k  k     III P
''', '''
 ______   _______    _________      __      ___  ____               _____ ______
|_   _ \ |_   __ \  |_   ___  |    /  \    |_  ||_  _|             |_   _|_   __ \ 
  | |_) |  | |__) |   | |_  \_|   / /\ \     | |_/ /                 | |   | |__) |
  |  __/.  |  __ /    |  _|  _   / ____ \    |  __'.                 | |   |  ___/ 
 _| |__) |_| |  \ \_ _| |___/ |_/ /    \ \_ _| |  \ \_    ______    _| |_ _| |_    
|_______/|____| |___|_________|____|  |____|____||____|  |______|  |_____|_____|
''', '''
                                                               
▀███▀▀▀██▄                       ▀███          ▀████▀███▀▀▀██▄ 
  ██    ██                         ██            ██   ██   ▀██▄
  ██    █████▄███  ▄▄█▀██ ▄█▀██▄   ██  ▄██▀      ██   ██   ▄██ 
  ██▀▀▀█▄▄ ██▀ ▀▀ ▄█▀   ███   ██   ██ ▄█         ██   ███████  
  █▓    ▀█ █▓     ▓█▀▀▀▀▀▀▄███▓█   ▓█▄██         █▓   ██       
  ▓▓    ▄█ █▓     ▓█▄    ▄▓   ▓█   ▓█ ▀██▄       █▓   █▓       
  ▓▒    ▀▓ ▓▓     ▓▓▀▀▀▀▀▀▓▓▓▓▒▓   ▓▓▓▓▓         ▓▓   █▓       
  ▓▒    ▓▓ ▓▒     ▒▓▓    ▓▓   ▒▓   ▒▓ ▀▓▓▓       ▒▓   ▓▓       
▒ ▓▒ ▒ ▒ ▒ ▒▒▒     ▒ ▒ ▒▒▒▓▒ ▒ ▓▒▒ ▒ ▒  ▒ ▒    ▒▓▒ ▒▒▓▒▓▒ 
''']


ban_num = ['''
 BBBB              k                       
 B   B             k k                     
 BBBB  rrr eee  aa kk       nnn  u  u mmmm 
 B   B r   e e a a k k      n  n u  u m m m
 BBBB  r   ee  aaa k  k     n  n  uuu m m m
                                           
''', '''
 ______   _________      __      ___  ____               ____  _____ _____  _____ ____    ____ 
|_   _ \ |_   ___  |    /  \    |_  ||_  _|             |_   \|_   _|_   _||_   _|_   \  /   _|
  | |_) |  | |_  \_|   / /\ \     | |_/ /                 |   \ | |   | |    | |   |   \/   |  
  |  __/.  |  _|  _   / ____ \    |  __'.                 | |\ \| |   | '    ' |   | |\  /| |  
 _| |__) |_| |___/ |_/ /    \ \_ _| |  \ \_    ______    _| |_\   |_   \ \--' /   _| |_\/_| |_ 
|_______/|_________|____|  |____|____||____|  |______|  |_____|\____|   \.__.'   |_____||_____|
''', '''
                                                                               
▀███▀▀▀██▄               ▀███                                                  
  ██    ██                 ██                                                  
  ██    ██ ▄▄█▀██ ▄█▀██▄   ██  ▄██▀    ▀████████▄ ▀███  ▀███ ▀████████▄█████▄  
  ██▀▀▀█▄▄▄█▀   ███   ██   ██ ▄█         ██    ██   ██    ██   ██    ██    ██  
  █▓    ▀█▓█▀▀▀▀▀▀▄███▓█   ▓█▄██         █▓    ██   ▓█    ██   ▓█    ██    ██  
  ▓▓    ▄█▓█▄    ▄▓   ▓█   ▓█ ▀██▄       █▓    ▓█   ▓█    █▓   ▓█    ▓█    ██  
  ▓▒    ▀▓▓▓▀▀▀▀▀▀▓▓▓▓▒▓   ▓▓▓▓▓         ▓▓    ▓▓   ▓█    ▓▓   ▓▓    ▓▓    ▓▓  
  ▓▒    ▓▓▒▓▓    ▓▓   ▒▓   ▒▓ ▀▓▓▓       ▓▓    ▓▓   ▓▓    ▓▓   ▒▓    ▒▓    ▓▓  
▒ ▓▒ ▒ ▒ ▒ ▒ ▒ ▒▒▒▓▒ ▒ ▓▒▒ ▒ ▒  ▒ ▒    ▒ ▒▒▒  ▒▓▒ ▒ ▒▒ ▓▒ ▒▓▒▒ ▒▓▒  ▒▒▒   ▒▒▓▒
''']


ban_mac = ['''
 BBBB              k        M   M AA   CCC
 B   B             k k      MM MMA  A C   
 BBBB  rrr eee  aa kk       M M MAAAA C   
 B   B r   e e a a k k      M   MA  A C   
 BBBB  r   ee  aaa k  k     M   MA  A  CCC                                       
''', '''
 ______   _______    _________      __      ___  ____               ____    ____      __        ______ 
|_   _ \ |_   __ \  |_   ___  |    /  \    |_  ||_  _|             |_   \  /   _|    /  \     ./ ___  |
  | |_) |  | |__) |   | |_  \_|   / /\ \     | |_/ /                 |   \/   |     / /\ \   / ./   \_|
  |  __/.  |  __ /    |  _|  _   / ____ \    |  __'.                 | |\  /| |    / ____ \  | |       
 _| |__) |_| |  \ \_ _| |___/ |_/ /    \ \_ _| |  \ \_    ______    _| |_\/_| |_ _/ /    \ \_\ \.___.'\
|_______/|____| |___|_________|____|  |____|____||____|  |______|  |_____||_____|____|  |____|\._____.'
''', '''
                                                                                      
▀███▀▀▀██▄                       ▀███          ▀████▄     ▄███▀     ██       ▄▄█▀▀▀█▄█
  ██    ██                         ██            ████    ████      ▄██▄    ▄██▀     ▀█
  ██    █████▄███  ▄▄█▀██ ▄█▀██▄   ██  ▄██▀      █ ██   ▄█ ██     ▄█▀██▓   ██▀       ▀
  ██▀▀▀█▄▄ ██▀ ▀▀ ▄█▀   ███   ██   ██ ▄█         █  █▓  █▀ ██    ▄█  ▀██   ██         
  █▓    ▀█ █▓     ▓█▀▀▀▀▀▀▄███▓█   ▓█▄██         ▓  █▓▄█▀  ██    ███▓█▓██  █▓▄        
  ▓▓    ▄█ █▓     ▓█▄    ▄▓   ▓█   ▓█ ▀██▄       ▓  ▀▓█▀   ██   ▓▀      ██ ▀▓█▄     ▄▀
  ▓▒    ▀▓ ▓▓     ▓▓▀▀▀▀▀▀▓▓▓▓▒▓   ▓▓▓▓▓         ▓  ▓▓▓▓▀  ▓▓    ▓▓▓▓█▓▓█  ▓▓▓        
  ▓▒    ▓▓ ▓▒     ▒▓▓    ▓▓   ▒▓   ▒▓ ▀▓▓▓       ▒  ▀▓▓▀   ▓▓   ▓▀      ▓▓ ▒▓▓▒     ▓▀
▒ ▓▒ ▒ ▒ ▒ ▒▒▒     ▒ ▒ ▒▒▒▓▒ ▒ ▓▒▒ ▒ ▒  ▒ ▒    ▒ ▒▒▒ ▒   ▒ ▒▒▒▒ ▒ ▒   ▒ ▒▒▒  ▒ ▒ ▒ ▒▓                                                                              
''']

ban_num_car = ['''
 BBBB              k                                        
 B   B             k k                                      
 BBBB  rrr eee  aa kk       nnn  u  u mmmm       ccc  aa rrr
 B   B r   e e a a k k      n  n u  u m m m     c    a a r  
 BBBB  r   ee  aaa k  k     n  n  uuu m m m      ccc aaa r  
''', '''
______   _______    _________      __      ___  ____               ____  _____ _____  _____ ____    ____                ______      __      _______    
|_   _ \ |_   __ \  |_   ___  |    /  \    |_  ||_  _|             |_   \|_   _|_   _||_   _|_   \  /   _|             ./ ___  |    /  \    |_   __ \   
  | |_) |  | |__) |   | |_  \_|   / /\ \     | |_/ /                 |   \ | |   | |    | |   |   \/   |              / ./   \_|   / /\ \     | |__) |  
  |  __/.  |  __ /    |  _|  _   / ____ \    |  __'.                 | |\ \| |   | '    ' |   | |\  /| |              | |         / ____ \    |  __ /   
 _| |__) |_| |  \ \_ _| |___/ |_/ /    \ \_ _| |  \ \_    ______    _| |_\   |_   \ \--' /   _| |_\/_| |_    ______   \ \.___.'\_/ /    \ \_ _| |  \ \_ 
|_______/|____| |___|_________|____|  |____|____||____|  |______|  |_____|\____|   \.__.'   |_____||_____|  |______|   \._____.'____|  |____|____| |___|
''', '''
                                                                                                                  
▀███▀▀▀██▄                       ▀███                                                                             
  ██    ██                         ██                                                                             
  ██    █████▄███  ▄▄█▀██ ▄█▀██▄   ██  ▄██▀    ▀████████▄ ▀███  ▀███ ▀████████▄█████▄      ▄██▀██ ▄█▀██▄ ▀███▄███ 
  ██▀▀▀█▄▄ ██▀ ▀▀ ▄█▀   ███   ██   ██ ▄█         ██    ██   ██    ██   ██    ██    ██     ██▀  ████   ██   ██▀ ▀▀ 
  █▓    ▀█ █▓     ▓█▀▀▀▀▀▀▄███▓█   ▓█▄██         █▓    ██   ▓█    ██   ▓█    ██    ██     █▓      ▄███▓█   █▓     
  ▓▓    ▄█ █▓     ▓█▄    ▄▓   ▓█   ▓█ ▀██▄       █▓    ▓█   ▓█    █▓   ▓█    ▓█    ██     █▓▄    ▄▓   ▓█   █▓     
  ▓▒    ▀▓ ▓▓     ▓▓▀▀▀▀▀▀▓▓▓▓▒▓   ▓▓▓▓▓         ▓▓    ▓▓   ▓█    ▓▓   ▓▓    ▓▓    ▓▓     ▓▓      ▓▓▓▓▒▓   ▓▓     
  ▓▒    ▓▓ ▓▒     ▒▓▓    ▓▓   ▒▓   ▒▓ ▀▓▓▓       ▓▓    ▓▓   ▓▓    ▓▓   ▒▓    ▒▓    ▓▓     ▓▒▓    ▓▓   ▒▓   ▓▒     
▒ ▓▒ ▒ ▒ ▒ ▒▒▒     ▒ ▒ ▒▒▒▓▒ ▒ ▓▒▒ ▒ ▒  ▒ ▒    ▒ ▒▒▒  ▒▓▒ ▒ ▒▒ ▓▒ ▒▓▒▒ ▒▓▒  ▒▒▒   ▒▒▓▒     ▒ ▒ ▒ ▒▓▒ ▒ ▓▒▒ ▒▒▒ 
''']

ban_dos = ['''
 DDD              W     W    FFFF   
 D  D             W     W ii F    ii
 D  D ooo  ss     W  W  W    FFF    
 D  D o o  s       W W W  ii F    ii
 DDD  ooo ss        W W   ii F    ii
''', '''
 ________     ____    _______              _____  _____ _____ _________ _____ 
|_   ___ \. .'    \. /  ___  |            |_   _||_   _|_   _|_   ___  |_   _|
  | |   \. \  .--.  \  (__ \_|              | | /\ | |   | |   | |_  \_| | |  
  | |    | | |    | |'.___\-.               | |/  \| |   | |   |  _|     | |  
 _| |___.' /  \--'  /\\____) |   ______     |   /\   |  _| |_ _| |_     _| |_ 
|________.' \.____.'|_______.'  |______|    |__/  \__| |_____|_____|   |_____|
''', '''
                                                      ▄▄            ▄▄  
▀███▀▀▀██▄                     ▀████▀     █     ▀███▀ ██ ▀███▀▀▀███ ██  
  ██    ▀██▄                     ▀██     ▄██     ▄█        ██    ▀█     
  ██     ▀██ ▄██▀██▄ ▄██▀███      ██▄   ▄███▄   ▄█  ▀███   ██   █ ▀███  
  ██      ████▀   ▀████   ▀▀       ██▄  █▀ ██▄  █▀    ██   ██▀▀██   ██  
  █▓     ▄████     ██▀█████▄       ▓██ █▀  ▀██ █▀     ▓█   ▓█   █   ▓█  
  █▓    ▄█▓▀██     ▓█     ██        ▓██▄    ▓██▄      ▓█   ▓█       ▓█  
  ▓▓     ▓▓▓▓█     ▓▓▀▓   █▓        ▓▓█▓▀   ▓▓█▓▀     ▓▓   ▓▓       ▓▓  
  ▓▒    ▓▓▒▀▓▓▓   ▓▓▓▓▓   ▓▓        ▓▓▓▓    ▓▓▓▓      ▓▓   ▒▓       ▓▓  
▒ ▒ ▒ ▒ ▒    ▒ ▒ ▒ ▒ ▒ ▒▓▒           ▒       ▒      ▒ ▒ ▒▒▓▒ ▒    ▒ ▒ ▒
''']

ban_search = ['''
  SSS               h        N   N         k   
 S                  h        NN  N ii      k k 
  SSS  eee  aa  ccc hhh      N N N     ccc kk  
     S e e a a c    h  h     N  NN ii c    k k 
 SSSS  ee  aaa  ccc h  h     N   N ii  ccc k  k
''', '''
  _______ _________      __        ______ ____  ____              ____  _____ _____   ______ ___  ____  
 /  ___  |_   ___  |    /  \     ./ ___  |_   ||   _|            |_   \|_   _|_   _|./ ___  |_  ||_  _| 
|  (__ \_| | |_  \_|   / /\ \   / ./   \_| | |__| |                |   \ | |   | | / ./   \_| | |_/ /   
 '.___\-.  |  _|  _   / ____ \  | |        |  __  |                | |\ \| |   | | | |        |  __'.   
|\\____) |_| |___/ |_/ /    \ \_\ \.___.'\_| |  | |_    ______    _| |_\   |_ _| |_\ \.___.'\_| |  \ \_ 
|_______.'_________|____|  |____|\._____.'____||____|  |______|  |_____|\____|_____|\._____.'____||____|
''', '''
                                ▄▄                         ▄▄                   
 ▄█▀▀▀█▄█                      ███           ▀███▄   ▀███▀ ██        ▀███       
▄██    ▀█                       ██             ███▄    █               ██       
▀███▄     ▄▄█▀██ ▄█▀██▄  ▄██▀██ ███████▄       █ ███   █ ▀███  ▄██▀██  ██  ▄██▀ 
  ▀█████▄▄█▀   ███   ██ ██▀  ██ ██    ██       █  ▀██▄ █   ██ ██▀  ██  ██ ▄█    
      ▀██▓█▀▀▀▀▀▀▄███▓█ █▓      ██    █▓       █   ▀██▄▓   ▓█ █▓       ▓█▄██    
██     ██▓█▄    ▄▓   ▓█ █▓▄    ▄█▓    █▓       ▓     ▓█▓   ▓█ █▓▄    ▄ ▓█ ▀██▄  
▓     ▀█▓▓▓▀▀▀▀▀▀▓▓▓▓▒▓ ▓▓      ▓▓    ▓▓       ▓   ▀▓▓▓▓   ▓▓ ▓▓       ▓▓▓▓▓    
▓▓     ▓▓▒▓▓    ▓▓   ▒▓ ▓▒▓    ▓▓▒    ▓▒       ▓     ▓▓▓   ▓▓ ▓▒▓    ▓ ▒▓ ▀▓▓▓  
▒▓▒ ▒ ▒▓  ▒ ▒ ▒▒▒▓▒ ▒ ▓▒ ▒ ▒ ▒ ▒ ▒   ▒ ▒ ▒   ▒ ▒ ▒    ▒▓▓▒ ▒ ▒ ▒ ▒ ▒ ▒ ▒ ▒  ▒ ▒ 
''']

ban_bomb = ['''
  SSS                BBBB            b   
 S                   B   B           b   
  SSS  mmmm   ss     BBBB  ooo mmmm  bbb 
     S m m m  s      B   B o o m m m b  b
 SSSS  m m m ss      BBBB  ooo m m m bbb 
''', '''
  _______ ____    ____  _______              ______     ____   ____    ____ ______   
 /  ___  |_   \  /   _|/  ___  |            |_   _ \  .'    \.|_   \  /   _|_   _ \  
|  (__ \_| |   \/   | |  (__ \_|   ______     | |_) |/  .--.  \ |   \/   |   | |_) | 
 '.___\-.  | |\  /| |  '.___\-.   |______|    |  __/.| |    | | | |\  /| |   |  __/. 
|\\____) |_| |_\/_| |_|\\____) |             _| |__) |  \--'  /_| |_\/_| |_ _| |__) |
|_______.'_____||_____|_______.'            |_______/ \.____.'|_____||_____|_______/ 
''', '''
                                                                            ▄▄        
 ▄█▀▀▀█▄█                              ▀███▀▀▀██▄                          ▄██        
▄██    ▀█                                ██    ██                           ██        
▀███▄   ▀████████▄█████▄  ▄██▀███        ██    ██ ▄██▀██▄▀████████▄█████▄   ██▄████▄  
  ▀█████▄ ██    ██    ██  ██   ▀▀        ██▀▀▀█▄▄██▀   ▀██ ██    ██    ██   ██    ▀██ 
      ▀██ ▓█    ██    ██  ▀█████▄ █████  █▓    ▀███     ██ ▓█    ██    ██   ▓█     ██ 
██     ██ ▓█    ▓█    ██       ██        ▓▓    ▄███     ▓█ ▓█    ▓█    ██   ▓▓▓   ▄█▓ 
▓     ▀█▓ ▓▓    ▓▓    ▓▓  ▀▓   █▓        ▓▒    ▀▓▓█     ▓▓ ▓▓    ▓▓    ▓▓   ▓▓     ▓▓ 
▓▓     ▓▓ ▒▓    ▒▓    ▓▓  ▓▓   ▓▓        ▓▒    ▓▓▓▓▓   ▓▓▓ ▒▓    ▒▓    ▓▓   ▒▓▓   ▓▓▓ 
▒▓▒ ▒ ▒▓▒ ▒▓▒  ▒▒▒   ▒▒▓▒ ▒ ▒▓▒        ▒ ▓▒ ▒ ▒ ▒ ▒ ▒ ▒ ▒▒ ▒▓▒  ▒▒▒   ▒▒▓▒  ▒ ▒ ▒ ▒▒ 
''']

fishing = ['''
FFFF        h               
F    ii     h    ii       g 
FFF      ss hhh     nnn  g g
F    ii  s  h  h ii n  n ggg
F    ii ss  h  h ii n  n   g
                         ggg
''', '''
           ▄▄         ▄▄         ▄▄                     
▀███▀▀▀███ ██        ███         ██                     
  ██    ▀█            ██                                
  ██   █ ▀███  ▄██▀██████████▄ ▀███ ▀████████▄  ▄█▀█████
  ██▀▀██   ██  ██   ▀▀██    ██   ██   ██    ██ ▄██  ██  
  ▓█   █   ▓█  ▀█████▄██    █▓   ▓█   █▓    ██ ▀▓▓███▀  
  ▓█       ▓█       ███▓    █▓   ▓█   █▓    ▓█ █▓       
  ▓▓       ▓▓  ▀▓   █▓▓▓    ▓▓   ▓▓   ▓▓    ▓▓ ▀▓▓▓▓▓▀  
  ▒▓       ▓▓  ▓▓   ▓▓▓▒    ▓▒   ▓▓   ▓▓    ▓▓ ▓▒       
▒▓▒ ▒    ▒ ▒ ▒ ▒ ▒▓▒ ▒ ▒   ▒ ▒ ▒ ▒ ▒▒ ▒▒▒  ▒▓▒ ▒▒ ▒▓▒ ▒ 
                                               ▒▒     ▒▒
                                               ▒▒▒▒ ▒▒ 
''', '''
 _________ _____  _______ ____  ____ _____ ____  _____   ______   
|_   ___  |_   _|/  ___  |_   ||   _|_   _|_   \|_   _|.' ___  |  
  | |_  \_| | | |  (__ \_| | |__| |   | |   |   \ | | / .'   \_|  
  |  _|     | |  '.___\-.  |  __  |   | |   | |\ \| | | |    ____ 
 _| |_     _| |_|\\____) |_| |  | |_ _| |_ _| |_\   |_\ \.___]  _|
|_____|   |_____|_______.'____||____|_____|_____|\____|\._____.'
''']
def main():
    def started_ban():
        print(random.choice(banners))

    def started_code():
        print(f"S"),sleep(0.5),print(f" O"),sleep(0.5),print(f"  S"),sleep(0.5),print(f"   1"),sleep(0.5),print(f"    S"),sleep(0.5),print(f"     K"),sleep(0.5),print(f"      A"),sleep(2)

    def ban_break_ip():
        print(random.choice(ban_ip))
        FWT.write(f'{user_usr}:Token "ban_break_ip" of "banners" - ' + str(date_write) + '\n')
        FWT.close()

    def ban_break_num():
        print(random.choice(ban_num))
        FWT.write(f'{user_usr}:Token "ban_break_num" of "banners" - ' + str(date_write) + '\n')
        FWT.close()

    def ban_break_num_car():
        print(random.choice(ban_num_car))
        FWT.write(f'{user_usr}:Token "ban_break_num_car" of "banners" - ' + str(date_write) + '\n')
        FWT.close()

    def ban_break_mac():
        print(random.choice(ban_mac))
        FWT.write(f'{user_usr}:Token "ban_break_mac" of "banners" - ' + str(date_write) + '\n')
        FWT.close()

    def ban_search_nick():
        print(random.choice(ban_search))
        FWT.write(f'{user_usr}:Token "ban_search_nick" of "banners" - ' + str(date_write) + '\n')
        FWT.close()

    def ban_sms_bomb():
        print(random.choice(ban_bomb))
        FWT.write(f'{user_usr}:Token "ban_sms_bomb" of "banners" - ' + str(date_write) + '\n')
        FWT.close()

    def ban_dos_wifi():
        print(random.choice(ban_dos))
        FWT.write(f'{user_usr}:Token "ban_dos_wifi" of "banners" - ' + str(date_write) + '\n')
        FWT.close()

    def ban_fishing():
        print(random.choice(fishing))
        FWT.write(f'{user_usr}:Token "ban_fishing" of "banners" - ' + str(date_write) + '\n')
        FWT.close()
    def test_ban(test):
      global cl
