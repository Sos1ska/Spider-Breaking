import datetime
import json
import os

date_write = datetime.datetime.now()

from files.ban.banners import ban_search_nick
from files.credits.credits import credits
from files.wrn.warn import (file_not_found_log, i_e_colo, i_e_url3,
                            i_e_url_requ, keyboard)

try:
    from colorama import Back, Fore, Style
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

def cl():
    os.system("clear")

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_menu").get("root_menu_usr")


def search_nick():
    try:
        global cl
        try:
            try:
                FWI = open('files/log/log.txt', 'a', encoding='utf-8')
                FWS = open('files/log/log.txt', 'a', encoding='utf-8')
            except FileNotFoundError:
                file_not_found_log()
            cl()
            ban_search_nick()
            credits()
            FWS.write('{root_usr}:StartCode "search_nick" - ' + str(date_write) + '\n')
            FWS.close()
            print(Fore.YELLOW + 'Укажите ник' + Style.RESET_ALL)
            nick = input(Fore.GREEN + '/Sos/search_nick/>>> ' + Style.RESET_ALL)
            FWI.write(f'{root_usr}:IntroducedCode "search_nick" - {str(nick)} - ' + str(date_write) + '\n')
            FWI.close()
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
            cont_input = input(Fore.GREEN + 'Нажмите [ENTER] для продолжения: ' + Style.RESET_ALL)
    except KeyboardInterrupt:
        keyboard()

def test_nick():
    global cl
    print()
    cl()
