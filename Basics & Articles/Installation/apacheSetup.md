# Apache Installation & Setup
```sh
# Installing Apache2
sudo apt update
sudo apt install apache2

# Creating directory with permissions
sudo mkdir /var/www/projects/
sudo chmod -R 777 /var/www/projects/

# Configuring Apache2
cd /etc/apache2/sites-available/
sudo cp 000-default.conf projects.conf
sudo a2ensite projects.conf

cd ..
sudo vim ports.conf
# Below Listen 80 add the following line
Listen 8080

systemctl reload apache2
```
Go to **localhost:8080** on the browser

Done!
