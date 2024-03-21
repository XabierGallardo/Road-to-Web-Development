# Frontend roadmap
- **HTML**: Tags, basic structure, forms, links, tables
- **CSS**: Selectors, box model, positions, sizing, flexbox vs grid
- **JavaScript**: Variables, data types, loops, functions, DOM, asynchronous
- **React**: Components, State | Events, Styling react apps, Hooks (userEffect), ContextAPI, React Router, Authentication, Testing, Redux
- **TypeScript**: Using types, Object types, Array types, Tuplas, Enums, Union/Literal Types, Function types, Using it with React

# Backend roadmap
- **Internet**: How does internet works, HTTP, Browsers and how they work, DNS and how it works, Domain name & Hostingss
- **Framework**:  Node.js, Laravel, Django
- **OS**: Terminal, how does an OS works, Memory management, Interprocess communication, Threads and concurrency, Process management
- **Databases**: Relational (MySQL), Non-relational database (MongoDB, Firebase)
- **APIs**: Software that allows communication between 2 apps. Mainly REST & JSON APIs. CHeck auth protocols (Basic Auth & JWT)
- **Testing**: Unit testings
- **CI/CD**: Or Continuous Integration/Continuous Deployment. Mainly Github actions. Pratice of automatize creation, tests & deployment of our app to detect early problems before deployment
- **Architecture patterns**: A way to define through a pattern, the architecture that our app must have. From monolithic apps, to Microservices, SOA, Serverless, etc
- **Deployment**: Either VMs or Containers. *Docker* is a platform to work with contanerized apps. It packs all the code, imgs, tests from our app in an only package to be deployed in a server. *Kubernetes* allows us to handler different containers with different versions of our apps
- **Web servers**: From hardware servers (computers that use server software and it stores our app) to software servers. Software servers have different software components that manage the way the online users access our files (Apache, NGINX)
- **Scalability**: It's the ability to perfeorm well under increased or expanding workload. A solid base on our web app will allowIt will allows us to not have to modify the entire structure when it gets bigger. Coupling, Observability, Evolvability & Infrastucture are essential keys for this.

# Internet, como funciona?

1. **HTTP (Hypertext Transfer Protocol)**:
   - HTTP es un protocolo de comunicación utilizado para transferir datos en la World Wide Web (WWW). Funciona siguiendo un modelo cliente-servidor, donde el cliente (generalmente un navegador web) envía solicitudes de recursos al servidor y el servidor responde con los datos solicitados.
   - Las solicitudes HTTP pueden tener diferentes métodos, siendo los más comunes GET (para solicitar datos) y POST (para enviar datos).
   - Las respuestas HTTP incluyen un código de estado (como 200 para "OK" o 404 para "No encontrado") y el contenido solicitado (generalmente en formato HTML, aunque puede ser cualquier tipo de recurso web, como imágenes, archivos CSS, JavaScript, etc.).

2. **Protocolo seguro HTTPS**: En muchos casos, especialmente cuando se trata de transacciones financieras o datos confidenciales, se utiliza el protocolo HTTPS en lugar de HTTP. HTTPS es HTTP sobre SSL/TLS, lo que significa que la comunicación entre el navegador y el servidor está encriptada, proporcionando un mayor nivel de seguridad y privacidad.

3. **Solicitud y respuesta HTTP**: Una vez que se ha resuelto la dirección IP del servidor, el navegador envía una solicitud HTTP al servidor para obtener la página web solicitada. Esta solicitud incluye información como el método de solicitud (GET, POST, etc.), la URL y cualquier otro dato necesario. El servidor recibe esta solicitud, procesa la solicitud y envía una respuesta HTTP de vuelta al navegador, que generalmente incluye el contenido HTML de la página solicitada, junto con otros recursos como CSS, JavaScript, imágenes, etc.

4. **URL y DNS**: Cuando un usuario escribe una URL en su navegador (por ejemplo, "https://www.ejemplo.com"), el navegador utiliza el Sistema de Nombres de Dominio (DNS) para traducir esa URL en una dirección IP numérica que identifica al servidor web donde está alojada la página. Esta resolución DNS se realiza a través de servidores DNS que mantienen una base de datos de nombres de dominio y sus direcciones IP correspondientes.
   - El DNS es un sistema de nombres jerárquico utilizado para traducir nombres de dominio legibles para los humanos (como "ejemplo.com") en direcciones IP numéricas (como "192.0.2.1") que identifican los servidores en Internet.
   - Cuando un usuario ingresa una URL en su navegador, como "https://www.ejemplo.com", el navegador utiliza el DNS para buscar la dirección IP asociada con ese nombre de dominio.
   - Este proceso de traducción de nombres de dominio en direcciones IP se realiza a través de una serie de servidores DNS distribuidos por todo el mundo, comenzando desde los servidores raíz y descendiendo a servidores de dominio más específicos hasta que se encuentra la dirección IP deseada.

   - Los nombres de dominio son identificadores únicos utilizados para identificar los sitios web y otros recursos en Internet. Están compuestos por una serie de etiquetas separadas por puntos, donde la etiqueta más a la derecha representa el nivel superior del dominio (TLD, como ".com", ".org", ".net", etc.).
   - Los nombres de dominio pueden tener subdominios, que son segmentos adicionales agregados al principio del nombre de dominio principal (por ejemplo, "blog.ejemplo.com" tiene "blog" como subdominio y "ejemplo.com" como dominio principal).

5. **Cliente y servidor**: En el desarrollo web, el concepto de cliente y servidor es fundamental. El cliente se refiere al navegador web que utiliza el usuario para acceder a la página web, mientras que el servidor es la computadora remota que almacena y sirve el contenido web solicitado. Los programadores web escriben código tanto para el lado del cliente (JavaScript, HTML, CSS) como para el lado del servidor (generalmente utilizando lenguajes como Python, PHP, Ruby, etc.) para crear aplicaciones web dinámicas y receptivas.


6. **Hosting**:
   - El hosting se refiere al servicio de alojamiento de sitios web y otros recursos en servidores conectados a Internet. Los proveedores de hosting ofrecen servicios que permiten a los usuarios publicar sus sitios web en Internet para que sean accesibles para otros usuarios.
   - Los servicios de hosting varían en términos de capacidad, rendimiento, seguridad, soporte y precio. Los sitios web pueden ser alojados en servidores compartidos, servidores dedicados o a través de servicios de alojamiento en la nube.
   - Un proveedor de hosting asigna una dirección IP y un espacio en disco para el sitio web de un cliente y generalmente proporciona herramientas y servicios adicionales, como almacenamiento de datos, servicios de correo electrónico, bases de datos, etc.

En resumen, Internet funciona como una red global de servidores y clientes que se comunican entre sí mediante protocolos estándar como HTTP, utilizando nombres de dominio y DNS para identificar y acceder a recursos en la web, y utilizando servicios de hosting para alojar y publicar contenido en línea. Es importante entender estos conceptos básicos para crear aplicaciones web efectivas y comprender cómo se realiza la transferencia de datos entre los usuarios y los servidores a través de la red.


# Computer Science
Computer science is the subject that studies what computers can do.

## Brief history of Theoretical Computer Science
Starts with Alan Turing who formalized the concept of a Turing Machine. A simple description of a general purpose computer.
It's the foundation of the computer science. It contains several parts:

- An infinitely long tape, that is split into cells containing simbols: 0, 1 (electricity, no electricity)
- A head that can read and write symbols to the tape
- A state register that stores the state of the head and a list os possible instructions

In todays computers, **the tape is the working memory or RAM**. **The head is the CPU** (Central Processing Unit) and **the list of instructions is held in the computer's memory**.
This is essentially what all computers do nowadays.

Every problem that is computable by a Turing machine is computable using Lambda calculus, which is the basis of research in programming languages.

# Software Engineering
Code is a bunch of instructions telling the computer what to do.
Good code is vital, it must be as efficient as possible and as free of errors as possible.

Therefore, there are many best practices and designing philosophies to follow, such as **Object Oriented Design**, **Formal Methods**, **Unit Testing** and **Version Control**.



### [Is computing difficult?](https://www.youtube.com/watch?v=wVeLg2PsVPg&t=324s) - Fundamentals on computing and abstraction layers

### [Map of Computer Science](https://www.youtube.com/watch?v=SzJ46YA_RaA) - Computer Science studies summarized on an image

### [Computing Manual](https://manuais.iessanclemente.net/index.php/Portada) - Generic manuals on Galician language

### [How computers read code](https://www.youtube.com/watch?v=QXjU9qTsYCc) - Basics on programming languages and compilers

