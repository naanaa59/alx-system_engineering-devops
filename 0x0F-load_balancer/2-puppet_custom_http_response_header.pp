# This is a puppet manifest that do the same config as previous bash script

exec { 'command':
	command => 'apt-get -y update;
	apt-get -y install nginx;
	sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-availabe/default;
	servie nginx restart',
	provider => shell,
}

