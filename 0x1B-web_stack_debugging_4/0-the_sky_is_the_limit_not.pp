# fix error by fix defult number of requests allowed in the web server 4096
file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT='-n 4096'\n",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
