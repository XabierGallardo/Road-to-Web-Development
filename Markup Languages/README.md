# CSS

## 1. CSS Nesting

**CSS Nesting** es una nueva característica de la especificación de CSS que permite **anidar reglas de estilo dentro de otras** siguiendo la jerarquía de los elementos HTML, en lugar de repetir selectores completos.

👉 Esto busca resolver el problema de repetición y mejorar la **legibilidad** y el **mantenimiento** del código CSS, inspirándose en preprocesadores como **Sass/SCSS** o **Less**.

---

### 📌 Problema en CSS tradicional

En **CSS normal**, si queremos aplicar estilos a un `h4` que está dentro de un `main`, escribimos:

```css
main {
  border: 2px solid;
}

main h4 {
  color: red;
}

main h4 span {
  font-weight: bold;
}
```

El problema es la **repetición del selector `main`** cada vez que se quiera aplicar un estilo descendente.

---

### 📌 Solución con CSS Nesting

Con CSS Nesting, podés escribir:

```css
main {
  border: 2px solid;

  & h4 {
    color: red;

    & span {
      font-weight: bold;
    }
  }
}
```

🔍 Explicación:

* `&` significa **el selector padre actual** (en este caso `main`).
* `& h4` equivale a `main h4`.
* `& span` dentro de `h4` equivale a `main h4 span`.

---

### 📌 Reglas sintácticas de CSS Nesting

### 1. **El uso del `&` es obligatorio en la mayoría de los casos**

A diferencia de SCSS, en CSS Nesting **no podés simplemente escribir el selector anidado sin `&`**.
Ejemplo ❌ (inválido en CSS estándar moderno):

```css
main {
  h4 {
    color: red;
  }
}
```

Ejemplo ✅ (válido):

```css
main {
  & h4 {
    color: red;
  }
}
```

### 2. **Pseudo-clases y pseudo-elementos**

Podés anidarlos fácilmente:

```css
button {
  color: white;

  &:hover {
    background: blue;
  }

  &::before {
    content: "👉 ";
  }
}
```

Esto equivale a:

```css
button { color: white; }
button:hover { background: blue; }
button::before { content: "👉 "; }
```

### 3. **Combinación con media queries y @rules**

Podés anidar consultas dentro de selectores:

```css
.card {
  padding: 1rem;

  @media (min-width: 768px) {
    padding: 2rem;
  }
}
```

Esto equivale a:

```css
.card { padding: 1rem; }
@media (min-width: 768px) {
  .card { padding: 2rem; }
}
```

### 4. **Selectores de hermano y adyacente**

```css
h2 {
  margin-bottom: 0.5rem;

  & + p {
    font-style: italic;
  }
}
```

Traducción:

```css
h2 { margin-bottom: 0.5rem; }
h2 + p { font-style: italic; }
```

---

### 📌 Diferencias con SCSS/Sass

| Característica         | SCSS/Sass               | CSS Nesting (estándar)      |
| ---------------------- | ----------------------- | --------------------------- |
| Anidar sin `&`         | ✅ permitido             | ❌ no permitido              |
| Variables              | ✅ `$color: red;`        | ❌ usa `var(--color)` de CSS |
| Mixins/funciones       | ✅ soportado             | ❌ no                        |
| Media queries anidadas | ✅                       | ✅                           |
| Compatibilidad         | Preprocesador requerido | Navegadores modernos        |

Ejemplo en SCSS:

```scss
main {
  h4 {
    color: red;
  }
}
```

En CSS Nesting eso es inválido, porque **siempre necesitas `&`**.

---

### 📌 Compatibilidad actual (2025)

* ✅ **Chrome** (desde 112+)
* ✅ **Edge** (desde 112+)
* ✅ **Safari** (desde 16.5+)
* ✅ **Firefox** (desde 117+)
* ⚠️ Internet Explorer: no soportado (y nunca lo estará)

👉 Hoy ya es **usable en producción**, pero se recomienda usar un **postcss-nesting** o **Autoprefixer** para mayor compatibilidad en proyectos legacy.

---

### 📌 Beneficios técnicos

1. **Menos repetición** → código más limpio y DRY (Don't Repeat Yourself).
2. **Mayor legibilidad** → estructura CSS refleja estructura HTML.
3. **Estandarización** → ya no dependés de preprocesadores (Sass/Less).
4. **Compatibilidad con cascade layers y custom properties**.

---

### 📌 Posibles riesgos / malas prácticas

* **Demasiada anidación**: puede generar CSS muy específico y difícil de sobrescribir.
  Ejemplo ❌:

  ```css
  main {
    & section {
      & article {
        & p {
          & span {
            color: red;
          }
        }
      }
    }
  }
  ```

  Resultado → `main section article p span { color: red; }` (hiper específico).

* **Uso sin control de `&`**: si se confunde con SCSS, puede romper compatibilidad.

---

✅ **Conclusión técnica:**
CSS Nesting es parte de la **nueva ola de CSS nativo** (junto con `:is()`, cascade layers, container queries, etc.). Ya es usable hoy, pero requiere usar `&` como referencia al selector padre. Reduce repetición y mejora la legibilidad, siempre que no se abuse de la profundidad de anidación.

---

## Ejemplo practico
### 📌 HTML del formulario

```html
<main>
  <form class="login-form">
    <h2>Login</h2>

    <label>
      Usuario
      <input type="text" name="username" />
    </label>

    <label>
      Contraseña
      <input type="password" name="password" />
    </label>

    <button type="submit">Ingresar</button>
  </form>
</main>
```

---

### 📌 CSS con **Nesting nativo**

```css
main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f5f5f5;

  .login-form {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    width: 300px;

    h2 {
      margin-bottom: 1.5rem;
      text-align: center;
      color: #333;
    }

    label {
      display: block;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: #555;

      input {
        width: 100%;
        padding: 0.6rem;
        margin-top: 0.3rem;
        border: 1px solid #ccc;
        border-radius: 8px;
        font-size: 1rem;

        &:focus {
          border-color: #9b59b6;
          outline: none;
          box-shadow: 0 0 4px rgba(155, 89, 182, 0.5);
        }
      }
    }

    button {
      width: 100%;
      padding: 0.7rem;
      border: none;
      border-radius: 8px;
      background: #9b59b6;
      color: white;
      font-size: 1rem;
      cursor: pointer;
      transition: background 0.3s;

      &:hover {
        background: #8e44ad;
      }

      &:active {
        background: #732d91;
      }
    }

    /* Responsive con nesting */
    @media (max-width: 480px) {
      width: 90%;
      padding: 1rem;

      h2 {
        font-size: 1.2rem;
      }
    }
  }
}
```

---

### 📌 Traducción a **CSS plano**

El navegador lo compila internamente a:

```css
main { display: flex; justify-content: center; ... }
main .login-form { background: white; ... }
main .login-form h2 { margin-bottom: 1.5rem; ... }
main .login-form label { display: block; ... }
main .login-form label input { width: 100%; ... }
main .login-form label input:focus { border-color: #9b59b6; ... }
main .login-form button { width: 100%; ... }
main .login-form button:hover { background: #8e44ad; }
main .login-form button:active { background: #732d91; }
@media (max-width: 480px) {
  main .login-form { width: 90%; padding: 1rem; }
  main .login-form h2 { font-size: 1.2rem; }
}
```

---

✅ **Ventajas del nesting en este ejemplo:**

* No repetimos `main .login-form` todo el tiempo.
* La jerarquía CSS refleja **la estructura HTML real**.
* Pseudo-clases (`:hover`, `:focus`, `:active`) y media queries quedan agrupadas en su contexto.


---

## La propiedad `box-sizing`

### 🔹 1. El **modelo de caja** en CSS

Cada elemento en una página HTML se representa como una **caja rectangular**, y esa caja está formada por varias capas:

1. **Content box** (contenido): el área donde se renderiza el contenido (texto, imágenes, etc.).
2. **Padding box**: espacio interno entre el contenido y el borde (relleno).
3. **Border box**: el borde que rodea al padding y al contenido.
4. **Margin box**: el espacio externo que separa el elemento de otros elementos.

📌 En CSS, cuando declaramos un `width` o `height`, por defecto, ese valor **aplica únicamente al content box**, y los `padding` y `border` se suman a ese tamaño.

---

### 🔹 2. La propiedad `box-sizing`

La propiedad [`box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) define **cómo el navegador calcula el tamaño total de un elemento**:

* Si el `width` y `height` afectan **solo al content box** (comportamiento por defecto).
* O si abarcan también `padding` y `border` (más predecible en layouts modernos).

Valores principales:

* `content-box` (valor por defecto).
* `border-box` (muy usado en frameworks como Bootstrap, Tailwind, etc.).
* `inherit`, `initial`, `unset` → heredan o resetean valores (menos usados directamente).

---

### 🔹 3. `box-sizing: content-box;` (el valor por defecto)

Esto significa:

* El valor de `width` y `height` **solo incluye el área de contenido**.
* El `padding` y el `border` **se suman** al tamaño final del elemento.

📐 Ejemplo:

```css
div {
  width: 200px;
  padding: 20px;
  border: 10px solid black;
  box-sizing: content-box;
}
```

👉 Cálculo del ancho total:

* Content: **200px**
* Padding izquierdo + derecho: **40px**
* Border izquierdo + derecho: **20px**

➡️ **Anchura final: 200 + 40 + 20 = 260px**

Esto suele generar problemas cuando quieres que un `div` encaje exactamente en un layout.

---

### 🔹 4. `box-sizing: border-box;`

Esto significa:

* El valor de `width` y `height` **incluyen el área de contenido + padding + border**.
* Es decir, el navegador "encaja" todo dentro del tamaño que declaraste.

📐 Ejemplo:

```css
div {
  width: 200px;
  padding: 20px;
  border: 10px solid black;
  box-sizing: border-box;
}
```

👉 Cálculo del ancho total:

* `width` declarado = **200px**
* De esos 200px, ya se reservan 40px para padding + 20px para border.
* El contenido (content box) se reduce a **140px**.

➡️ **Anchura final = 200px exactos** (no crece con padding ni borde).

---

### 🔹 5. Comparación visual

| Propiedad                 | ¿Qué incluye `width`?        | Ancho final si `width=200px; padding=20px; border=10px` |
| ------------------------- | ---------------------------- | ------------------------------------------------------- |
| `box-sizing: content-box` | Solo contenido               | 260px                                                   |
| `box-sizing: border-box`  | Contenido + padding + border | 200px                                                   |

---

### 🔹 6. Ejemplo práctico

```html
<style>
  .content-box {
    width: 200px;
    padding: 20px;
    border: 10px solid red;
    box-sizing: content-box;
  }

  .border-box {
    width: 200px;
    padding: 20px;
    border: 10px solid blue;
    box-sizing: border-box;
  }
</style>

<div class="content-box">Content-box</div>
<div class="border-box">Border-box</div>
```

👉 Resultado:

* El `.content-box` ocupará **260px de ancho** (más grande de lo que pediste).
* El `.border-box` ocupará **200px exactos**.

---

### 🔹 7. ¿Por qué se recomienda `border-box`?

Hoy en día, casi todos los proyectos grandes aplican un **reset CSS global** como este:

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

Porque:

* Evita cálculos extra: `width` significa **lo que ves**.
* Facilita layouts responsivos.
* Hace que `padding` y `border` **no rompan el diseño**.
* Es el estándar de facto en frameworks modernos.

---

✅ **En resumen:**

* `box-sizing: content-box` (default): `width` solo mide contenido → el tamaño total puede crecer.
* `box-sizing: border-box`: `width` incluye contenido + padding + border → el tamaño total siempre coincide con el declarado.

---


## 2. Selectores universales `*`, `html` y `body`
### Selectores Universales en CSS

El **selector universal** en CSS es representado por el asterisco (`*`) y selecciona **todos los elementos** del documento, aplicando un conjunto de reglas de estilo a todos ellos sin importar el tipo o su posición en el árbol DOM.

#### Sintaxis:
```css
* {
  propiedad: valor;
}
```

Este código selecciona todos los elementos de la página y aplica las propiedades especificadas. Por ejemplo:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

Este uso del selector universal establece que todos los elementos del documento tendrán márgenes y rellenos en `0`, además de asegurarse de que el `box-sizing` esté configurado en `border-box` para todos los elementos. Este es un ejemplo típico de cómo se usa en "reset" o "normalize" de CSS, donde se eliminan los márgenes y rellenos predeterminados del navegador para obtener un punto de partida consistente para el diseño.

### Características del Selector Universal

1. **Alcance Global:** Afecta a todos los elementos del documento, como `div`, `p`, `span`, `h1`, `img`, y todos los demás.
   
2. **Especificidad Baja:** Tiene una especificidad muy baja (0,0,0,0), lo que significa que las reglas definidas por este selector pueden ser sobrescritas fácilmente por otros selectores más específicos (clases, IDs, etc.).

3. **Rendimiento:** En documentos pequeños, el uso del selector universal no supone un problema de rendimiento. Sin embargo, en documentos grandes o complejos, puede impactar el rendimiento del navegador, ya que el selector tiene que buscar y aplicar los estilos a cada elemento de la página.

4. **Combinación con otros selectores:** Puedes limitar su uso aplicándolo en combinación con otros selectores para restringir el alcance de la regla. Por ejemplo:

   ```css
   div * {
     color: red;
   }
   ```

   Esto selecciona todos los elementos que son descendientes de cualquier `div`, aplicando el color rojo a esos elementos solamente.

---

### Comparación y uso: `*`, `html`, y `body`

Aunque el selector universal (`*`), el selector `html`, y el selector `body` pueden parecer similares en cuanto a su capacidad de aplicar estilos globales, tienen diferencias clave y se utilizan en situaciones diferentes. A continuación, se detalla cuándo y cómo utilizar cada uno.

#### 1. Selector Universal (`*`)

El selector `*` selecciona todos los elementos del documento sin ninguna distinción. Se utiliza cuando se desea aplicar un estilo de manera **global** a todos los elementos o cuando se desea asegurar que todos los elementos sigan una regla específica.

**Cuándo usarlo:**
- Para resetear o normalizar estilos predeterminados del navegador.
- Para aplicar una propiedad como `box-sizing: border-box` de manera uniforme en todos los elementos.
- Para establecer márgenes, rellenos o bordes comunes en todos los elementos de la página.

**Ejemplo:**
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```
Este uso asegura que todos los elementos tengan márgenes y rellenos en cero y que el tamaño de la caja incluya bordes y rellenos en su cálculo total.

#### 2. Selector `html`

El selector `html` selecciona el elemento raíz del documento HTML. En términos de estructura del DOM, `html` es el primer y más alto elemento del árbol, que contiene todos los demás elementos. Cualquier estilo que se aplique al `html` afectará indirectamente a todo lo que está dentro de la página, aunque es más limitado que el selector universal.

**Cuándo usarlo:**
- Para definir estilos base de toda la página que dependen del contenedor del documento completo, como el tamaño de fuente o la altura mínima.
- Para establecer propiedades de visualización o dimensiones en el nivel raíz de la página.
- Para definir variables CSS globales con `:root`, que también selecciona el `html`.

**Ejemplo:**
```css
html {
  font-size: 16px;
  height: 100%;
}
```
Aquí, el tamaño de fuente predeterminado de toda la página es de `16px` y la altura del documento se establece al 100% del viewport del navegador.

#### 3. Selector `body`

El selector `body` selecciona el cuerpo del documento, es decir, el contenedor principal de todo el contenido visual de la página. Este selector afecta directamente a todo lo que está dentro del cuerpo del documento (como los párrafos, encabezados, imágenes, etc.). A diferencia del `html`, el `body` excluye algunos elementos especiales como los metadatos o scripts que no forman parte de la estructura visible.

**Cuándo usarlo:**
- Para aplicar estilos a todo el contenido visible de la página.
- Para controlar la disposición de los elementos principales, el color de fondo, y la tipografía general.
- Para definir márgenes automáticos, centrado de contenido o reglas de diseño de página.

**Ejemplo:**
```css
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
}
```
En este caso, se eliminan los márgenes del `body`, se define una tipografía general para el contenido y se aplica un color de fondo a la página visible.

---

### Diferencias Clave entre `*`, `html`, y `body`

| Selector | Descripción | Aplicación | Cuándo usar |
|----------|-------------|------------|-------------|
| `*`      | Selecciona todos los elementos del documento sin excepción. | Aplicar estilos globales o resetear márgenes, rellenos, etc. | Cuando se necesita aplicar una regla a todos los elementos sin excepción. |
| `html`   | Selecciona el elemento raíz del documento, el contenedor de todo. | Establecer tamaños o propiedades que afectan a toda la página, como el tamaño de fuente o altura mínima. | Cuando necesitas controlar el elemento raíz del documento. |
| `body`   | Selecciona el cuerpo del documento, que contiene el contenido visible. | Aplicar estilos globales al contenido visible, como fuentes, márgenes, y fondos. | Para controlar el diseño y la apariencia de todo el contenido visible de la página. |

---

### Ejemplo Comparativo:

```css
* {
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  background-color: #eaeaea;
}

body {
  font-family: 'Arial', sans-serif;
  margin: 20px auto;
  max-width: 1200px;
  background-color: white;
}
```

- **`*`**: Elimina los márgenes y rellenos de **todos los elementos** de la página.
- **`html`**: Establece el tamaño de fuente base y el color de fondo del documento completo.
- **`body`**: Controla la apariencia y el layout del contenido principal visible de la página.

En resumen, `*` es ideal para aplicar estilos generales a todos los elementos, `html` para definir reglas que afectan todo el documento a nivel raíz, y `body` para diseñar el contenido visual principal.


<hr>


## 3. `:root { }`
En CSS, `:root` es un selector pseudo-clase que se refiere al elemento raíz del documento, generalmente el elemento `<html>`. Es similar a usar `html` como selector, pero con una ventaja clave: es más específico y se puede utilizar para definir variables CSS globales (también llamadas *custom properties*).

### ¿Qué puedes hacer con `:root`?

1. **Definir variables globales:**
   Una de las principales aplicaciones de `:root` es definir variables CSS que pueden ser reutilizadas en todo el documento. Estas variables se declaran usando el prefijo `--`, y se acceden con la función `var()`.

   ```css
   :root {
     --main-color: #3498db;
     --font-size: 16px;
   }

   body {
     background-color: var(--main-color);
     font-size: var(--font-size);
   }
   ```

   En este ejemplo, las variables `--main-color` y `--font-size` se definen en el `:root`, lo que las hace accesibles en cualquier parte del documento.

2. **Especificidad alta:**
   Al usar `:root`, el estilo aplicado tiene una mayor especificidad que el selector `html`, lo que significa que puede sobrescribir estilos aplicados directamente a `html`.

3. **Estilos específicos para todo el documento:**
   Puedes aplicar estilos que afecten a todo el documento desde `:root`. Aunque esto también se podría hacer con el selector `html`, `:root` te permite combinarlo con otras características, como las variables.

### ¿Cuándo usar `:root`?

- **Variables CSS globales:** Útil cuando necesitas definir y reutilizar valores como colores, tamaños de fuente, o márgenes de forma consistente en tu sitio web.
- **Control temático:** Puedes usarlo para definir temas o cambios de estilo global de manera eficiente.

### Ejemplo más avanzado con temas:

```css
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
}

.dark-theme {
  --primary-color: #2c3e50;
  --secondary-color: #1abc9c;
}

body {
  background-color: var(--primary-color);
  color: var(--secondary-color);
}
```

En este ejemplo, puedes cambiar de tema oscuro a claro al alternar la clase `dark-theme` en el `body` o cualquier contenedor principal.


<hr>


## 4. Margin Collapse
El fenómeno por el cual la etiqueta `margin` de un elemento hijo no separa dicho elemento del contenedor padre en CSS se conoce como **colapso de márgenes** (*margin collapsing*). Este es un comportamiento estándar en CSS que afecta a los márgenes verticales (márgenes `top` y `bottom`) en ciertas situaciones.

### **¿Qué es el colapso de márgenes?**

El colapso de márgenes ocurre cuando dos márgenes verticales adyacentes (de un elemento hijo y su contenedor padre, o entre dos elementos hermanos) se combinan o "colapsan" en un solo margen. En lugar de que los márgenes se sumen, se toma solo el margen más grande de los dos.

### **Por qué sucede con los elementos hijos y el contenedor padre:**

Si un contenedor padre no tiene relleno (`padding`), borde (`border`), o contenido entre su margen superior e inferior y el de su hijo, el margen superior o inferior del hijo puede "colapsar" con el margen del padre. Esto significa que en lugar de sumar ambos márgenes, se visualiza solo el más grande de los dos.

#### **Ejemplo:**
```html
<div class="padre">
  <div class="hijo">Contenido</div>
</div>
```

```css
.padre {
  background-color: lightgray;
  margin: 20px;
}

.hijo {
  background-color: lightblue;
  margin: 30px 0;
}
```

En este caso, esperarías que el `hijo` tuviera un margen de 30px dentro del `padre`, pero puede parecer que el `padre` no se separa correctamente de su contenedor o de otros elementos debido al colapso de márgenes.

### **Cómo evitar el colapso de márgenes:**

Para asegurarte de que el margen del elemento hijo se respete dentro del contenedor, puedes aplicar alguna de las siguientes soluciones:

1. **Agregar un `padding` o `border` al contenedor padre**:
   Cuando el contenedor tiene un `padding` o `border`, el colapso de márgenes no ocurre.
   
   ```css
   .padre {
     background-color: lightgray;
     padding: 1px; /* Evita el colapso de márgenes */
   }
   ```

2. **Establecer `overflow: hidden` o `overflow: auto` en el contenedor padre**:
   Esto crea un nuevo contexto de formato que impide el colapso de márgenes.
   
   ```css
   .padre {
     overflow: hidden; /* Previene el colapso */
   }
   ```

3. **Usar `display: flex` o `display: grid` en el contenedor padre**:
   Los contenedores flexibles o de cuadrícula no colapsan márgenes con sus hijos.
   
   ```css
   .padre {
     display: flex;
   }
   ```

4. **Cambiar el flujo de diseño del hijo con `float` o `position: absolute`**:
   Un elemento que está flotando o posicionado absolutamente tampoco participará en el colapso de márgenes.
   
   ```css
   .hijo {
     float: left; /* Evita el colapso */
   }
   ```

### **Resumiendo**:
El colapso de márgenes en CSS ocurre cuando los márgenes verticales adyacentes se combinan en uno solo, causando que el margen del hijo no parezca separar el elemento hijo del contenedor padre. Puedes evitarlo usando `padding`, `border`, `overflow`, o alterando el flujo de diseño del contenedor o del hijo.


---

## When to use `<form>` element?
Your button and input elements do not necessarily need to be under a `<form>` label, **unless you are using them as part of a form submission process where you want to capture and process user input**. However, in many cases, it is perfectly acceptable and common to use buttons and input elements outside of a `<form>` label, especially if they are used for other purposes such as triggering actions or displaying information.

The `<form>` element in HTML is typically used to group and submit user input controls (such as text inputs, checkboxes, radio buttons, etc.) to a server for processing. When you submit a form, the browser collects the data from the form controls and sends it to the specified URL for further processing, typically through an HTTP request.

If you are not submitting any form data or using the form for its traditional purpose, you do not necessarily need to enclose your elements within a `<form>` label. However, it is always important to structure your HTML in a way that makes sense for your specific use case and maintains accessibility and usability for your users. If your buttons and input elements logically belong together and serve a common purpose, you may choose to group them together under a `<form>` label for clarity and organization. But if they are independent elements with distinct functions, it is perfectly fine to use them outside of a `<form>` label.
