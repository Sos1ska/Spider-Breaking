import datetime
import win10toast
import getpass
import json
import os
import subprocess
from time import sleep

date_write = datetime

execute = subprocess.call

toaster = win10toast.ToastNotifier()

user_name = getpass.getuser()

try:
    with open("Spider-Breaking\Windows\\files\config\config.json") as f:
        notification_os = json.load(f)
    notification_type = notification_os.get("Setting notification").get("notification")
except FileNotFoundError:
    execute("csripts file_not_found_notification")

try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
    FWSC = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
    FWTC = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
    FWAS = open("Spider-Brekaing\Windows\\files\log\log.txt")
except FileNotFoundError:
    execute("csripts file_not_found_log_main.vbs")

FWS.write(f'{user_name}:StartCode "performer" - ' + str(date_write) + '\n')
FWS.close()

def cl():
    os.system("cls")

def main():
    global cl
    def new_notification():
        global cl
        def keyboard_not_new(keyboard_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "keyboard_main" - ' + str(date_write) + '\n')
                toaster.show_toast("Warning", "Keys were pressed 'CTRL+C")
                FWSC.write(f'{user_name}:Launched scripts "keyboard_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "keyboard_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "keyboard_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_log_nnew(file_not_found_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_log_main" - ' + str(date_write) + '\n')
                toaster.show_toast("Error", "File not found 'log.txt'")
                FWSC.write(f'{user_name}:Launched scripts "file_not_found_log_main" - ' + str(date_write) + '\n')
                FWAS.WRITE(f'{user_name}:Attempt to start scripts "file_not_found_log_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_log_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_notification_new(file_not_found_notification_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_notification_main" - ' + str(date_write) + '\n')
                toaster.show_toast("ImportError", "File not found 'notification.json")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_notification_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_notification_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_notification_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_test_log_new(file_not_found_test_log_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_test_log_main" - ' + str(date_write) + '\n')
                toaster.show_toast("Error", "File not found 'test_log.txt'")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_test_log_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_test_log_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_test_log_main" - False - ' + str(date_write) + '\n')
                quit()
        def i_e_colo_new(i_e_colo_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_colo_main" - ' + str(date_write) + '\n')
                toaster.show_toast("ImportError", "No module 'colorama'")
                FWSC.write(f'{user_name}:Lauched scripts "i_e_colo_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_colo_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_colo_main" - False - ' + str(date_write) + '\n')
                quit()
        def i_e_url_requ_new(i_e_url_requ_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url_requ_main" - ' + str(date_write) + '\n')
                toaster.show_toast("ImportError", "No module 'urllib/requests'")
                FWSC.write(f'{user_name}:Lauched scripts "i_e_url_requ_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url_requ_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url_requ_main" - False - ' + str(date_write) + '\n')
                quit()
        def i_e_url3_new(i_e_url3_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url3_main" - ' + str(date_write) + '\n')
                toaster.show_toast("ImportError", "No module 'urllib3'")
                FWSC.write(f'{user_name}:Lauched scripts "i_e_url3_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url3_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url3_main" - False - ' + str(date_write) + '\n')
                quit()
        def e_lang_new(e_lang_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "e_lang" - ' + str(date_write) + '\n')
                toaster.show_toast("Warning", "File not found 'language.json'")
                FWSC.write(f'{user_name}:Lauched scripts "e_lang" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "e_lang" - True - ' +  str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "e_lang" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_version_new(file_not_found_version_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_version_main" - ' + str(date_write) + '\n')
                toaster.show_toast("Error", "File not found 'version.json'")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_version_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_version_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_version_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_work_proxy_new(file_not_found_work_proxy_main_new):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_work_proxy_main" - ' + str(date_write) + '\n')
                toaster.show_toast("Error", "File not found 'work_proxy.json'")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_work_proxy_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_work_proxy_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt tp start scripts "file_not_found_work_proxy_main" - False - ' + str(date_write) + '\n')
                quit()

    def test_performer_main(test_performer_main):
        global cl
        print()
        cl()
    return test_performer_main

    def retro_notification():
        global cl
        def keyboard_not_ret(keyboard_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "keyboard_main" - ' + str(date_write) + '\n')
                execute("csripts keyboard_main.vbs")
                FWSC.write(f'{user_name}:Launched scripts "keyboard_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "keyboard_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "keyboard_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_log_ret(file_not_found_log_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_log_main" - ' + str(date_write) + '\n')
                execute("csripts file_not_found_log_main.vbs")
                FWSC.write(f'{user_name}:Launched scripts "file_not_found_log_main" - ' + str(date_write) + '\n')
                FWAS.WRITE(f'{user_name}:Attempt to start scripts "file_not_found_log_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_log_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_notification_ret(file_not_found_notification_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_notification_main" - ' + str(date_write) + '\n')
                execute("csripts file_not_found_notification_main.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_notification_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_notification_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_notification_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_test_log_ret(file_not_found_test_log_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_test_log_main" - ' + str(date_write) + '\n')
                execute("csripts file_not_found_test_log_main.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_test_log_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_test_log_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_test_log_main" - False - ' + str(date_write) + '\n')
                quit()
        def i_e_colo_ret(i_e_colo_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_colo_main" - ' + str(date_write) + '\n')
                execute("csripts i_e_colo_main.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "i_e_colo_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_colo_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_colo_main" - False - ' + str(date_write) + '\n')
                quit()
        def i_e_url_requ_ret(i_e_url_requ_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url_requ_main" - ' + str(date_write) + '\n')
                execute("csripts i_e_url_requ_main.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "i_e_url_requ_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url_requ_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url_requ_main" - False - ' + str(date_write) + '\n')
                quit()
        def i_e_url3_ret(i_e_url3_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url3_main" - ' + str(date_write) + '\n')
                execute("csripts i_e_url3_main.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "i_e_url3_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url3_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "i_e_url3_main" - False - ' + str(date_write) + '\n')
                quit()
        def e_lang_ret(e_lang_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "e_lang" - ' + str(date_write) + '\n')
                execute("csripts e_lang.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "e_lang" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "e_lang" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "e_lang" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_version_ret(file_not_found_version_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_version_main" - ' + str(date_write) + '\n')
                execute("csripts file_not_found_version_main.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_version_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_version_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_version_main" - False - ' + str(date_write) + '\n')
                quit()
        def file_not_found_work_proxy_ret(file_not_found_work_proxy_main_ret):
            try:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_work_proxy_main" - ' + str(date_write) + '\n')
                execute("csripts file_not_found_work_proxy_main.vbs")
                FWSC.write(f'{user_name}:Lauched scripts "file_not_found_work_proxy_main" - ' + str(date_write) + '\n')
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_work_proxy_main" - True - ' + str(date_write) + '\n')
            except:
                FWAS.write(f'{user_name}:Attempt to start scripts "file_not_found_work_prxoy_main" - False - ' + str(date_write) + '\n')
                quit()

def test_performer_main():
    my_test = main.test_performer_main(test_performer_main)
    FWTC.write(f'{user_name}:Launched as a check - ' + str(date_write) + '\n')
    my_test
    FWTC.close()

def keyboard_main_new():
    keyboardinterrupt = main.new_notification.keyboard_not_new(keyboard_main_new)
    keyboardinterrupt
def file_not_found_log_main_new():
    file_not_found_log = main.new_notification.file_not_found_log_nnew(file_not_found_log_main_new)
    file_not_found_log
def file_not_found_notification_main_new():
    file_not_found_notification = main.new_notification.file_not_found_notification_new(file_not_found_notification_main_new)
    file_not_found_notification
def file_not_found_test_log_main_new():
    file_not_found_test_log = main.new_notification.file_not_found_test_log_new(file_not_found_test_log_main_new)
    file_not_found_test_log
def i_e_colo_main_new():
    i_e_colo = main.new_notification.i_e_colo_new(i_e_colo_main_new)
    i_e_colo
def i_e_url_requ_main_new():
    i_e_url_requ = main.new_notification.i_e_url_requ_new(i_e_colo_main_new)
    i_e_url_requ
def i_e_url3_main_new():
    i_e_url3 = main.new_notification.i_e_url3_new(i_e_url3_main_new)
    i_e_url3
def e_lang_main_new():
    e_lang = main.new_notification.e_lang_new(e_lang_main_new)
    e_lang
def file_not_found_version_main_new():
    file_not_found_version = main.new_notification.file_not_found_version_new(file_not_found_version_main_new)
    file_not_found_version
def file_not_found_work_proxy_main_new():
    file_not_found_work_proxy = main.new_notification.file_not_found_work_proxy_new(file_not_found_work_proxy_main_new)
    file_not_found_work_proxy

def keyboard_main_ret():
    keyboardinterrupt = main.retro_notification.keyboard_not_ret(keyboard_main_ret)
    keyboardinterrupt
def file_not_found_log_main_ret():
    file_not_found_log = main.retro_notification.file_not_found_log_ret(file_not_found_log_main_ret)
    file_not_found_log
def file_not_found_notification_main_ret():
    file_not_found_notification = main.retro_notification.file_not_found_notification_ret(file_not_found_notification_main_ret)
    file_not_found_notification
def file_not_found_test_log_main_ret():
    file_not_found_test_log = main.retro_notification.file_not_found_test_log_ret(file_not_found_test_log_main_ret)
    file_not_found_test_log_main_ret
def i_e_colo_main_ret():
    i_e_colo = main.retro_notification.i_e_colo_ret(i_e_colo_main_ret)
    i_e_colo
def i_e_url_requ_main_ret():
    i_e_url_requ = main.retro_notification.i_e_url_requ_ret(i_e_url_requ_main_ret)
    i_e_url_requ
def i_e_url3_main_ret():
    i_e_url3 = main.retro_notification.i_e_url3_ret(i_e_url3_main_ret)
    i_e_url3
def e_lang_main_ret():
    e_lang = main.retro_notification.e_lang_ret(e_lang_main_ret)
    e_lang
def file_not_found_version_main_ret():
    file_not_found_version = main.retro_notification.file_not_found_version_ret(file_not_found_version_main_ret)
    file_not_found_version
def file_not_found_work_proxy_main_ret():
    file_not_found_work_proxy = main.retro_notification.file_not_found_work_proxy_ret(file_not_found_work_proxy_main_ret)
    file_not_found_work_proxy
