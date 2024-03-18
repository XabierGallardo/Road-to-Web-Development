# API / Application Programming Interfaces

### Qué es una API? de manera sencilla
- Imagina que estás en un restaurante y quieres pedir comida. En lugar de ir a la cocina y hacer la comida tú mismo, simplemente le das tu pedido al camarero y él se encarga de llevarlo a la cocina, obtener la comida y traértela a la mesa.
- En el desarrollo web, una API es como el camarero en este ejemplo. Es un intermediario que te permite solicitar datos o servicios a un sistema externo, como una base de datos o un servicio web, sin necesidad de saber cómo funciona internamente ese sistema. Simplemente envías una solicitud a través de la API y recibes una respuesta con los datos que necesitas.
- Por ejemplo, si estás construyendo un sitio web de comercio electrónico, podrías utilizar una API para solicitar información sobre los productos disponibles en tu inventario desde una base de datos externa. La API se encargaría de obtener esos datos y devolvértelos en un formato que puedas usar en tu sitio web.
- En resumen, una API en el desarrollo web es como un camarero que te ayuda a obtener datos o servicios de otros sistemas sin tener que preocuparte por los detalles internos de cómo funcionan esos sistemas. Te permite interactuar con otros sistemas de manera sencilla y eficiente.

Las APIs pueden ser utilizadas para una variedad de propósitos, como acceder a funcionalidades de un sistema operativo, interactuar con servicios web, consumir datos de bases de datos, enviar y recibir datos entre aplicaciones, y mucho más. Permiten la integración de sistemas y aplicaciones de manera eficiente y efectiva.

*En el contexto de desarrollo web, una API generalmente se refiere a un conjunto de puntos de acceso (endpoints) que una aplicación web expone para permitir que otras aplicaciones o servicios accedan a sus datos o funcionalidades de manera controlada y segura. Estos endpoints pueden aceptar solicitudes en ciertos formatos (por ejemplo, JSON o XML) y devolver respuestas estructuradas que contienen la información solicitada.*

En resumen, una API proporciona una manera estándarizada y segura para que las aplicaciones se comuniquen entre sí y accedan a funcionalidades o datos de otras aplicaciones o sistemas. Esto facilita la interoperabilidad y la integración de sistemas en el desarrollo de software.


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

# Qué es una API? Nociones básicas
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
    <img src="../Images/tiposAPI.png" alt="Tipos de API">
</p>


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


## Some other concepts
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

## API Specifications
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
