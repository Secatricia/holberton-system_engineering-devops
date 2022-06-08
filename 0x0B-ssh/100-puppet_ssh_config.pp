# client SSH configuration file so that you can
# connect to a server without typing a password

exec {'sudo sed -i "s/^.*PasswordAuthentication.*$/    PasswordAuthentication no/g" /etc/ssh/ssh_config':
  path => '/usr/bin',
}

exec {'sudo sed -i "s/^.*id_rsa.*$/    IdentityFile ~\/.ssh\/school/g" /etc/ssh/ssh_config':
  path => '/usr/bin',
}