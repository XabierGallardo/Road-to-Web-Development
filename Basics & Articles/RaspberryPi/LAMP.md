# How to install LAMP Server on Raspberry Pi

LAMP (Linux, Apache, MySQL, PHP) server is a software bundle used for web development
The LAMP server is one of the most important servers to set up, it'll serve up dynamic, database-driven websites and driven on Linux
We can either run the comands on a Raspberry Pi our using an SSH connection

*We need a Raspberry Pi computer connected to the internet with at least a 8GB flash card with Raspbian on it*


## Raspbian Image
Create a Raspbian Stretch Lite image to a MicroSD card (or USB)
Once the Raspberry has booted, log in *Username: pi / Password: raspberry*
```sh
# To note the Raspberry IP address
hostname -I

# To change the default password and activate SSH
sudo raspi-config

# Option 1 - "Change User Password" > OK > Enter new UNIX password > Retype > OK
# Option 5 - "Interfacing Options" > P2 SSH > Yes > Finish and Enter

sudo reboot
```


## Updating and Upgrading
Before starting the installation, we'll update our Raspberry
```sh
sudo apt update && sudo apt upgrade -y
```


## Install Apache2 on Raspberry Pi
Apache2 is the most widely used web server software
A web server is the software that handles request to access a web page
Depending on the page we request, the server will generate the document to serve (.html, .php, etc)

- A computer running a web browser connects to the Raspberry Server and request a page
- Our Raspberry running a LAMP server sends the requested page

To install Apache2 on our Raspberry Pi
```sh
sudo apt install apache2 -y
```
If the installation is ok, we'll have an index.html file on /var/www/html directory
To open that page in our browser, we must know the Raspberry Pi IP address
```sh
hostname -I
```
An example of a Raspberry IP address could be 192.168.1.86
If we write that IP address on a browser we'll see the Apache default welcome page


## Install PHP on Raspberry Pi
PHP (Hypertext PreProcessor) is a server side scripting language used to develop dynamic web applications
A PHP file contains **<?php ...?>** tags and ends with the extension .php

To install PHP on Raspberry Pi
```sh
sudo apt install php -y

# We can remove the index.html file and create a PHP script to test the installation
sudo rm index.html
sudo nano index.php

# On our index.php
<?php echo "Hello World"; ?>

# After saving and exit, we'll restart Apache2
sudo service apache2 restart
```

If we write again our Raspberry's IP address we'll see **Hello World** displayed on the screen instead of the Apache welcome page
Now we can remove our index.php file from the **/var/www/html** directory


## MySQL vs MariaDB
Before installing our relational database management system (RDBMS) we'll see the main differences between MySQL and MariaDB
Both are the most used RDBMS worldwide. Originally open-source, MySQL belongs nowadays to Oracle and the original creators of MySQL decided to create MariaDB with the same open-source philosophy

Among the clients of MySQL we can say Github, NASA, Netflix, Facebook, Twitter, Youtube, Spotify, etc
MariaDB counts with most of the Linux distros, it has Google, Wikipedia, RedHat, CentOS, Fedora, Suse, Ubuntu, AWS, Nokia, Samsung, etc

##### Compatibility between MySQL & MariaDB

**MysQL** is a relational database management system and **MariaDB** is a fork or bifurcation of MySQL
Data structures and indexes are the same
This allows to migrate from MySQL to MariaDB without changing our apps, data and structures
- Data config files and tables are compatible
- Structures, protocols and client APIs are the same
- MySQL connectors also work with MariaDB

##### Syntax differences
Queries are exactly the same
```sh
# MariaDB
SELECT *
FROM clients;

# MySQL
SELECT *
FROM clients;
```

###### Database connectors
Database connectors are access standards, they make possible the access to a Database's data

**MySQL connectors**
MySQL offers a wide variety of DB connectors, included: C, C++, Delphi, Perl, Java, Lua, .NET, Node.js, Python, PHP, Lisp, Go, R, D and Erlang

**MariaDB connectors**
MariaDB also offers a huge variety of connectors: ADO.NET, C, C++, D, Java, JavaScript, ODBC, Perl, PHP, Python, Ruby and Visual Studio


## Install MySQL (MariaDB Server) on Raspberry Pi
MySQL is a popular open-source relational database

To install the MySQL Server and PHP-MySQL packages
```sh
sudo apt install mariadb-server php-mysql -y

# After the installation, we'll restart Apache
sudo service apache2 restart

# After installing MySQL, we'll secure our MySQL installation
sudo mysql_secure_installation
```
After the last command, we'll do set up
- It will ask to enter **current password for root**
- Type Y and press Enter to Set root password
- Write a new password and write it down, we'll need it later
- Type Y ro Remove anonymous users
- Type Y to Disallow root login remotely
- Type Y to Remove test database and access to it
- Type Y to reload privilege tables

After completing this prompt, we'll see the message *Thanks for using MariaDB!*

If there's any error login into phpMyAdmin, we'll create a new user to login
Those commands will create a new user with name (admin) and a password (our_password)

```sh
sudo mysql --user=root --password
>create user admin@localhost identified by 'our_password';
>grant all privileges on *.* to admin@localhost;
>FLUSH PRIVILEGES;
>exit;
```


## Install phpMyAdmin on Raspberry Pi
phpMyAdmin is a free software tool written in PHP, intended to handle the administration of MySQL using a web interface

To install phpMyAdmin on a Raspberry Pi
```sh
sudo apt install phpmyadmin -y
```
PHPMyAdmin installation program will ask some questions, we'll use the **dbconfig-common**
- Select **Apache2** when prompted and press Enter
- Configuring **phpmyadmin?** **OK**
- Configure database for phpmyadmin with **dbconfig-common**? **Yes**
- Type the **password** and press **OK**

Enable the PHP MySQLi extension and restart Apache2 for changes to take effect
```sh
sudo phpenmod mysqli
sudo service apache2 restart
```
If we type the Raspberry's IP address followed by **/phpmyadmin** like *http://192.168.1.86/phpmyadmin* we'll probably see a "Not Found" error page in the browser
If that were the case, we'll move the **phpmyadmin** folder to /var/www/html
```sh
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin

# We'll list the files and it should return the phpmyadmin folder
ls
```
Reload the page *http://192.168.1.86/phpmyadmin**http://192.168.1.86/phpmyadmin* and we should see the login page for phpMyAdmin web interface
Now we enter our defined username (**Username = root**) and the password we defined during the installation
After pressing Enter a new page loads and that's phpMyAdmin

Done! Now our Raspberry Pi is prepared with a LAMP server: Apache2, MySQL, PHP
We'd decided to include phpMyAdmin on this installation for an easier database management through a web interface


## Setup FTP
```sh
sudo apt intall vsftpd -y
sudo nano /etc/vsftpd.conf

# Comment with a # the following lines
# local_enable=YES
# ssl_enable=NO

# Add to the bottom of the file
# CUSTOM
ssl_enable=YES
local_enable=YES
chroot_local_user=YES
local_root=/var/www
user_sub_token=pi
write_enable=YES
local_umask=002
allow_writeable_chroot=YES
ftpd_banner=Welcome to my Raspberry Pi FTP service.
```

After saving and exit, we'll finish with the next commands
```sh
sudo usermod -a -G www-data pi
sudo usermod -m -d /var/www pi
sudo chown -R www-data:www-data /var/www
sudo chmod -R 775 /var/www
sudo reboot
```
Done!


## Optional Step / Changing permissions
To manage our web pages, we should change the permissions for **/var/www/html/** directory
```sh
ls -lh /var/www/
sudo chown -R pi:www-data /var/www/html/
sudo chmod -R 770 /var/www/html/
ls -lh /var/www/
```
