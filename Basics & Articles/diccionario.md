# Diccionario IT

### Qué significa mockear una API?
"Mockear" una API significa **simular su comportamiento sin que exista realmente una conexión con el servidor real**. Es decir, en lugar de hacer peticiones reales a un backend o a una API externa, se **crean respuestas falsas (mocked)** que imitan lo que esa API devolvería. Esto es especialmente útil en desarrollo y pruebas.

---

### 🛠 ¿Por qué se mockea una API?

1. **Desarrollo frontend sin backend disponible**.
2. **Pruebas unitarias o de integración** sin depender de un servidor real.
3. **Evitar peticiones reales** (por costos, rendimiento o límites de uso).
4. **Probar diferentes escenarios** (errores, respuestas lentas, datos específicos).

---

### 💡 Ejemplo simple (mock en JavaScript):

Supongamos que una API real devuelve esto:

```json
{
  "user": { "id": 1, "name": "María" }
}
```

En lugar de hacer:

```js
fetch("https://api.ejemplo.com/user")
  .then(res => res.json())
  .then(data => console.log(data));
```

Podés mockear así:

```js
const mockUser = {
  user: { id: 1, name: "María" }
};

function getUserMock() {
  return new Promise(resolve => {
    setTimeout(() => resolve(mockUser), 500); // simula retardo
  });
}

getUserMock().then(data => console.log(data));
```

---

### 🔧 Herramientas comunes para mockear APIs

- **JavaScript puro**: como en el ejemplo anterior.
- **Librerías**:  
  - `json-server`: crea un servidor REST falso desde un archivo JSON.  
  - `msw` (Mock Service Worker): intercepta peticiones fetch/xhr a nivel de navegador o tests.  
  - `nock`: simula respuestas HTTP en tests de Node.js.  
  - `axios-mock-adapter`: para simular respuestas de `axios`.

---

### 🧪 ¿Y en pruebas?

En testing, mockear es parte esencial del proceso para aislar componentes. Por ejemplo:

```js
jest.mock('./api'); // en Jest
```

Con esto podés controlar qué devuelve una función sin que haga la llamada real.

---

## MVP (Minimum Viable Product)
- El MVP es un producto con suficientes características para satisfacer a los clientes iniciales, y proporcionar retroalimentación para el desarrollo futuro.
- Un producto viable mínimo tiene solo las características básicas suficientes para lanzar el producto, y no más. Los desarrolladores típicamente lanzan el producto para un subconjunto de los posibles clientes, como los "primeros seguidores", que son más tolerantes, más propensos a dar retroalimentación y capaces de captar la visión de producto a partir de un prototipo temprano. Esta estrategia va enfocada a evitar la construcción de productos que los clientes no quieren y busca maximizar la obtención de información sobre el cliente con respecto a los gastos. "El producto mínimo viable es la versión de un nuevo producto que un equipo utiliza para obtener la cantidad máxima de conocimiento validado sobre los clientes con el menor esfuerzo". Las palabras máximo y mínimo no se utilizan formulaicamente. Se requiere una evaluación del contexto para que el alcance del MVP tenga sentido.

- Un MVP puede ser parte de la estrategia y el proceso para vender un producto a los clientes.​ Es un artefacto central en un proceso iterativo de generación de ideas, creación de prototipos, presentación, recopilación de datos, análisis y aprendizaje.

- El MVP o Minimum Viable Product, o en castellano el Producto Mínimo Viable, es aquel enfoque que permite el desarrollo de lo esencial en un proyecto, en este caso que comentamos, en el desarrollo app o web. Es decir, enfocar a no desarrollar un proyecto o producto hasta las últimas consecuencias, sino seguir la estrategia de invertir el mínimo de tiempo posible para conseguir algo que funcione, quizás no como esperamos en su forma completa, pero si que permita captar la esencia y salir al mercado o en grupo de testing, con algo probable.

---

## Principios SOLID
Los principios SOLID son un conjunto de cinco principios de diseño orientados a objetos que ayudan a crear software más comprensible, flexible y mantenible.

1. **S - Single Responsibility Principle (Principio de Responsabilidad Única)**:
   - **Resumen**: Una clase debe tener una sola responsabilidad o motivo para cambiar.
   - **Explicación sencilla**: Cada clase debe encargarse de hacer una sola cosa, para que sea más fácil de entender y modificar sin afectar otras partes del código.
```ts
// Mal diseño: la clase UserManager maneja tanto usuarios como la gestión de notificaciones.
class UserManager {
    addUser(user: string) {
        console.log(`Adding user: ${user}`);
        this.sendWelcomeEmail(user);
    }

    sendWelcomeEmail(user: string) {
        console.log(`Sending welcome email to ${user}`);
    }
}

// Buen diseño: separación de responsabilidades en dos clases.
class UserManager {
    addUser(user: string) {
        console.log(`Adding user: ${user}`);
    }
}

class EmailService {
    sendWelcomeEmail(user: string) {
        console.log(`Sending welcome email to ${user}`);
    }
}
```

2. **O - Open/Closed Principle (Principio de Abierto/Cerrado)**:
   - **Resumen**: Las entidades de software deben estar abiertas para la extensión, pero cerradas para la modificación.
   - **Explicación sencilla**: Puedes añadir nuevas funcionalidades a una clase sin cambiar el código existente, lo cual ayuda a evitar errores al modificar código ya probado.
```ts
// Mal diseño: hay que modificar la clase para añadir un nuevo tipo de descuento.
class Discount {
  calculate(price: number, type: string): number {
    if (type === "summer") {
      return price * 0.9;
    } else if (type === "winter") {
      return price * 0.8;
    }
    return price;
  }
}

// Buen diseño: uso de polimorfismo para extender la funcionalidad sin modificar el código existente.
abstract class Discount {
  abstract calculate(price: number): number;
}

class SummerDiscount extends Discount {
  calculate(price: number): number {
    return price * 0.9;
  }
}

class WinterDiscount extends Discount {
  calculate(price: number): number {
    return price * 0.8;
  }
}

```

3. **L - Liskov Substitution Principle (Principio de Sustitución de Liskov)**:
   - **Resumen**: Los objetos de una clase derivada deben ser reemplazables por objetos de la clase base sin alterar el comportamiento del programa.
   - **Explicación sencilla**: Si tienes una clase base y una clase derivada, deberías poder usar objetos de la clase derivada en lugar de la clase base sin que el programa falle o se comporte incorrectamente.
```ts
// Mal diseño: Square no puede reemplazar Rectangle sin causar problemas.
class Rectangle {
  constructor(public width: number, public height: number) {}

  setWidth(width: number) {
    this.width = width;
  }

  setHeight(height: number) {
    this.height = height;
  }

  area(): number {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  constructor(size: number) {
    super(size, size);
  }

  setWidth(width: number) {
    this.width = width;
    this.height = width;
  }

  setHeight(height: number) {
    this.width = height;
    this.height = height;
  }
}

// Buen diseño: evitar la herencia problemática.
class Rectangle {
  constructor(public width: number, public height: number) {}

  area(): number {
    return this.width * this.height;
  }
}

class Square {
  constructor(public size: number) {}

  area(): number {
    return this.size * this.size;
  }
}

```

4. **I - Interface Segregation Principle (Principio de Segregación de Interfaces)**:
   - **Resumen**: Los clientes no deben estar obligados a depender de interfaces que no utilizan.
   - **Explicación sencilla**: En lugar de tener una gran interfaz que haga muchas cosas, divide las interfaces en partes más pequeñas y específicas. Así, las clases solo implementan lo que realmente necesitan.
```ts
// Mal diseño: una interfaz grande obliga a implementar métodos innecesarios.
interface Worker {
  work(): void;
  eat(): void;
  sleep(): void;
}

class Robot implements Worker {
  work() {
    console.log("Robot working");
  }

  eat() {
    // No aplica para robots
  }

  sleep() {
    // No aplica para robots
  }
}

// Buen diseño: interfaces más pequeñas y específicas.
interface Workable {
  work(): void;
}

interface Eatable {
  eat(): void;
}

interface Sleepable {
  sleep(): void;
}

class Human implements Workable, Eatable, Sleepable {
  work() {
    console.log("Human working");
  }

  eat() {
    console.log("Human eating");
  }

  sleep() {
    console.log("Human sleeping");
  }
}

class Robot implements Workable {
  work() {
    console.log("Robot working");
  }
}
```

5. **D - Dependency Inversion Principle (Principio de Inversión de Dependencias)**:
   - **Resumen**: Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.
   - **Explicación sencilla**: En lugar de que una clase dependa directamente de otra clase concreta, debería depender de una interfaz o una clase abstracta. Esto facilita cambiar implementaciones sin afectar otras partes del código.
```ts
// Mal diseño: la clase Frontend depende directamente de la clase Backend.
class Backend {
  getData() {
    return "Backend data";
  }
}

class Frontend {
  private backend: Backend;

  constructor() {
    this.backend = new Backend();
  }

  render() {
    const data = this.backend.getData();
    console.log(`Rendering data: ${data}`);
  }
}

// Buen diseño: la clase Frontend depende de una abstracción.
interface DataService {
  getData(): string;
}

class Backend implements DataService {
  getData() {
    return "Backend data";
  }
}

class Frontend {
  private dataService: DataService;

  constructor(dataService: DataService) {
    this.dataService = dataService;
  }

  render() {
    const data = this.dataService.getData();
    console.log(`Rendering data: ${data}`);
  }
}

const backend = new Backend();
const frontend = new Frontend(backend);
frontend.render();
```

Los principios SOLID promueven la escritura de código que es fácil de entender, probar y mantener, ayudando a construir sistemas más robustos y escalables.



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