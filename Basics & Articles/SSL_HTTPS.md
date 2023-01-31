# ES / SSL & HTTPS Config
Para cualquier sitio web es necesario definir estandares de seguridad solidos
Tanto SSL *Secure Sockets Layer* como HTTPS *Secure Hypertext Transfer Protocol* son clave para esto
SSL y HTTPS funcionan de la mano, primero hay que obtener el certificado y luego configurar Wordpress para que cargue HTTPS

## SSL
SSL es una tecnología que crea una conexión segura entre un sitio web y un navegador
Los sitios web que utilizan SSL tiene certificados que te permiten saber que tu información privada está segura durante cada transferencia

<p align="center">
	<img src="../Images/candado-verde.png" alt="Candado verde SSL" />
</p>

- Los datos de los usuarios en nuestra web serán más seguros
- La web será más confiable
- Clave para el SEO

**Para instalar el certificado SSL en nuestro sitio Wordpress, instalaremos el plugin Really Simple SSL**

<p align="center">
	<img src="../Images/reallysimple-ssl.png" alt="Really Simple SSL" />
</p>


## HTTPS
Asi como configuramos el SSL, también debemos configurarlo para transmitir datos mediante el Protocolo de transferencia de hipertexto seguro HTTPS. HTTPS aplica estándares de seguridad más altos que HTTPS
Para configurarlo, el sitio web necesita tener un certificado SSL

**Para configurar HTTPS en Wordpress, iremos a Settings, General Settings y escribir https en los campos de la url**

<p align="center">
	<img src="../Images/https-wp.png" alt="HTTPS config Wordpress" />
</p>
