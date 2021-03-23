#!/usr/bin/bash

clear
echo
echo ".-------------------------------------------."
echo "|                 Кто ты?                   |"
echo "| _________________________________________ |"
echo "|                                           |"
echo "| 1 - Termux                                |"
echo "| 2 - Другая UNIX система                   |"
echo "| 3 - iSH                                   |"
echo "|                                           |"
echo "'-------------------------------------------'"
echo
read numb
if [ $numb = "1" ]
then
    pkg install python3 -y
    pip3 install requests urllib3 colorama
    pkg install dos2unix -y
    pkg install curl -y
    pkg install wget -y
    rm -rf /data/data/com.termux/files/usr/bin/spider-new && rm -rf /data/data/com.termux/files/usr/bin/spider
    mkdir ~/.spider
    cp ~/Spider-Breaking/Breaking3.0/Unix/spider-new.py ~/.spider
    chmod -R 777 ~/.spider
    rm -rf ~/Spider-Breaking
    cp ~/.spider/spider-new.py $PREFIX/bin/spider-new
    dos2unix $PREIFX/bin/spider-new
    clear
    echo "spider-new для вызова"
else
    if [ $numb = "2" ]
    then
        if [ "$(whoami)" != 'root' ];
		then
			echo "У вас нет прав. Запустите install.sh с root правами (sudo sh ~/Spider-Breaking2.0/Unix/install.sh)"
			exit
        else
            apt install python3
            pip3 install requests urllib3 colorama
            apt install dos2unix
            apt install curl
            apt install wget
            rm -rf /data/data/com.termux/files/usr/bin/spider-new && rm -rf /data/data/com.termux/files/usr/bin/spider
            mkdir ~/.spider
            cp ~/Spider-Breaking/Breaking3.0/Unix/spider-new.py ~/.spider
            chmod -R 777 ~/.spider
            rm -rf ~/Spider-Breaking
            cp ~/.spider/spider-new.py $PREFIX/bin/spider-new
            dos2unix $PREIFX/bin/spider-new
            clear
            echo "spider_new для вызова"
        fi
    else
        if [ $numb = "3" ]
        then
            apk add python3
            pip3 install requests urllib3 colorama
            rm -rf /data/data/com.termux/files/usr/bin/spider-new && rm -rf /data/data/com.termux/files/usr/bin/spider
            mkdir ~/.spider
            cp ~/Spider-Breaking/Breaking3.0/Unix/spider-new.py ~/.spider
            chmod -R 777 ~/.spider
            rm -rf ~/Spider-Breaking
            cp ~/.spider/spider-new.py $PREFIX/bin/spider-new
            dos2unix $PREIFX/bin/spider-new
            clear
            echo "spider_new для вызова"
        else
            echo "Некорретный ввод"
        fi
    fi
fi