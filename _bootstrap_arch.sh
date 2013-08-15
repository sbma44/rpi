# ssh key
mkdir ~/.ssh
curl https://raw.github.com/sbma44/rpi/master/tom_lee_dsa_key.pub >> ~/.ssh/authorized_keys

# python / virtualenv / utils
pacman -S
pacman -S python2 python2-distribute extra/git extra/screen	
ln -s /usr/bin/python2 /usr/bin/python
easy_install-2.7 pip
pip install virtualenvwrapper
mkdir ~/Devel
mkdir ~/.virtualenvs
curl https://raw.github.com/sbma44/rpi/master/rpi_virtualenvconfig_arch.txt >> ~/.bashrc
source ~/.bashrc
