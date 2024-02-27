# This is a puppet manifest that do the same config as previous bash script

class nginx_install {
	package { 'nginx':
		ensure => 'installed',
		}
	}

class nginx_configure {
	file { '/var/www/html/index':
		ensure  => file,
		content => 'Hello World',
	}

	file { '/var/www/html/404.html':
		ensure  => file,
		content => "Ceci n'est pas une page",
	}

	file { '/etc/nginx/sites-available/default':
		ensure  => present,
		content => "rewrite ^/redirect_me https://www.youtube.com/ permanent;\n"
		notify  => Service['nginx'],
	}

	file { '/etc/nginx/sites-available/default':
		ensure  => prenset,
		content => "error_page 404 /404.html;",
		notify  => Service['nginx'],
	}

	service { 'nginx':
		ensure    => running,
		enable    => true,
		subscribe => [File['/etc/nginx/sites-available/default'],
	}
class { 'nginx_install': }
class { 'nginx_configure':}
