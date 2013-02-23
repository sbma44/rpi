# baseline update / tools
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install screen

# ssh key
mkdir ~/.ssh
curl https://sbma44.s3.amazonaws.com/rpi/tom_lee_dsa_key.pub >> ~/.ssh/authorized_keys

# python / git
sudo apt-get -y install python-setuptools git
sudo easy_install pip

# virtualenv
sudo pip install virtualenvwrapper
mkdir ~/Devel
mkdir ~/.virtualenvs
curl https://sbma44.s3.amazonaws.com/rpi/rpi_virtualenvconfig.txt >> ~/.bashrc
source ~/.bashrc
