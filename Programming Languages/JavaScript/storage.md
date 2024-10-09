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