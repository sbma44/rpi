import os, re

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
f.write('\n')
f.close()

os.system('sudo apt-get -y install watchdog chkconfig')
os.system('chkconfig watchdog on')
os.system('sudo /etc/init.d/watchdog start')

f = open('/etc/watchdog.conf', 'r')
lines = f.readlines()
f.close()
out_lines = []
for line in lines:
	if re.search(r'^\s*#\s*watchdog-device\s*=\s*/dev/watchdog', line) is not None:
		out_lines.append('watchdog-device = /dev/watchdog')
	else:
		out_lines.append(line)
f = open('/etc/watchdog.conf', 'w')
f.writelines(out_lines)
f.write('\n')
f.close()
