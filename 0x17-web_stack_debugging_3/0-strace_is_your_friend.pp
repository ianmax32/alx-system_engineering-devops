# this is to find out why apache is returning a 500 error using strace
exec {
	'phpp':
	command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
