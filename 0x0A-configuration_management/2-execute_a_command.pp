#This puppet script kills process killmenow

exec { 'pkill':
command => 'pkill killmenow',
provider => 'shell',
}
