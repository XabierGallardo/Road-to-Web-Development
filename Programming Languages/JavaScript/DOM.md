# DOM en JavaScript
## Propagacion de eventos en JavaScript
La **propagación de eventos** en el DOM de JavaScript es el proceso mediante el cual un evento activado en un nodo de la página web puede viajar a través de varios elementos. Entender este proceso es fundamental para manipular correctamente los eventos en una aplicación web. En JavaScript, la propagación de eventos se maneja en tres fases principales:

### 1. **Fase de Captura**: (Event Capturing)
En esta fase, el evento se propaga desde el nodo más alto del DOM (generalmente `window`) hasta el nodo objetivo, pasando por cada elemento padre de manera descendente.

### 2. **Fase de Objetivo**: (Target)
En esta fase, el evento alcanza el nodo en el que ocurrió (el elemento donde se originó el evento, llamado `target`).

### 3. **Fase de Burbuja**: (Event Bubbling)
Después de que el evento llega al objetivo, se propaga de nuevo hacia arriba desde el nodo objetivo hacia el nodo más alto, pasando por cada uno de los ancestros.

### Ejemplo básico de propagación de eventos

Imagina una estructura HTML con un botón dentro de un div, y ese div dentro del body:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Propagación de Eventos</title>
</head>
<body>
    <div id="miDiv">
        <button id="miBoton">Clic aquí</button>
    </div>

    <script>
        document.body.addEventListener('click', function() {
            console.log('Evento en Body');
        });

        document.getElementById('miDiv').addEventListener('click', function() {
            console.log('Evento en Div');
        });

        document.getElementById('miBoton').addEventListener('click', function() {
            console.log('Evento en Botón');
        });
    </script>
</body>
</html>
```

### Orden de ejecución:

1. **Fase de Captura**: El evento viaja desde `window`, pasando por `body`, luego por `div` y finalmente llega al `button`.
2. **Fase de Objetivo**: El evento es manejado en el botón.
3. **Fase de Burbuja**: El evento sube de nuevo pasando por `div`, luego `body`, y finalmente `window`.

Si haces clic en el botón, la consola mostrará:
```
Evento en Botón
Evento en Div
Evento en Body
```

Esto es un ejemplo de **event bubbling** (propagación en burbuja), donde el evento comienza en el nodo objetivo y luego "burbujea" hacia arriba.

### Deteniendo la propagación de eventos con `event.stopPropagation()`

A veces, queremos evitar que el evento se propague más allá de un determinado elemento. Para esto, usamos `event.stopPropagation()`. Este método detiene la propagación en cualquiera de las fases (captura o burbuja).

#### Modificamos el ejemplo anterior:

```javascript
document.getElementById('miBoton').addEventListener('click', function(event) {
    event.stopPropagation(); // Detiene la propagación del evento
    console.log('Evento en Botón');
});
```

Ahora, si haces clic en el botón, solo se registrará el evento del botón, sin que el evento se propague al `div` ni al `body`. La consola solo mostrará:
```
Evento en Botón
```

### Evitar el comportamiento predeterminado con `event.preventDefault()`

Algunos eventos tienen comportamientos predeterminados del navegador. Por ejemplo, en un formulario, al hacer clic en un botón de tipo submit, se recarga la página. Si queremos evitar ese comportamiento, usamos `event.preventDefault()`.

#### Ejemplo con un formulario:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event preventDefault</title>
</head>
<body>
    <form id="miFormulario">
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        <button type="submit">Enviar</button>
    </form>

    <script>
        document.getElementById('miFormulario').addEventListener('submit', function(event) {
            event.preventDefault(); // Evita que el formulario se envíe
            console.log('Formulario no enviado');
        });
    </script>
</body>
</html>
```

En este caso, aunque el botón tiene el tipo `submit`, el formulario no se enviará ni la página se recargará gracias a `event.preventDefault()`. En su lugar, se mostrará en la consola:
```
Formulario no enviado
```

### Propagación en Fase de Captura

Para que el evento sea capturado en la fase de captura (antes de llegar al objetivo), puedes pasar un tercer argumento `true` en el `addEventListener`. Esto cambia el comportamiento por defecto y captura el evento durante la fase descendente.

#### Ejemplo de fase de captura:

```javascript
document.getElementById('miDiv').addEventListener('click', function() {
    console.log('Evento en Div - Captura');
}, true);
```

En este caso, el evento será capturado en el `div` antes de llegar al botón, incluso si el clic fue en el botón.

### Resumen:

1. **Propagación de eventos**: Se refiere al recorrido que realiza un evento a través del DOM, pasando por sus fases de captura, objetivo y burbuja.
2. **Fase de Captura**: El evento viaja desde el nodo más alto (`window`) hacia el nodo objetivo.
3. **Fase de Objetivo**: El evento se maneja en el nodo donde ocurrió.
4. **Fase de Burbuja**: El evento se propaga hacia arriba desde el nodo objetivo hacia los ancestros.
5. **`event.stopPropagation()`**: Detiene la propagación del evento en cualquier fase.
6. **`event.preventDefault()`**: Evita el comportamiento predeterminado asociado con el evento (como el envío de un formulario o el enlace a una nueva página).

Con estas técnicas, puedes tener un control más fino sobre cómo se manejan los eventos en tu aplicación web, lo cual es crucial para desarrollar interfaces interactivas y eficientes.

___


## El objeto `document` en JavaScript
El `document` es un **objeto** que forma parte del modelo de objetos del documento o **DOM (Document Object Model)**. El DOM es una representación estructurada de un documento HTML o XML, donde cada parte del documento se convierte en un objeto que se puede manipular mediante JavaScript.

### El objeto `document`

El objeto `document` en JavaScript representa la página web cargada en el navegador. Es una interfaz que te permite acceder y manipular el contenido y la estructura del documento HTML. A través del objeto `document`, puedes modificar elementos, crear nuevos, eliminar otros, cambiar sus atributos, estilos, entre muchas otras operaciones.

### Características clave del objeto `document`:
- **Es parte del objeto global `window`**: `document` es una propiedad del objeto `window`, por lo que en el entorno del navegador, puedes acceder a él directamente sin necesidad de hacer referencia explícita a `window.document`.

### Operaciones comunes con `document`:

1. **Acceso a elementos HTML**: 
   Puedes acceder a elementos en la página mediante diversos métodos:
   
   - `document.getElementById('id')`: Obtiene un elemento por su ID.
   - `document.querySelector('.clase')`: Obtiene el primer elemento que coincida con un selector CSS.
   - `document.getElementsByClassName('class')`: Obtiene una colección de todos los elementos con una clase específica.

   ```javascript
   let encabezado = document.getElementById('miEncabezado');
   ```

2. **Manipulación del contenido**: 
   El objeto `document` permite modificar el contenido de los elementos HTML. Por ejemplo, usando la propiedad `innerHTML` o `textContent`.

   ```javascript
   document.getElementById('miEncabezado').innerHTML = 'Nuevo título';
   ```

3. **Creación de nuevos elementos**: 
   Puedes crear nuevos nodos y elementos y añadirlos al DOM.

   ```javascript
   let nuevoParrafo = document.createElement('p');
   nuevoParrafo.textContent = 'Este es un nuevo párrafo';
   document.body.appendChild(nuevoParrafo);
   ```

4. **Modificar atributos**:
   También puedes cambiar atributos de los elementos HTML, como clases, identificadores, o incluso agregar nuevos atributos.

   ```javascript
   document.getElementById('miEncabezado').setAttribute('class', 'nuevo-estilo');
   ```

5. **Manipulación de estilos**:
   A través del objeto `document`, también puedes modificar estilos CSS de los elementos.

   ```javascript
   document.getElementById('miEncabezado').style.color = 'blue';
   ```

6. **Interacción con eventos**:
   El `document` también permite manipular eventos, como hacer clic, pasar el ratón, cargar la página, entre otros. Un ejemplo común es agregar un "escuchador" de eventos:

   ```javascript
   document.getElementById('miBoton').addEventListener('click', function() {
       alert('¡Botón clickeado!');
   });
   ```

### Ejemplo práctico:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejemplo de Document</title>
</head>
<body>
    <h1 id="miEncabezado">Hola Mundo</h1>
    <button id="miBoton">Cambiar título</button>

    <script>
        document.getElementById('miBoton').addEventListener('click', function() {
            document.getElementById('miEncabezado').textContent = 'Nuevo Título';
        });
    </script>
</body>
</html>
```

### Resumen:

El objeto `document` es esencial en JavaScript para trabajar con la estructura del documento HTML. Permite acceder, modificar, eliminar y crear contenido y elementos en la página web, lo que lo convierte en una pieza fundamental para la interacción con el DOM.