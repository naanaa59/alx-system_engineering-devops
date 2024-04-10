# Fixing typo of "phpp" extension of wp-setting file
exec {' fixing wordpress phpp error':
        command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        path    => '/usr/local/bin/:/bin/'
}
