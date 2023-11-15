#settings for the maximum number of open files (file descriptors) for the "holberton" user.
file { '/etc/security/limits.conf':
  ensure  => present,
  content => "hard nofile 5000\nsoft nofile 4000\n",
}
