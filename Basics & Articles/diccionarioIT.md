# Diccionario IT

## Resumen `MVC` y `Middlewares`
- Modelo
- Middleware
- Controladores

## Que son los modelos?
Un modelo es una representacion de una entidad o concepto en el dominio de la aplicación. En una aplicación web un modelo suele ser una clase o función que define las propiedades y comportamientos de una entidad como un usuario, un producto, una orden, etc.

### Ejemplo de modelo Usuario con Mongoose
Mongoose es una biblioteca para interactuar con MongoDB.
El modelo User tiene tres propiedades, name, email y password que son definidas en el esquema userSchema.
```js
// models/User.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String
});

const User = mongoose.model('User', userSchema);

module.exports = User;
```

Luego se puede utilizar este modelo en el controlador para interactuar con la base de datos
```js
// controllers/userController.js
const User = require('../models/User');

// Controlador para obtener todos los usuarios
app.get('users', async(req, res) => {
    try {
        // Obtener todos los usuarios de la BBDD
        const users = await User.find();

        // Devolver la lista de usuarios en JSON
        res.json(users);

    } catch(error) {
        console.error(error);
        res.status(500).json({message: 'Error al obtener usuarios' });
    }
});
```
En este ejemplo utilizamos el modelo User para obtener todos los usuarios de la BBDD utilizando el metodo `find()`. Luego se devuelve la lista de usuarios en formato JSON.




## Que son el middleware y los controladores y cómo se relacionan?
En una aplicación web, el middleware y los controladores son conceptos clave para manejar las solicitudes HTTP y realizar acciones específicas.

El middleware se ejecuta antes de que la solicitud llegue al controlador. El middleware entonces puede:
- Modificar la solicitud antes de que llegue al controlador
- Redirigir la solicitud a un controlador diferente
- Devolver una respuesta sin llegar al controlador

Una vez que la solicitud para por el middleware, llega al controlador que se encarga de realizar la lógica de negocio y devolver una respuesta

## Middleware
**El middleware es un software que se ejecuta entre la solicitud del cliente y la respuesta del servidor**. Su propósito es realizar tareas adicionales como:
- Autenticación y autorización
- Manejo de errores
- Login y registro
- Compresión y descompresión de datos
- Manejo de CORS, Cross Origin Resource Sharing
- Enrutamiento y redirección

El middleware se ejecuta en un orden específico y cada middleware puede modificar la solicitud o la respuesta antes de pasarla al siguiente middleware. De manera que se pueden encadenar varios middleware para realizar tareas complejas.

### Ejemplo de Middleware
```js
// middleware para autenticación
const authMiddleware = (req, res, next) => {
  // lógica para autenticar al usuario
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).json({ message: 'No autorizado' });
  }
  next();
};

// middleware para manejar errores
const errorMiddleware = (err, req, res, next) => {
  // lógica para manejar errores
  console.error(err);
  res.status(500).json({ message: 'Error interno del servidor' });
};

// middleware para loguear solicitudes
const logMiddleware = (req, res, next) => {
  // lógica para loguear solicitudes
  console.log(`Solicitud ${req.method} a ${req.url}`);
  next();
};
```




## Controladores
**Los controladores son funciones que se encargan de manejar las solicitudes HTTP y devolver una respuesta**, su propósito es:
- Recibir la solicitud HTTP y los parámetros asociados
- Realizar acciones específicas como leer o escribir datos en la BBDD
- Devolver una respuesta HTTP como un objeto JSON, un archivo o un mensaje de error

Los controladores suelen ser específicos para una ruta o un conjunto de rutas y se encargan de realizar la lógica de negocio asociada a esa ruta.


## Ejemplos de Middleware y Controladores para una app CRUD con Express
### Ejemplo de Controladores
```js
// controlador para obtener todos los usuarios
app.get('/users', (req, res) => {
  // lógica para obtener todos los usuarios
  const users = [{ id: 1, name: 'Johnny' }, { id: 2, name: 'Shauna' }];
  res.json(users);
});

// controlador para crear un nuevo usuario
app.post('/users', (req, res) => {
  // lógica para crear un nuevo usuario
  const user = { id: 3, name: req.body.name };
  res.json(user);
});

// controlador para obtener un usuario por ID
app.get('/users/:id', (req, res) => {
  // lógica para obtener un usuario por ID
  const id = (link unavailable);
  const user = { id: 1, name: 'Juan' };
  res.json(user);
});

// controlador para actualizar un usuario
app.put('/users/:id', (req, res) => {
  // lógica para actualizar un usuario
  const id = (link unavailable);
  const user = { id: 1, name: req.body.name };
  res.json(user);
});

// controlador para eliminar un usuario
app.delete('/users/:id', (req, res) => {
  // lógica para eliminar un usuario
  const id = (link unavailable);
  res.json({ message: 'Usuario eliminado' });
});
```




---

## CLI, Command Line Interface
¿Qué es una CLI?

La Interfaz de Línea de Comandos (CLI, por sus siglas en inglés) es una interfaz de usuario basada en texto que permite a los usuarios interactuar con un sistema operativo o un programa específico mediante la introducción de comandos de texto en una terminal o consola A diferencia de las interfaces gráficas de usuario (GUI), que utilizan elementos visuales como botones, ventanas y menús, la CLI se basa completamente en comandos escritos en texto plano, lo que requiere que el usuario escriba instrucciones directamente

El funcionamiento de la CLI depende de un programa llamado *shell* (o intérprete de comandos), que actúa como un puente entre el usuario y el núcleo del sistema operativo Cuando se escribe un comando, el shell lo interpreta, lo procesa y lo ejecuta, mostrando el resultado, conocido como salida estándar (stdout), o posibles errores (stderr), en la misma interfaz Esta interacción puede ser interactiva, donde el usuario escribe comandos uno a uno, o automatizada mediante scripts, que son archivos con una serie de comandos guardados para ejecutar tareas repetitivas sin intervención manual

La CLI existe desde los primeros años de la computación y fue estandarizada con el sistema operativo Unix en la década de 1970, introduciendo conceptos clave como las tuberías y el filtrado de archivos Aunque las interfaces gráficas se han vuelto dominantes en los sistemas de escritorio, la CLI sigue siendo ampliamente utilizada por desarrolladores, administradores de sistemas y en entornos científicos e ingenieriles debido a sus ventajas en eficiencia, control preciso y bajo consumo de recursos computacionales Además, permite tareas avanzadas, como la automatización de procesos, el acceso remoto a servidores y la gestión de grandes volúmenes de datos de manera más rápida que las GUI

Las CLI están disponibles en todos los principales sistemas operativos, incluyendo Linux, macOS y Windows, donde se presentan a través de diferentes herramientas: el Terminal en macOS, diversas terminales en Linux (como Bash, Zsh o Fish) y el Símbolo del sistema o PowerShell en Windows Aunque puede parecer desalentadora al principio para usuarios no familiarizados con la sintaxis de los comandos, dominar la CLI es considerado una habilidad valiosa para optimizar flujos de trabajo y acceder a funcionalidades avanzadas que no siempre están disponibles en las interfaces gráficas

---


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