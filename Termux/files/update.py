#!/data/data/com.termux/files/usr/bin/python3
import json, os, time

from files.wrn.warn import i_e_url_requ

try:
    import requests, urllib
except ImportError:
    i_e_url_requ()

with open('files/config/config.json') as f:
    version_data = json.load(f)
version_usr = version_data.get("Verwion").get("Version")

def update():
    print('Начинаю проверку обновленя....')
    getcheckupdate = 'https://raw.githubusercontent.com/Sos1ska/Spider-Breaking/Sos1ska/Termux/files/config/config.json'
    try:
        checkupdate = urllib.request.urlopen( getcheckupdate )
    except:
        print('Проверьте интернет!')
        pass
    check = json.load(check)
    if version_usr == check:
        os.system('wget https://raw.githubusercontent.com/Sos1ska/Spider-Breaking/Sos1ska/install.sh')
        os.system("chmod 777 ~/Spider-Breaking/install.sh")
        os.system("sh ~/Spider-Breaking/install.sh")
    else:
        print('У вас установлена последняя версия кода')
        time.sleep(3)
