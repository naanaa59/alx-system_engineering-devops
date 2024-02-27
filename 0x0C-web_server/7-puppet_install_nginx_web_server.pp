# This is a puppet manifest that do the same config as previous bash script

exec { 'apt-get-update':
	command => '/usr/bin/apt-get update',
}
package { 'nginx':
	ensure  => installed,
	require => Exec['apt-get-update'],
	}


file { '/var/www/html/index.html':
	content => 'Hello World',
	require => Package['nginx'],
}

exec { 'redirect_me':
	command => 'sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}
service { 'nginx':
	ensure  => running,
	require => Package['nginx'],
}

