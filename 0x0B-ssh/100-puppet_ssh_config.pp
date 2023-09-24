#!/usr/bin/env bash
# set up your client SSH configuration file so that you can connect to a server without typing a password.
file_line{'identity file':
path   => '/etc/ssh/ssh_config'
match  => '^ IdentityFile '
line   => ' IdentityFile ~/.ssh/school'
}
file_line{'passwd auth':
path   => '/etc/ssh/ssh_config'
match  => '^ PasswordAuthentication '
line   => 'no'
}
