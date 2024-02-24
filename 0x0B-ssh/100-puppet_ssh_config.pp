# This puppet manifest configuration file

include stdlib

file_line { 'Use private key in path':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	 IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Refuse password authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '   PasswordAuthentication no',
  replace => true,
}
