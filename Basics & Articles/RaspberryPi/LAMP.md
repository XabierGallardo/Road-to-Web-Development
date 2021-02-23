# How to install LAMP Server on Raspberry Pi

LAMP (Linux, Apache, MySQL, PHP) server is a software bundle used for web development
We'll install this software on our Raspbian OS

We can either run the comands on a Raspberry Pi our using an SSH connection


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

//We can remove the index.html file and create a PHP script to test the installation
sudo rm index.html
sudo nano index.php

//On our index.php
<?php echo "Hello World"; ?>

//After saving and exit, we'll restart Apache2
sudo service apache2 restart
```

If we write again our Raspberry's IP address we'll see **Hello World** displayed on the screen instead of the Apache welcome page
Now we can remove our index.php file from the **/var/www/html** directory
```sh
sudo rm index.php
```


## Install MySQL (MariaDB Server) on Raspberry Pi
MySQL is a popular open-source relational database

To install the MySQL Server and PHP-MySQL packages
```sh
sudo apt install mariadb-server php-mysql -y

//After the installation, we'll restart Apache
sudo service apache2 restart

//After installing MySQL, we'll secure our MySQL installation
sudo mysql_secure_installation
```
