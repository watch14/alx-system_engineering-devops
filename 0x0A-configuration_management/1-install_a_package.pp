# 1-install_a_package.pp

# X
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# pack
package { 'python3-pip':
  ensure => 'installed',
}
