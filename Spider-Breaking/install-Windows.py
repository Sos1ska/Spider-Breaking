import os

os.system("cls")

os.system("pip3 install --upgrade pip")
os.system("cls")
mod = ["html2text", "requests", "bs4", "vk_api", "urllib3"]
for i in range(len(mod)):
    os.system("pip3 install "+mod[i])