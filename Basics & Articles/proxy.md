# Qué es un proxy?
Un **servidor proxy** es un intermediario que gestiona las peticiones de red entre un cliente y un servidor de destino, actuando como puente para filtrar, anonimizar o almacenar en caché el tráfico.

### Ejemplo práctico de funcionamiento
Si un usuario intenta acceder a un sitio web bloqueado o restringido geográficamente, su dispositivo envía la solicitud al **proxy** en lugar de conectarse directamente al sitio. El proxy **modifica la dirección IP** de origen, presenta la petición desde una ubicación permitida y devuelve la respuesta al usuario, permitiendo el acceso sin revelar la identidad real de la red local.

### Casos de uso comunes
*   **Filtrado corporativo:** Las empresas usan **proxys transparentes** para bloquear el acceso a redes sociales o sitios no laborales, registrando el tráfico para auditorías.
*   **Caché y rendimiento:** Un **ISP** puede instalar un proxy con caché para guardar copias de sitios web frecuentados, reduciendo la latencia y el ancho de banda al servir el contenido directamente sin contactar al servidor original.
*   **Anonimato:** Herramientas como **Hide.me** o **VPNBook** ofrecen proxies gratuitos que enmascaran la IP del usuario, haciendo parecer que la navegación proviene de otro país.
*   **Desarrollo web:** Los desarrolladores utilizan **proxys de reenvío locales** (como en Vite o Webpack) para evitar restricciones de **CORS** durante el desarrollo, reescribiendo encabezados y dirigiendo las solicitudes a la API de destino.