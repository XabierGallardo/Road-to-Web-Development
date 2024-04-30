## Kiosk mode in Raspberry Pi
Kiosk mode on a Raspberry Pi (or any other system) refers to a configuration where the device is set up to run a single application or website in full-screen mode, restricting access to other applications or system functions. This is often used in scenarios where the device is deployed for a specific purpose, such as a digital signage display, information kiosk, or interactive exhibit.

In kiosk mode, the Raspberry Pi boots directly into the desired application or website, providing a seamless and focused user experience without distractions.

### Optional / Stable underclock for saving temperature & power comsumption
```sh
# /boot/firmware/config.txt
[all]
arm_freq_max=900
arm_freq_min=900
gpu_freq=400
core_freq=400
```

# Autorefresh chromium custom script :globe_with_meridians: :repeat:
### Update 2024 on Debian GNU/Linux 12 (bookworm) aarch64
xdotool not working on modern raspbian with default [wayland](https://www.omglinux.com/raspberry-pi-os-bookworm/)

## [Step 1 / Change Wayland to X11](https://forums.raspberrypi.com/viewtopic.php?t=364116)
*xdotool doesn't work with the now default Wayland*

Use **sudo raspi-config** (advanced menu) to switch back to X11

## [Step 2 / Create systemd service file](https://raspberrypi.stackexchange.com/questions/72644/unable-to-run-reboot-crontab-at-reboot)
*Execute script after 10 secs when network service starts*
```sh
[Install]
WantedBy=multi-user.target

[Unit]
Description=Autorefresh chromium
Wants=network-online.target
After=network-online.target

[Service]
User=pi
Group=pi
ExecStart=/home/pi/autorefresh-chromium.sh
ExecStartPre=/bin/sleep 10
Type=simple

[Timer]
OnStartupSec=25
```

## Step 3 / Create autorefresh-chromium.sh script
```sh
# Install xdotool
sudo apt-get install xdotool

# EXTRA wifi non-sudo commands to manage wifi
sudo apt install tlp



# 1. Copy the autostart file
cp /etc/xdg/lxsession/LXDE-pi/autostart /home/pi/.config/lxsession/LXDE-pi/autostart



# 2. Create a file called autorefresh-chromium.sh in /home/pi/
touch autorefresh-chromium.sh



# 3. Chmod the file to make it executable
chmod 755 /home/pi/autorefresh-chromium.sh



# 4. Edit /home/pi/autorefresh-chromium.sh

#!/bin/bash
export XAUTHORITY=/home/pi/.Xauthority
export DISPLAY=:0

# 0 /First page refresh at startup
sleep 15
xdotool key F5

# Loop (24h x 2) x 7 days a week, should last 1 to 2 weeks
i=0
while [ $i -le 336 ]
do
	random=$(( 1800 + $RANDOM % 1800 )) #random number between 30 to 60 minutes
	sleep $random

	# 1 /Turn off & on wifi to avoid wifi connection drops
	wifi off
	sleep 10

	wifi on
	sleep 15
	
	# 2 /Perform Full Screen & F5 refresh
	xdotool key F11 #full screen
	xdotool key F5 #refresh

	((i++))
done



#5. Add chromium & autorefresh to /home/pi/.config/lxsession/LXDE-pi/autostart
@xscreensaver -no-splash
@xset s off
@xset -dpms
@xset s noblank
@chromium-browser
```

#### OLD Source [Raspberry Pi Forums](https://forums.raspberrypi.com/viewtopic.php?t=178206)


### What is Wayland?
Wayland is a protocol for a compositor to talk to its clients as well as a library implementing this protocol. On Raspbian, which is a Debian-based operating system optimized for the Raspberry Pi, *Wayland can be used as an alternative to the more traditional X11 windowing system*.

Wayland is designed to provide smoother graphics rendering and better performance compared to X11, particularly for modern graphical environments and hardware acceleration. It is becoming increasingly popular as an alternative display server protocol in Linux-based systems.

By using Wayland on Raspbian, users can potentially benefit from improved graphics performance and better support for modern graphical applications. However, it's important to note that Wayland may have different compatibility and support levels for certain applications compared to X11, so users should consider their specific requirements and compatibility when choosing between the two.

### Que es Wayland?
Wayland es un protocolo de servidor de visualización y un conjunto de bibliotecas y herramientas asociadas que se utilizan en sistemas operativos basados en Linux para manejar la composición de ventanas y la representación gráfica en el entorno de escritorio. A diferencia de X11, que es el sistema de ventana tradicional utilizado en muchos entornos de escritorio de Linux, Wayland se diseñó con un enfoque más moderno y eficiente en mente.

Wayland ofrece varios beneficios sobre X11, como:

1. **Mejor rendimiento**: Wayland está diseñado para proporcionar un rendimiento más suave y una menor latencia en comparación con X11, lo que puede resultar en una experiencia de usuario más fluida, especialmente en dispositivos con recursos limitados como la Raspberry Pi.

2. **Mejor seguridad**: Wayland se esfuerza por proporcionar un modelo de seguridad más robusto que X11, lo que puede ayudar a mitigar ciertas vulnerabilidades de seguridad relacionadas con el sistema de ventana.

3. **Diseño moderno**: Wayland está diseñado para aprovechar características modernas de hardware y gráficos, lo que permite un mejor aprovechamiento de las capacidades de aceleración de hardware disponibles en dispositivos como la Raspberry Pi.
