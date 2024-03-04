# This is a puppet manifest that do the same config as previous bash script

exec { 'apt-get-update':
command => '/usr/bin/apt-get update || true',
}
package { 'nginx':
ensure  => installed,
require => Exec['apt-get-update'],
}


exec { 'X-Served-By':
	command  => 'sudo sed -i "/server {/a \	add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
	provider => 'shell',
}
service { 'nginx':
	ensure  => running,
	require => Package['nginx'],
}

