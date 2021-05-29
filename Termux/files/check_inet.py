#!/data/data/com.termux/files/usr/bin/python3
import datetime, os

from files.wrn.warn import i_e_url_requ

try:
    import requests
except ImportError:
    i_e_url_requ()

def cl():
    os.system("clear")

def check_inet():
    try:
        response = requests.get("http://www.google.com")
        print()
        print("Интернет есть")
    except requests.ConnectionError:
        print()
        print("Интернета нету")
