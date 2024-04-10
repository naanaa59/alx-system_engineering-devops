# Technical Postmortem: Debugging a 500 Internal Server Error in an Apache Server using Wordpress

## Issue Summary
During the last web stack debbuging project , an outage was observed on an isolated Ubuntu 14.04 container running an Apache web server. GET requests resulted in 500 Internal Server Errors, whereas the expected response was an HTML file defining a simple Holberton WordPress site.
Fixing it took me 4 hours to figure it out and te learn how to use tools like strace.
The problem was caused by a typo in an configuration file.

## Timeline
The issue started:  Wednesday 10 april 2024 at 14h48 PM GMT
Fixed :Wednesday 10 april 2024 AT 18:49 PM GMT

## Debugging Steps

### Process Verification
- Utilized `ps aux` to verify the running processes.
- Two Apache2 processes, `www-data` and `apache2`, were confirmed to be running properly.

### Web Server Configuration
- Inspected the `/etc/apache2/sites-available` directory to confirm that the web server was serving content from `/var/www/html/`.

### Initial Strace Attempt
- Ran `strace` on the root Apache process PID in one terminal and attempted to curl the server in another.
- This step did not yield useful information.

### Second Strace Attempt
- Repeated the strace process on the `www-data` process PID.
- This revealed an `-1 ENOENT (No such file or directory)` error when attempting to access `/var/www/html/wp-includes/class-wp-locale.phpp`.

### File Extension Error Identification
- Utilized Vim's pattern matching to search through the `/var/www/html/` directory for the erroneous `.phpp` file extension.
- The error was located in `wp-settings.php` on line 137.

## Correction
The issue was identified as a typo in the file extension, specifically a `.phpp` extension instead of the correct `.php`. Correcting the typo resolved the issue, allowing the server to return the expected 200 OK response.

## Automation and Prevention
To prevent future occurrences of this error, a Puppet manifest was written to automate the error-fixing process. This manifest replaces all `phpp` extensions in the file `/var/www/html/wp-settings.php` with `php`.

## Lessons Learned

### Application Errors
- This incident highlighted that the outage was due to an application error rather than a web server issue.

### Testing
- Testing the application before deployment could have identified and resolved this error earlier.

### Status Monitoring
- Implementing uptime-monitoring services like UptimeRobot can provide instant alerts upon website outages, aiding in quicker resolution.

## Conclusion
The resolution of this issue underscores the importance of thorough testing, meticulous debugging, and proactive error prevention measures. By leveraging tools like `strace` and automating error fixes with Puppet, we can enhance our ability to quickly identify and resolve issues, ensuring a more stable and reliable system.

