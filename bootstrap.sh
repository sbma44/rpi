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
# NOTE: these lines require the use of @sbma44's private encryption key. which you (hopefully)
# don'e have. So instead just have a look at the sample wifi config files, okay?
#pip install pycrypto
#sudo python setup_wireless.py

# remove swapfile for SD card longevity
sudo swapoff --all
sudo apt-get -y remove dphys-swapfile

# watchdog
sudo python watchdog.py

# want to install email routing through a gmail account?
# sudo ./postfix.sh

# want to install phantom.js?
# sudo ./phantomjs.sh

# TODO: more improvements from http://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card
