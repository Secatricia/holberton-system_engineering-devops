#Just as in task #0 but with Puppet

exec { 'update':
    command => '/usr/bin/apt update -y',
}

package { 'nginx':
    ensure  => installed,
    require => Exec['update'],
}

file_line { 'header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
