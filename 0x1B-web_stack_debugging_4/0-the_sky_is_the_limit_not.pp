# This script increases traffic an Nginx server can handle

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/2000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
