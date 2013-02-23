pacman -S python2 python2-distribute extra/git extra/screen	
ln -s /usr/bin/python2 /usr/bin/python
easy_install-2.7 pip
pip install virtualenvwrapper
mkdir ~/Devel
mkdir ~/.virtualenvs
curl https://sbma44.s3.amazonaws.com/rpi/rpi_virtualenvconfig_arch.txt >> ~/.bashrc
source ~/.bashrc
