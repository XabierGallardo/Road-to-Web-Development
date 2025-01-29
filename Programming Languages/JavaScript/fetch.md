# **I** / Introduccion a `fetch` en JavaScript

El método `fetch` en JavaScript se utiliza para realizar solicitudes HTTP de forma asíncrona. Es una función incorporada que devuelve una **promesa**, lo que permite manejar la solicitud y respuesta fácilmente usando `then` o `async/await`.  

### Sintaxis básica:
```javascript
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Convierte la respuesta en JSON
  })
  .then(data => console.log(data)) // Maneja los datos
  .catch(error => console.error('There was a problem with the fetch operation:', error));
```

### Puntos clave:
- **GET por defecto:** El método HTTP es `GET` si no se especifica.
- **Configuración avanzada:** Puedes agregar opciones como método, encabezados y cuerpo. Ejemplo:
  ```javascript
  fetch('https://api.example.com/data', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ key: 'value' })
  });
  ```
- **Errores:** `fetch` solo lanza errores para problemas de red; para manejar errores HTTP, verifica manualmente `response.ok`.


---


# **II** / GET, POST, PUT Y DELETE con `fetch` en JavaScript

El método `fetch` en JavaScript permite realizar solicitudes HTTP para interactuar con APIs, soportando operaciones como **GET**, **POST**, **PUT**, y **DELETE**. Aquí te explico cómo usar cada uno:

---

### **GET** (Obtener datos)
```javascript
fetch('https://api.example.com/items')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```
- Solicita datos al servidor.  
- No incluye un cuerpo en la solicitud.

---

### **POST** (Crear datos)
```javascript
fetch('https://api.example.com/items', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'Nuevo Item', price: 100 })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```
- Envía datos al servidor para crear un recurso.  
- Incluye un cuerpo en formato JSON.

---

### **PUT** (Actualizar datos)
```javascript
fetch('https://api.example.com/items/1', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ name: 'Item Actualizado', price: 150 })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```
- Actualiza un recurso completo en el servidor.  
- Requiere el ID del recurso y un cuerpo con los nuevos datos.

---

### **DELETE** (Eliminar datos)
```javascript
fetch('https://api.example.com/items/1', {
  method: 'DELETE'
})
  .then(response => {
    if (response.ok) console.log('Recurso eliminado');
    else console.error('Error al eliminar');
  })
  .catch(error => console.error('Error:', error));
```
- Elimina un recurso especificado en el servidor.  
- Normalmente no requiere un cuerpo.

---

### Notas clave:
- Siempre verifica el estado de la respuesta con `response.ok`.  
- Usa `async/await` para un flujo más claro:
  ```javascript
  async function fetchData() {
    try {
      const response = await fetch('https://api.example.com/items');
      if (!response.ok) throw new Error('Error en la solicitud');
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('Error:', error);
    }
  }
  fetchData();
  ```


---


# **III** / Autenticación y manejo de errores con `fetch` en JavaScript

```javascript
const API_URL = 'https://api.example.com/protected-data';
const TOKEN = 'your-authentication-token-here';

// Función para realizar la solicitud
async function fetchProtectedData() {
  try {
    // Configuración de la solicitud
    const response = await fetch(API_URL, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${TOKEN}` // Autenticación
      }
    });

    // Manejo de errores HTTP
    if (!response.ok) {
      const errorMessage = `Error ${response.status}: ${response.statusText}`;
      throw new Error(errorMessage);
    }

    // Parseo de los datos
    const data = await response.json();
    console.log('Datos obtenidos:', data);
  } catch (error) {
    // Manejo de errores generales
    console.error('Error al realizar la solicitud:', error.message);
    if (error.message.includes('401')) {
      console.error('Autenticación fallida. Verifica tu token.');
    } else if (error.message.includes('500')) {
      console.error('Error del servidor. Inténtalo más tarde.');
    }
  }
}

// Llamada a la función
fetchProtectedData();
```

---

### Características:
1. **Autenticación con Bearer Token:** Se agrega el token en el encabezado `Authorization`.
2. **Manejo de errores HTTP:** Verifica si `response.ok` es `false` y lanza un error con un mensaje descriptivo.
3. **Errores específicos:** Manejo de errores basados en códigos HTTP (e.g., `401`, `500`).
4. **Logs claros:** Muestra mensajes de error y advertencias según el problema.


---


# **IV** / Explicación técnica de `fetch` en JavaScript

`fetch` es una función nativa de JavaScript que proporciona una forma moderna y más flexible para realizar solicitudes HTTP desde el navegador o entornos compatibles como Node.js. Es parte de la **Fetch API**, introducida en ECMAScript 2015 (ES6), diseñada para reemplazar `XMLHttpRequest` con una sintaxis más intuitiva basada en Promesas.

### Características principales de `fetch`
1. **Promesas:** 
   - `fetch` devuelve una Promesa que resuelve en un objeto de respuesta (`Response`).
   - Si la solicitud falla (por problemas de red, por ejemplo), la Promesa se rechaza.
   - Las respuestas HTTP con códigos de error (como 404 o 500) **no rechazan la Promesa**. Se considera que la solicitud se realizó correctamente y hay que verificar el estado manualmente.

2. **Interfaz basada en Streams:**
   - El cuerpo de la respuesta (`response.body`) es un `ReadableStream`. Esto permite procesar grandes respuestas de manera eficiente sin cargar todo el contenido en memoria.

3. **Modularidad:**
   - Puedes configurar diversos aspectos de la solicitud, como métodos HTTP, encabezados, cuerpo, y más, usando un objeto de configuración (`init`).

---

### Sintaxis básica
```javascript
fetch(url, options)
  .then(response => {
    // Verificar si la respuesta fue exitosa
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json(); // Parsear el cuerpo como JSON
  })
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

**Parámetros:**
1. `url`: Especifica la dirección del recurso.
2. `options`: Objeto opcional para configurar detalles como método, encabezados, y cuerpo.

---

### Propiedades y métodos clave

#### **Request**
El objeto `Request` encapsula los detalles de la solicitud.
```javascript
const request = new Request('https://api.example.com/data', {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
});
fetch(request);
```

**Atributos comunes:**
- `method`: Método HTTP (`GET`, `POST`, `PUT`, `DELETE`, etc.).
- `headers`: Encabezados de la solicitud como un objeto `Headers`.
- `body`: El contenido del cuerpo (en métodos como `POST` o `PUT`).

#### **Response**
El objeto `Response` representa la respuesta de la solicitud.
```javascript
fetch('https://api.example.com/data')
  .then(response => {
    console.log(response.ok);        // true si el estado está entre 200-299
    console.log(response.status);    // Código de estado HTTP
    console.log(response.headers);   // Headers
    return response.text();          // Otros métodos: json(), blob(), etc.
  });
```

**Métodos comunes:**
- `json()`: Devuelve un objeto o array parseado del cuerpo JSON.
- `text()`: Devuelve el cuerpo como texto.
- `blob()`: Devuelve datos binarios como un `Blob`.
- `arrayBuffer()`: Devuelve datos como un `ArrayBuffer`.

**Propiedades importantes:**
- `ok`: Booleano que indica si el estado HTTP está entre 200-299.
- `status`: Código de estado HTTP (200, 404, etc.).
- `headers`: Encabezados de la respuesta, manipulables con la API `Headers`.

---

### Ejemplo avanzado: `POST` con datos
```javascript
const data = { name: 'John Doe', age: 30 };

fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer my-token',
  },
  body: JSON.stringify(data),
})
  .then(response => {
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    return response.json();
  })
  .then(result => console.log('Success:', result))
  .catch(error => console.error('Error:', error));
```

---

### Opciones avanzadas

#### **Cabeceras personalizadas**
Usando el constructor `Headers`:
```javascript
const headers = new Headers();
headers.append('Content-Type', 'application/json');
headers.append('Authorization', 'Bearer my-token');

fetch('https://api.example.com/data', { headers });
```

#### **Control de tiempo de espera (Timeout)**
`fetch` no tiene soporte nativo para timeouts, pero puede implementarse con `AbortController`:
```javascript
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 5000); // 5 segundos

fetch('https://api.example.com/data', { signal: controller.signal })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => {
    if (error.name === 'AbortError') {
      console.error('Request timed out');
    } else {
      console.error('Fetch error:', error);
    }
  });
```

#### **Manejo de cookies**
`fetch` no envía cookies automáticamente a menos que se use el modo correcto:
```javascript
fetch('https://api.example.com/data', {
  credentials: 'include', // Enviar cookies incluso con CORS
});
```

---

### Beneficios de `fetch` frente a `XMLHttpRequest`
1. **Promesas:** Simplifica el manejo asíncrono en comparación con los callbacks.
2. **Modularidad:** Más opciones configurables como `AbortController`.
3. **Mejor manejo de streams:** Permite trabajar con datos grandes de forma eficiente.

---

### Limitaciones de `fetch`
1. **Errores HTTP no rechazan la Promesa:** Debes verificar manualmente el estado con `response.ok`.
2. **Falta de soporte nativo para tiempo de espera:** Necesitas implementarlo usando `AbortController`.
3. **Compatibilidad:** Algunos navegadores antiguos requieren polyfills como `whatwg-fetch`.


---


# **V** / `fetch` con `async/await`

La palabra clave `async` permite definir una función asíncrona que automáticamente devuelve una Promesa. Dentro de estas funciones, el operador `await` pausa la ejecución hasta que una Promesa se resuelve, facilitando un enfoque síncrono en la escritura de código asíncrono.

### **Ventajas de usar `async/await` con `fetch`:**
1. **Legibilidad**: El código es más lineal y fácil de entender.
2. **Control de flujo**: El manejo de errores se simplifica con `try/catch`.
3. **Evita anidación excesiva**: Se elimina la necesidad de múltiples `then` en las cadenas de Promesas.

---

### **Ejemplo básico con `async/await`**
```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');

    // Verificar si la solicitud fue exitosa
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json(); // Esperar el parsing del JSON
    console.log(data);
  } catch (error) {
    console.error('Error en la solicitud:', error);
  }
}

fetchData();
```

### **Detalles técnicos del ejemplo:**
1. La función `fetchData` se declara como `async`, lo que permite usar `await` dentro de ella.
2. `await fetch()` detiene la ejecución hasta que la Promesa de `fetch` se resuelve.
3. El bloque `try/catch` captura errores de red o errores lanzados manualmente (como cuando el estado no es `ok`).
4. `await response.json()` espera a que los datos del cuerpo de la respuesta se parseen como JSON antes de continuar.

---

### **Opciones configurables de `fetch` con `async/await`**
La API `fetch` acepta un segundo argumento opcional para configurar detalles como:
- **Método HTTP (`method`)**
- **Encabezados (`headers`)**
- **Cuerpo de la solicitud (`body`)**

#### Ejemplo avanzado: Enviar datos con `POST`
```javascript
async function postData(url, payload) {
  try {
    const response = await fetch(url, {
      method: 'POST', // Especificar el método HTTP
      headers: {
        'Content-Type': 'application/json', // Tipo de contenido
        'Authorization': 'Bearer my-token', // Token de autenticación
      },
      body: JSON.stringify(payload), // Serializar los datos
    });

    if (!response.ok) {
      throw new Error(`Error HTTP: ${response.status}`);
    }

    const result = await response.json();
    console.log('Respuesta del servidor:', result);
  } catch (error) {
    console.error('Error al enviar datos:', error);
  }
}

postData('https://api.example.com/users', { name: 'John Doe', age: 30 });
```

---

### **Manejo de errores con `async/await`**
En `fetch`, las Promesas se rechazan únicamente por errores de red, como pérdida de conexión. Los errores HTTP (como 404 o 500) **no rechazan la Promesa**. Esto requiere verificar manualmente `response.ok` o el código de estado (`response.status`).

#### Ejemplo con manejo avanzado de errores:
```javascript
async function fetchWithErrorHandling(url) {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      // Lanza un error con el código y texto de estado
      throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    console.log('Datos recibidos:', data);
  } catch (error) {
    if (error.name === 'TypeError') {
      console.error('Error de red o problema CORS:', error);
    } else {
      console.error('Otro error:', error);
    }
  }
}

fetchWithErrorHandling('https://api.example.com/resource');
```

---

### **Abortar una solicitud con `AbortController`**
La API `AbortController` permite cancelar solicitudes `fetch` en progreso, una funcionalidad crucial para evitar problemas como solicitudes colgadas.

#### Ejemplo: Timeout con `AbortController`
```javascript
async function fetchWithTimeout(url, timeout) {
  const controller = new AbortController();
  const signal = controller.signal;

  // Configurar un timeout
  const timeoutId = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, { signal });

    if (!response.ok) {
      throw new Error(`Error HTTP: ${response.status}`);
    }

    const data = await response.json();
    console.log('Datos recibidos:', data);
  } catch (error) {
    if (error.name === 'AbortError') {
      console.error('Solicitud cancelada debido al timeout');
    } else {
      console.error('Error:', error);
    }
  } finally {
    clearTimeout(timeoutId); // Limpiar el timeout
  }
}

fetchWithTimeout('https://api.example.com/data', 5000); // Timeout de 5 segundos
```

---

### **Iteración sobre datos obtenidos con `fetch`**
En casos donde se reciben múltiples registros, puedes usar técnicas modernas como `for...of` y `map` para procesarlos:

```javascript
async function fetchAndProcess(url) {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }

    const data = await response.json();

    // Procesar y mostrar cada elemento
    for (const item of data) {
      console.log('Elemento:', item);
    }

    // Alternativa con map
    data.map(item => console.log('Procesado:', item));
  } catch (error) {
    console.error('Error al procesar datos:', error);
  }
}

fetchAndProcess('https://api.example.com/items');
```

---

### **Encadenar múltiples solicitudes**
`async/await` facilita el encadenamiento de múltiples solicitudes, especialmente en casos como APIs dependientes.

```javascript
async function fetchChainedRequests() {
  try {
    // Primera solicitud
    const userResponse = await fetch('https://api.example.com/user/123');
    if (!userResponse.ok) {
      throw new Error(`Error al obtener usuario: ${userResponse.status}`);
    }
    const user = await userResponse.json();

    // Segunda solicitud basada en datos del usuario
    const postsResponse = await fetch(`https://api.example.com/posts?userId=${user.id}`);
    if (!postsResponse.ok) {
      throw new Error(`Error al obtener posts: ${postsResponse.status}`);
    }
    const posts = await postsResponse.json();

    console.log('Usuario:', user);
    console.log('Posts:', posts);
  } catch (error) {
    console.error('Error en las solicitudes encadenadas:', error);
  }
}

fetchChainedRequests();
```

---

### **Comparativa entre `async/await` y Promesas tradicionales**
1. **Promesas tradicionales:**
   ```javascript
   fetch('https://api.example.com/data')
     .then(response => {
       if (!response.ok) throw new Error(`Error: ${response.status}`);
       return response.json();
     })
     .then(data => console.log(data))
     .catch(error => console.error(error));
   ```

2. **Con `async/await`:**
   ```javascript
   async function fetchData() {
     try {
       const response = await fetch('https://api.example.com/data');
       if (!response.ok) throw new Error(`Error: ${response.status}`);
       const data = await response.json();
       console.log(data);
     } catch (error) {
       console.error(error);
     }
   }
   fetchData();
   ```

### Resumen:
- `async/await` es más legible y lineal, especialmente para flujos complejos.
- Ambos enfoques son compatibles y puedes combinarlos según el caso.

---

### **Conclusión**
El uso de `fetch` con `async/await` proporciona una manera robusta y moderna de realizar solicitudes HTTP en JavaScript. Combina la potencia de Promesas con una sintaxis más limpia, especialmente útil en aplicaciones que manejan múltiples operaciones asíncronas y dependen de datos en tiempo real.


---


# **VI** Cuando usar `async/await` y cuando `.then/.catch` para manejar promesas con `fetch`?
La elección entre usar `async/await` y `.then/.catch` para manejar promesas con `fetch` en JavaScript depende del contexto, la legibilidad y la complejidad del código. Ambas formas son válidas y hacen lo mismo, pero cada una tiene sus ventajas y casos de uso ideales.

---

## 1. **`async/await`**
`async/await` es una sintaxis más moderna y legible que permite escribir código asíncrono de manera similar al código síncrono. Es especialmente útil en los siguientes casos:

### a) **Cuando el código asíncrono es complejo**
Si tienes múltiples operaciones asíncronas que dependen unas de otras, `async/await` hace que el código sea más fácil de leer y mantener.

Ejemplo:
```javascript
async function fetchData() {
  try {
    const response1 = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const data1 = await response1.json();

    const response2 = await fetch(`https://jsonplaceholder.typicode.com/users/${data1.userId}`);
    const data2 = await response2.json();

    console.log('Post:', data1);
    console.log('User:', data2);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
```

### b) **Cuando necesitas manejar errores de manera centralizada**
Con `async/await`, puedes usar un solo bloque `try/catch` para manejar errores en múltiples operaciones asíncronas.

Ejemplo:
```javascript
async function fetchData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/invalid-url');
    if (!response.ok) {
      throw new Error('Error HTTP: ' + response.status);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
```

### c) **Cuando prefieres un estilo de código más lineal**
`async/await` elimina el anidamiento excesivo que puede ocurrir con `.then/.catch`, lo que hace que el código sea más fácil de seguir.

Ejemplo:
```javascript
async function fetchData() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
  const data = await response.json();
  console.log(data);
}

fetchData();
```

---

## 2. **`.then/.catch`**
`.then/.catch` es la forma tradicional de manejar promesas y es útil en los siguientes casos:

### a) **Cuando el código asíncrono es simple**
Si solo necesitas hacer una solicitud y manejar la respuesta, `.then/.catch` puede ser más conciso.

Ejemplo:
```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### b) **Cuando trabajas con código más antiguo**
Si estás trabajando en un proyecto que no soporta `async/await` (por ejemplo, en entornos muy antiguos o con versiones de JavaScript anteriores a ES2017), `.then/.catch` es la opción obligatoria.

### c) **Cuando prefieres un enfoque funcional**
`.then/.catch` sigue un estilo más funcional, lo que puede ser preferible si estás acostumbrado a trabajar con programación funcional.

Ejemplo:
```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    if (!response.ok) {
      throw new Error('Error HTTP: ' + response.status);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

---

## 3. **Casos mixtos**
En algunos casos, puedes combinar ambas formas para aprovechar las ventajas de cada una. Por ejemplo, puedes usar `async/await` para manejar la lógica principal y `.then/.catch` para operaciones secundarias.

Ejemplo:
```javascript
async function fetchData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const data = await response.json();

    // Usar .then para una operación secundaria
    fetch(`https://jsonplaceholder.typicode.com/users/${data.userId}`)
      .then(response => response.json())
      .then(user => console.log('User:', user))
      .catch(error => console.error('Error fetching user:', error));

    console.log('Post:', data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
```

---

## 4. **Resumen de cuándo usar cada uno**

| **Caso de uso**                          | **`async/await`**                          | **`.then/.catch`**                        |
|------------------------------------------|--------------------------------------------|-------------------------------------------|
| Código asíncrono complejo                | ✅ Ideal                                   | ❌ Menos legible                          |
| Manejo centralizado de errores           | ✅ Ideal                                   | ❌ Requiere más anidamiento               |
| Código lineal y fácil de seguir          | ✅ Ideal                                   | ❌ Puede ser confuso con anidamientos     |
| Código simple y conciso                  | ❌ Puede ser excesivo                      | ✅ Ideal                                  |
| Compatibilidad con versiones antiguas    | ❌ No compatible (necesita ES2017+)        | ✅ Compatible                             |
| Estilo funcional                         | ❌ No es funcional                         | ✅ Ideal                                  |

---

## 5. **Conclusión**
- Usa **`async/await`** cuando:
  - El código asíncrono es complejo.
  - Prefieres un estilo de código más lineal y legible.
  - Necesitas manejar errores de manera centralizada.
- Usa **`.then/.catch`** cuando:
  - El código es simple y no requiere mucha lógica.
  - Trabajas en un entorno que no soporta `async/await`.
  - Prefieres un enfoque más funcional.

Ambas formas son válidas, y la elección depende de tus preferencias y del contexto del proyecto. En proyectos modernos, `async/await` es generalmente la opción preferida debido a su claridad y facilidad de uso.


---


# **VII** Resumen de `fetch`
En JavaScript, `fetch` es una API moderna y poderosa para realizar solicitudes HTTP asíncronas. Permite hacer consultas a URLs para obtener recursos, como datos JSON, HTML, imágenes, etc.

---

## 1. **Sintaxis básica de `fetch`**
La función `fetch` toma dos argumentos:
1. **URL**: La dirección del recurso que deseas consultar.
2. **Opciones (opcional)**: Un objeto de configuración que permite personalizar la solicitud (método HTTP, cabeceras, cuerpo, etc.).

```javascript
fetch(url, options)
  .then(response => {
    // Manejar la respuesta
  })
  .catch(error => {
    // Manejar errores
  });
```

---

## 2. **Métodos HTTP comunes**
`fetch` puede realizar solicitudes con diferentes métodos HTTP, como `GET`, `POST`, `PUT`, `DELETE`, etc. Aquí te muestro cómo hacerlo:

### a) **GET**: Obtener datos de un servidor
Es el método predeterminado si no especificas uno.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json()) // Convertir la respuesta a JSON
  .then(data => console.log(data))   // Mostrar los datos
  .catch(error => console.error('Error:', error));
```

### b) **POST**: Enviar datos al servidor
Debes especificar el método `POST` y proporcionar un cuerpo (body) con los datos.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json' // Especificar el tipo de contenido
  },
  body: JSON.stringify({ // Convertir el objeto a JSON
    title: 'foo',
    body: 'bar',
    userId: 1
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### c) **PUT**: Actualizar un recurso existente
Similar a `POST`, pero se usa para actualizar datos.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    id: 1,
    title: 'foo updated',
    body: 'bar updated',
    userId: 1
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### d) **DELETE**: Eliminar un recurso
No requiere un cuerpo, solo el método `DELETE`.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'DELETE'
})
  .then(response => {
    if (response.ok) {
      console.log('Recurso eliminado');
    }
  })
  .catch(error => console.error('Error:', error));
```

---

## 3. **Manejo de respuestas**
La respuesta de `fetch` es un objeto `Response` que contiene información sobre la solicitud. Puedes verificar el estado de la respuesta y convertirla a diferentes formatos.

### a) **Verificar el estado de la respuesta**
- `response.ok`: Devuelve `true` si el código de estado HTTP está en el rango 200-299.
- `response.status`: Devuelve el código de estado HTTP (por ejemplo, 200, 404, 500).

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Error en la solicitud: ' + response.status);
    }
  })
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

### b) **Convertir la respuesta a diferentes formatos**
- `response.json()`: Convierte la respuesta a un objeto JSON.
- `response.text()`: Devuelve la respuesta como texto.
- `response.blob()`: Devuelve la respuesta como un objeto `Blob` (útil para archivos binarios).
- `response.arrayBuffer()`: Devuelve la respuesta como un `ArrayBuffer`.

Ejemplo con `text()`:
```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.text())
  .then(text => console.log(text))
  .catch(error => console.error('Error:', error));
```

---

## 4. **Manejo de errores**
`fetch` solo rechaza la promesa si hay un error de red (por ejemplo, no hay conexión a Internet). Los errores HTTP (como 404 o 500) no causan un rechazo automático, por lo que debes verificarlos manualmente.

### a) **Manejo de errores de red**
```javascript
fetch('https://jsonplaceholder.typicode.com/invalid-url')
  .then(response => {
    if (!response.ok) {
      throw new Error('Error HTTP: ' + response.status);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

### b) **Manejo de errores con `async/await`**
Puedes usar `async/await` para manejar errores de manera más limpia.

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    if (!response.ok) {
      throw new Error('Error HTTP: ' + response.status);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
```

---

## 5. **Configuración avanzada**
El objeto de opciones de `fetch` permite personalizar la solicitud. Algunas opciones comunes incluyen:

- **headers**: Cabeceras HTTP personalizadas.
- **mode**: Modo de la solicitud (`cors`, `no-cors`, `same-origin`).
- **credentials**: Indica si se deben enviar cookies (`include`, `same-origin`, `omit`).
- **cache**: Controla el comportamiento de la caché (`default`, `no-store`, `reload`, etc.).

Ejemplo con cabeceras personalizadas:
```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  headers: {
    'Authorization': 'Bearer token',
    'Custom-Header': 'value'
  }
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

---

## 6. **Ejemplo completo con `async/await`**
Aquí tienes un ejemplo completo que combina todo lo anterior:

```javascript
async function fetchUserData(userId) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error('Error HTTP: ' + response.status);
    }

    const user = await response.json();
    console.log('Datos del usuario:', user);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchUserData(1);
```

---

## 7. **Consideraciones adicionales**
- **Compatibilidad**: `fetch` es compatible con la mayoría de los navegadores modernos. Si necesitas soporte para navegadores antiguos, puedes usar polyfills o librerías como `axios`.
- **CORS**: Si la URL a la que haces la solicitud está en un dominio diferente, asegúrate de que el servidor permita solicitudes CORS.
- **Limitaciones**: `fetch` no soporta cancelación de solicitudes de forma nativa (aunque puedes usar `AbortController` para ello).
