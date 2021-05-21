apt update && apt upgrade
pkg install python -y
pip install --upgrade pip
pip install requests
pip install colorama 
pip install urllib3
pkg install unzip -y
pkg install git -y
pkg upgrade -y
git clone https://github.com/Sos1ska/Spider-Breaking
unzip ~/Spider-Breaking/Termux.zip
rm -rf ~/Spider-Breaking/Termux.zip
cd ~/Spider-Breaking/ && chmod -R 777 Termux
clear
echo 'cd ~/Spider-Breaking/Termux && python spider-breaking.py or python ~/Spider-Breaking/Termux/spider-breaking'
rm -rf ~/Spider-Breaking/install.sh
