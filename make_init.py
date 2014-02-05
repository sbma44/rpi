import os, sys

if os.getuid()!=0:
    raise Exception('This script must be run as root')

path = sys.argv[1]
service_name = path.split('/')[-2]

initfile = """#!/bin/bash
#
# This starts and stops %(service_name)s
#
### BEGIN INIT INFO
# Provides:          %(service_name)s
# Required-Start:    $network
# Required-Stop:
# Short-Description: %(service_name)s
# Description:       Does something neat with Raspberry Pi PWM pins (probably)
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO


# Source function library.
. /lib/lsb/init-functions

NAME=%(service_name)s
DAEMON="%(path)s"
PIDFILE=/var/run/$NAME.pid
DAEMON_ARGS=""

[ -x $binary ] || exit 0

RETVAL=0

start() {
    echo -n "Starting %(service_name)s daemon: "
    start-stop-daemon --start --quiet    \
    --make-pidfile --pidfile $PIDFILE --background       \
    --exec /bin/bash -- -c "$DAEMON $DAEMON_ARGS > /var/log/%(service_name)s.log 2>&1"
    log_end_msg $?
}

stop() {
    echo -n "Shutting down %(service_name)s daemon: "
    start-stop-daemon --stop --quiet --pidfile "$PIDFILE" --retry 1 --oknodo
    log_end_msg $?
}

restart() {
    stop
    sleep 1
    start
}

case "$1" in
    start)
        start
    ;;
    stop)
        stop
    ;;
    status)
        status stephmeter
    ;;
    restart)
        restart
    ;;
    *)
        echo "Usage: $0 {start|stop|status|restart}"
    ;;
esac

exit 0
""" % {'path': path, 'service_name': service_name}

f = open('/etc/init.d/%s' % service_name, 'w')
f.write(initfile)
f.close()

os.system('sudo chmod +x /etc/init.d/%s' % service_name)
os.system('sudo update-rc.d %s defaults' % service_name)
