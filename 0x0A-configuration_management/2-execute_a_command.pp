# This manifest kills a process named killmenow
exec { 'execute_a_command'
command     => '/usr/bin/pkill killmenow',
path        => '/usr/bin',
onlyif      => '/usr/bin/pgrep killmenow',
refreshonly => true,
}
