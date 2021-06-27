import datetime
import getpass
import json
import os

date_write = datetime.datetime.now()

user_name = getpass.getuser()

from files.scripts.performer import (e_lang_main_new, e_lang_main_ret,
                                     file_not_found_log_main_new,
                                     file_not_found_log_main_ret,
                                     file_not_found_notification_main_new,
                                     file_not_found_notification_main_ret,
                                     file_not_found_test_log_main_new,
                                     file_not_found_test_log_main_ret,
                                     file_not_found_version_main_new,
                                     file_not_found_version_main_ret,
                                     file_not_found_work_proxy_main_new,
                                     file_not_found_work_proxy_main_ret,
                                     i_e_colo_main_new, i_e_colo_main_ret,
                                     i_e_url3_main_new, i_e_url3_main_ret,
                                     i_e_url_requ_main_new,
                                     i_e_url_requ_main_ret, keyboard_main_new,
                                     keyboard_main_ret)
try:
    FWS = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
    FWSP = open("Spider-Breaking\Windows\\files\log\log.txt", "a", encoding="utf-8")
try:
    with open("Spider-Breaking\Windows\\files\config\\notification_config.json") as f:
        notification = json.load(f)
    notification_type = notification.get("Setting notification").get("notification")
except:
    cl()
    print("An error has occurred")

def cl():
    os.system("cls")

def else_warn():
    global cl
    cl()
    print("Could not determine type for notification")
    quit()

def main():
    global cl
    global else_warn
    def keyboard_warn(keyboard):
        global cl
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                keyboard_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                keyboard_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def e_lang_warn(e_lang):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                e_lang_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                e_lang_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def i_e_colo_warn(i_e_colo):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                i_e_colo_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                i_e_colo_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def i_e_url_requ_warn(i_e_url_requ):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                i_e_url_requ_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                i_e_url_requ_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def i_e_url3_warn(i_e_url3):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                i_e_url3_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                i_e_url3_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    
    def test_warn(test_warn):
        global cl
        print()
        cl()
    return test_warn
    
    def file_not_found_log_warn(file_not_found_log):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_log_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_log_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def file_not_found_test_log_warn(file_not_found_test_log):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_test_log_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_test_log_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def file_not_found_version_warn(file_not_found_version):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_version_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_version_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def file_not_found_work_proxy_warn(file_not_found_work_proxy):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_work_proxy_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_work_proxy_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()
    def file_not_found_notification_warn(file_not_found_notification):
        global cl
        global else_warn
        if str(notification_type) == "new":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_notification_main_new()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        elif str(notification_type) == "retro":
            FWS.write(f'{user_name}:StartCode "warn" - ' + str(date_write) + '\n')
            try:
                try:
                    FWSP.write(f'{user_name}:Making a code call "performer" - ' + str(date_write) + '\n')
                except:
                    FWSP.write(f'{user_name}:No response from the code "performer" - ' + str(date_write) + '\n')
                    quit()
                FWSP.write(f'{user_name}:Making a code call "performer" - True - ' + str(date_write) + '\n')
                file_not_found_notification_main_ret()
            except:
                FWSP.write(f'{user_name}:Making a code call "performer" - False - ' + str(date_write) + '\n')
                quit()
            FWS.close()
        else:
            else_warn()

def test_warn():
    my_test = main.test_warn(test_warn)
    FWS.write(f'{user_name}:Lauched as a check - ' + str(date_write) + '\n')
    my_test
    FWS.close()

def keyboard():
    keyboardd = main.keyboard_warn(keyboard)
    keyboardd
def i_e_colo():
    i_e_colod = main.i_e_colo_warn(i_e_colo)
    i_e_colod
def i_e_url_requ():
    i_e_url_requd = main.i_e_url_requ_warn(i_e_url_requ)
    i_e_url_requd
def i_e_url3():
    i_e_url3d = main.i_e_url3_warn(i_e_url3)
    i_e_url3d
def file_not_found_log():
    file_not_found_logg = main.file_not_found_log_warn(file_not_found_log)
    file_not_found_logg
def file_not_found_test_log():
    file_not_found_test_logg = main.file_not_found_test_log_warn(file_not_found_test_log)
    file_not_found_test_logg
def file_not_found_notification():
    file_not_found_notificationn = main.file_not_found_notification_warn(file_not_found_notification)
    file_not_found_notificationn
def file_not_found_version():
    file_not_found_versionn = main.file_not_found_version_warn(file_not_found_version)
    file_not_found_versionn
def file_not_found_work_proxy():
    file_not_found_work_proxyy = main.file_not_found_work_proxy_warn(file_not_found_work_proxy)
    file_not_found_work_proxyy
