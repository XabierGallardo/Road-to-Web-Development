# 0. Conceptos basicos
### 0.1 Que es Angular?
Angular es un framework de desarrollo de aplicaciones que permite crear aplicaciones de una sola página, SPAs. Es de codigo abierto y utiliza TypeScript. 

Es un framework o marco de trabajo rígido y robusto, lo que nos permite construír apps sólidas y estrictas. Se trabaja de una forma muy particular y poco flexible, al contrario que la librería React.js. 

Entre sus características se destacan:

1. **Arquitectura MVC**: Sigue el patron Modelo-Vista-Controlador para separar la lógica de presentación de los datos y la interfaz de usuario
2. **Componentes**: Angular se basa en una estructura de componentes, lo que permite a los desarrolladores crear aplicaciones modulares y reutilizables
3. **Data Binding Bidireccional**: Angular ofrece enlaces de datos bidireccionales, lo que implica que *los cambios realizados en el modelo de datos se reflejan automáticamente en la IU y viceversa*.
4. **Inyección de dependencias**: Angular proporciona un sistema de inyección de dependencias que facilita la creación y gestión de dependencias entre los distintos componentes de una app.
5. **Directivas**: Angular incluye un conjunto de directivas predefinidas que permiten extender el comportamiento de HTML y añadir funcionalidades dinámicas a las vistas.
6. **Enrutamiento**: Angular ofrece un enrutador incorporado que permite a los desarrolladores gestionar las rutas y la navegación dentro de una app de forma eficiente
 

### 0.2 Que es MVC?
Es un patron de diseño de software muy popular cuyo objetivo es dividir una app en tres componentes para mejorar la modularidad, mantenibilidad y escalabilidad del código.

En Angular, el patrón Modelo-Vista-Controlador (MVC) se aplica de manera similar a otros frameworks que siguen este patrón, pero con algunas diferencias debido a la arquitectura específica de Angular:


1. **Modelo (Model)**:
   - El modelo en Angular representa los datos de la aplicación y su lógica subyacente. 
   - *Por ejemplo, en el caso de un banco, el modelo representa su lógica de negocios. Si el cliente tiene cuenta corriente, caja de ahorro, el login de usuarios. Toda esa info la maneja el modelo para que cuando se necesite consumir por la vista, se pueda manipular esos datos*
   - Los modelos en Angular son generalmente clases TypeScript que definen la estructura y el comportamiento de los datos.
   - Los modelos pueden contener métodos para recuperar, actualizar o manipular los datos.


2. **Vista (View)**:
   - La vista en Angular es la representación visual de los datos del modelo en la interfaz de usuario.
   - En Angular, las vistas están escritas en HTML con directivas y enlaces de datos que permiten mostrar dinámicamente los datos del modelo.
   - Las vistas pueden contener directivas estructurales y atributos de enlace de datos que permiten una manipulación dinámica de la interfaz de usuario.

3. **Controlador (Componentes y Servicios)**:
    - *Actúa como intermediario entre el modelo y la vista. Se encarga de manejar las interacciones del usuario, como los clicks, eventos de entrada, y coordina las acciones necesarias para que el modelo y la vista se mantengan sintonizados.* **Es decir, el controlador controla el flujo de datos entre el modelo y la vista.** 
   - En Angular, el controlador se divide en dos partes: componentes y servicios.
   - Los componentes actúan como controladores en Angular. Cada componente controla una parte específica de la interfaz de usuario y está asociado con una vista HTML.
   - Los servicios en Angular encapsulan la lógica de negocio y proporcionan funcionalidades compartidas entre componentes.
   - Los componentes y los servicios trabajan juntos para controlar la lógica de la aplicación, manipular los datos del modelo y manejar las interacciones del usuario.

En Angular, el patrón MVC se implementa mediante la separación de responsabilidades entre modelos (datos y lógica), vistas (interfaz de usuario) y controladores (componentes y servicios) para crear aplicaciones web escalables y mantenibles.

### 0.3 Angular CLI
**Angular Command Line Interface** es una herramienta de línea de comandos para crear, desarrollar y administrar apps web en Angular.
El CLI proporciona una serie de utilidades y comandos que simplifican muchas tareas comunes en el proceso de desarrollo.
```sh
# Crear una app en Angular
ng new nombre-aplicacion

# Nuevo componente en Angular
ng generate component <component-name>
```



# 1. Estructura de directorios Angular
```
|-- e2e/
|   |-- app.e2e-spec.ts
|   |-- app.po.ts
|-- node_modules/
|-- src/
|   |-- app/
|   |   |-- components/
|   |   |-- services/
|   |   |-- models/
|   |   |-- app-routing.module.ts
|   |   |-- app.component.html
|   |   |-- app.component.scss
|   |   |-- app.component.spec.ts
|   |   |-- app.component.ts
|   |   |-- app.module.ts
|   |-- assets/
|   |-- environments/
|   |   |-- environment.prod.ts
|   |   |-- environment.ts
|   |-- index.html
|   |-- main.ts
|   |-- styles.scss
|-- angular.json
|-- package.json
|-- tsconfig.json
|-- README.md
```

- **e2e/**: Contiene pruebas de extremo a extremo (end-to-end) escritas utilizando Protractor.
  - **app.e2e-spec.ts**: Archivo de especificaciones de prueba de extremo a extremo.
  - **app.po.ts**: Page Object utilizado para interactuar con elementos en las pruebas de extremo a extremo.
  
- **node_modules/**: Contiene las dependencias de npm instaladas para el proyecto.

- **src/**: Contiene el código fuente de la aplicación.
  - **app/**: El directorio principal de la aplicación.
    - **components/**: Componentes de la aplicación.
    - **services/**: Servicios de la aplicación.
    - **models/**: Modelos de datos de la aplicación.
    - **app-routing.module.ts**: Módulo de enrutamiento de la aplicación.
    - **app.component.html**: Plantilla HTML principal de la aplicación.
    - **app.component.scss**: Estilos SCSS para el componente principal de la aplicación.
    - **app.component.spec.ts**: Especificaciones de prueba para el componente principal.
    - **app.component.ts**: Lógica del componente principal.
    - **app.module.ts**: Módulo raíz de la aplicación.
  - **assets/**: Contiene archivos estáticos como imágenes, fuentes, etc.
  - **environments/**: Contiene archivos de configuración para diferentes entornos, como desarrollo y producción.
    - **environment.prod.ts**: Configuración para el entorno de producción.
    - **environment.ts**: Configuración para el entorno de desarrollo.
  - **index.html**: Punto de entrada HTML de la aplicación.
  - **main.ts**: Punto de entrada de la aplicación Angular.
  - **styles.scss**: Archivo de estilos globales de la aplicación.

- **angular.json**: Archivo de configuración de Angular CLI que define la configuración del proyecto. *Es importante no tocar nada! Es la configuración clave de nuestra aplicación. Aca podremos poner estilos de terceros, como bootstrap en "styles" así como los archivos de JavaScript que necesite alguna librería externa en "scripts"*

- **package.json**: Archivo de configuración de npm que define las dependencias del proyecto y los scripts de comandos.
*Este es el archivo en el que se fija Node.js para poder instalar los paquetes*

- **tsconfig.json**: Archivo de configuración de TypeScript que define las opciones de compilación de TypeScript.

- **README.md**: Archivo de documentación que proporciona información sobre el proyecto.

- **.gitignore**: Es el archivo de git que nos permite excluir directorios que no queremos subir a un repositorio, como un archivo environment `.env` donde ubicamos nuestros usuarios y contraseñas. De esta manera, cada usuario parte de nuestro proyecto tendrá que tener sus propias variables de entorno secretas en su repositorio.

También incluiremos aquí al directorio `node_modules` para no subir gigas de módulos de node que podemos instalarlos con npm install cuando bajemos nuestro repositorio.

#### src/
Todo por fuera de la carpeta source es configuración de nuestro proyecto angular. El código de nuestra aplicación Angular está en source o `src`

- **styles.css**: Archivo general de estilos globales de la app
- **main.ts**: No se suele tocar, archivo de configuración general de typescript
- **index.html**: Es el archivo inicial que buscan todos los servidores. La clave acá está en `<app-root>` que indica el punto de entrada de la aplicación Angular

#### El elemento `<app-root>`
En una aplicación de Angular, `<app-root>` es la etiqueta raíz que se utiliza en el archivo HTML principal (`index.html`) para indicar el punto de entrada de la aplicación Angular. Esta etiqueta se define en el archivo `app.component.html` del proyecto Angular.

Cuando Angular inicia la aplicación, busca la etiqueta `<app-root>` en el archivo HTML principal y reemplaza esta etiqueta con el componente principal de la aplicación, que generalmente se llama `AppComponent` y está definido en el archivo `app.component.ts`.

Por lo tanto, `<app-root>` es esencialmente el contenedor principal de toda la aplicación Angular. Todos los demás componentes y contenido de la aplicación se renderizan dentro de este contenedor.

Es importante destacar que `<app-root>` es solo una convención de nomenclatura predeterminada, y puedes cambiar este nombre si lo deseas, pero asegúrate de ajustar también la configuración correspondiente en los archivos de configuración de Angular.

#### El directorio src/app
Es el directorio principal de nuestra aplicación Angular, acá tenemos tres archivos fundamentales como son 
- `app-routing-module`: El archivo de enrutamiento o **routing**
- `app-module-module`: El archivo de **modulo**
- `app-component-module`: El archivo de **componente**



# 2. Modulos
Son una parte fundamental de la arquitectura de la aplicación. Ayudan a dividir una aplicación en partes más pequeñas y manejables, lo que facilita el desarrollo, mantenibilidad y escalabilidad. Un modulo es por tanto una division organizativa de una aplicacion.

Un módulo es un mecanismo de organización y encapsulación que se utiliza para agrupar componentes, directivas, pipes (filtros) y servicios para proporcionar funcionalidades específicas a una aplicación. 

Un módulo en Angular se define mediante la decoración `@NgModule`, que se importa desde `@angular/core`. Al definir un módulo, puedes especificar qué componentes, directivas, pipes y servicios pertenecen a ese módulo, así como también qué otros módulos necesita importar.

Los módulos en Angular pueden dividirse en dos tipos principales:

1. **Módulos de la aplicación (App Module)**: Este tipo de módulo es el módulo raíz de la aplicación Angular y se utiliza para inicializar y configurar la aplicación. Contiene componentes principales, servicios globales y otros módulos de la aplicación. Por lo general, se nombra `AppModule` y se encuentra en el archivo `app.module.ts`.

2. **Módulos de funcionalidad (Feature Modules)**: Estos son módulos que encapsulan características específicas de la aplicación, como funcionalidades relacionadas con la autenticación, el enrutamiento, el formulario, etc. Los módulos de funcionalidad permiten organizar el código de la aplicación en unidades lógicas y promueven la reutilización. Por lo general, cada característica importante de la aplicación tiene su propio módulo de funcionalidad.

En resumen, los módulos en Angular son contenedores que encapsulan y organizan el código de la aplicación en unidades lógicas y cohesivas, lo que facilita su desarrollo, mantenimiento y escalabilidad.

Son la forma en que se organiza la aplicación, los módulos no se ven, los componentes sí. Son unidades organizativas, encapsulan funcionalidades, dividen la aplicación, importan y exportan elementos, registran proveedores y evitan conflictos de nombres.
```sh
ng generate module module-name
```

```ts
// Importaciones, este modulo tendra disponible informacion y caracteristicas de otros modulos
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component'; // Mi componente

// NgModule indica que es un Modulo, adentro mandamos un objecto
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule, // Modulo que nos permite enrutar y navegar la app
    bootstrap: [AppComponent] // Configuracion por defecto de Angular para renderizar dinamicamente el AppModule
  ],
// Podemos exportar nuestro modulo con exports: []
})
export class AppModule { }
```
**El modulo es la división organizativa**



# 3. Componentes
Son bloques para la construccion de IUs en una aplicacion web. Definen como se ve y e comporta una parte especifica de la IU. Cada componente represente un elemento visual o funcional, header, footer, form, etc.

Los componentes son piezas reutilizables de código que pueden contener plantillas HTML, estilos CSS y lógica TypeScript, todo ello trabajando juntos para definir cómo se ve y se comporta una parte de la interfaz de usuario de la aplicación.

Cada componente consta de tres partes principales:

1. **Clase de componente (Component Class)**: Esta es una clase TypeScript que define la lógica del componente, incluidas las propiedades y métodos que controlan su comportamiento. La clase de componente se puede decorar con metadatos de Angular para configurar su comportamiento y su apariencia.

2. **Plantilla (Template)**: La plantilla HTML define la estructura visual del componente y cómo se muestran los datos en la interfaz de usuario. La plantilla puede contener enlaces de datos, directivas estructurales y de atributos, y referencias a estilos CSS.

3. **Estilos (Styles)**: Los estilos CSS definen la apariencia visual del componente. Pueden ser estilos en línea, estilos embebidos o estilos externos importados.

Los componentes son la piedra angular de la arquitectura de una aplicación Angular y se utilizan para construir la interfaz de usuario de manera modular y reutilizable. Cada componente representa una parte específica de la aplicación y se puede integrar fácilmente en otras partes de la aplicación según sea necesario.

Angular utiliza el Atomic Design, consiste en diseñar en cadena bloques reutilizablesz. Toda la pantalla acaba siendo un componente grande compuesto a su vez por otros componentes


Para crear un componente en Angular, se utiliza el comando `ng generate component` o su forma abreviada `ng g c nombrecomponente`. Este comando crea automáticamente los archivos necesarios para el componente, incluida la clase de componente, la plantilla y los estilos, y los coloca en la ubicación adecuada dentro del proyecto.

### El comando `n g c padre` nos agrega automaticamente nuestro nuevo componente al modulo raiz! `app.module.ts`
```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PadreComponent } from './padre/padre.component';

@NgModule({
  declarations: [
    AppComponent,
    PadreComponent // Se agrego automaticamente, por eso ahora podemos poner <app-padre> en app.component.html
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

```

- **El archivo del componente**: `component-name.component.ts`
```ts
// nombre-del-componente.component.ts
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nombre-del-componente',
  templateUrl: './nombre-del-componente.component.html',
  styleUrls: ['./nombre-del-componente.component.css']
})

export class AppComponent implements OnInit {
  
  // Propiedades del componente
  title = 'notepad-angular';

  // Constructor
  constructor() { }

  // Metodo de inicializacion
  ngOnInit(): void {

  }

  // Otros metodos y logica del componente
}

```

- **El archivo HTML de la plantilla**: `component-name.component.html`
- **El archivo de estilos**: `component-name.component.css`
- **El archivo de prueba**: `component-name.component.specs.ts`
