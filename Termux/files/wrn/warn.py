import datetime
import json
import os
import time

date_write = datetime.datetime.now()

def cl():
    os.system("clear")

def test_warn():
    global cl
    print()
    cl()

with open('files/config/config.json') as f:
    root_data = json.load(f)
root_usr = root_data.get("root_name_usr").get("root_input_usr")

def keyboard():
    global cl
    try:
        FWW = open('files/log/log.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        try:
            FWE1 = open('files/error.txt', 'a', encoding='utf-8')
            FWE1.write(f'{root_usr}:Error "FileNotFoundError - log.txt" - ' + str(date_write) + '\n')
            FWE1.close()
            cl()
            print('Сохранено по пути files/error.txt')
            quit()
        except FileNotFoundError:
            FWE2 = open('files/error.txt', 'w', encoding='utf-8')
            FWE2.write(f'{root_usr}:Error "FileNotFoundError - log.txt" - ' + str(date_write) + '\n')
            FWE2.close()
            cl()
            print('Сохранено по пути files/error.txt')
    FWW.write(f'{root_usr}:Warning "KeyboardInterrupt" - ' + str(date_write) + '\n')
    FWW.close()
    cl()
    print('Сохранено по пути files/log/log.txt')
    quit()

def file_not_found_log():
    global cl
    try:
        FWE = open('files/log/log.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        try:
            FWE1 = open('Spider-Breaking\Termux-new\error.txt', 'a', encoding='utf-8')
            FWE1.write(f'{root_usr}:Error "FileNotFoundError - log.txt" - ' + str(date_write) + '\n')
            FWE1.close()
            cl()
            print('Сохранено по пути Spider-Breaking/Termux/error.txt')
            quit()
        except FileNotFoundError:
            FWE2 = open('files/error.txt', 'w', encoding='utf-8')
            FWE.write(f'{root_usr}:Error "FileNotFoundError - log.txt" - ' + str(date_write) + '\n')
            FWE2.close()
            cl()
            print('Сохранено по пути files/error.txt')
            quit()
    FWE.write(f'{root_usr}:Error "FileNotFound" - ' + str(date_write) + '\n')
    FWE.close()
    cl()
    print('Сохранено по пути Spider-Breaking/Termux/files/log/log.txt')
    quit()

def i_e_colo():
    global cl
    FWE = open('files/log/log.txt', 'a', encoding='utf-8')
    FWE.write(f'{root_usr}:Error "ImportError - Colorama" - ' + str(date_write) + '\n')
    FWE.close()
    cl()
    print('Сохранено по пути Spider-Breaking/Termux/files/log/log.txt')
    quit()

def i_e_url_requ():
    global cl
    FWE = open('files/log/log.txt', 'a', encoding='utf-8')
    FWE.write(f'{root_usr}:Error "ImportError - Requests" - ' + str(date_write) + '\n')
    FWE.close()
    cl()
    print('Сохранено по пути Spider-Breaking/Termux/files/log/log.txt')
    quit()

def i_e_url3():
    global cl
    FWE = open('files/log/log.txt', 'a', encoding='utf-8')
    FWE.write(f'{root_usr}:Error "ImportError - Urllib3" - ' + str(date_write) + '\n')
    FWE.close()
    cl()
    print('Сохранено по пути Spider-Breaking/Termux/files/log/log.txt')
    quit()

def file_not_found_test():
    global cl
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
    print('Сохранено по пути Spider-Breaking/Termux/files/log/log.txt')
    quit()
