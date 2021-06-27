import datetime
import os
import json

def cl():
    os.system("cls")

def main():
    global cl
    def create_and_write_config(start_create_and_write_config):
        try:
            CFC = open('Spider-Breaking\Windows\\files\config\config.json', 'r', encoding='utf-8')
        except FileNotFoundError:
            CFC = open('Spider-Breaking\Windows\\files\config\config.json', 'w', encoding='utf-8')
            import getpass
            user_name = getpass.getuser()
            CFC.write('{\n')
            CFC.write('\t"user_name_usr":{\n')
            CFC.write(f'\t\t"user_input_usr":"{str(user_name)}"\n')
            CFC.write('\t},\n')
            CFC.write('\t"user_menu":{\n')
            CFC.write(f'\t\t"user_menu_usr":"{str(user_name)}@Sos1ska"\n')
            CFC.write('\t}\n')
            CFC.write('}')
            CFC.close()
    def test_ccf(test_ccf):
        global cl
        print()
        cl()
    return test_ccf

def test_ccf():
    my_test = main.test_ccf(test_ccf)

def start_create_and_write_config():
    go_ccf = main.create_and_write_config(start_create_and_write_config)
    go_ccf
