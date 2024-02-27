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
		content => "Ceci n'est pas une page\n",
	}

	file { '/etc/nginx/sites-available/default':
		ensure  => present,
		content => "server {
  		  	  	   listen 80 default_server;
        			   listen [::]:80 default_server;
               				root /var/www/html;
        			   index index.html index.htm index.nginx-debian.html;
        			   server_name _;
        			   location / {
                			try_files \$uri \$uri/ =404;
        			   }
        			   error_page 404 /404.html;
        			   location  /404.html {
            				internal;
        			  }
        			  if (\$request_filename ~ redirect_me){
            				rewrite ^ https://www.youtube.com/ permanent;
        			  }
}
",
		notify  => Service['nginx'],
	}

	service { 'nginx':
		ensure    => running,
		enable    => true,
		subscribe => [File['/etc/nginx/sites-available/default']],
	}
}
class { 'nginx_install': }
class { 'nginx_configure':}

