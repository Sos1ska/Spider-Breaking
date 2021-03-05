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
    pkg install python -y
    clear
    pkg install dos2unix -y
    clear
    pip install requests urllib3 json
    clear
    cp ~/Spider-Breaking/Spider-Breaking/Unix/break.py $PREFIX/bin/spider
    dos2unix $PREFIX/bin/spider
    dos2unix $PREFIX/bin/information
    chmod -R 777 ~/Spider-Breaking
    chmod 777 $PREFIX/bin/spider
    echo "spider - Вызов кода"
else
    if [ $numb = "2" ]
    then
        if [ "$(whoami)" != 'root' ];
		then
			echo "У вас нет прав. Запустите install.sh с root правами (sudo sh ~/Spider-Breaking2.0/Unix/install.sh)"
			exit
        else
            apt install python3 python3-pip dos2unix
			pip3 install requests urllib3 json
            cp ~/Spider-Breaking2.0/Unix/break.py $PREFIX/bin/spider
            dos2unix $PREFIX/bin/spider
            chmod -R 777 ~/Spider-Breaking2.0
            chmod 777 $PREFIX/bin/spider
            echo "break - Вызов кода"
        fi
    else
        if [ $numb = "3" ]
        then
            apk add python
			apk add python3
			apk add dos2unix
			pip3 install requests
			pip3 install json
			pip3 install urllib3
            cp ~/Spider-Breaking2.0/Unix/break.py /usr/bin/spider
            dos2unix /usr/bin/spider
            chmod -R 777 ~/Spider-Breaking2.0
            chmod 777 /usr/bin/spider
			echo "break - Вызов кода"
        else
            echo "Некорректный ввод"
        fi
    fi
fi
