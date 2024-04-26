# SCRUM
Scrum es un marco de trabajo simple que promueve la colaboración en los equipos para lograr desarrollar productos complejos

**Define un conjunto de eventos, prácticas y roles, puede tomarse como conjunto base para definir el proceso de producción que usará un equipo de trabajo.**

Los eventos Scrum se utilizan para minimizar la necesidad de reuniones no definidas en Scrum
Todos los eventos tienen una caja de tiempo, una vez que se inicia un Sprint este tiene una duración fija y no se puede acortar o alargar

1. **Roles**:
   - Product Owner: Representa los intereses del cliente y es responsable de definir y priorizar los requisitos del producto.
   - Scrum Master: Facilita el proceso Scrum, elimina obstáculos y fomenta un ambiente colaborativo y de mejora continua.
   - Equipo de Desarrollo: Un grupo autoorganizado y multifuncional responsable de entregar las funcionalidades del producto.

2. **Eventos**:
   - Sprint: Período de tiempo fijo, típicamente de una a cuatro semanas, durante el cual se desarrolla y entrega un incremento de producto potencialmente utilizable.
   - Reunión de Planificación del Sprint: Al inicio de cada Sprint, el equipo planifica las funcionalidades que se desarrollarán durante el Sprint.
   - Reunión Diaria de Scrum: Breve reunión diaria donde el equipo revisa el progreso, identifica obstáculos y actualiza el plan para alcanzar el objetivo del Sprint.
   - Revisión del Sprint: Al final de cada Sprint, el equipo demuestra el incremento de producto al Product Owner y a otros interesados y recibe retroalimentación.
   - Retrospectiva del Sprint: Reunión donde el equipo reflexiona sobre el Sprint pasado para identificar mejoras y oportunidades de cambio en el proceso.

3. **Artefactos**: *formas de proveer transparencia y oportunidades de inspección y adaptación*
   - Product Backlog: Lista priorizada de todas las funcionalidades, cambios y mejoras pendientes para el producto.
   - Sprint Backlog: Lista de tareas seleccionadas del Product Backlog que el equipo se compromete a completar durante el Sprint.
   - Incremento: La suma de todas las funcionalidades desarrolladas y entregadas al final de cada Sprint, que constituye una versión potencialmente utilizable del producto.

A través de la colaboración continua, la comunicación abierta y la entrega iterativa, Scrum permite a los equipos responder rápidamente a los cambios en los requisitos del cliente y en el entorno del proyecto, lo que resulta en un producto final que mejor se adapta a las necesidades del cliente.


# Kanban
#### El tablero Kanban está dividido en columnas que representan diferentes etapas del proceso, como "Por hacer", "En progreso" y "Hecho".
En el contexto del desarrollo de software y otros proyectos, Kanban se utiliza como una herramienta para visualizar, gestionar y mejorar el flujo de trabajo.

Los principios clave de Kanban incluyen:

1. **Visualización del trabajo**:
   - Utiliza tableros Kanban para representar visualmente el flujo de trabajo.
   - *El tablero Kanban está dividido en columnas que representan diferentes etapas del proceso, como "Por hacer", "En progreso" y "Hecho".*
   - Cada tarea o elemento de trabajo se representa como una tarjeta que se mueve de una columna a otra a medida que avanza a través del proceso.

2. **Limitación del trabajo en curso**:
   - Kanban limita la cantidad de trabajo en curso en cada etapa del proceso.
   - Establecer límites claros en el trabajo en curso ayuda a evitar la sobrecarga del equipo y a mantener un flujo de trabajo constante y equilibrado.

3. **Gestión del flujo**:
   - Kanban se centra en optimizar y mejorar el flujo de trabajo para maximizar la eficiencia y la entrega continua.
   - Los equipos identifican cuellos de botella y áreas de congestión en el proceso y toman medidas para mejorar la velocidad y el flujo de trabajo.

4. **Feedback y mejora continua**:
   - Kanban promueve una cultura de mejora continua, donde los equipos revisan y reflexionan regularmente sobre su proceso y su desempeño.
   - Se fomenta la retroalimentación constante de los miembros del equipo y de los interesados para identificar oportunidades de mejora y realizar ajustes en el proceso.

Kanban es altamente adaptable y puede aplicarse a una variedad de contextos y tipos de proyectos. Se puede utilizar en combinación con otros enfoques ágiles, como Scrum, o como un marco de trabajo independiente. Kanban ofrece flexibilidad y permite a los equipos adaptar el proceso a medida que cambian las necesidades y prioridades del proyecto, lo que lo convierte en una herramienta poderosa para la gestión ágil de proyectos.



## Buenas prácticas
1. Debe hacer **consenso**, orden y coordinación a la hora de hacer deploys
2. Fast rollback o **retroceso rápido**, práctica que sirve para volver al código anterior si se rompe algo, es decir, volver a la versión estable anterior
3. **Correctness** quiere decir que todos tengan la versión correcta del nodo o del código
4. **Homogeneizar**, esto se usa para reducir el número de errores que pueden llegar a producción. Es decir, que todos los ambientes de desarrollo, testing y producción deben ser lo más idénticos posible
5. **Testing**, debemos asegurarnos de probar todo lo que se pueda

## Desarrollo Ágil o Metodología Ágil
El enfoque ágil para el desarrollo de software busca distribuír de forma permanente sistemas de software en funcionamiento diseñados con iteraciones rápidas
Se trata de una forma de pensar en la colaboración y los flujos de trabajo, y define un conjunto de valores que guían las decisiones sobre cómo hacer y de qué manera

En concreto, las metodologías ágiles buscan proporcionar en poco tiempo, piezas pequeñas de sistemas de software en funcionamiento para mejorar la satisfacción del cliente
Estas metodologías utilizan enfoques flexibles y el tarbajo en equipo para ofrecer mejoras constantes

Por lo general, el desarrollo ágil implica que pequeños equipos autoorganizados de desarrolladores y empresas se reúnan regularmente en persona durante el ciclo de vida del desarrollo de software

La metodología ágil favorece un enfoque sencillo de la documentación del software y acepta los cambios que puedan surgir en las etapas del desarrollo
Entre sus principios destacamos:
- Las personas y las interacciones antes que los procesos y las herramientas
- El software en funcionamiento antes que la documentación exhaustiva
- La colaboración con el cliente antes que la negociación contractual
- La respuesta ante el cambio antes que el apego a un plan

El desarrollo ágil es la respuesta al **desarrollo en cascada**, en el cual una fase debe finalizarse por completo antes de poder pasar a la siguiente, mientras que el ágil permite que varias secuencias sucedan al mismo tiempo

Entre sus métodos destacamos Scrum, Kanban o FDD


## SOLID
Solid es un acrónimo que representa los 5 principios básicos de la programación orientada a objetos y el diseño
Los principios SOLID nos permiten administrar la mayoría de problemas de diseño de software, consiguiendo un *código más limpio, mantenible, estalable y menos propenso a errores*

**S** *Single Responsibility Principle*, un objeto debería tener una única responsabilidad

**O** *Open/Closed principle*, las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación

**L** *Liskov substitution principle*, los objetos de un programa deberían ser reemplazables por instancias de sus subtipos sin alterar el correcto funcionamiento del programa

**I** *Interface segregation principle*, muchas interaces cliente específicas son mejores que una única interfaz de propósito general

**D** *Dependency inversion principle*, depender de abstracciones, no debpender de implementaciones


