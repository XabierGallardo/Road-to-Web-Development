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


## Step 1 / Setting up an OS on the Pi
Connect the microsd card on the computer and download *NOOBS* (New Out of Box Software), which is a tool to install an OS on the Raspberry Pi
**https://www.raspberrypi.org/downloads/%20NOOBS/**
**https://www.raspberrypi.org/help/noobs%20setup/**

Insert the sd card onto the Pi and connect it with a power supply, as well as keyboard, monitor and mouse
While there are multiple choices, the recommended one is Raspbian


## Step 2 / Accessing Raspberry Pi Web Server with SSH

Secure Shell Network protocol (SSH) allows to make a connection between the Raspberry Pi and the computer to transfer data
It also useful to control the Raspberry with the terminal

Raspbian OS comes with a SSH pre-installed, so in order to visualize the IP address
```sh
sudo ifconfig
```
The IP address will appear on top of the screen
With an ethernet cable the address will start with "eth0" while with Wi-Fi it'll appear as "wlan0"
This address will get us access to the Raspberry Pi from our computer


## Step 3 / Updating the Raspberry Pi

After the connection, we'll check if everything is updated on it before installing Apache on the server

```sh
sudo apt update
sudo apt upgrade
```

All the packages and directories will be updated and our server is ready to install Apache


## Step 4 / Installing Apache

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

//It'll say active(running) if it's running properly
sudo service apache2 status

//If the server goes down
sudo service apache2 start
```

After this we'll be able to browse the Pi from our computer's browser
Since we are using SSH, we can access the Raspberry using the IP address on our browser
*http://192.167.2.2*

We'll have a confirmation box saying that Apache is successfully installed


## Step 5 / Making a simple HTML website

When our Raspberry Pi is done with the Apache installation, it will automally generate a simple HTML website
We'll access that website typing the IP address of the Raspberry on our computer's browser
It's a basic index.html that allows us to know that it's working fine, it comes preinstalled with the Apache software

To make changes on it
```sh
cd /var/www/

sudo nano index.html
```


## Step 6 / Configuring FTP

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
//To access the conf file
sudo nano /etc/vsftpd.conf

//Change anonymous_enable from YES to NO
#anonymous_enable=NO

//Remove the # symbol from the following lines to uncomment
#local_enable=YES
#write_enable=YES

//Add a new line at the end
force_dot_files=YES
```

The last line force the server file's display that starts with ".", like .htcaccess
Save changes and exit the terminal, after the confirmation of the changes, restart the FTP

```sh
sudo service vsftpd restart
```

This allows us to connect our Raspberry Pi and upload the files to **/var/www/html** directory


## Getting a domain name

While we can visit our website, it's not visible to everyone
To make it accesible for everyone, we need to get it online

While it's possible to access our website from anywhere with an external IP address, the best solution is to have a domain name with words

Websites like DNSdynamic or freenom.com will allow us to translate our IP address into a preferable domain name for free

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

//add the following line onto the rc.local file
sudo noip2
```

Save and reboot the Pi

```sh
sudo reboot
```



