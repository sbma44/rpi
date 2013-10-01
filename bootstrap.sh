# baseline update / tools
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install vim screen libnss-mdns watchdog chkconfig

# ssh key
mkdir ~/.ssh
curl https://raw.github.com/sbma44/rpi/master/tom_lee_dsa_key.pub >> ~/.ssh/authorized_keys

# python / git
sudo apt-get -y install python-setuptools python-dev git 
sudo easy_install pip

pip install pycrypto

# virtualenv
sudo pip install virtualenvwrapper wiringpi wiringpi2
mkdir ~/Devel
mkdir ~/.virtualenvs
curl https://raw.github.com/sbma44/rpi/master/rpi_virtualenvconfig.txt >> ~/.bashrc
source ~/.bashrc

# wifi & preferred networks
sudo python setup_wireless.py

# email
sudo postfix.sh

# remove swapfile for SD card longevity
sudo swapoff --all
sudo apt-get -y remove dphys-swapfile

# TODO: more improvements from http://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card


