apt update && apt upgrade
pkg install python3 -y
pip install --upgrade pip
pip install colorama
pip install requests
pip install urllib3
pkg install git -y
mdkir /data/data/com.termux/files/Sos1ska
git clone https://github.com/Sos1ska/Spider-Breaking.git
mv ~/Spider-Breaking/Termux /data/data/com.termux/files/Sos1ska/.Termux
chmod -R 777 /data/data/com.termux/files/Sos1ska/.Termux
rm -rf ~/Spider-Breaking
cd $PREFIX/bin && ln -s /data/data/com.termux/files/Sos1ska/.Termux/Spider-Breaking.py spider
clear
echo 'spider - Запуск кода'
