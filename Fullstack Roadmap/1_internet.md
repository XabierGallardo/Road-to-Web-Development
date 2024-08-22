## [Protocolo HTTP y lenguaje HTML](https://www.youtube.com/watch?v=l6oF_RpBf64)

# 1. Introducción a Internet
Internet es una **red global de computadoras interconectadas que permite la comunicación y el intercambio de información a través de distintos sistemas y tecnologías**. Sus orígenes se remontan a la década de 1960, cuando el Departamento de Defensa de los Estados Unidos desarrolló ARPANET, una red de computadoras diseñada para permitir la comunicación entre diferentes instituciones académicas y gubernamentales.

ARPANET fue el precursor de Internet, y su creación marcó el inicio de la era digital. La primera comunicación exitosa en ARPANET tuvo lugar en 1969, cuando una computadora en la Universidad de California, Los Ángeles (UCLA) se conectó con otra en el Instituto de Investigación de Stanford. Esta red inicial utilizaba conmutación de paquetes, una tecnología que permite que los datos se dividan en pequeños bloques o paquetes antes de ser enviados a su destino final, donde se vuelven a ensamblar.

A lo largo de las décadas de 1970 y 1980, ARPANET se expandió y se conectó con otras redes, como NSFNET, que fue financiada por la Fundación Nacional para la Ciencia de los Estados Unidos. **En 1983, ARPANET adoptó el protocolo TCP/IP (Transmission Control Protocol/Internet Protocol), que se convirtió en el estándar para la transmisión de datos en Internet. Este protocolo permitió la interoperabilidad entre diferentes redes y sentó las bases para la expansión global de Internet.**

### Componentes Fundamentales
Internet se compone de diversos elementos y tecnologías que trabajan juntos para facilitar la comunicación y el intercambio de información. Entre los componentes fundamentales se incluyen:

1. **Protocolos de Comunicación:** Los protocolos son conjuntos de reglas que permiten la comunicación entre dispositivos en una red. Los más importantes son TCP/IP, que garantizan la transmisión de datos de manera fiable y eficiente.

2. **Direcciones IP:** Cada dispositivo conectado a Internet tiene una dirección IP (Internet Protocol) única, que actúa como su identificador en la red. Las direcciones IP pueden ser IPv4 (formato numérico) o IPv6 (formato alfanumérico).

3. **Servidores y Clientes:** Internet está compuesto por servidores, que almacenan y proporcionan información, y clientes, que solicitan y utilizan esa información. Por ejemplo, cuando accedes a un sitio web, tu navegador actúa como un cliente que solicita datos de un servidor web.

4. **DNS (Domain Name System):** El DNS es un sistema que traduce nombres de dominio legibles por humanos (como www.ejemplo.com) en direcciones IP. Esto permite a los usuarios acceder a sitios web sin tener que recordar direcciones IP numéricas.

5. **Ruteadores y Conmutadores:** Estos dispositivos dirigen el tráfico de datos a través de la red, asegurando que los paquetes de información lleguen a su destino correcto.

6. **Infraestructura Física:** Incluye cables de fibra óptica, cables de cobre, satélites y torres de telecomunicaciones que forman la columna vertebral de Internet, permitiendo la transmisión de datos a largas distancias.



# 2. El protocolo TCP-IP
El protocolo TCP/IP es un conjunto fundamental de protocolos utilizados para la comunicación en redes de computadoras, incluyendo Internet. Se compone de dos protocolos principales: TCP (Transmission Control Protocol) y IP (Internet Protocol). A continuación, se detalla de manera extensa cada uno de estos componentes y su funcionamiento conjunto.

TCP/IP es la columna vertebral de la comunicación en redes modernas, incluyendo Internet. Su diseño modular y robusto permite una comunicación fiable y eficiente entre dispositivos de todo el mundo. La comprensión de cómo funcionan TCP e IP juntos es esencial para cualquier profesional de TI o desarrollador que trabaje con redes y aplicaciones distribuidas.

### 2.1 Modelo de Referencia
TCP/IP se basa en un modelo de referencia que consta de cuatro capas, cada una con funciones específicas. Estas capas son:

1. **Capa de Aplicación**: Proporciona protocolos que facilitan la comunicación entre aplicaciones. Ejemplos incluyen HTTP (para la web), FTP (para transferencia de archivos), y SMTP (para correo electrónico).
   
2. **Capa de Transporte**: Garantiza una transferencia de datos fiable y ordenada. Aquí reside TCP (Transmission Control Protocol), que divide los datos en segmentos y asegura su entrega correcta.
   
3. **Capa de Internet**: Maneja el direccionamiento y el encaminamiento de paquetes a través de múltiples redes. El protocolo principal en esta capa es IP (Internet Protocol), que se encarga de la dirección IP y el encaminamiento de los paquetes.
   
4. **Capa de Enlace**: Maneja la transmisión de datos dentro de una red local. Incluye protocolos como Ethernet y Wi-Fi.


### 2.2 Protocolo IP (Internet Protocol)
El protocolo IP se encarga de la direccionamiento y el encaminamiento de los paquetes de datos desde el origen hasta el destino. Cada dispositivo en una red TCP/IP tiene una dirección IP única que lo identifica.

#### Versiones de IP
- **IPv4**: La versión más utilizada, utiliza direcciones de 32 bits (por ejemplo, 192.168.0.1).
- **IPv6**: La nueva versión, desarrollada debido a la escasez de direcciones IPv4, utiliza direcciones de 128 bits (por ejemplo, 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

#### Encaminamiento
El encaminamiento es el proceso por el cual los routers (enrutadores) determinan el mejor camino para enviar un paquete de datos desde su origen hasta su destino final. Los routers utilizan tablas de encaminamiento para tomar estas decisiones.


### 2.3 Protocolo TCP (Transmission Control Protocol)
TCP proporciona una comunicación fiable y ordenada entre aplicaciones. Divide los datos en segmentos y los envía al destinatario, asegurando que se entreguen correctamente y en el orden adecuado.

#### Características de TCP
- **Conexión Orientada**: TCP establece una conexión entre el origen y el destino antes de transmitir datos. Este proceso se llama establecimiento de conexión o handshake (apretón de manos).
  
- **Fiabilidad**: TCP garantiza la entrega de datos mediante el uso de confirmaciones (ACKs) y la retransmisión de segmentos perdidos.
  
- **Control de Flujo**: TCP ajusta la velocidad de transmisión de datos según la capacidad del receptor para evitar la congestión.
  
- **Control de Congestión**: TCP implementa algoritmos para evitar la sobrecarga de la red.


### 2.4 Funcionamiento Conjunto de TCP/IP
1. **Fragmentación y Ensamblaje**: Los datos de una aplicación se dividen en segmentos por TCP. Cada segmento recibe un número de secuencia y se envuelve en un paquete IP que contiene las direcciones IP de origen y destino.

2. **Encaminamiento**: Los paquetes IP se envían a través de la red. Cada router en el camino utiliza la dirección IP de destino para determinar el siguiente salto en la ruta hacia el destino final.

3. **Entrega y Ensamblaje**: Una vez que los paquetes IP llegan al destino, TCP los reensambla en el orden correcto utilizando los números de secuencia y entrega los datos completos a la aplicación de destino.


### 2.5 Ejemplo de Comunicación TCP/IP
Supongamos que un usuario quiere acceder a un sitio web:

1. El navegador del usuario envía una solicitud HTTP (protocolo de aplicación) a través de TCP (capa de transporte).
2. TCP divide esta solicitud en segmentos y los envuelve en paquetes IP.
3. Los paquetes IP son enviados a través de la red, donde los routers encaminan los paquetes hasta el servidor web.
4. El servidor web recibe los paquetes, TCP reensambla los segmentos y entrega la solicitud HTTP al servidor web.
5. El servidor web responde con la página web solicitada, siguiendo el mismo proceso en sentido inverso.



# 3. Que es la web?
## 3.1 Resumen resumido
La web, también conocida como la World Wide Web (WWW), es un sistema de información interconectado a través de Internet, que permite a los usuarios acceder a una vasta colección de documentos y recursos multimedia. Fue inventada en 1989 por Tim Berners-Lee, un científico británico, mientras trabajaba en CERN (Organización Europea para la Investigación Nuclear). Su objetivo era facilitar el intercambio de información entre científicos de diferentes ubicaciones geográficas.

Berners-Lee desarrolló tres tecnologías fundamentales que aún forman la base de la web:

1. **HTML (HyperText Markup Language):** Un lenguaje de marcado utilizado para crear y estructurar páginas web mediante elementos como encabezados, párrafos, listas, enlaces, imágenes, etc.

2. **HTTP (HyperText Transfer Protocol):** Un protocolo para la transferencia de datos entre un cliente (navegador web) y un servidor web.

3. **URL (Uniform Resource Locator):** Un sistema de direcciones utilizado para localizar y acceder a recursos en la web.

#### Cómo Funciona la Web
El funcionamiento de la web se basa en la interacción entre clientes y servidores a través del protocolo HTTP. Su proceso básico es el siguiente:

1. **Solicitud del Cliente:** El usuario ingresa una URL en su navegador web (cliente), que envía una solicitud HTTP al servidor que aloja el sitio web.

2. **Respuesta del Servidor:** El servidor web recibe la solicitud y responde con el contenido solicitado, generalmente en forma de un documento HTML, pero también puede incluir otros recursos como imágenes, archivos CSS (Cascading Style Sheets) y JavaScript.

3. **Renderizado en el Cliente:** El navegador web recibe la respuesta del servidor y procesa el HTML, CSS y JavaScript para renderizar y mostrar la página web al usuario.


## 3  .2 Introducción a la Web para Desarrolladores
La Web, o World Wide Web (WWW), es un sistema de documentos interconectados y otros recursos, enlazados por hipervínculos y accesibles a través de Internet. Fue inventada por Tim Berners-Lee en 1989 mientras trabajaba en CERN, y ha evolucionado desde una colección de documentos estáticos a una plataforma dinámica e interactiva que soporta aplicaciones sofisticadas y servicios.

### Fundamentos de la Web
#### 1. **Protocolo HTTP**
El Protocolo de Transferencia de Hipertexto (HTTP) es el protocolo fundamental que permite la comunicación entre los navegadores web y los servidores. HTTP es un protocolo sin estado, lo que significa que cada solicitud es independiente y no retiene información de solicitudes anteriores. Esto se compensa con el uso de cookies, sesiones y otras técnicas de gestión de estado.

- **HTTP/1.1**: Introdujo mejoras como conexiones persistentes y chunked transfer encoding.
- **HTTP/2**: Mejora la eficiencia y velocidad mediante multiplexación de solicitudes y compresión de encabezados.
- **HTTP/3**: Utiliza el protocolo QUIC basado en UDP para reducir la latencia y mejorar la seguridad y rendimiento.

#### 2. **HTML (HyperText Markup Language)**

HTML es el lenguaje estándar para crear y estructurar contenido en la web. Utiliza una serie de etiquetas (tags) para definir elementos como párrafos, encabezados, enlaces, imágenes, listas, formularios y más.

- **HTML4**: Incluyó formularios, tablas y marcos (frames).
- **HTML5**: Introdujo nuevas etiquetas semánticas, soporte para audio y video nativo, gráficos SVG y Canvas, y APIs para almacenamiento local y geolocalización.

#### 3. **CSS (Cascading Style Sheets)**

CSS es un lenguaje de estilo utilizado para describir la presentación de un documento HTML. Permite separar el contenido (HTML) del diseño visual, facilitando el mantenimiento y la flexibilidad.

- **CSS1**: Primera versión con soporte básico para fuentes, colores y alineación.
- **CSS2**: Añadió soporte para medios de impresión, posicionamiento y pseudo-elementos.
- **CSS3**: Modularizó el estándar en diferentes módulos (flexbox, grid, animaciones, transiciones) y añadió soporte para media queries, transformaciones 3D y efectos de sombra.

#### 4. **JavaScript**

JavaScript es un lenguaje de programación que permite crear contenido dinámico y interactivo en la web. Se ejecuta en el navegador del cliente y puede manipular el DOM (Document Object Model) para actualizar el contenido de la página sin necesidad de recargarla.

- **ES5**: Estándarización de muchas características como JSON, array methods (forEach, map, filter).
- **ES6 (ECMAScript 2015)**: Introdujo características como clases, módulos, arrow functions, let/const, y promesas.
- **Frameworks y Librerías**: Incluyen React, Angular, Vue.js, que facilitan la creación de aplicaciones web complejas y reactivas.

#### 5. **DOM (Document Object Model)**

El DOM es una representación estructurada de un documento HTML o XML como una estructura de árbol. JavaScript puede interactuar con el DOM para modificar el contenido, estructura y estilo de una página web en tiempo real.

### Desarrollo Web: Frontend y Backend

#### Frontend Development

El desarrollo frontend se enfoca en la parte de la web que los usuarios interactúan directamente. Los desarrolladores frontend utilizan HTML, CSS y JavaScript para crear interfaces de usuario atractivas y funcionales.

1. **HTML**: Marca la estructura del contenido.
2. **CSS**: Aplica el diseño visual y el estilo.
3. **JavaScript**: Añade interactividad y comportamiento dinámico.

**Herramientas y Frameworks**:
- **React**: Biblioteca de JavaScript para construir interfaces de usuario.
- **Angular**: Framework de aplicaciones web desarrollado por Google.
- **Vue.js**: Framework progresivo para construir interfaces de usuario.

**Build Tools**:
- **Webpack**: Empaquetador de módulos.
- **Babel**: Compilador de JavaScript.
- **Sass/Less**: Preprocesadores CSS.

#### Backend Development

El desarrollo backend se ocupa de la lógica del servidor, la gestión de bases de datos y la comunicación entre el servidor y el cliente. Los desarrolladores backend trabajan con lenguajes de programación como JavaScript (Node.js), Python, Ruby, PHP, Java y frameworks como Express, Django, Ruby on Rails, Laravel y Spring.

**Componentes Clave**:
- **Servidores Web**: Apache, Nginx.
- **Bases de Datos**: MySQL, PostgreSQL, MongoDB.
- **APIs**: REST, GraphQL para la comunicación entre frontend y backend.
- **Autenticación y Autorización**: JWT, OAuth para la gestión de usuarios y permisos.

### Tecnologías y Conceptos Avanzados

#### 1. **Single Page Applications (SPA)**

SPAs son aplicaciones web que cargan una sola página HTML y actualizan dinámicamente el contenido según la interacción del usuario, utilizando JavaScript. React, Angular y Vue.js son populares para construir SPAs.

#### 2. **Progressive Web Apps (PWA)**

Las PWAs combinan lo mejor de las aplicaciones web y móviles, ofreciendo experiencias rápidas, confiables y atractivas. Utilizan tecnologías como Service Workers para trabajar offline y Push Notifications para reenganchar a los usuarios.

#### 3. **Microservicios**

Arquitectura en la que una aplicación se divide en pequeños servicios independientes que se comunican entre sí a través de APIs. Cada servicio es autónomo y puede ser desarrollado, desplegado y escalado de manera independiente.

#### 4. **CI/CD (Continuous Integration/Continuous Deployment)**

Prácticas de desarrollo que automatizan el proceso de integración y despliegue de código, facilitando la entrega rápida y fiable de software. Herramientas populares incluyen Jenkins, Travis CI y GitHub Actions.

#### 5. **Serverless Computing**

Modelo de ejecución en el que el proveedor de la nube gestiona la infraestructura y la asignación de recursos. Los desarrolladores escriben funciones que se ejecutan en respuesta a eventos y no gestionan servidores directamente. AWS Lambda, Azure Functions y Google Cloud Functions son ejemplos de servicios serverless.

### Seguridad en la Web

La seguridad es un aspecto crucial del desarrollo web. Algunas prácticas esenciales incluyen:

- **Cifrado HTTPS**: Protege la comunicación entre el cliente y el servidor.
- **Validación de Entrada**: Prevenir inyecciones SQL, cross-site scripting (XSS) y otros ataques.
- **Gestión de Sesiones**: Utilizar tokens seguros y expirar sesiones inactivas.
- **Control de Acceso**: Implementar políticas de acceso y autorización robustas.

### Futuro de la Web

La web sigue evolucionando con nuevas tecnologías y estándares. Algunas tendencias emergentes incluyen:

- **WebAssembly (Wasm)**: Permite ejecutar código de bajo nivel en el navegador, mejorando el rendimiento de aplicaciones complejas.
- **WebXR**: Estándar para experiencias de realidad aumentada y virtual en la web.
- **Inteligencia Artificial**: Integración de AI y machine learning en aplicaciones web para ofrecer experiencias personalizadas y análisis avanzados.

