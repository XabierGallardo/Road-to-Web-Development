# Instalar phpMyAdmin Linux Mint 22 / Ubuntu 24.04

### **1. Actualiza los paquetes del sistema**
Abre la terminal y ejecuta:

```bash
sudo apt update && sudo apt upgrade -y
```

---

### **2. Instala el servidor web y PHP**
Asegúrate de tener Apache o Nginx instalado junto con PHP. Usa Apache para este ejemplo:

```bash
sudo apt install apache2 php libapache2-mod-php -y
```

---

### **3. Instala MySQL**
Instala el servidor de MySQL (o MariaDB):

```bash
sudo apt install mysql-server -y
```

Durante la instalación, sigue las instrucciones para configurar la contraseña del usuario `root`.

Verifica que MySQL esté corriendo:

```bash
sudo systemctl status mysql
```

Inicia el servidor si es necesario:

```bash
sudo systemctl start mysql
```

---

### **4. Asegura MySQL**
Ejecuta el siguiente comando para configurar MySQL y mejorar su seguridad:

```bash
sudo mysql_secure_installation
```

Sigue las instrucciones en pantalla para establecer contraseñas y eliminar configuraciones inseguras.

---

### **5. Instala phpMyAdmin**
Instala phpMyAdmin con:

```bash
sudo apt install phpmyadmin -y
```

Durante la instalación:

- Selecciona `apache2` como servidor web cuando se te pregunte.
- Configura la base de datos para phpMyAdmin con `dbconfig-common`.
- Introduce una contraseña para el usuario de phpMyAdmin cuando se te solicite.

Si accidentalmente omites alguna configuración, puedes reconfigurar phpMyAdmin con:

```bash
sudo dpkg-reconfigure phpmyadmin
```

---

### **6. Habilita el archivo de configuración de phpMyAdmin en Apache**
Verifica que el archivo de configuración de phpMyAdmin esté habilitado:

```bash
sudo ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-available/phpmyadmin.conf
sudo a2enconf phpmyadmin
```

Luego reinicia Apache:

```bash
sudo systemctl restart apache2
```

---

### **7. Accede a phpMyAdmin**
Abre tu navegador y ve a:

```
http://localhost/phpmyadmin
```

Inicia sesión con el usuario `root` de MySQL y su contraseña.

---

### **8. Solución de problemas comunes**
- **Extensiones de PHP faltantes:** Instala extensiones adicionales si phpMyAdmin muestra errores.
  Por ejemplo:

  ```bash
  sudo apt install php-mbstring php-zip php-gd php-json php-curl -y
  sudo systemctl restart apache2
  ```

- **Acceso denegado:** Asegúrate de que el usuario `root` tenga permisos para acceder a phpMyAdmin.
