pkg install python
pkg install dos2unix
cp ~/Spider-Breaking1.0/Spider-Breaking/Spider-Breaking.py $PREFIX/bin/Breaking
cp ~/Spider-Breaking1.0/Spider-Breaking/collector.txt &PREFIX/bin/Informant
dos2unix $PREFIX/bin/Breaking
chmod -R 777 ~/Breaking
chmod 777 $PREFIX/bin/Breaking
dos2unix &PREFIX/bin/Informant
chmod -R 777 ~/Informant
chmod 777 &PREFIX/bin/Informant
Breaking
