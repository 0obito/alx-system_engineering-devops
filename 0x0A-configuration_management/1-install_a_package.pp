#!/usr/bin/pup
# This puppet code installs Flask version 2.1.0 from pip3
package {'flask':
  name     => 'flask',
  ensure   => '2.1.0',
  provider => 'pip3',
}
