# test for root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

aptitude -y install postfix mailutils libsasl2-2 ca-certificates libsasl2-modules

echo "relayhost = [smtp.gmail.com]:587
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous
smtp_tls_CAfile = /etc/postfix/cacert.pem
smtp_use_tls = yes" >> /etc/postfix/main.cf

echo "Enter @gmail.com username: "
read username
echo "Enter @gmail.com password: "
read password
echo "[smtp.gmail.com]:587    $username@gmail.com:$password" > /etc/postfix/sasl_passwd

chmod 400 /etc/postfix/sasl_passwd
postmap /etc/postfix/sasl_passwd

cat /etc/ssl/certs/Thawte_Premium_Server_CA.pem | tee -a /etc/postfix/cacert.pem

/etc/init.d/postfix reload

echo "Test mail from postfix" | mail -s "Postfix configuration successful" thomas.j.lee@gmail.com
