# Puppet script to create ssh config file

file_line {'Password auth off':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '   PasswordAuthentication no'

}

file_line {'IdentityFile':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '   IdentityFile ~/.ssh/school'
}