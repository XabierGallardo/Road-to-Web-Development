# Almacenamiento persistente en JavaScript

### Introducción
En JavaScript, cuando trabajas con un archivo JSON local, tienes varias opciones para modificarlo, dependiendo de dónde esté alojado el archivo y el entorno en el que estés trabajando. En el navegador, el enfoque estará limitado a trabajar en memoria, mientras que en Node.js puedes hacer cambios permanentes en archivos locales.

**En una aplicación web (navegador): No puedes modificar directamente un archivo JSON** que esté almacenado localmente en el navegador, ya que JavaScript en el navegador no tiene permiso para escribir archivos en el sistema de archivos local por motivos de seguridad. Sin embargo, puedes leer el archivo, modificar los datos en memoria y luego enviarlos a un servidor si deseas almacenarlos permanentemente.

En un entorno de servidor o aplicación Node.js: Si trabajas en un entorno donde puedes interactuar con el sistema de archivos, como con Node.js, puedes cargar el archivo JSON, modificar los datos y guardarlos de nuevo en el archivo.


### Ejemplo modificando un JSON desde Node.js
- Se usa fs.readFile para leer el archivo JSON.
- Se convierte el contenido a un objeto JavaScript con JSON.parse.
- Se modifica el objeto en memoria y luego se guarda de nuevo el archivo usando fs.writeFile con el JSON actualizado.

```js
const fs = require('fs');

// Leer el archivo JSON
fs.readFile('data.json', 'utf8', (err, data) => {
  if (err) {
    console.error("Error al leer el archivo:", err);
    return;
  }

  // Parsear los datos JSON en un objeto
  let jsonData = JSON.parse(data);

  // Modificar el JSON en memoria
  jsonData.edad = 26;

  // Escribir el archivo de nuevo
  fs.writeFile('data.json', JSON.stringify(jsonData, null, 2), (err) => {
    if (err) {
      console.error("Error al escribir en el archivo:", err);
      return;
    }
    console.log("Archivo JSON modificado correctamente");
  });
});
```


### Introducción a `localStorage`
`localStorage` es una API del navegador que permite almacenar datos de manera persistente en el cliente (es decir, en el navegador del usuario). A diferencia de las cookies, los datos en `localStorage` no tienen una fecha de expiración y permanecen disponibles incluso después de cerrar la pestaña o el navegador. 


### ¿Cuándo usar `localStorage`?
`localStorage` es útil para almacenar datos que no son sensibles y que necesitan ser persistentes a través de múltiples sesiones. Puede ser usado para guardar configuraciones de usuario, temas de preferencia, datos temporales, entre otros.


### Características de `localStorage`
- **Capacidad máxima**: Varía entre navegadores, generalmente hasta 5MB.
- **Persistencia**: Los datos persisten incluso después de cerrar el navegador.
- **Almacenamiento basado en clave-valor**: Los datos se almacenan como pares de `clave`-`valor`.
- **Alcance**: Los datos son específicos de cada dominio. No se comparten entre diferentes sitios.

Vamos a ver cómo se realizan las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en `localStorage` usando JavaScript.


#### 1. **Guardar datos en `localStorage`** (`setItem`)
Para almacenar un dato en `localStorage`, usamos el método `setItem`, que recibe dos argumentos:
- **Clave**: Es el nombre que identificará al dato.
- **Valor**: Es el dato que deseas almacenar, y se guarda como una cadena de texto.

```javascript
// Guardar un nombre de usuario
localStorage.setItem("usuario", "Juan Perez");

// Guardar una edad
localStorage.setItem("edad", "25");
```

> **Nota**: `localStorage` solo almacena cadenas de texto, por lo que si deseas almacenar un objeto o un arreglo, debes convertirlo a una cadena JSON.

**Ejemplo con JSON:**

```javascript
const usuario = { nombre: "Juan", edad: 25 };
localStorage.setItem("usuario", JSON.stringify(usuario));
```


#### 2. **Leer datos de `localStorage`** (`getItem`)
Para leer un dato almacenado en `localStorage`, utilizamos `getItem`, que recibe la clave del elemento que queremos obtener. Si el elemento no existe, devolverá `null`.

```javascript
// Leer un valor simple
const nombreUsuario = localStorage.getItem("usuario");
console.log(nombreUsuario); // Imprime "Juan Perez"

// Leer un objeto JSON
const usuarioGuardado = JSON.parse(localStorage.getItem("usuario"));
console.log(usuarioGuardado); // Imprime { nombre: "Juan", edad: 25 }
```


#### 3. **Actualizar datos en `localStorage`**
Para actualizar un dato, simplemente usamos `setItem` con la misma clave. Esto reemplazará el valor anterior por el nuevo valor.

```javascript
// Actualizar la edad del usuario
localStorage.setItem("edad", "26");

// Actualizar el objeto usuario
const usuarioActualizado = { nombre: "Juan", edad: 26 };
localStorage.setItem("usuario", JSON.stringify(usuarioActualizado));
```


#### 4. **Eliminar datos de `localStorage`** (`removeItem`)
Para eliminar un dato específico en `localStorage`, usamos el método `removeItem` pasando la clave del elemento que queremos eliminar.

```javascript
// Eliminar un solo dato
localStorage.removeItem("edad");
```


#### 5. **Eliminar todos los datos en `localStorage`** (`clear`)
Si deseas borrar todos los datos almacenados en `localStorage`, usa el método `clear`.

```javascript
// Borrar todos los datos
localStorage.clear();
```

---

### Ejemplos Prácticos

#### Ejemplo 1: Guardar las preferencias de tema de un usuario
Vamos a suponer que un usuario puede seleccionar un tema entre "oscuro" y "claro", y queremos guardar su elección.

```javascript
// Guardar la preferencia de tema
function guardarTema(tema) {
  localStorage.setItem("tema", tema);
  console.log(`Tema guardado: ${tema}`);
}

// Leer la preferencia de tema
function obtenerTema() {
  return localStorage.getItem("tema") || "claro"; // Valor por defecto "claro"
}

// Aplicar tema
function aplicarTema() {
  const tema = obtenerTema();
  document.body.className = tema;
  console.log(`Tema aplicado: ${tema}`);
}

// Ejemplo de uso
guardarTema("oscuro");
aplicarTema();
```

En este ejemplo, se guarda la preferencia de tema y se aplica al cuerpo del documento.

#### Ejemplo 2: Guardar y mostrar una lista de tareas

```javascript
// Guardar una lista de tareas
function guardarTareas(tareas) {
  localStorage.setItem("tareas", JSON.stringify(tareas));
}

// Leer lista de tareas
function obtenerTareas() {
  return JSON.parse(localStorage.getItem("tareas")) || [];
}

// Agregar una tarea
function agregarTarea(tarea) {
  const tareas = obtenerTareas();
  tareas.push(tarea);
  guardarTareas(tareas);
  console.log(`Tarea agregada: ${tarea}`);
}

// Mostrar todas las tareas
function mostrarTareas() {
  const tareas = obtenerTareas();
  tareas.forEach((tarea, index) => {
    console.log(`Tarea ${index + 1}: ${tarea}`);
  });
}

// Ejemplo de uso
agregarTarea("Estudiar JavaScript");
agregarTarea("Hacer ejercicio");
mostrarTareas();
```

En este ejemplo:
1. Se guardan las tareas en `localStorage` como un arreglo de cadenas de texto.
2. Cada vez que se agrega una nueva tarea, se lee el arreglo, se agrega la nueva tarea y se guarda el arreglo actualizado.
3. Finalmente, se muestra la lista de tareas almacenadas.

---

### Buenas Prácticas

1. **Convertir a JSON**: Para almacenar datos complejos (objetos, arreglos), usa `JSON.stringify` al guardarlos y `JSON.parse` al leerlos.
2. **Verificar disponibilidad**: Asegúrate de que `localStorage` está disponible en el entorno del navegador.
3. **Evitar información sensible**: No almacenes datos sensibles, ya que `localStorage` es accesible desde cualquier JavaScript en el dominio y puede ser vulnerable a ataques de XSS.
4. **Gestionar el almacenamiento**: Monitorea el espacio utilizado para evitar superar el límite (aproximadamente 5MB).


___


# Almacenamiento en JavaScript: `localStorage`, `sessionStorage` y Cookies
El almacenamiento en JavaScript es una parte fundamental para crear aplicaciones web que puedan recordar información del usuario entre sesiones o durante la navegación. Los tres métodos principales para el almacenamiento en el lado del cliente son `localStorage`, `sessionStorage`, y las **cookies**. Cada uno de ellos tiene sus propias características, limitaciones y casos de uso.

---

## 1. **localStorage**

### ¿Qué es `localStorage`?
`localStorage` es una API que permite almacenar datos de manera persistente en el navegador. Los datos almacenados en `localStorage` no tienen una fecha de expiración, lo que significa que estarán disponibles incluso después de que el usuario cierre el navegador o apague el ordenador.

### Características de `localStorage`:
- **Capacidad de almacenamiento**: Alrededor de 5-10 MB (dependiendo del navegador).
- **Persistencia**: Los datos permanecen almacenados hasta que son eliminados manualmente.
- **Almacenamiento por origen (dominio y protocolo)**: Los datos se almacenan por dominio, lo que significa que solo son accesibles dentro del mismo dominio.
- **Datos almacenados como strings**: Todos los datos almacenados en `localStorage` son de tipo string. Si se quiere almacenar otros tipos de datos, como objetos, deben ser convertidos a strings (usualmente mediante JSON).

### Métodos de `localStorage`:

1. **Guardar datos**: `localStorage.setItem(key, value)`
2. **Leer datos**: `localStorage.getItem(key)`
3. **Eliminar un dato**: `localStorage.removeItem(key)`
4. **Eliminar todos los datos**: `localStorage.clear()`

### Ejemplo:

```javascript
// Guardar datos en localStorage
localStorage.setItem("nombre", "Juan");

// Obtener datos de localStorage
const nombre = localStorage.getItem("nombre");
console.log(nombre); // Output: "Juan"

// Eliminar un dato específico
localStorage.removeItem("nombre");

// Limpiar todo el localStorage
localStorage.clear();
```

### Almacenando objetos en `localStorage`:
Debido a que `localStorage` solo almacena datos como cadenas de texto, es necesario convertir los objetos a JSON antes de almacenarlos.

```javascript
const usuario = {
    nombre: "Juan",
    edad: 30
};

// Convertir el objeto a JSON y almacenarlo
localStorage.setItem("usuario", JSON.stringify(usuario));

// Obtener el objeto de localStorage y convertirlo de nuevo a un objeto
const usuarioGuardado = JSON.parse(localStorage.getItem("usuario"));
console.log(usuarioGuardado.nombre); // Output: "Juan"
```

---

## 2. **sessionStorage**

### ¿Qué es `sessionStorage`?
`sessionStorage` es una API similar a `localStorage`, pero con una diferencia clave: los datos almacenados en `sessionStorage` solo se mantienen disponibles durante la sesión del navegador. Cuando se cierra la pestaña o ventana del navegador, los datos se eliminan automáticamente.

### Características de `sessionStorage`:
- **Capacidad de almacenamiento**: Similar a `localStorage`, alrededor de 5 MB.
- **Persistencia**: Solo durante la sesión activa. Si se cierra la pestaña, los datos se pierden.
- **Almacenamiento por origen (dominio y protocolo)**: Similar a `localStorage`, los datos son accesibles solo dentro del mismo dominio.
- **Datos almacenados como strings**: Igual que en `localStorage`, los datos se almacenan como cadenas de texto.

### Métodos de `sessionStorage`:

1. **Guardar datos**: `sessionStorage.setItem(key, value)`
2. **Leer datos**: `sessionStorage.getItem(key)`
3. **Eliminar un dato**: `sessionStorage.removeItem(key)`
4. **Eliminar todos los datos**: `sessionStorage.clear()`

### Ejemplo:

```javascript
// Guardar datos en sessionStorage
sessionStorage.setItem("nombre", "Ana");

// Obtener datos de sessionStorage
const nombre = sessionStorage.getItem("nombre");
console.log(nombre); // Output: "Ana"

// Eliminar un dato específico
sessionStorage.removeItem("nombre");

// Limpiar todo el sessionStorage
sessionStorage.clear();
```

### Diferencia con `localStorage`:

La principal diferencia entre `sessionStorage` y `localStorage` es la duración de los datos. Mientras que `localStorage` guarda los datos de forma persistente hasta que se eliminen manualmente, `sessionStorage` solo almacena los datos durante la sesión del navegador, lo que puede ser útil en situaciones donde la persistencia a largo plazo no es necesaria (por ejemplo, en un carrito de compras temporal).

---

## 3. **Cookies**

### ¿Qué son las Cookies?
Las **cookies** son pequeños fragmentos de información que se almacenan en el navegador del usuario y que se envían con cada petición HTTP al servidor. Son más antiguas que `localStorage` y `sessionStorage` y han sido ampliamente utilizadas para mantener la sesión del usuario, guardar preferencias, entre otros usos.

### Características de las Cookies:
- **Capacidad de almacenamiento**: Limitada, generalmente unos 4 KB por cookie.
- **Persistencia**: Las cookies pueden tener una fecha de expiración específica. Si no se establece una fecha de expiración, la cookie será eliminada al cerrar la sesión del navegador.
- **Envío al servidor**: A diferencia de `localStorage` y `sessionStorage`, las cookies se envían automáticamente al servidor con cada solicitud HTTP, lo que puede ser útil pero también puede generar sobrecarga en la red.
- **Almacenamiento por origen (dominio y protocolo)**: Al igual que `localStorage` y `sessionStorage`, las cookies están asociadas a un dominio específico.

### Manipulación de Cookies en JavaScript:
No existe una API estándar para gestionar cookies, pero se pueden manejar usando el objeto `document.cookie`.

### Crear una cookie:

```javascript
// Crear una cookie
document.cookie = "usuario=Juan; expires=Fri, 31 Dec 2024 23:59:59 GMT; path=/";

// Crear una cookie sin expiración (se eliminará al cerrar el navegador)
document.cookie = "pais=España; path=/";
```

### Leer cookies:

```javascript
// Leer todas las cookies
console.log(document.cookie); // Output: "usuario=Juan; pais=España"
```

### Eliminar una cookie:
Para eliminar una cookie, se establece una fecha de expiración en el pasado.

```javascript
// Eliminar una cookie
document.cookie = "usuario=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/";
```

### Ejemplo completo de uso de Cookies:

```javascript
// Crear una cookie que expira en 7 días
function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// Obtener el valor de una cookie
function getCookie(name) {
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookies = decodedCookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.indexOf(name + "=") === 0) {
            return cookie.substring(name.length + 1, cookie.length);
        }
    }
    return "";
}

// Establecer una cookie
setCookie("idioma", "es", 7);

// Leer una cookie
console.log(getCookie("idioma")); // Output: "es"
```

---

## Comparación entre `localStorage`, `sessionStorage` y Cookies:

| Característica           | `localStorage`                    | `sessionStorage`                 | **Cookies**                        |
|--------------------------|-----------------------------------|----------------------------------|------------------------------------|
| **Tamaño máximo**         | 5-10 MB                           | 5 MB                             | 4 KB                              |
| **Duración de los datos** | Persistente                       | Solo durante la sesión           | Definida por el usuario o el servidor |
| **Envío al servidor**     | No                                | No                               | Sí, con cada solicitud HTTP        |
| **Alcance**               | Dentro del dominio y protocolo    | Dentro del dominio y protocolo   | Dentro del dominio y protocolo     |
| **Tipo de datos**         | String                            | String                           | String                            |
| **API de JavaScript**     | Fácil de usar con métodos nativos | Fácil de usar con métodos nativos| No estándar, se manipula como cadenas|

---

## Conclusión:
El almacenamiento en el navegador comprende una serie herramientas que nos permite guardar datos de los usuarios de manera temporal o persistente. Dependiendo de la necesidad de nuestra aplicación, podemos elegir entre:

- **`localStorage`**: Si necesitas almacenar datos de forma persistente, incluso después de cerrar el navegador.
- **`sessionStorage`**: Si los datos solo deben mantenerse durante la sesión del navegador.
- **Cookies**: Si necesitas que los datos sean enviados al servidor en cada solicitud o si estás trabajando con límites más estrictos en cuanto a tamaño y seguridad.

Cada una de estas opciones tiene sus ventajas y limitaciones, por lo que es importante seleccionar la más adecuada según el caso de uso.