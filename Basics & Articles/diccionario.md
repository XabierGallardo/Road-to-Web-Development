# Diccionario IT

# Algorithms
An algorithm is a set of instructions independent of the hardware or programming language, designed to solve a particular problem.
It's like a recipe of how to build a program. A lot of work is put into developing algorithms to get the best out of computers.

Some algorithms are much more efficient than others. This is studied in **Algorithmic Complexity** and **Analysis of Algorithms**.

Other fields of the theoretical computers science are **Computability Theory**, **Computational Complexity**, **Information Theory**, **Cryptography**, **Logic**, **Graph Theory**, **Automata Theory**, **Quantum Computation**, **Paralel Programming**, **Formal Methods**, **Data Structures**.

En programación, un algoritmo es un conjunto ordenado y finito de pasos bien definidos que se utilizan para resolver un problema específico o realizar una tarea determinada. Los algoritmos son la base fundamental de la programación y se utilizan para diseñar soluciones eficientes a una amplia variedad de problemas en campos como la informática, las matemáticas, la ingeniería y muchas otras disciplinas.

Los algoritmos pueden expresarse en diferentes formas, incluyendo pseudocódigo, diagramas de flujo, descripciones verbales o código de programación real en algún lenguaje específico. Independientemente de la forma en que se expresen, los algoritmos deben tener ciertas características:

1. **Precisión**: Cada paso del algoritmo debe estar claramente definido y ser comprensible. No puede haber ambigüedad en las instrucciones.

2. **Finitud**: El algoritmo debe tener un número finito de pasos. No debe entrar en un bucle infinito o repetir infinitamente las mismas acciones.

3. **Efectividad**: El algoritmo debe ser capaz de resolver el problema para el que fue diseñado en un tiempo razonable y utilizando una cantidad razonable de recursos.

4. **Determinismo**: Para una entrada dada, un algoritmo siempre debe producir el mismo resultado. Es decir, debe ser determinista y no depender de factores aleatorios o impredecibles.

Los algoritmos pueden clasificarse en diferentes categorías según su naturaleza y su propósito. Algunas de las categorías comunes incluyen algoritmos de búsqueda, algoritmos de ordenamiento, algoritmos de grafos, algoritmos de árboles, entre otros. Cada tipo de algoritmo está diseñado para resolver un conjunto específico de problemas de manera eficiente y efectiva. Los algoritmos juegan un papel fundamental en el desarrollo de software, ya que proporcionan la base para implementar soluciones a problemas computacionales de manera sistemática y estructurada.


# Plataformas de servicios en la nube, AWS, Azure y Google Cloud
Una plataforma de servicios en la nube es una infraestructura en línea que proporciona una variedad de servicios y recursos informáticos a través de internet. Estas plataformas permiten a los usuarios acceder a recursos informáticos, como servidores, almacenamiento, bases de datos, redes, software y otros servicios, sin necesidad de poseer ni mantener su propia infraestructura física. En lugar de eso, los usuarios pueden consumir estos servicios bajo demanda, generalmente a través de un modelo de pago por uso.

Las plataformas de servicios en la nube ofrecen ventajas significativas, como escalabilidad, flexibilidad, alta disponibilidad, seguridad y costos reducidos, lo que las hace muy atractivas para empresas de todos los tamaños y sectores.

Algunas de las plataformas de servicios en la nube más populares son:

1. **Amazon Web Services (AWS)**: AWS es una de las plataformas de servicios en la nube más grandes y populares del mundo, ofreciendo una amplia gama de servicios, incluyendo computación, almacenamiento, bases de datos, análisis, machine learning, IoT y más.

2. **Microsoft Azure**: Azure es la plataforma de servicios en la nube de Microsoft, que ofrece una variedad de servicios, incluyendo hospedaje de aplicaciones, almacenamiento, bases de datos, inteligencia artificial, IoT y más. Es muy utilizada por empresas que ya están integradas en el ecosistema de Microsoft.

3. **Google Cloud Platform (GCP)**: GCP es la plataforma de servicios en la nube de Google, que proporciona servicios de computación, almacenamiento, bases de datos, machine learning, análisis de datos, IoT y más. Google es conocido por su experiencia en el campo de la infraestructura escalable y la tecnología de búsqueda.

4. **IBM Cloud**: La plataforma de servicios en la nube de IBM ofrece una variedad de servicios, incluyendo computación, almacenamiento, bases de datos, inteligencia artificial, blockchain y más. Se enfoca en ofrecer soluciones empresariales integrales y de alto rendimiento.

5. **Oracle Cloud**: Oracle Cloud es la plataforma de servicios en la nube de Oracle Corporation, que ofrece servicios de computación, almacenamiento, bases de datos, aplicaciones empresariales y más. Se especializa en ofrecer soluciones empresariales integradas y seguras.

Estas son solo algunas de las plataformas de servicios en la nube más populares y ampliamente utilizadas en la actualidad. Cada una tiene sus propias características, fortalezas y áreas de especialización, por lo que la elección de una plataforma en particular dependerá de las necesidades específicas de cada empresa o proyecto.





# Team Work Concepts

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


## SCRUM
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


## SOLID
Solid es un acrónimo que representa los 5 principios básicos de la programación orientada a objetos y el diseño
Los principios SOLID nos permiten administrar la mayoría de problemas de diseño de software, consiguiendo un *código más limpio, mantenible, estalable y menos propenso a errores*

**S** *Single Responsibility Principle*, un objeto debería tener una única responsabilidad

**O** *Open/Closed principle*, las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación

**L** *Liskov substitution principle*, los objetos de un programa deberían ser reemplazables por instancias de sus subtipos sin alterar el correcto funcionamiento del programa

**I** *Interface segregation principle*, muchas interaces cliente específicas son mejores que una única interfaz de propósito general

**D** *Dependency inversion principle*, depender de abstracciones, no debpender de implementaciones


