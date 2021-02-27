# Hosting on RaspberryPi

## Benefits of hosting a website on the Pi
- Usual website hosting is expensive, specially in medium and long-term
- Raspberry Pi can easily run on low energy
- The Pi is portable, cheap and can fit anywhere
- Hosting is a matter of minutes on the Pi



## What do I need
- Raspberry Pi, any version, from 2gb of RAM, the bigger the RAM, the easier to handle the resources
- A Router or Modem, neccesary to get internet services
- Ethernet cable, definitely the best option to have a permanent internet conection without interruptions, a wireless usb adapter is also a choice



## Setting up our Raspberry Pi
Connect the microsd card on the computer and download *NOOBS* (New Out of Box Software), which is a tool to install an OS on the Raspberry Pi
**https://www.raspberrypi.org/downloads/%20NOOBS/**
**https://www.raspberrypi.org/help/noobs%20setup/**

Insert the sd card onto the Pi and connect it with a power supply, as well as keyboard, monitor and mouse
While there are multiple choices, the recommended one is RaspbianOS



## Accessing Raspberry Pi Web Server with SSH
Secure Shell Network protocol (SSH) allows to make a connection between the Raspberry Pi and the computer to transfer data
It also useful to control the Raspberry with the terminal

Raspbian OS comes with a SSH pre-installed, so in order to visualize the IP address
```sh
sudo ifconfig
```
The IP address will appear on top of the screen
With an ethernet cable the address will start with "eth0" while with Wi-Fi it'll appear as "wlan0"
This address will get us access to the Raspberry Pi from our computer



## Updating the Raspberry Pi
After the connection, we'll check if everything is updated on it before installing Apache on the server
```sh
sudo apt update
sudo apt upgrade
```
All the packages and directories will be updated and our server is ready to install Apache

While hosting a website on the Raspberry is not a complicated process, it's not the best web server for a production-level speed
If possible, setting the server on a USB drive rather than an SD card is a better option
The time to read and write will be significant faster, also, using RAM for write and read file storage will also help with the possible speed problems

When it comes to security, it's a good idea to change the default password of our Pi to another much more stronger and hard to guess
```sh
Passwd
```
This way, our website will be safer at least from somebody familiar with the Raspberry Pi OS



## Hosting Steps
We can access any website through a browser using a DNS name
A DNS name should have been mapped with our web server IP address (**A record**)
Once the IP adress is mapped, we need the web server running to listen and reply on the IP and port

1. Getting a free DNS
2. Installing Apache
3. Configuring Apache
4. Configuring FTP
5. Configuring SSL encryption
6. Hosting with LAMP




## Step 1 / Getting a free DNS
While we can visit our website, it's not visible to everyone
To make it accesible for everyone, we need to get it online

While it's possible to access our website from anywhere with an external IP address, the best solution is to have a domain name with words
Websites like DNSdynamic or freenom.com will allow us to translate our IP address into a preferable domain name for free

##### Option 1 freenom & ipchicken
On *freenom.com* we'll search for a domain name and get the free one
It needs a registration first, then we can use the free domain up to a year

After getting the domain, we need to add *'A'* record
We'll go to ipchicken.com to find the same

Next, login to the freenom website, go to Services > **my domains** > **manage domain** for the dns name we want to change
Manage Domain > Manage Freenom DNS > Add *'A'* record with target as router IP address

##### Option 2 dnsdynamic & no-ip
After a registration (on DNSdynamic) we'll have a human-readable domain name ready

In case of not having an static IP address and our ISP changes the address everyday, we can use services like the no-ip server to get a domain name
A no-ip will automatically update our domain name according to the last IP address we had

On noip.com, we'll create a free acount and register a hostname
It will look like *rspi;.no-ip.org*, and after it's done, we'll write the next command lines to install the server on our Pi
```sh
cd /usr/local/src/
sudo wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
tar xf noip-duc-linux.tar.gz
sudo rm noip-duc-linux.tar.gz
cd noip-2.1.9-1/
sudo make install
```
After that, the system will start the configuration automatically and will ask for our username and password
When everything is set, we'll make sure that the server starts everytime we open the Pi
```sh
cd /etc/
sudo nano rc.local

# Add the following line onto the rc.local file
sudo noip2
```
Save and reboot the Pi
```sh
sudo reboot
```
If we used DNSdynamic, we should nee the exact domain name to access our website
It'll be possible to visit our website by entering the domain name on the browser
Same functionality with a no-ip server

With No-IP, if possible to test if the service is running properly by writing
```sh
sudo noip2 -S
```
*Even a better plan than No-IP is to get a cheap domain and add it to cloudflare and using cloudflare-ddns*



## Step 2 / Installing Apache
Apache is a free open-source HTTP server software that will help us to host websites onto our Raspberry Pi

After updating our software, we'll install it
```sh
sudo apt-get install apache2 php5 libapache2-mod-php5
```
This command line also install other packages like PHP and PHP library for Apache
PHP is needed to build a web framework for our website to connect to the database

After the installation is done, we'll restart the program to activate the software
```sh
sudo service apache2 restart

# It'll say active(running) if it's running properly
sudo service apache2 status

# If the server goes down
sudo service apache2 start
```
After this we'll be able to browse the Pi from our computer's browser
Since we are using SSH, we can access the Raspberry using the IP address on our browser
*http://192.167.2.2*

We'll have a confirmation box saying that Apache is successfully installed



## Step 3 / Configuring Apache
When our Raspberry Pi is done with the Apache installation, it will automally generate a simple HTML website
We'll access that website typing the IP address of the Raspberry on our computer's browser
It's a basic index.html that allows us to know that it's working fine, it comes preinstalled with the Apache software

We'll create a configuration for our domain name using following command and configure the Virtual host & doc path
```sh
sudo cp /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/{dnsName}.conf
```
**configuration**
```sh
    <VirtualHost {dnsName}:80>
    # The ServerName directive sets the request scheme, hostname and port that
    # the server uses to identify itself. This is used when creating
    # redirection URLs. In the context of virtual hosts, the ServerName
    # specifies what hostname must appear in the request’s Host: header to
    # match this virtual host. For the default virtual host (this file) this
    # value is not decisive as it is used as a last resort host regardless.
    # However, you must set it for any further virtual host explicitly.
    ServerName www.{dnsName} #www.example.org
    ServerName {dnsName} # example.org

    ServerAdmin {emailAddress}
    DocumentRoot /var/www/html

    # Available loglevels: trace8, …, trace1, debug, info, notice, warn,
    # error, crit, alert, emerg.
    # It is also possible to configure the loglevel for particular
    # modules, e.g.
    #LogLevel info ssl:warn

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
```

Now we'll reload the configuration and restart the server
```sh
sudo a2ensite {dnsName}
sudo service apache2 reload
sudo systemctl daemon-reload
sudo service apache2 restart
```

We'll check that the router/firewall is not blocking the port 80
Now everything is ready, if we enter the dns name created from freenom.com, it'll go through our raspberry apache2 server and load the index.html stored on
**DocumentRoot(/var/www/html)** specified in conf file


## Step 4 / Configuring FTP
File Transfer Protocol or FTP is a network protocol to transfer files between systems connected on a TCP net, it's based on the client-server architecture

To make changes on the index file when our website is made, we'll need to create a www directory and install FTP software
```sh
sudo chown -R pi /var/www
sudo apt install vsftpd
```

vsftpd or Very Secure FTP Daemon is a secure and super fast FTP server for Unix-like systems, including Linux
It's licensed under the GNU General Public License and supports IPv6, TLS and FTPS

Now we'll change some configuration settings
```sh
# To access the conf file
sudo nano /etc/vsftpd.conf

# Change anonymous_enable from YES to NO
#anonymous_enable=NO

# Remove the # symbol from the following lines to uncomment
#local_enable=YES
#write_enable=YES

# Add a new line at the end
force_dot_files=YES
```
The last line force the server file's display that starts with ".", like .htcaccess
Save changes and exit the terminal, after the confirmation of the changes, restart the FTP
```sh
sudo service vsftpd restart
```
This allows us to connect our Raspberry Pi and upload the files to **/var/www/html** directory



# Step 5 / Configuring SSL encryption using cloudflare


## Step 6 / Hosting with LAMP (Quick guide)

**Full lesson on LAMP.md**
A LAMP server configuration is the recommended one with the Raspberry
A LAMP server support both PHP and MySQL
```sh
sudo apt install mysql-server php-mysql -y

# Restart the apache after the installation
sudo service apache2 restart

# Install PHP
sudo apt install php -y
```
After the installation is done, we'll restart Apache Again
This way our LAMP server is ready!


## Advanced Tips on hosting on a Raspberry
- It's recommended to not use No-IP, a better option could be a cheap domain and adding it to a cloudflare and using cloudflare-ddns
- Using docker + portainer to host your production builds, only keep port 80 exposed (and forwarded) to web, keep the rest inside docker virtual network
- Setup wireguard VPN on the Raspberry for remote working. Don't expose port 22 to internet (an option when using a key based auth, but this option is better and gives easier access to internal ports)
- Taking regular RPI backups due to the problems of flash drives on a long-term basis
- Before the RPI backups, check that the ISP isn't behind a CGNAT or block incoming traffic on certain ports (port 80, 443, 25 are commonly blocked)

# Step 5 / Configuring SSL encryption using cloudflare
We'll learn how to configure SSL Encryption using cloudflare
Cloudflare provides free https certificate
