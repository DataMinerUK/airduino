node default {


  ##############################################################################
  #
  # Apt preliminaries and basic packages
  #
  ##############################################################################

  exec {
    'apt-update': command => '/usr/bin/apt-get update';
  }

  package {
    [
      'bash-completion',
      'vim',
      'curl',
      'unzip',
      'bzip2'
    ]: ensure => latest;
  }

  Exec['apt-update'] -> Package <| |>



  ##############################################################################
  #
  # NodeJS
  #
  ##############################################################################

  package {
    [
      'git',
      'build-essential'
    ]: ensure => latest;
  }

  include nodejs

  exec {
    'install-grunt':
      command => '/usr/local/bin/npm install -g grunt-cli',
      creates => '/usr/local/bin/grunt',
      timeout => 0;
  }

  Package['build-essential'] -> Class['nodejs'] -> Exec['install-grunt']



  ##############################################################################
  #
  # Development
  #
  ##############################################################################

  apt::source {
    'puppet':
      location    => 'http://apt.puppetlabs.com',
      release     => 'precise',
      repos       => 'main dependencies',
      key         => '4BD6EC30',
      key_server  => 'keyserver.ubuntu.com',
      include_src => false;
  }

  package {
    [
      'ruby',
      'ruby-dev',
      'rake',
      'irb',
      'rubygems'
    ]: ensure => latest;
  }

  package {
    [
      'puppet-lint',
      'librarian-puppet'
    ]:
      ensure   => latest,
      provider => 'gem';
  }

  Package['ruby-dev'] -> Package['librarian-puppet']
  Package['rubygems'] -> Package['puppet-lint', 'librarian-puppet']

}
