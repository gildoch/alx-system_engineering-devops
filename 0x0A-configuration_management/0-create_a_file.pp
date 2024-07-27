# create a file in /tmp with specific requirements

file { 'school':
  ensure  => file,
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data',
  replace => true,
}
