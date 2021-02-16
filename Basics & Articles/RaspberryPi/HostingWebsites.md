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
