cd /tmp
wget https://github.com/aeberhardo/phantomjs-linux-armv6l/archive/master.zip
unzip master.zip
cd phantomjs-linux-armv6l-master
bunzip2 *.bz2 && tar xf *.tar
mv ./phantomjs-1.9.0-linux-armv6l/bin/phantomjs /usr/bin/
rm -rf /tmp/phantomjs*
rm -rf /tmp/master.zip

cd /usr/share
sudo mv fonts fonts.bak
sudo mkdir fonts

sudo apt-get install -y --reinstall ttf-mscorefonts-installer

sudo rm /usr/share/fonts/truetype/msttcorefonts/andalemo.ttf
sudo rm /usr/share/fonts/truetype/msttcorefonts/Andale_Mono.ttf

sudo fc-cache -rv
