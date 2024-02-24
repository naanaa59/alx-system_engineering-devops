# This puppet manifest configure the /etc/ssh/ssh_config file to use the private key and refuse to authenticate using a password

file_line { 'Use private key in path':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Refuse password authentification':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentification no',
  replace => true,
}
