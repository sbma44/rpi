rpi
===

Raspberry Pi bootstrap resources. Designed for my own use, but others might find something useful here. 

Features:

* Installs Bonjour so you can get to the Pi without looking up its DHCP-delivered IP address
* Gets a decent Python development environment in place, complete with virtualenv
* Installs the wiringpi and wiringpi2 libraries, which are what you’ll want to use to control the General Purpose Input/Ouput (GPIO) pins on the device
* Sets up my default wifi networks. Whoops! You probably don’t want that. But you can use the /etc/network/interfaces and /etc/wpa_supplicant/wpa_supplicant.conf file templates to get yourself online. Note that you can have more than one network={} statement in the latter.
* Gives my SSH key root on the system. You probably don’t want that either.
* Turns off the swap file. Swap files are the means by which your disk impersonates RAM to expand your system’s capabilities. It’s a super-neat idea in general, but less so if your disk self-destructs the more often you write to it — which is indeed the case with a flash SD card. You should find a way to make do with physical memory. I’ve gone through a lot of SD cards.
* Turns on the watchdog module in the Broadcom processor that lives at the heart of the Pi. This is a little piece of hardware that listens for a heartbeat signal from the system and, if it doesn’t hear one, reboots everything. Step one is turning on the hardware; step two is setting up the heartbeat. This can give your system a gentle kick when something you’ve done screws it up.
* Want to install a Python script in your virtualenv as a system service that starts at boot and runs as root (which is necessary for GPIO access)? I’ve made that fairly simple with make_init.py, though the script does bake in a few assumptions about your directory structure.
* Optionally, this script will help you set up outbound mail via your Gmail account
* Finally, there’s a script to install an ARM processor-compatible version of PhantomJS.

Not included but an extremely good idea if you aren't using an enormous SD card:

* [You should turn off journaling in the filesystem](http://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card). Journaling is a neat idea by which every change to the filesystem is first cached in a central location before being executed as a transaction. This allows for graceful recovery from a number of failure modes that can occur if an operation that requires multiple steps — and which really, really needs to complete all of them for things to make sense — is abruptly interrupted by a power loss or other failure. But that caching requires a ton of writes to disk, and will burn up your SD card in short order. You’ll just have to get by without journaling, and commit to pulling the power as little as possible.

Thanks to @konklone for making me realize I should get this README into shape.