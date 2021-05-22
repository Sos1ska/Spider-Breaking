import os
import time
print("Обновление pip...")
os.system("pip install --upgrade pip")
os.system("clear")
print("              [Installer]\n")
mod = ["requests", "urllib3"]
print("Для работы этой версии шерлока, нужен доступ к хранилищу.")
print("Начало установки.")
for i in range(len(mod)):
    print("Установка "+mod[i]+"...")
    os.system("pip3 install "+mod[i])
print('Установка компонентов завершена')
time.sleep(5)