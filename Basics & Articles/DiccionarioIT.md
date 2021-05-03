# Diccionario IT
### Patrones de diseño
Los patrones de diseño son **soluciones para problemas típicos y recurrentes** que nos encontramos al desarrollar aplicaciones
Estos problemas pueden venir de partes genéricas como el acceso a datos, la creación de objetos, operaciones entre sistemas, etc

Los patrones de diseño nos ayudan a cumplir muchos de estos principios o reglas al diseñar una aplicación
Entre los numerosos patrones de diseño existentes, podemos agruparlos según su propósito

- **Patrones creacionales**, *Abstract Factory* utilizados para instanciar objetos y separar la implementación del cliente de la de los objetos que se utilizan. La idea es separar la lógica de creación de objetos y encapsularla

- **Patrones de comportamiento**, *Command, Iterator, Strategy, Visitor* utilizados a la hora de definir cómo las clases y objetos interaccionan entre ellos

- **Patrones estructurales**, *Bridge, Composite, Decorator* utilizados para crear clases u objetos incluídos dentro de estructuras más complejas

Los Patrones de diseño, además de solucionar problemas genéricos y recurrentes, ayudan a estandarizar el código, ayudando a que sea más comprensible para otros programadores

Uno de los más conocidos es el **MVC** o *Modelo-Vista-Controlador*, que proviene del principio de que dos aplicaciones se pueden dividir en tres áreas separadas
- **Modelo**: Los datos utilizados en la aplicación
- **Vista**: Cómo se representan los datos al usuario
- **Controlador**: Cómo se procesa la información en la interfaz del usuario


### Desarrollo Ágil o Metodología Ágil
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


### SCRUM
Scrum es un marco de trabajo simple que promueve la colaboración en los equipos para lograr desarrollar productos complejos

Define un conjunto de eventos, prácticas y roles, puede tomarse como conjunto base para definir el proceso de producción que usará un equipo de trabajo

Los eventos Scrum se utilizan para minimizar la necesidad de reuniones no definidas en Scrum
Todos los eventos tienen una caja de tiempo, una vez que se inicia un Sprint este tiene una duración fija y no se puede acortar o alargar

Los **eventos** de Scrum son:
- Sprint
- Sprint Planning
- Daily Scrum
- Sprint Review
- Sprint Retrospective

Los **artefactos** de Scrum son formas de proveer transparencia y oportunidades de inspección y adaptación
- Product Backlog
- Sprint Backlog
- Increment


### SOLID
Solid es un acrónimo que representa los 5 principios básicos de la programación orientada a objetos y el diseño
Los principios SOLID nos permiten administrar la mayoría de problemas de diseño de software, consiguiendo un *código más limpio, mantenible, estalable y menos propenso a errores*

**S** *Single Responsibility Principle*, un objeto debería tener una única responsabilidad

**O** *Open/Closed principle*, las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación

**L** *Liskov substitution principle*, los objetos de un programa deberían ser reemplazables por instancias de sus subtipos sin alterar el correcto funcionamiento del programa

**I** *Interface segregation principle*, muchas interaces cliente específicas son mejores que una única interfaz de propósito general

**D** *Dependency inversion principle*, depender de abstracciones, no debpender de implementaciones


### TDD Test Driven Development
El Desarrollo guiado por pruebas de software hace referencia un estilo de programación que combina **codificación**, **testeo** y **diseño**
El testeo se realiza mediante *tests unitarios* y el diseño mediante *refactorización*

- Escribir un test unitario simple que describa un aspecto del programa
- Ejecutar el test, que debería fallar porque el programa carece de ese elemento
- Escribir el código más simple posible para hacer pasar el test
- Refactorizar el código hasta que cumple el criterio de simplicidad
- Repetir, acumulando tests unitarios

Entre las ventajas de este desarrollo se destacan el poder hacer aplicaciones de más calidad en menos tiempo
La primera meta es superar la prueba, alcanzar la funcionalidad principal y ocuparse más adelante de los casos excepcionales y el manejo de errores

El ciclo del TDD se llama *red-green-refactor*
1. **Fase roja**: Se redacta un test que contenga componentes no implementados, para luego decidir qué elementos son realmente necesarios para que el código funcione

2. **Fase verde**: Suponiendo que el test falle, se busca una solución simple, este código se integra en el código productivo para que el test quede marcado en verde

3. **Refactorización**: El código productivo se pasa a limpio y se perfecciona, para que quede elegante y comprensible, se eliminan los duplicados en el código y se vuelve más profesional

A partir del **TDD** se desarrolló el **BDD** *Behavior-Driven Development*, es decir el desarrollo guiado por comportamiento
Esta metodología no se guía inicialmente por la adecuación del código sino por el comportamiento que se desea ver en el software
Por lo general, el BDD es el mejor método a la hora de diseñar pruebas, mientras que el TDD da como resultado una arquitectura más limpia


### Unit Testing
Los test unitarios o pruebas unitarias nos permiten comprobar los componentes individuales de los programas informáticos

Estos tests se realizan en las primeras fases del desarrollo, ya que en la fase de prueba se pueden corregir los errores de manera rápida y poco costosa

Las pruebas unitarias son pequeñas piezas de código diseñadas para comprobar que el código principal está funcionando como esperábamos
El proceso que se lleva a cabo consta de tres partes:

- **Arrange**, donde se devinen los requisitos que debe cumplir el código principal
- **Act**, el proceso de ceración donde vamos acumulando los resultados que analizaremos
- **Assert**, se considera el momento en que comprobamos si los resultados agrupados son correctos o incorrectos. Y depende del resultado, se valida o se continúa