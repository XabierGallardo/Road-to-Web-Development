# [Documentacion Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
Bootstrap es uno de los frameworks de CSS más populares para diseñar sitios web responsivos y móviles. Fue desarrollado por Twitter y se lanzó como un proyecto de código abierto en 2011. Bootstrap simplifica el desarrollo web al proporcionar una colección de componentes prediseñados, como formularios, botones, menús, y grids, junto con un sistema de clases que permiten al desarrollador estilar y organizar el contenido de manera eficiente y rápida.

<p>
  <img src="sample.png" alt="imagen muestra">
</p>

### Ventajas de Boostrap
- **Fácil de usar**: Cualquier persona con conocimientos básicos de HTML y CSS puede empezar a utilizar Bootstrap
- **Características responsive**: El CSS responsivo de Bootstrap se ajusta a teléfonos, tabletas y ordenadores de sobremesa.
- **Compatibilidad entre navegadores**: Bootstrap 5 es compatible con todos los navegadores modernos

### [Empezar con Bootstrap 5.3](https://getbootstrap.com/)
- Incluir Bootstrap 5 desde una CDN (Content Delivery Network)
- Descargar Boostrap 5 desde getbootstrap.com
Bootstrap 5 está diseñado para ser responsivo para dispositivos móviles. Para asegurar un correcto renderizado y zoom táctil, es imprescindible añadir
```html
<meta name=«viewport» content=«width=device-width, initial-scale=1»>
```
**width=ancho-dispositivo** ajusta el ancho de la página al ancho de pantalla del dispositivo.
**initial-scale=1** establece el nivel de zoom inicial cuando el navegador carga la página por primera vez.

### Características principales de Bootstrap:
1. **Grid System (Sistema de cuadrícula):** Facilita la creación de layouts responsivos.
2. **Componentes predefinidos:** Incluye elementos como botones, barras de navegación, formularios, etc.
3. **Estilos de tipografía:** Estilos de texto predefinidos para encabezados, párrafos, listas, etc.
4. **Compatibilidad con navegadores:** Es compatible con la mayoría de los navegadores.
5. **Personalización:** Se puede modificar y personalizar fácilmente mediante Sass o variables CSS.


## 1. Grid System
Uno de los puntos más fuertes de Bootstrap es su **Sistema de Cuadrícula** o Grid System, que facilita la organización de contenido de manera responsiva. Bootstrap utiliza un sistema de 12 columnas que se puede combinar para crear diferentes layouts.

```html
<div class="container">
  <div class="row">
    <div class="col-md-4">Columna 1 (4/12)</div>
    <div class="col-md-4">Columna 2 (4/12)</div>
    <div class="col-md-4">Columna 3 (4/12)</div>
  </div>
</div>
```

### Explicación:
- El contenedor (`container`) mantiene el layout centrado y con márgenes adecuados.
- La fila (`row`) organiza el espacio horizontal.
- Las columnas (`col-md-4`) indican cuántas de las 12 columnas disponibles ocupa cada elemento. En este ejemplo, hay tres columnas de tamaño mediano (en pantallas medianas o más grandes) que ocupan 4 espacios cada una (4+4+4 = 12).


### Layout responsivo
Bootstrap permite crear layouts responsivos que se adaptan a diferentes tamaños de pantalla. Las clases cambian según el tamaño de la pantalla:
- `col-xs-*`: Extra pequeña (<576px)
- `col-sm-*`: Pequeña (≥576px)
- `col-md-*`: Mediana (≥768px)
- `col-lg-*`: Grande (≥992px)
- `col-xl-*`: Extra grande (≥1200px)

Ejemplo:

```html
<div class="container">
  <div class="row">
    <div class="col-sm-6 col-md-4 col-lg-3">Columna 1</div>
    <div class="col-sm-6 col-md-4 col-lg-3">Columna 2</div>
    <div class="col-sm-6 col-md-4 col-lg-3">Columna 3</div>
    <div class="col-sm-6 col-md-4 col-lg-3">Columna 4</div>
  </div>
</div>
```

En este ejemplo:
- Para pantallas pequeñas, cada columna ocupa la mitad del espacio (`col-sm-6`).
- Para pantallas medianas, cada columna ocupa un tercio (`col-md-4`).
- Para pantallas grandes, cada columna ocupa un cuarto (`col-lg-3`).


## 2. Componentes
Bootstrap incluye una gran variedad de componentes que puedes utilizar para construir tu interfaz de usuario. Algunos de los más comunes son:

#### Botones
Bootstrap proporciona estilos predefinidos para botones, con clases como `.btn`, `.btn-primary`, `.btn-secondary`, entre otros.

```html
<button class="btn btn-primary">Primary Button</button>
<button class="btn btn-secondary">Secondary Button</button>
<button class="btn btn-success">Success Button</button>
```

Cada botón tiene un estilo diferente:
- `.btn-primary`: Botón azul (principal).
- `.btn-secondary`: Botón gris (secundario).
- `.btn-success`: Botón verde (indica éxito).

#### Formularios
Bootstrap facilita el diseño de formularios con clases como `.form-group`, `.form-control`, etc.

```html
<form>
  <div class="form-group">
    <label for="email">Correo Electrónico:</label>
    <input type="email" class="form-control" id="email" placeholder="Ingresa tu email">
  </div>
  <div class="form-group">
    <label for="pwd">Contraseña:</label>
    <input type="password" class="form-control" id="pwd" placeholder="Ingresa tu contraseña">
  </div>
  <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```


## 3. Tipografía
Bootstrap tiene clases para estilizar la tipografía de manera coherente en todo el sitio.

- **Encabezados:** Clases como `.h1`, `.h2`, `.h3`, etc., para ajustar el tamaño de los encabezados.
- **Texto en negrita y cursiva:** Puedes usar `.font-weight-bold` para negrita y `.font-italic` para cursiva.

```html
<h1 class="h1">Encabezado principal</h1>
<h2 class="h2">Encabezado secundario</h2>
<p class="font-weight-bold">Este es un texto en negrita.</p>
<p class="font-italic">Este es un texto en cursiva.</p>
```


## 4. Navegación (Navbars)
El componente de barra de navegación es fundamental para crear menús de navegación. Bootstrap proporciona la clase `.navbar` para estilar las barras de navegación, junto con otras clases para hacerlas responsivas.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Mi sitio</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Inicio <span class="sr-only">(actual)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Enlace</a>
      </li>
    </ul>
  </div>
</nav>
```

Este código genera una barra de navegación con un botón "hamburguesa" para pantallas pequeñas. El contenido del menú se colapsa en dispositivos móviles y se expande en pantallas más grandes.


## 5. Utilidades
Bootstrap incluye diversas clases utilitarias para ajustar márgenes, padding, colores y más.

- **Márgenes y padding:** Las clases de margen (`m-*`) y padding (`p-*`) permiten ajustar rápidamente los espacios alrededor de los elementos.
  ```html
  <div class="mt-4 mb-2">Márgenes</div>
  <div class="p-3">Padding</div>
  ```
  Donde `mt-4` significa margen superior (`margin-top`) de 4 unidades, y `mb-2` es margen inferior (`margin-bottom`) de 2 unidades.

- **Colores de fondo y texto:** Se pueden usar clases como `.bg-primary`, `.text-light`, etc., para aplicar colores de fondo y texto.
  ```html
  <div class="bg-primary text-light p-3">Fondo azul con texto blanco</div>
  ```


## 6. Rejillas flexibles (Flexbox)
Bootstrap también utiliza flexbox para la disposición de elementos. Algunas de las clases más comunes incluyen:

- **d-flex**: Para activar el modo flex en un contenedor.
- **justify-content-*:** Para alinear elementos a lo largo del eje principal (horizontal).
- **align-items-*:** Para alinear elementos a lo largo del eje transversal (vertical).

Ejemplo:

```html
<div class="d-flex justify-content-between">
  <div class="p-2">Elemento 1</div>
  <div class="p-2">Elemento 2</div>
  <div class="p-2">Elemento 3</div>
</div>
```