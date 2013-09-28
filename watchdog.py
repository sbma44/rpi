import os

# modprobe
os.system('sudo modprobe bcm2708_wdog')

# update module load list
f = open('/etc/modules', 'r')
lines = f.readlines()
if not 'bcm2708_wdog' in lines:
	lines.append('bcm2708_wdog')
f.close()
f = open('/etc/modules', 'w')
f.writelines(lines)
f.close()

os.system('sudo apt-get install watchdog chkconfig')
os.system('chkconfig watchdog on')
os.system('sudo /etc/init.d/watchdog start')

f = open('/etc/watchdog.conf', 'r')
lines = f.readlines()
f.close()
out_lines = []
for line in lines:
	if line=='#watchdog-device = /dev/watchdog':
		out_lines.append('watchdog-device = /dev/watchdog')
	else:
		out_lines.append(line)
f = open('/etc/watchdog.conf', 'w')
f.writelines()
f.close()
