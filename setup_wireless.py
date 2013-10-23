import simple_crypto, os

if os.getuid()!=0:
	raise Exception('This script must be run as root')

os.system('pip install pycrypto')

f = open('wpa_supplicant.conf.encrypted', 'r')
wpa_supp = simple_crypto.decrypt(f.read())
f.close()

f = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w')
f.write(wpa_supp)
f.close()

os.system('cp interfaces /etc/network/interfaces')
