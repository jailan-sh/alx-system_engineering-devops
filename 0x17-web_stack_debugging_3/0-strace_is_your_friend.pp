# wrong typo cuz the error + manually (curl...., ps -aux(get apache pid), strace -p)
# if = -1 ps error, now u know the path name cuz of error write the script
exec { '/var/www/html/wp-settings.php':
  path    => ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
