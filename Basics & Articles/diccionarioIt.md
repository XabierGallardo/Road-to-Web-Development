# Diccionario IT

# Team Working Basics
## Deploy
- Desploy, desplegar o lanzar, es la actividad de llevar nuestro código a producción
- Cuando subimos nuestro proyecto a la nube, le hacemos un deploy a un servidor a la nube
- El término deploy se usa para describir el proceso de llevar nuestro sitio web a internet
- También es el proceso de llevar una aplicación web donde trabajamos al cliente, 100% en línea
- En el proceso de deploy es importante hacer prueba para saber que todo está corriendo bien.

## Buenas prácticas
1. Debe hacer **consenso**, orden y coordinación a la hora de hacer deploys
2. Fast rollback o **retroceso rápido**, práctica que sirve para volver al código anterior si se rompe algo, es decir, volver a la versión estable anterior
3. **Correctness** quiere decir que todos tengan la versión correcta del nodo o del código
4. **Homogeneizar**, esto se usa para reducir el número de errores que pueden llegar a producción. Es decir, que todos los ambientes de desarrollo, testing y producción deben ser lo más idénticos posible
5. **Testing**, debemos asegurarnos de probar todo lo que se pueda

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


