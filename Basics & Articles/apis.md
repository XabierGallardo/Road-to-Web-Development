# API / Application Programming Interface

## **¿Qué es una API?**

Una **API (Application Programming Interface)** es un conjunto de definiciones, protocolos y herramientas que permite la comunicación entre diferentes sistemas de software. Es una interfaz que especifica cómo interactuar con un sistema o una aplicación, proporcionando métodos y reglas que facilitan el intercambio de datos y funcionalidades sin necesidad de conocer su implementación interna.

---

### **1. Características Clave de una API**
- **Interoperabilidad:** Facilita la comunicación entre diferentes aplicaciones o sistemas, independientemente del lenguaje de programación o la plataforma.
- **Encapsulación:** Oculta la complejidad del sistema interno, exponiendo solo lo necesario para la interacción.
- **Reusabilidad:** Las APIs permiten reutilizar funcionalidades existentes en nuevos desarrollos.
- **Estándares:** Las APIs suelen seguir estándares como REST, SOAP o GraphQL, lo que las hace predecibles y consistentes.

---

### **2. Tipos de APIs**

Las APIs pueden clasificarse según su uso, accesibilidad y el estilo arquitectónico utilizado. 

#### **2.1. Según Accesibilidad**

1. **APIs Públicas (Open APIs):**
   - Están disponibles públicamente para cualquier desarrollador.
   - Generalmente requieren autenticación mediante claves API.
   - Se utilizan para ampliar el alcance de un servicio.
   - **Ejemplo:** API de Google Maps, API de Twitter.

2. **APIs Privadas:**
   - Solo son accesibles dentro de una organización.
   - Diseñadas para integrar sistemas internos.
   - Mejoran la eficiencia operativa y la seguridad al restringir el acceso.
   - **Ejemplo:** API para gestionar los datos internos de empleados en una empresa.

3. **APIs de Socios (Partner APIs):**
   - Limitan el acceso a socios comerciales específicos.
   - Están diseñadas para fomentar colaboraciones controladas entre organizaciones.
   - **Ejemplo:** API de un proveedor de pagos para integrarla con socios comerciales.

4. **APIs Compuestas (Composite APIs):**
   - Combinan múltiples llamadas de API en una sola solicitud.
   - Útiles para operaciones que involucran múltiples recursos o datos.
   - **Ejemplo:** Una API que devuelva el historial de pedidos de un usuario junto con sus detalles de perfil.

---

#### **2.2. Según el Estilo Arquitectónico**

1. **APIs REST (Representational State Transfer):**
   - Arquitectura basada en recursos accesibles a través de URLs.
   - Usa métodos HTTP (GET, POST, PUT, DELETE) para interactuar con recursos.
   - Es ligera, rápida y ampliamente utilizada.
   - **Ejemplo:** API de GitHub.

   **Ejemplo de interacción REST:**
   ```http
   GET https://api.example.com/users/123
   ```
   Respuesta:
   ```json
   {
       "id": 123,
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```

2. **APIs SOAP (Simple Object Access Protocol):**
   - Protocolo basado en XML para intercambio de información.
   - Ofrece seguridad avanzada y transacciones robustas.
   - Más pesado en comparación con REST.
   - **Ejemplo:** APIs en sistemas bancarios o gubernamentales.

   **Ejemplo de solicitud SOAP:**
   ```xml
   <soap:Envelope>
       <soap:Body>
           <GetUserDetails>
               <UserId>123</UserId>
           </GetUserDetails>
       </soap:Body>
   </soap:Envelope>
   ```

3. **APIs GraphQL:**
   - Permite que los clientes soliciten exactamente los datos que necesitan.
   - Usa un único endpoint para todas las consultas.
   - Ideal para aplicaciones con datos complejos.
   - **Ejemplo:** API de Facebook.

   **Ejemplo de consulta GraphQL:**
   ```graphql
   query {
       user(id: "123") {
           name
           email
       }
   }
   ```

4. **APIs RPC (Remote Procedure Call):**
   - Invocan funciones en un servidor remoto como si fueran locales.
   - Hay dos variantes: JSON-RPC y XML-RPC.
   - Más simples, pero menos flexibles.
   - **Ejemplo:** Sistemas de control remoto.

---

#### **2.3. Según Funcionalidad**

1. **APIs de Datos:**
   - Proporcionan acceso a datos almacenados en una base de datos o sistema.
   - **Ejemplo:** APIs meteorológicas que devuelven pronósticos del tiempo.

2. **APIs de Servicios:**
   - Permiten interactuar con servicios externos como pagos, mensajería, etc.
   - **Ejemplo:** API de PayPal para procesar pagos.

3. **APIs de Hardware:**
   - Interactúan con dispositivos físicos como cámaras, sensores o impresoras.
   - **Ejemplo:** API de la cámara en dispositivos móviles.

4. **APIs de Sistemas Operativos:**
   - Proveen acceso a funciones del sistema operativo.
   - **Ejemplo:** API de Windows para manipular el sistema de archivos.

5. **APIs de Bibliotecas/Frameworks:**
   - Permiten utilizar funcionalidades predefinidas en bibliotecas o frameworks.
   - **Ejemplo:** API de jQuery o API de React.

---

### **3. Cómo Funciona una API**

1. **Solicitud:** Un cliente realiza una solicitud (por ejemplo, a través de HTTP) especificando el recurso o servicio requerido.
2. **Procesamiento:** El servidor que implementa la API procesa la solicitud, ejecutando las operaciones necesarias.
3. **Respuesta:** El servidor envía una respuesta, generalmente en formato JSON o XML, con los datos solicitados o un estado del resultado.

---

### **4. Componentes Principales de una API**

1. **Endpoint:** Es la URL que expone la funcionalidad o recurso.
2. **Métodos:** Son las operaciones disponibles para interactuar con la API (GET, POST, PUT, DELETE).
3. **Formato de Datos:** JSON, XML o cualquier formato estándar para el intercambio de datos.
4. **Autenticación:** Métodos para garantizar que solo los usuarios autorizados accedan a la API (OAuth, tokens API).
5. **Documentación:** Proporciona detalles sobre cómo usar la API.

---

### **5. Ejemplo de Uso Práctico de una API**

#### **API RESTful: Clima**
1. **URL del Endpoint:**
   ```http
   GET https://api.openweathermap.org/data/2.5/weather?q=London&appid=tu_api_key
   ```
2. **Respuesta (JSON):**
   ```json
   {
       "weather": [
           {
               "description": "clear sky"
           }
       ],
       "main": {
           "temp": 285.32
       },
       "name": "London"
   }
   ```

---

### **6. Ventajas de las APIs**

- **Facilitan la integración:** Permiten que diferentes sistemas trabajen juntos sin esfuerzo.
- **Aceleran el desarrollo:** Ofrecen funcionalidades preexistentes para evitar desarrollarlas desde cero.
- **Escalabilidad:** Permiten dividir sistemas grandes en componentes independientes.
- **Innovación:** Abren nuevas posibilidades para aplicaciones de terceros.

---

### **7. Conclusión**

Las **APIs** son fundamentales en el desarrollo de software moderno, permitiendo la integración, reusabilidad y escalabilidad de sistemas. Existen múltiples tipos de APIs, cada uno diseñado para cumplir propósitos específicos, desde compartir datos hasta interactuar con hardware. Su correcta implementación y uso puede ser clave para el éxito de una aplicación o sistema.



---



## Relación entre un servidor y una API
La diferencia principal entre un **servidor** y una **API** radica en sus roles y funcionalidades dentro de una arquitectura de software. Mientras que un servidor es la infraestructura física o virtual que alberga y ejecuta servicios, una API es una interfaz que define cómo interactuar con esos servicios. A continuación, se detalla la relación y diferencias entre ambos conceptos:

---

### **1. Qué es un Servidor**
Un servidor es una máquina (física o virtual) o programa que ofrece servicios a otras máquinas o programas (clientes) a través de una red. Estos servicios pueden incluir almacenamiento de datos, procesamiento de solicitudes o entrega de contenido.

#### **Características principales de un servidor:**
- **Físico o virtual:** Puede ser un hardware dedicado o un sistema en la nube.
- **Función general:** Maneja solicitudes de los clientes y las procesa según su propósito.
- **Versatilidad:** Puede albergar varios servicios, como servidores web, de correo, de bases de datos, etc.
- **Ejemplo común:** Un servidor web como **Apache** o **NGINX**, que entrega contenido HTML al navegador.

#### **Ejemplo de un servidor en acción:**
1. Un usuario accede a `www.example.com`.
2. El servidor recibe la solicitud, busca el archivo correspondiente y lo envía al navegador del usuario.

---

### **2. Qué es una API**
Una **API** es una interfaz que define cómo los clientes (aplicaciones, sistemas o dispositivos) pueden interactuar con un servicio que normalmente se ejecuta en un servidor. Es el "puente" que permite acceder a los servicios de un servidor sin conocer sus detalles internos.

#### **Características principales de una API:**
- **Interfaz de comunicación:** Define un conjunto de reglas para enviar y recibir datos.
- **No es hardware:** Es puramente un conjunto de métodos, rutas y reglas.
- **Estándares específicos:** Como REST, SOAP o GraphQL.
- **Usada para integrar:** Facilita la interacción entre diferentes aplicaciones o sistemas.

#### **Ejemplo de una API en acción:**
1. Una aplicación móvil quiere mostrar el clima.
2. Envía una solicitud a una API de clima (como la de OpenWeatherMap).
3. La API responde con datos estructurados (generalmente en JSON) sobre la temperatura y condiciones actuales.

---

### **Diferencias entre un Servidor y una API**

| **Aspecto**           | **Servidor**                                                                                       | **API**                                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Definición**        | Máquina física o virtual que ofrece servicios a través de una red.                               | Interfaz que define cómo interactuar con un servicio o aplicación alojado en un servidor.              |
| **Función principal** | Ejecutar y albergar aplicaciones, bases de datos, archivos o servicios.                          | Proveer acceso a funcionalidades o datos de una aplicación o servicio de forma estructurada.           |
| **Tipo de entidad**   | Puede ser hardware (servidor físico) o software (servidor virtual o servicio).                   | Es un conjunto de rutas, métodos y reglas para acceder a funcionalidades o datos de un sistema.        |
| **Interacción**       | Responde solicitudes de clientes (navegadores, dispositivos, etc.) y entrega recursos (HTML, datos, etc.). | Responde solicitudes específicas sobre datos o funcionalidades, generalmente en un formato como JSON o XML. |
| **Ejemplo**           | Un servidor web que entrega un archivo HTML a un navegador.                                      | Una API que entrega información del clima en formato JSON cuando se llama desde una aplicación móvil.  |
| **Relación**          | Alberga y ejecuta la lógica que permite que la API funcione.                                     | Define cómo interactuar con los servicios ofrecidos por el servidor.                                   |

---

### **3. Relación entre un Servidor y una API**
1. **Complementarios:** Un servidor a menudo es el "hogar" donde reside la lógica que define las funcionalidades expuestas por una API.
2. **Ejemplo:**
   - **Servidor:** Un servidor ejecuta un backend hecho en **Node.js** con Express.
   - **API:** Ese backend expone rutas RESTful como `/users` o `/products` que los clientes pueden consumir.

---

### **4. Caso Práctico**
Imagina que tienes una aplicación móvil para pedir comida en línea.

#### **Servidor:**
- Es el sistema central que:
  - Procesa pedidos.
  - Interactúa con bases de datos para obtener información del menú.
  - Administra usuarios y pagos.

#### **API:**
- Es la interfaz que:
  - Define rutas como `/menu` (para obtener el menú) y `/order` (para hacer pedidos).
  - Se asegura de que la aplicación móvil pueda interactuar con el servidor sin conocer detalles internos.

---

### **Conclusión**
En resumen, un **servidor** es el lugar donde se ejecutan las aplicaciones o servicios, mientras que una **API** es el conjunto de reglas que permite que otros sistemas accedan a esos servicios de forma controlada y estructurada. Ambos son fundamentales en la arquitectura moderna de aplicaciones, pero cumplen roles distintos.


---


## Explicacion 1 / APIs y APIs REST
### **¿Qué es una API en programación?**

Una **API** (Application Programming Interface, o Interfaz de Programación de Aplicaciones) es un conjunto de reglas y herramientas que permite a diferentes sistemas de software comunicarse entre sí. En términos más simples, es un intermediario que permite que dos aplicaciones hablen entre sí. 

Por ejemplo, cuando usas una aplicación en tu teléfono móvil para consultar el clima, la aplicación realiza una solicitud a un servidor y obtiene los datos meteorológicos en tiempo real a través de una API.

---

#### **Componentes clave de una API**
1. **Interfaz**: Define cómo las aplicaciones interactúan con el sistema. Esto incluye las funciones o endpoints disponibles, los parámetros requeridos y los formatos de las respuestas.
2. **Protocolo**: Define las reglas para la comunicación. Por ejemplo, las API web suelen usar el protocolo HTTP.
3. **Entrada y salida**:
   - **Entrada**: Una solicitud que el cliente envía al servidor con parámetros específicos.
   - **Salida**: Una respuesta del servidor al cliente con los datos solicitados.

---

#### **Ejemplo de una API simple**

Supongamos que una tienda tiene una API para consultar productos. Podríamos usar un endpoint como:

- **URL de la API**: `https://api.tienda.com/productos`
- **Solicitud**: `GET /productos`
- **Respuesta**:
   ```json
   [
       { "id": 1, "nombre": "Laptop", "precio": 800 },
       { "id": 2, "nombre": "Mouse", "precio": 20 }
   ]
   ```

En este ejemplo:
- El cliente solicita todos los productos disponibles en la tienda.
- El servidor devuelve una lista de productos en formato JSON.

---

### **¿Qué es una API REST en programación web?**

Una **API REST (Representational State Transfer)** es un estilo arquitectónico para diseñar APIs que permiten la comunicación entre un cliente (como un navegador o aplicación móvil) y un servidor. REST se basa en principios sencillos que aprovechan el protocolo HTTP, lo que lo convierte en una de las formas más populares de diseñar APIs en la programación web.

---

#### **Principios de una API REST**

1. **Cliente-servidor**: El cliente (por ejemplo, el navegador) y el servidor (donde se alojan los datos) están separados. Esto mejora la escalabilidad y permite que ambos evolucionen de manera independiente.

2. **Sin estado**: Cada solicitud del cliente al servidor debe contener toda la información necesaria para procesarla. El servidor no guarda información sobre el estado de la sesión del cliente entre solicitudes.

3. **Caché**: Las respuestas del servidor deben ser cacheables para mejorar el rendimiento y reducir la carga en el servidor.

4. **Uniformidad**:
   - Usar rutas coherentes para acceder a recursos.
   - Por ejemplo:
     - `GET /usuarios` para obtener todos los usuarios.
     - `GET /usuarios/1` para obtener un usuario con ID 1.

5. **Representación de recursos**: Los datos se representan en formatos legibles como JSON o XML. REST no se limita a un formato específico, pero JSON es el más común.

6. **Uso de métodos HTTP**: REST utiliza los métodos HTTP estándar para realizar diferentes acciones:
   - **GET**: Obtener datos (sin modificar el recurso).
   - **POST**: Crear nuevos recursos.
   - **PUT**: Actualizar un recurso existente.
   - **DELETE**: Eliminar un recurso.
   - **PATCH**: Actualizar parcialmente un recurso.

---

#### **Ejemplo de API REST**

Supongamos que queremos crear, leer, actualizar y eliminar usuarios de una aplicación. Nuestra API REST podría tener los siguientes endpoints:

| Método HTTP | Endpoint         | Acción                                 |
|-------------|------------------|----------------------------------------|
| `GET`       | `/usuarios`      | Obtener una lista de usuarios          |
| `GET`       | `/usuarios/:id`  | Obtener un usuario específico por ID   |
| `POST`      | `/usuarios`      | Crear un nuevo usuario                 |
| `PUT`       | `/usuarios/:id`  | Actualizar un usuario existente        |
| `DELETE`    | `/usuarios/:id`  | Eliminar un usuario por ID             |

**Ejemplo práctico (en JSON)**:

1. **Crear un usuario**:
   - **Solicitud**:
     ```http
     POST /usuarios
     Content-Type: application/json
     Body: { "nombre": "Juan", "edad": 25 }
     ```
   - **Respuesta**:
     ```json
     { "mensaje": "Usuario creado", "id": 1 }
     ```

2. **Obtener todos los usuarios**:
   - **Solicitud**:
     ```http
     GET /usuarios
     ```
   - **Respuesta**:
     ```json
     [
         { "id": 1, "nombre": "Juan", "edad": 25 },
         { "id": 2, "nombre": "Ana", "edad": 30 }
     ]
     ```

3. **Actualizar un usuario**:
   - **Solicitud**:
     ```http
     PUT /usuarios/1
     Content-Type: application/json
     Body: { "nombre": "Juan Pérez", "edad": 26 }
     ```
   - **Respuesta**:
     ```json
     { "mensaje": "Usuario actualizado" }
     ```

4. **Eliminar un usuario**:
   - **Solicitud**:
     ```http
     DELETE /usuarios/1
     ```
   - **Respuesta**:
     ```json
     { "mensaje": "Usuario eliminado" }
     ```

---

#### **Beneficios de usar una API REST**

1. **Simplicidad**: REST utiliza los principios y verbos HTTP estándar, lo que lo hace fácil de entender.
2. **Escalabilidad**: La separación cliente-servidor permite una escalabilidad eficiente.
3. **Portabilidad**: REST usa formatos estándar como JSON, lo que permite que sea utilizado por diferentes lenguajes de programación.
4. **Independencia de plataforma**: El cliente y el servidor pueden estar en plataformas diferentes y aún comunicarse sin problemas.

---

### **Resumen**

- **API**: Es un puente entre sistemas, permitiendo la comunicación entre aplicaciones.
- **API REST**: Es un tipo de API diseñada siguiendo los principios de REST. Es popular en aplicaciones web por su simplicidad, flexibilidad y uso de estándares HTTP.

REST es ampliamente utilizado para construir aplicaciones modernas, especialmente en el desarrollo de frontends que necesitan comunicarse con backends. Su diseño basado en recursos y el uso de JSON como formato estándar lo hacen una opción versátil y poderosa.

___

## Explicacion 2 / Qué es una API? Ejemplo sencillo
- Imagina que estás en un restaurante y quieres pedir comida. En lugar de ir a la cocina y hacer la comida tú mismo, simplemente le das tu pedido al camarero y él se encarga de llevarlo a la cocina, obtener la comida y traértela a la mesa.
- En el desarrollo web, una API es como el camarero en este ejemplo. Es un intermediario que te permite solicitar datos o servicios a un sistema externo, como una base de datos o un servicio web, sin necesidad de saber cómo funciona internamente ese sistema. Simplemente envías una solicitud a través de la API y recibes una respuesta con los datos que necesitas.
- Por ejemplo, si estás construyendo un sitio web de comercio electrónico, podrías utilizar una API para solicitar información sobre los productos disponibles en tu inventario desde una base de datos externa. La API se encargaría de obtener esos datos y devolvértelos en un formato que puedas usar en tu sitio web.
- En resumen, una API en el desarrollo web es como un camarero que te ayuda a obtener datos o servicios de otros sistemas sin tener que preocuparte por los detalles internos de cómo funcionan esos sistemas. Te permite interactuar con otros sistemas de manera sencilla y eficiente.

Las APIs pueden ser utilizadas para una variedad de propósitos, como acceder a funcionalidades de un sistema operativo, interactuar con servicios web, consumir datos de bases de datos, enviar y recibir datos entre aplicaciones, y mucho más. Permiten la integración de sistemas y aplicaciones de manera eficiente y efectiva.

**En el contexto de desarrollo web, una API generalmente se refiere a un conjunto de puntos de acceso (endpoints) que una aplicación web expone para permitir que otras aplicaciones o servicios accedan a sus datos o funcionalidades de manera controlada y segura. Estos endpoints pueden aceptar solicitudes en ciertos formatos (por ejemplo, JSON o XML) y devolver respuestas estructuradas que contienen la información solicitada.**

En resumen, una API proporciona una manera estándarizada y segura para que las aplicaciones se comuniquen entre sí y accedan a funcionalidades o datos de otras aplicaciones o sistemas. Esto facilita la interoperabilidad y la integración de sistemas en el desarrollo de software.

## Qué es una API? Nociones básicas
- Las API nos permiten aprovechar el desarrollo de otras empresas para nuestra app. Desde las funcionalidades de mapas y geolocalización de google maps como las pasarelas de pagos de Paypal o Stripe.
- Las API permite que nuestras aplicaciones se conecten con otras.
- Capa de abstracción para que dos sistemas se comuniquen. La **capa de abstración** nos permite interactuar con un sistema sin necesidad de saber qué pasa por abajo. Como el volante que nos permite mover el auto sin necesitar saber qué sucede mecánicamente
- Una API es una interfaz. Application Programming Interface. Una **interfaz** para que se comuniquen aplicaciones y compartan datas entre ellos
- **Arquitectura de software** es la forma en que está diseñado un sistema y cómo se organizan sus componentes, qué funciones cumplen
- Un **servicio web** permite la comunicación entre equipos en una red, que se comunican con ciertos estándares y protocolos, como el HTTP. Es la base de las API remotas
- **REST** es una arquitectura, las APIS pueden ser de varios tipos. Representation State Transfer. Esta arquitectura implica que pueden guardarse los datos en cache, que el estado no se envía en las peticiones y que definimos qué datos permitimos que otra aplicación accede, revise o manipule de nuestra app
- XML es el formato tradicional de envío de datos, aunque hoy en día el formato más usado es **JSON** y el standard de hoy en día de envío de datos.
- Las APIS pueden ser locales o remotas. Si desarrollamos una app de Android que require que las notificaciones vibren, nos comunicamos con la API local de vibración del teléfono. Las APIs remotas consumen datos que están físicamente en otro sitio y usan servicios web usando el protocolo HTTP. En su momento se usaba el protocolo SOAP, pero hoy se usa REST, que es la arquitectura más usada para las APIs. Cuando hablamos de REST estamos hablando de **Restful**
- Cada recurso que consultamos, tiene un identificador único llamado **URI**, así podemos acceder a cualquier recurso o lista de ellos.
- Cuando solicitamos información a una API, el servidor nos puede contestar con varios códigos para saber qué pasó con nuestra petición. 2xx success, 3xx redirection, 4xx error, 5xx error en el servidor
- **Métodos HTTP**: *GET* recibir info, *POST* enviar info, *PUT* actualizar info existente, *DELETE* borrar un recurso.
- Las APIs puede devolver info en formato JSON, XML o texto plano.

<p>
    <img src="../img/tiposAPI.png" alt="Tipos de API">
</p>

# API Security
<p align="center">
    <img src="../img/apiSecurity.png" alt="API Security">
</p>



### API Crud y ABM
"CRUD" es un acrónimo que se utiliza comúnmente en el desarrollo de software para describir las operaciones básicas que pueden realizarse sobre los datos de una aplicación. CRUD significa:

- **Create** (Crear): La capacidad de crear nuevos registros de datos en una base de datos o en algún otro tipo de almacenamiento.
- **Read** (Leer): La capacidad de leer, recuperar o consultar los datos existentes de la base de datos o de otro tipo de almacenamiento.
- **Update** (Actualizar): La capacidad de actualizar o modificar los datos existentes en la base de datos o en otro tipo de almacenamiento.
- **Delete** (Eliminar): La capacidad de eliminar registros de datos existentes en la base de datos o en otro tipo de almacenamiento.

Por lo tanto, un "API CRUD" se refiere a una interfaz de programación de aplicaciones (API) que proporciona métodos o endpoints para realizar estas operaciones CRUD en los datos de una aplicación. Por ejemplo, si estás construyendo una aplicación web que gestiona una lista de tareas, tu API CRUD podría proporcionar endpoints para crear nuevas tareas, recuperar todas las tareas existentes, actualizar tareas existentes y eliminar tareas.

El uso de un API CRUD facilita el desarrollo de aplicaciones al proporcionar una interfaz coherente y predecible para interactuar con los datos, lo que simplifica la implementación tanto del lado del cliente como del servidor.


"ABM" es un acrónimo que significa "Alta, Baja y Modificación". En el contexto de la programación y el desarrollo de software, un "ABM" se refiere a un conjunto de operaciones básicas que se realizan sobre una entidad o conjunto de datos. Estas operaciones son:

- **Alta (Create)**: Implica la creación de nuevos registros o entidades en una base de datos o sistema.
  
- **Baja (Delete)**: Implica la eliminación de registros o entidades existentes en una base de datos o sistema.
  
- **Modificación (Update)**: Implica la actualización o modificación de registros o entidades existentes en una base de datos o sistema.

Un ABM se usa comúnmente en el desarrollo de software para aplicaciones que gestionan datos, como sistemas de gestión de bases de datos, aplicaciones web, aplicaciones móviles, entre otros. Proporciona las operaciones básicas necesarias para administrar y manipular los datos dentro de una aplicación.

Por ejemplo, en un sistema de gestión de empleados, el ABM permitiría agregar nuevos empleados (Alta), eliminar empleados existentes (Baja) y actualizar la información de los empleados (Modificación).

En resumen, un ABM es un conjunto de operaciones básicas que permiten crear, leer, actualizar y eliminar datos en una aplicación o sistema de software.

## API KEY
- Una API key es un identificador que sirve para la autenticación de un usuario para el uso de un servicio. Es decir una llave y contraseña para autenticarte cada vez que se utiliza
- Las API keys facilitan la posibilidad de que diferentes servicios se conecten entre sí.
- Un ejemplo son las API que se pueden realizar desde otros software con redes sociales como fb, twitter e ig. Siendo la propia red quien facilita estas APIs de integracion destinadas a servicios para poder trabajar sobre el primario
- Una API es fundamentalmente una forma de hacer una solicitud a otra aplicación



# What is a REST API
*REST APIs provide a flexible, lightweight way to integrate applications and it is the most common method for connecting components in microservices architectures*

**An API**, or *Application Programming Interface*, **is a set of rules that define how applications or devices can connect to and communicate with each other**

**A REST API is an API that conforms to the design principles of the REST** or *Representational State Transfer* architectural style

#### REST design principles
At the most basic level, **an API is a mechanism that enables an applications or service to access a resource within another application or service**. The application or service doing the accessing is called the client, and the application or service containing the resource is called the server.

Some APIs (SOAP or XML-RPC) impose a strict framework on developers. But REST APIs can be developed using virtually any programming language and support a variety of data formats. The only requirement is that they align to the following 6 REST design principles

1. **Uniform interface**: All API request for the same resource should look the same, no matter where the request comes from. The REST API should ensure that the same piece of data, such as the name or email address of an user, belongs to only one uniform resource identifier (URI)

2. **Client-server decoupling**: Client and server apps must be completely independent from each other. The only information the client application should know is the URI of the requested resource; it can't interact with the server application in any other ways. Similarly, a server application shouldn't modify the client application other than passing it to the requested data via HTTP

3. **Statelessness**: REST APIs are stateless, meaning that each request needs to include all the information necessary for processing it. REST APIs do not require any server-side sessions. Server apps aren't allowed to storey any data related to a client request

4. **Cacheability**: When possible, resources should be cacheable on the client or server side. Server responses also need to contain info about wether caching is allowed for the delivered resource. The goal is to improve performance on the client side, while increasing scalability on the server side

5. **Layered system architecture**: In REST APIs, the calls and responses go through different layers. REST APIs need to be designed so that neither the client nor the server can tell wether it communicates with the end application or an intermediary

6. **Code on demand**: This is an optional step, REST APIs usually send static resources, but in certain cases, responses can also contain executable code (Java applets). In these cases, the code should only run on-demand


# How REST APIs work
REST APIs communicate via HTTP request ot perform standard database functions like creating, reading, updating and deleting records (also known as CRUD) within a resource.

A REST API would use
- A **GET** request to retieve a record
- A **POST** request to create one
- A **PUT** request to update a record
- A **DELETE** request to delete one

All HTTP methods can be used in API calls. A well-designed REST API is similar to a website running in a web browser with built-in HTTP functionality

*The state of a resource at any particular instante or timestamp, is known as the resource representation*
This information can be delivered to a client in virtually any format including the popular JSON, HTML, XLT, Pyhton, PHP or plain text

Request headers and parameters are also important in REST API calls because they include important identifier information such as metadata, authorizations, uniform resource identifiers (URIs), caching, cookies and more
Request headers and response headers, along with conventional HTTP status codes, are used within well-designed REST APIs

### REST Client
The browser can act as an uncontrolled REST client (the website handles the browser requests).
The browser, for a long time, used an in-built function called XMLHttpRequest for all REST request.
But this was succeeded by FetchAPI, a modern, promise based approach to request.
Others examples are code libraries like axios, superagent and got or some dedicated apps like Postman, or a command line took like cURL.

### REST Service
The server.
There are many popular libraries that make creation of these servers a breeze, like ExpressJS for NodeJS and Django for Python

### REST API
This defines the endpoint and methods allowed to access/submit data to the server.
We will talk about this in great detail below. Other alternatives to this are: GraphQL, JSON-Pure and oData

### How does it work?
In broad terms, you ask the server for a certain data or ask it to save some data, and the server responds to the requests.

In programming terms, there is an endpoint (a URL) that the server is waiting to get a request.
We connect to that endpoint and send in some data about us (REST is stateless, no data about the request is stored) and the server responds with the correct response.

### Anatomy of REST
1. **Endpoint**: It's the URL where the REST Server is listening

2. **Method**: Earlier, I wrote that you can either request data or modify it, but how will the server know what kind of operation the client wants to perform? REST implements multiple 'methods' for different types of request, the following are most popular
*GET*: Get resource from the server
*POST*: Create resource to the server
*PATCH or PUT*: Update existing resource on the server
*DELETE*: Delete existing resource from the server

3. **Headers**: The additional details provided for communication between client and server. Some of the common headers are:

*Request* host (the IP of client), accept-language (language understandable by the client), user-agent (data about client, operating system and vendor)

*Response* status (the status of request or HTTP code), content-type (type of resource sent by server), set-cookie (sets cookies by server)

4. **Data**: Contains info you want to send to the server.


## Another APIs Explanation with examples
An API or *Application Programming Interface* is a way for 2 computers to talk to each other
Using an API would be like using a website on our browser
But instead of clicking buttons and filling out forms, we write code to explicity request data from a server

For example, we could visit the NASA website to look at asteroids or we could use their Rest API to request the raw JSON data that is shown on the screen
There are 3 main types, Private, Public and External

- Private APIs are classified as an in-house application for employees to automate business processes and delivery
- Public/Partner APIs are openly promoted but available for known developers or business partners
- External APIs are available to any third-party developer and are mostly designed or built for end-users/customers

APIs make it easier to access to a variety of resources
**APIs are efficient**, they can significantly reduce the amount of work and will speed up the development process of an application
**APIs make things simpler**


# Restful API vs Database
There are reasons to use a REST API, when we have an app that will be available to the public, we don't want to write our SQL queries directly in our code, as well as the credentials to connect to our server

Anyone with the knowledge could decompile our app and see our code and have access to the credentials to our database server
The good approach is to write an REST API to handle the flow of data between our app and database, since REST API should be designed to be accesed publicy, we'll only have to pass in the data, or just call the API we need
We don't need the server credentials to connect

If we're going local, then we could use the database approach of ours, since our app will be used only by our clients


# API Specifications

##### Service Object Access Protocol / SOAP
SOAP is a lightweight protocol for exchanging structured information in a decentralized, distributed environment
This contains rules guiding requests and responses sent from web applications using XML between systems through HTTP

##### GraphQL
GraphQL is a query language for APIs, it provides an absolute and simplified description of the data in APIs, which gives us the power to get the exact data we need
This makes easier to evolve APIs over time and also enables powerful developer tools

##### Representational State Transfer (REST)
*Representational State Transfer* or *REST* is a style of architecture that provides standars on the web between computer systems which makes communication flow easier within applications
REST APIs are stateless and can be used for seperation of concecrns between the client and the server

**RESTful** means they follow a set of rules or constraints known as **Representational State Transfer**, which has been the standard for API development since early 2000s


## How an API organizes the data?
A restful API organizes data entities or resources into a bunch of unique URLs or specifically URIs *Uniform Resource Identifiers*
URIs differentiate different types of data resources on a server *https://api.com/v2/comet*
```sh
https://api.com/v2
# Asteroid data
/asteroid
# Meteor data
/meteor
# Comet data
/comet

# Requesting asteroid data from an API
https://api.com/v2/asteroid
```

**https://api.com/v2** is the *Network Location*
**/comet** is the *Resource*

A client can get data about a resource by making a request to that endpoint over HTTP
The request message has a very specific format

## REQUEST
*The start line contains the URI we want to access* preceded by an HTTP verb or request which signal our intent with the resource
```sh
POST /dinosaur HTTP/1.1 
```
- **GET** / READ data
- **POST** / CREATE data
- **PATCH** / UPDATE data
- **DELETE** / DESTROY data

Below the start line we have the *Headers* that contain metadata about the request
```sh
Accept: application/json
Authorization: <token>
Connection: jeep-alive
```
- **Accept** header can tell the server we want the data in an specific format like *I only accept JSON*
- **Authorization** header can be used to tell the server that we're allowed to make that request

The body contains a custom payload of data
```sh
{
 "face": "anydata"
}
```
The server will receive the request message, then execute some code usualy to read from a database that can then be formatted into a response message

## RESPONSE
The top of the message contains a status code to tell the client what happened to their request
```sh
HTTP /1.1 200 OK
```
- **2xx** GOOD
- **4xx** Something WRONG with the request
- **5xx** Server BROKEN

After the status code we have the *Response Headers* which contain information about the server
```sh
Server: nginx
Age: 2323
Connection: keep-alive
```

Followed by the *Response Body* which contains the data payload and is usually formatted in JSON when talking about APIs
```sh
{
 "id": "123-xyz",
 "status": "success",
}
```

## About the architecture
The important part about this architecture is that it's **Stateless**
This means that the 2 parties don't need to store any info about each other, and every request response cycle is independent from all other communication
