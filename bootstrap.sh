# baseline update / tools
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install vim screen wicd wicd-curses

# ssh key
mkdir ~/.ssh
curl https://raw.github.com/sbma44/rpi/master/tom_lee_dsa_key.pub >> ~/.ssh/authorized_keys

# python / git
sudo apt-get -y install python-setuptools python-dev git 
sudo easy_install pip

# virtualenv
sudo pip install virtualenvwrapper wiringpi wiringpi2
mkdir ~/Devel
mkdir ~/.virtualenvs
curl https://raw.github.com/sbma44/rpi/master/rpi_virtualenvconfig.txt >> ~/.bashrc
source ~/.bashrc
