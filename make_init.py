import os, sys

if os.getuid()!=0:
    raise Exception('This script must be run as root')

path = sys.argv[1]
service_name = path.split('/')[-2]

supervisor_conf = """[program:%(service_name)s]
command=%(path)s
numprocs=1
autostart=true
autorestart=true""" % {'path': path, 'service_name': service_name}

f = open('/etc/supervisor/conf.d/%s.conf' % service_name, 'w')
f.write(initfile)
f.close()

