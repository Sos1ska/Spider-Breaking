#!/data/data/com.termux/files/usr/bin/python3
import datetime
import json
import time
import os

from files.main import start_main
from files.test import read_test_log, start_test
from files.RecordConfig.record import read_start_license, no_read_license
from files.wrn.warn import keyboard, file_not_found_log, file_not_found_test
from files.chech_inet import check_inet

date_write = datetime.datetime.now()

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_name_usr").get("root_input_usr")

def cl():
    os.system("clear")

try:
    try:
        FWS = open('files/log/log.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        file_not_found_log()
    FWS.write(f'{root_usr}:StartCode "Spider-Breaking" - ' + str(date_write) + '\n')
    FWS.close()
    cl()
    check_inet()
    time.sleep(3)
    cl()
    start_test()
    read_test_log()
    cl()
    start_main()
except KeyboardInterrupt:
    keyboard()
