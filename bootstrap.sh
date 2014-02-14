HOME=/home/pi

# baseline update / tools
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install vim screen libnss-mdns supervisor

# ssh key
mkdir $HOME/.ssh
curl https://raw.github.com/sbma44/rpi/master/tom_lee_dsa_key.pub >> $HOME/.ssh/authorized_keys

# python / git
sudo apt-get -y install python-setuptools python-dev git 
sudo easy_install pip

# virtualenv
sudo pip install virtualenvwrapper wiringpi wiringpi2
mkdir $HOME/Devel
mkdir $HOME/.virtualenvs
curl https://raw.github.com/sbma44/rpi/master/rpi_virtualenvconfig.txt >> $HOME/.bashrc
source $HOME/.bashrc

# wifi & preferred networks
pip install pycrypto
sudo python setup_wireless.py

# email
sudo postfix.sh

# remove swapfile for SD card longevity
sudo swapoff --all
sudo apt-get -y remove dphys-swapfile

# watchdog
sudo python watchdog.py

# TODO: more improvements from http://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card