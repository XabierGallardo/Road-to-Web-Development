# Angular :a:
# 0. Conceptos basicos

### 0.1 Que es una SPA?
Una SPA es una forma moderna de construir aplicaciones web que ofrece una experiencia de usuario más fluida y receptiva al cargar una sola página HTML inicial y actualizar dinámicamente el contenido en respuesta a las acciones del usuario, todo dentro del navegador web.
En lugar de cargar páginas completamente nuevas desde el servidor, en una SPA, toda la interfaz de usuario se construye y se actualiza dinámicamente en el navegador web a medida que el usuario interactúa con la aplicación, sin la necesidad de recargar la página. Entre sus características están:

1. **Carga inicial rápida**: Cuando un usuario accede a una SPA por primera vez, se carga una única página HTML inicial que contiene la estructura básica de la aplicación y los recursos necesarios, como JavaScript, CSS y posiblemente algunas plantillas de contenido.

2. **Interacciones sin recarga de página**: Una vez que la SPA se ha cargado inicialmente, todas las interacciones del usuario, como hacer clic en enlaces, enviar formularios o interactuar con elementos de la interfaz, se manejan a través de JavaScript. En lugar de cargar páginas completamente nuevas desde el servidor, la SPA utiliza JavaScript para hacer solicitudes al servidor y actualizar dinámicamente el contenido de la página actual en función de la respuesta del servidor.

3. **Navegación fluida**: La navegación en una SPA es fluida y rápida, ya que las transiciones entre vistas se realizan de forma dinámica en el navegador, sin la necesidad de cargar una nueva página desde el servidor.

4. **Mejora de la experiencia del usuario**: Debido a su enfoque en la actualización dinámica del contenido y la navegación fluida, las SPAs suelen ofrecer una experiencia de usuario más interactiva y receptiva en comparación con las aplicaciones web tradicionales.

5. **Frameworks y bibliotecas populares**: Hay varios frameworks y bibliotecas populares para desarrollar SPAs, como React, Angular, Vue.js, entre otros. Estas herramientas proporcionan funcionalidades avanzadas y patrones de desarrollo que facilitan la construcción de aplicaciones web modernas y eficientes.

6. **Gestión del estado**: Dado que las SPAs tienden a ser más complejas en términos de interacciones y vistas dinámicas, a menudo *requieren una gestión avanzada del estado de la aplicación*. Los frameworks y bibliotecas modernas proporcionan *herramientas para facilitar esta gestión del estado, como el uso de componentes reactivos, patrones de diseño como Flux o Redux, y el enlace de datos bidireccional*.


### 0.2 Que es el estado en una SPA?
El estado se refiere a la representación de los datos de la aplicación en un momento dado. 
Define cómo se comporta y se presenta la aplicación en cualquier momento. Un manejo eficiente del estado es crucial para crear aplicaciones web interactivas y responsivas.

El estado es un objeto que contiene toda la información necesaria para que la interfaz de usuario de la SPA funcione y se muestre correctamente. Este concepto es crucial para el manejo y la actualización dinámica de la UI sin necesidad de recargar la página completa. Entre sus componentes destacan:

1. **Datos de la Aplicación**: Información como los datos del usuario, el contenido mostrado, los resultados de búsquedas, etc.
2. **Estado de la UI**: Datos sobre el estado visual de la aplicación, como cuál pestaña está activa, si un modal está abierto, etc.
3. **Datos Temporales**: Información que puede no necesitarse permanentemente, como valores de formularios no guardados.
4. **Configuraciones y Preferencias**: Preferencias del usuario, configuraciones de la aplicación, etc.


### 0.2 Que es Angular?
Angular es un framework de desarrollo de aplicaciones que permite crear aplicaciones de una sola página, SPAs. Es de codigo abierto y utiliza TypeScript. 

Es un framework o marco de trabajo rígido y robusto, lo que nos permite construír apps sólidas y estrictas. Se trabaja de una forma muy particular y poco flexible, al contrario que la librería React.js. 

Entre sus características se destacan:

1. **Arquitectura MVC**: Sigue el patron Modelo-Vista-Controlador para separar la lógica de presentación de los datos y la interfaz de usuario
2. **Componentes**: Angular se basa en una estructura de componentes, lo que permite a los desarrolladores crear aplicaciones modulares y reutilizables
3. **Data Binding Bidireccional**: Angular ofrece enlaces de datos bidireccionales, lo que implica que *los cambios realizados en el modelo de datos se reflejan automáticamente en la IU y viceversa*.
4. **Inyección de dependencias**: Angular proporciona un sistema de inyección de dependencias que facilita la creación y gestión de dependencias entre los distintos componentes de una app.
5. **Directivas**: Angular incluye un conjunto de directivas predefinidas que permiten extender el comportamiento de HTML y añadir funcionalidades dinámicas a las vistas.
6. **Enrutamiento**: Angular ofrece un enrutador incorporado que permite a los desarrolladores gestionar las rutas y la navegación dentro de una app de forma eficiente
 

### 0.3 Que es MVC?
#### MVC en Angular con ejemplos
Angular se basa en el patrón de diseño Modelo-Vista-Controlador (MVC), que es un enfoque de arquitectura de software que separa la aplicación en tres componentes principales: Modelo, Vista y Controlador.

1. **Modelo (Model)**:
   - El Modelo representa los datos y el estado de la aplicación. Esto puede incluir datos de usuario, datos de la aplicación, información de configuración, etc.
   - En Angular, los Modelos se definen utilizando clases TypeScript o interfaces para representar la estructura de los datos.

   Ejemplo en Angular:
   ```typescript
   export class Usuario {
       id: number;
       nombre: string;
       email: string;
   }
   ```

2. **Vista (View)**:
   - La Vista es la interfaz de usuario con la que interactúa el usuario final. Muestra los datos al usuario y recibe las interacciones del usuario, como clics de botones o entradas de formulario.
   - En Angular, las Vistas están definidas usando plantillas HTML que están vinculadas a los datos y comportamientos definidos en los componentes de Angular.

   Ejemplo en Angular (archivo `usuario.component.html`):
   ```html
   <div>
       <p>Nombre: {{ usuario.nombre }}</p>
       <p>Email: {{ usuario.email }}</p>
   </div>
   ```

3. **Controlador (Controller)**:
   - El Controlador actúa como intermediario entre el Modelo y la Vista. Se encarga de manejar las interacciones del usuario, actualizar el Modelo en consecuencia y actualizar la Vista para reflejar los cambios en los datos.
   - En Angular, los Controladores se implementan mediante componentes, que son clases TypeScript decoradas con el decorador `@Component`.

   Ejemplo en Angular (archivo `usuario.component.ts`):
   ```typescript
   import { Component, OnInit } from '@angular/core';
   import { Usuario } from './usuario.model';

   @Component({
       selector: 'app-usuario',
       templateUrl: './usuario.component.html',
       styleUrls: ['./usuario.component.css']
   })
   export class UsuarioComponent implements OnInit {
       usuario: Usuario;

       ngOnInit(): void {
           // Aquí podrías obtener los datos del usuario desde una API
           this.usuario = { id: 1, nombre: 'Juan', email: 'juan@example.com' };
       }
   }
   ```

En este ejemplo, el Modelo (`Usuario`) representa los datos del usuario, la Vista (`usuario.component.html`) muestra la información del usuario utilizando la sintaxis de interpolación de Angular (`{{ usuario.nombre }}`, `{{ usuario.email }}`), y el Controlador (`UsuarioComponent`) proporciona la lógica para obtener los datos del usuario y manejar su representación en la Vista.


### No siempre tiene por que haber un Modelo
Aunque Angular se considera un framework que sigue el patrón de diseño Modelo-Vista-Controlador (MVC), en la práctica, el uso del modelo puede variar según la complejidad y los requisitos de la aplicación. Hay varias razones por las cuales algunas aplicaciones de Angular pueden no tener modelos explícitos:

1. **Simplicidad de la Aplicación**:
   - En aplicaciones pequeñas o simples, puede no ser necesario definir modelos explícitos. Los datos pueden manejarse directamente dentro de los componentes o servicios sin la necesidad de crear clases de modelo separadas.
   - Ejemplo: Una aplicación que solo muestra datos estáticos o realiza operaciones muy básicas puede no requerir una capa de modelos.

2. **Prototipos y MVPs**:
   - Durante las etapas iniciales de desarrollo, como en la creación de prototipos o productos mínimos viables (MVP), los desarrolladores pueden optar por una estructura más simple para acelerar el proceso de desarrollo. En estas fases, los modelos pueden parecer innecesarios hasta que la aplicación se vuelva más compleja.

3. **Uso de Interfaces en lugar de Clases de Modelo**:
   - En muchos casos, los desarrolladores de Angular utilizan interfaces TypeScript para definir la forma de los datos en lugar de clases de modelo completas. Las interfaces proporcionan una estructura ligera y son suficientes para definir contratos de datos.
   - Ejemplo:
     ```typescript
     export interface User {
       id: number;
       name: string;
       email: string;
     }
     ```

4. **Aplicaciones de Formulario o CRUD Simples**:
   - Las aplicaciones que simplemente manejan formularios o realizan operaciones CRUD básicas pueden no necesitar una capa de modelo compleja. Los datos pueden manejarse directamente en los componentes, y los servicios pueden manejar la comunicación con la API sin necesidad de definir modelos separados.

5. **Uso de Bibliotecas y Servicios Externos**:
   - Algunas aplicaciones pueden depender de bibliotecas o servicios externos que proporcionan sus propias estructuras de datos. En estos casos, los desarrolladores pueden utilizar directamente las estructuras proporcionadas por esas bibliotecas en lugar de definir sus propios modelos.

6. **Evolución del Proyecto**:
   - A medida que un proyecto evoluciona, la necesidad de modelos puede surgir más adelante. Inicialmente, un proyecto puede comenzar sin modelos explícitos y, con el tiempo, a medida que la complejidad crece, los desarrolladores pueden refactorizar el código para incluir modelos.

*Aunque Angular está diseñado para soportar el patrón MVC, la presencia de modelos explícitos depende del contexto y los requisitos específicos de la aplicación. No todas las aplicaciones necesitan una capa de modelos completa desde el principio, y algunas pueden nunca necesitarla si permanecen simples. La flexibilidad de Angular permite a los desarrolladores adaptar la arquitectura según las necesidades del proyecto, lo que puede resultar en aplicaciones sin modelos definidos explícitamente.*


#### MVC Teoría
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



### 0.4 Angular CLI
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

Un módulo en Angular se define mediante la decoración `@NgModule`, que se importa desde `@angular/core`. *Al definir un módulo, puedes especificar qué componentes, directivas, pipes y servicios pertenecen a ese módulo, así como también qué otros módulos necesita importar.*

Los módulos en Angular pueden dividirse en dos tipos principales:

1. **Módulos de la aplicación (App Module)**: Este tipo de módulo es el módulo raíz de la aplicación Angular y se utiliza para inicializar y configurar la aplicación. Contiene componentes principales, servicios globales y otros módulos de la aplicación. Por lo general, se nombra `AppModule` y se encuentra en el archivo `app.module.ts`.

2. **Módulos de funcionalidad (Feature Modules)**: Estos son módulos que encapsulan características específicas de la aplicación, como funcionalidades relacionadas con la autenticación, el enrutamiento, el formulario, etc. Los módulos de funcionalidad permiten organizar el código de la aplicación en unidades lógicas y promueven la reutilización. Por lo general, cada característica importante de la aplicación tiene su propio módulo de funcionalidad.

En resumen, **el modulo es la división organizativa**, los módulos son contenedores que encapsulan y organizan el código de la aplicación en unidades lógicas y cohesivas, lo que facilita su desarrollo, mantenimiento y escalabilidad.

*Son la forma en que se organiza la aplicación, los módulos no se ven, los componentes sí. Son unidades organizativas, encapsulan funcionalidades, dividen la aplicación, importan y exportan elementos, registran proveedores y evitan conflictos de nombres.*

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




# 3. Componentes
Son bloques para la construccion de IUs en una aplicacion web. Definen como se ve y e comporta una parte especifica de la IU. Cada componente represente un elemento visual o funcional, header, footer, form, etc.

Los componentes son piezas reutilizables de código que pueden contener plantillas HTML, estilos CSS y lógica TypeScript, todo ello trabajando juntos para definir cómo se ve y se comporta una parte de la interfaz de usuario de la aplicación.

Cada componente consta de tres partes principales:

1. **Clase de componente (Component Class)**: Esta es una clase TypeScript que define la lógica del componente, incluidas las propiedades y métodos que controlan su comportamiento. La clase de componente se puede decorar con metadatos de Angular para configurar su comportamiento y su apariencia.

2. **Plantilla (Template)**: La plantilla HTML define la estructura visual del componente y cómo se muestran los datos en la interfaz de usuario. La plantilla puede contener enlaces de datos, directivas estructurales y de atributos, y referencias a estilos CSS.

3. **Estilos (Styles)**: Los estilos CSS definen la apariencia visual del componente. Pueden ser estilos en línea, estilos embebidos o estilos externos importados.

Los componentes son la piedra angular de la arquitectura de una aplicación Angular y se utilizan para construir la interfaz de usuario de manera modular y reutilizable. Cada componente representa una parte específica de la aplicación y se puede integrar fácilmente en otras partes de la aplicación según sea necesario.

Angular utiliza el Atomic Design, consiste en diseñar en cadena bloques reutilizables. Toda la pantalla acaba siendo un componente grande compuesto a su vez por otros componentes


Para crear un componente en Angular, se utiliza el comando `ng generate component` o su forma abreviada `ng g c nombre-componente`. Este comando crea automáticamente los archivos necesarios para el componente, incluida la clase de componente, la plantilla y los estilos, y los coloca en la ubicación adecuada dentro del proyecto. El más recomendado es `ng g c components/nuevo-componente`


### El comando `n g c components/padre` nos agrega automaticamente nuestro nuevo componente al modulo raiz! `app.module.ts`
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




# 4. Binding o Enlace de datos
Es el ida y vuelta de datos entre la vista y el controlador (componente). 

<p>
  <img src="img/binding-esquema.jpeg" alt="Esquema de binding">
</p>

En Angular, el data binding es una característica fundamental que permite establecer una conexión bidireccional entre el modelo de datos de la aplicación y la interfaz de usuario (UI). Esto *significa que los cambios en el modelo de datos se reflejan automáticamente en la UI, y viceversa, sin necesidad de escribir código manualmente para sincronizar los datos*.

El data binding en Angular se puede dividir en tres tipos principales:

1. **Interpolación ({{ }})**: La interpolación se utiliza para mostrar valores de propiedades del componente en la plantilla HTML. Se utiliza la sintaxis de doble llave `{{ }}` para insertar dinámicamente el valor de una expresión del componente en la plantilla.

   Ejemplo:
   ```html
   <h1>{{ title }}</h1>
   ```

2. **Enlace de propiedades (Property Binding)**: El enlace de propiedades permite establecer el valor de un atributo de HTML dinámicamente en función de una propiedad del componente. Se utiliza la sintaxis de corchetes `[]` para enlazar una propiedad del componente con un atributo HTML.

   Ejemplo:
   ```html
   <img [src]="imageUrl">
   ```

3. **Enlace de eventos (Event Binding)**: El enlace de eventos permite responder a eventos del usuario, como clics de botón, pulsaciones de teclas, etc., y ejecutar funciones en respuesta a esos eventos en el componente. Se utiliza la sintaxis de paréntesis `()` para enlazar eventos del DOM con métodos del componente.

   Ejemplo:
   ```html
   <button (click)="onClick()">Click me</button>
   ```

Además de estos tipos de data binding, Angular también ofrece la capacidad de realizar data binding bidireccional con `ngModel`, que combina la funcionalidad de enlace de propiedades y enlace de eventos para permitir la sincronización automática de datos entre un elemento de formulario HTML y una propiedad del componente.

En resumen, el data binding en Angular facilita la sincronización de datos entre el modelo y la vista de una aplicación, lo que permite una experiencia de usuario dinámica y receptiva sin la necesidad de escribir mucho código manualmente. Entre sus características están:

- **Conexión automática**: Sincroniza datos entre el modelo y la vista
- **Unidireccional**: Los cambios en el modelo se reflejan en la vista
- **Bidireccional**: Los cambios en la vista actualizan el modelo
- **Reactivo**: utiliza observables para actualizaciones en tiempo real
- **Simplifica la interacción**: Facilita la creación de aplicaciones interactivas
- **Automatiza las actualizaciones**: Los cambios se reflejan sin intervención manual

En nuestro nuevo componente `ng g c components/contador`
```ts
// contador.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-contador',
  templateUrl: './contador.component.ts',
  stylesUrls: ['./contador.component.css']
})
export class ContadorComponent {
  valorContador: number = 0; // binding de propiedad

  incrementar() {
    this.valorContador++;
  }

  decrementar() {
    this.valorContador--;
  }
}
```

```html
<!-- contador.component.html -->
<p>contador works!</p>
<h1>Contador: {{ valorContador }}</h1>
<button (click)="incrementar()">Incrementar</button>
<button (click)="decrementar()">Decrementar</button>
```

<p>
  <img src="img/contador-component.png" alt="Componente contador">
</p>


### Metadata
La metadata es la información adicional que se proporciona mediante decoradores para configurar y definir el comportamiento de una clase, un componente, un servicio o cualquier otra estructura en una aplicación Angular.

La metadata se utiliza en Angular para decorar clases y proporcionar información sobre cómo deben comportarse esas clases en tiempo de ejecución. Los decoradores son funciones que modifican el comportamiento de las clases a las que se aplican.

La metadata en Angular se define utilizando decoradores especiales proporcionados por el framework. Algunos de los decoradores más comunes utilizados para definir metadata en Angular incluyen:

1. **@NgModule**: Se utiliza para decorar clases de módulo y proporcionar información sobre cómo se compila y ejecuta el módulo.

2. **@Component**: Se utiliza para decorar clases de componente y proporcionar información sobre cómo se debe crear y procesar el componente.

3. **@Injectable**: Se utiliza para decorar clases de servicio y proporcionar información sobre cómo se debe crear y proporcionar el servicio en la aplicación.

4. **@Directive**: Se utiliza para decorar clases de directiva personalizada y proporcionar información sobre cómo se debe comportar la directiva.

5. **@Input** y **@Output**: Se utilizan para decorar propiedades y eventos de componente respectivamente, para permitir el enlace de datos y la comunicación entre componentes.

Entre sus características:
- **Configuración**: Define cómo se comportan las partes de la aplicación
- **Decoradores**: Se utiliza con decoradores como `@Component`, `@NgModule` o `@Injectable`
- **Personalización**: Ajusta el comportamiento con propiedades clave
- **Componente**: Metadata para componentes, incluye plantilla y estilos
- **Módulo**: Configuración de módulos como declaraciones e importaciones
- **Servicio**: Metadata para servicios, define su alcance y proveedores
- **Directiva**: Define metadata de directivas personalizadas como selectores




# 5. Comunicacion entre Componentes / Input-Output
### Resumen Input Output
En Angular, se pueden enviar datos entre componentes utilizando las propiedades de entrada (`@Input`) y las propiedades de salida (`@Output`). 

1. **Propiedades de entrada (`@Input`)**:
   - Las propiedades de entrada se utilizan para pasar datos desde un componente padre a un componente hijo.
   - Se definen en el componente hijo utilizando el decorador `@Input`.
   - En el componente padre, se enlazan con valores de la plantilla utilizando la sintaxis de enlace de propiedades `[]`.
   - Cuando el valor de la propiedad de entrada cambia en el componente padre, se refleja automáticamente en el componente hijo.

   Ejemplo:
   ```typescript
   // En el componente hijo
   @Input() inputValue: string;
   ```

   ```html
   <!-- En el componente padre -->
   <app-child [inputValue]="parentValue"></app-child>
   ```

2. **Propiedades de salida (`@Output`)**:
   - Las propiedades de salida se utilizan para emitir eventos desde un componente hijo hacia un componente padre.
   - Se definen en el componente hijo utilizando el decorador `@Output`, que se asocia con un EventEmitter.
   - Cuando ocurre un evento en el componente hijo, se emite a través de la propiedad de salida y puede ser capturado por el componente padre.
   - En el componente padre, se enlazan con manejadores de eventos utilizando la sintaxis de enlace de eventos `()`.
   
   Ejemplo:
   ```typescript
   // En el componente hijo
   @Output() outputEvent = new EventEmitter<string>();

   emitEvent() {
     this.outputEvent.emit('data from child');
   }
   ```

   ```html
   <!-- En el componente padre -->
   <app-child (outputEvent)="handleEvent($event)"></app-child>
   ```


### Padre -> Hijo / @Input() 
1. En el componente hijo, puedes definir propiedades de entrada utilizando el decorador `@Input()`. Estas propiedades representarán los datos que se esperan recibir del componente padre
```ts
// Componente hijo
@Input() datoEntrada : string;
```

2. En el componente padre, puedes vincular datos a la propiedad de entrada del componente hijo utilizando la sintaxis de corchetes `[]` en el template
```html
<!-- padre.component.html -->
<app-hijo [datoEntrada]="valorDesdePadre"></app-hijo>
```


3. Cuando el valor de la propiedad en el componente padre cambia, Angular actualiza automaticamente la propiedad de entrada en el componente hijo, asi se mantienen sincronizados los datos entre componentes
```ts
// Componente padre
valorDesdePadre = "Hola mundo!";
```

4. En el componente hijo, puedes utilizar la propiedad de entrada (datoEntrada) como cualquier otra propiedad local y mostrarla en el template
```html
<!-- Componente hijo html -->
<p>{{ datoEntrada }}</p
```


### Hijo -> Padre / @Output()
1. Se usa `@Output` y `EventEmitter` para lograr la comunicación entre un componente hijo y su componente padre. Declaras una propiedad con `@Output` en el componente hijo y emites eventos con `EventEmitter`
```ts
// hijo.component.ts
@Output() messageEvent = new EventEmitter<string>();
message: string = '';

sendMessage() {
  this.messageEvent.emit(this.message);
}
```

2. Este archivo HTML contiene la IU del componenente hijo. Incluye un input para que el usuario ingrese un mensaje y un boton para enviarlo. Utiliza `ngModel` para vincular el input con la propiedad message del componente TypeScript.
```html
<!-- hijo.component.html -->
<div>
  <label for="childInput">Mensaje:</label>
  <input id="childInput" [(ngModel)]="Message" />
  <button (click)="sendMessage()">Enviar Mensaje</button>
</div>
```

3. El archivo TypeScript define el componente ParentComponent, que tiene una propiedad (receivedMessage) que actualiza esta propiedad cuando se emite el evento desde el componente hijo
```ts
// padre.component.ts
receivedMessage: string = '';

receiveMessage(message: string) {
  this.receivedMessage = message;
}
```

4. La plantilla HTML del componente padre incluye el componente hijo app-child y utiliza el evento de salida messageEvent para llamar al método receiveMessage cuando se emite un mensaje desde el componente hijo. Muestra el mensaje recibido en la interfaz del componente padre.
```html
<!-- padre.component.html -->
<div>
  <app-child (messageEvent)="receiveMessage($event)"></app-child>
  <p>Mensaje recibido en el padre: {{ receivedMessage }}</p>
</div>
```




# 5. Servicios y Dependencias
### Resumen de servicios, inyección y dependencias
En Angular, **los servicios** son clases que se utilizan para organizar y compartir lógica de negocio, funciones y datos entre diferentes partes de una aplicación. **Se utilizan para centralizar la lógica que no pertenece directamente a un componente en particular, como el acceso a datos externos, la manipulación de datos, la autenticación, etc.**

Los servicios en Angular se definen como clases decoradas con el decorador `@Injectable()`. Esto les permite ser inyectados como dependencias en otros componentes, directivas o servicios utilizando el mecanismo de inyección de dependencias de Angular.

La inyección de dependencias es un patrón de diseño que se utiliza en Angular para gestionar las dependencias entre diferentes partes de una aplicación de manera eficiente y desacoplada. **Con la inyección de dependencias, los servicios se pueden inyectar en los componentes que los necesitan en lugar de que los componentes** creen o gestionen directamente las instancias de los servicios.

**Las dependencias en Angular son los objetos o instancias que un componente, directiva o servicio necesita para realizar su trabajo. Estas dependencias pueden ser otros servicios, módulos, servicios externos**, o incluso instancias de clases personalizadas. Angular se encarga de gestionar la creación y la inyección de dependencias automáticamente, lo que simplifica la configuración y el mantenimiento de la aplicación.

En resumen, los servicios y las dependencias son conceptos fundamentales en Angular que se utilizan para organizar y compartir la lógica de la aplicación de manera modular, reutilizable y desacoplada. Los servicios encapsulan la lógica de negocio y los datos, mientras que la inyección de dependencias permite a los componentes y otros servicios acceder a estas funcionalidades de manera sencilla y eficiente.


### Que son los Servicios?
Otra manera de comunicar nuestros componentes es a través de los servicios.

Un servicio es una clase typescript que se utiliza para organizar y compartir lógica, datos o funcionalidades comunes entre diferentes componentes de una aplicación. Los servicios son una parte fundamental de la arquitectura de Angular y proporcionan una **forma de centralizar y reutilizar la lógica que no está relacionada directamente con la IU**.
*Así como los componentes nos permiten reutilizar fragmentos de código en la IU, los servicios nos permiten reutilizar fragmentos de código de lógica. Entre sus características destacamos*

- **Reutilización**: Lógica compartida
- **Separación de preocupaciones**: Divide lógica e IU
- **Inyección de dependencias**: Instancias proporcionadas
- **Centralización de datos**: Almacena y gestiona datos compartidos
- **Comunicación entre componentes**: Facilita la comunicación
- **Lifecycle independiente**: No vinculado a vistas
- **Testeabilidad**: Fácil de probar

```sh
ng generate service nombre-servicio

ng g s nombre-servico
```

```ts
import { Injectable } from '@angular/core';

@Injectable({
  provideIn: 'root'
})
export class MiServicioService {
  
  constructor() { }
  // Metodos y lógica del servicio
}
```
En nuestro componente se puede inyectar el servicio de la siguiente manera
```ts
// Metodo 1 de inyeccion de dependencias
constructor(
  private _nuevoServicio: NuevoServicioService
) { }

// Metodo 2 de inyeccion de dependencias
private _nuevoServicio = inject(NuevoServicioService)
```




# 6. Directivas
### Que son las directivas?
Son instrucciones en el marcado HTML que proporcionan funcionalidad adicional a los elementos DOM o personalizan su comportamiento. Son un componente clave en la construcción de aplicaciones web en Angular ya que permiten extender y manipular el DOM de manera declarativa, lo que facilita la creación e interfaces de usuario dinámicas e interactivas.

- **Instrucciones HTML**: Extienden o personalizan elementos HTML
- **Directivas Incorporadas**: Ofrecen funcionalidad predefinida
- **Directivas Estructurales**: Manipulan la estructura del DOM
- **Directivas de Atributos**: Cambian atributos y propiedades
- **Directivas de Eventos**: Capturan y responden a eventos del usuario
- **Directivas Personalizadas**: Creadas para necesidades específicas
- **Inyección de Dependencias**: Acceso a servicios y datos
- **Flexibilidad de Aplicación**: Se pueden aplicar como atributos o elementos

```sh
# Crear una directiva
ng generate directive nombre-directiva
ng g d nombre-directiva
```
Nuestra directiva se ve de la siguiente forma
```ts
// nombre-directiva.directive.ts
import { Directive, ElementRef } from '@angular/core';

@Directive({
  selector: '[appMiDirectiva]'
})
export class MiDirectivaDirective {
  constructor(private el: ElementRef) {
    // Accede al elemento del DOM en el que se aplica la directiva (this.el.nativeElement)
    this.el.nativeElement.style.backgroundColor = 'yellow';
  }
}
```
Se llama a nuestra directiva con el tag HTML
```html
<div appMiDirectiva>
  <!-- Se pondra de color amarillo como indicamos arriba -->
  Este es un elemento con mi directiva personalizada.
</div>
```

La directiva no sólo sirve para poner estilos, se usa mucho para ocultar si no tiene permisos, poner en mayúsculas el texto, etc.
Todo lo que se escribe al lado de los tags son directivas





# 7. Pipes
### Resumen
Los pipes en Angular son una característica que permite transformar datos en la interfaz de usuario de manera declarativa en las plantillas HTML. Los pipes se utilizan para formatear, filtrar y transformar datos antes de que se muestren en la vista de la aplicación.

1. **Formateo de Datos**: Los pipes se utilizan comúnmente para formatear datos en diferentes formatos, como fechas, números, monedas, etc. Angular proporciona varios pipes integrados para este propósito, como `DatePipe`, `DecimalPipe`, `CurrencyPipe`, entre otros.

   ```html
   <p>{{ fecha | date:'dd/MM/yyyy' }}</p>
   <p>{{ cantidad | currency:'USD':'symbol':'1.2-2' }}</p>
   ```

2. **Filtrado de Datos**: Los pipes también se pueden utilizar para filtrar datos en una lista o colección, mostrando sólo los elementos que cumplan ciertos criterios.

   ```html
   <ul>
     <li *ngFor="let producto of productos | filter:'categoria':'electrónica'">{{ producto.nombre }}</li>
   </ul>
   ```

3. **Ordenación de Datos**: Los pipes pueden ordenar una lista de elementos basados en ciertos criterios, como el nombre, la fecha, el valor numérico, etc.

   ```html
   <ul>
     <li *ngFor="let producto of productos | orderBy:'nombre'">{{ producto.nombre }}</li>
   </ul>
   ```

4. **Personalización de Pipes**: También puedes crear tus propios pipes personalizados para adaptarse a tus necesidades específicas. Esto se hace creando una clase TypeScript que implementa la interfaz `PipeTransform` y proporciona la lógica de transformación deseada.

   ```typescript
   import { Pipe, PipeTransform } from '@angular/core';

   @Pipe({
     name: 'miPipePersonalizado'
   })
   export class MiPipePersonalizado implements PipeTransform {
     transform(valor: any, ...args: any[]): any {
       // Implementa la lógica de transformación aquí
     }
   }
   ```

   ```html
   <p>{{ dato | miPipePersonalizado }}</p>
   ```

En resumen, los pipes en Angular son una forma poderosa y flexible de transformar datos en las plantillas HTML, permitiendo formatear, filtrar y ordenar datos de manera declarativa y mantener así una interfaz de usuario dinámica y rica en funcionalidades.


### Que son los Pipes?
Son una característica que permite formatear y transformar datos en la vista de una aplicación web de manera sencilla y legible.
Los pipes son funciones que toman un valor de entrada y lo procesan para proporcionar una representación modificada o formateada en la IU.

Los pipes se usan en las plantillas HTML de Angular y se aplican utilizando el símbolo `|`. Algunos ejemplos comunes de uso de pipes incluyen el formateo de fechas, números, monedas, texto en mayúsculas o minúsculas, etc.

*Angular proporciona una serie de pipes integrados, como DatePipe, UpperCasePipe, LowerCasePipe, CurrencyPipe, DecimalPipe, PercentPipe, etc.*
También podes crear tus propios pipes personalizados cuando necesites realizar transformaciones específicas.

- **Formateo de Datos**: Transforma datos para presentarlos
- **Sintaxis de Pipe**: Se aplica en plantillas con `|`
- **Pipes Integrados**: Angular propociona pipes predefinidos
- **Pipes Encadenados**: Se pueden combinar varios pipes
- **Pipes Personalizados**: Creados para necesidades específicas
- **Parámetros de Pipe**: Aceptan configuración adicional
- **Inmutabilidad**: No alteran los datos originales

```sh
# Generar un pipe
ng generate pipe nombre-pipe
ng g p nombre-pipe
```
Nuestro pipe se ve de la siguiente forma
```ts
// nombre-pipe.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'miPipe'
})
export class MiPipe implements PipeTransform {

  transform(valor: any): any {

    // Implementa la logica de transformacion
    return valor.toUpperCase();
  }
}
```

Se aplica de la siguiente manera
```html
<p>{ texto | miPipe }}</p>
```
La inmutabilidad quiere decir que la variable mantiene su formato original. El pipe muestra la forma que queremos pero sin cambiar el valor original




# 8. Routes / Enrutamiento
El enrutamiento (routing) en Angular es un sistema que permite la navegación entre diferentes vistas o componentes dentro de una aplicación Angular sin recargar la página completa. Es una característica esencial delas SPA donde la navegación entre secciones de la aplicación se maneja mediante la manipulación del estado de la URL y la actualización dinámica del contenido de la página.


#### Definicion de rutas en el módulo de la aplicación
Las rutas definen la correspondencia entre las URL y los componentes que deben cargarse cuando esa URL está activa. Se configuran en un array dentro del módulo de la aplicación `app-routing.module.ts`
```ts
const routes: Routes = [
  { path: 'inicio', component: InicioComponent },
  { path: 'productos', component: ProductosComponent },
  { path: 'contacto', component: ContactoComponent },
];
```


#### Cargando nuestros componentes con Router Outlet
La directiva `router-outlet` se utiliza en la plantilla para indicar el lugar donde Angular debe cargar dinámicamente los componentes asociados a las rutas
```html
<!-- Acá van a girar las pantallas, generalmente se ubica abajo del nav y arriba del footer -->
<router-outlet></router-outlet>
```


#### Navegacion y Parámetros de Ruta
La navegación entre rutas se puede realizar mediante `<a>`, botones o programáticamente utilizando el servicio Router de Angular

Las rutas también pueden componer parámetros que permiten pasar datos específicos entre componentes
```html
<a routerLink="/inicio">Inicio</a>

<!-- Usando parámetros para pasar datos entre componentes -->
<a [routerLink]="['/producto', producto.id]">Ver Detalles</a>
```
```ts
{ path: 'producto/:id', component: DetalleProductoComponent }
```

Para marcar una clase CSS como activa podemos usar tanto la directiva `ngClass` como con la vieja propiedad `routerLinkActive`


#### Pasando parámetros por la URL
1. Definimos una ruta con varios parámetros
```ts
consr routes: Routes = [
  { path: 'producto/"categoria/:id', component: DetalleProductoComponent },
];
```
2. Enlazamos a la ruta con múltiples parámetros
```html
<a [routerLink]="['/producto', producto.categoria, producto.id]">Ver Detalles</a>
```
3. Recuperamos los parámetros en el componente
*Queremos capturar el producto de limpieza con id lavandina*
```ts
// micomponente.component.ts
import { ActivatedRoute } from '@angular/router';

constructor(private route: ActivatedRoute) { } // Inyectamos el ActivatedRoute en el constructor

ngOnInit() { // Al iniciar el componente se subscribe lo que diga la URL, y separamos de la URL categoria y id
  this.route.params.subscribe(params => {
    const categoria = params['categoria'];
    const productId = params['id'];

    // Hacer algo con los valores de los parámetros
  });
}
```
De esta manera, cuando hacemos el componente de vista del detalle del producto, podemos capturar esa info para hacer la vista del componente específico que queremos mostrar


#### También podemos navegar desde el controlador
Para navegar programáticamente desde TypeScript en Angular, podemos usar el servicio Router.
Este servicio proporciona métodos para realizar la navegación entre rutas.
```ts
import { Router } from '@angular/router';

constructor(private router: Router) { }

navegarAProducto(productoId: number) {
  // Podemos navegar a una ruta específica programáticamente
  this.router.navigate(['/producto', productoId]);
}
```

## Routing explicación en detalle
### 8.1 Características principales del enrutamiento en Angular

1. **Definición de Rutas**: Las rutas se definen en un archivo de configuración de rutas, generalmente llamado `app-routing.module.ts`, utilizando el módulo `RouterModule` de Angular. Cada ruta se asocia con un componente específico que se renderiza cuando la ruta está activa.

2. **Enlace a Rutas**: Angular proporciona directivas como `routerLink` para enlazar a diferentes rutas dentro de las plantillas HTML.

3. **Parámetros de Ruta**: Permite pasar parámetros a través de las rutas, que pueden ser utilizados por los componentes para mostrar contenido dinámico.

4. **Protección de Rutas**: Utiliza `Guards` (guardias) para proteger rutas, asegurando que solo usuarios autorizados puedan acceder a ciertas partes de la aplicación.

5. **Carga Diferida (Lazy Loading)**: Permite cargar módulos y componentes bajo demanda, mejorando el rendimiento de la aplicación.

### 8.3 Ejemplo de Configuración de Rutas

1. **Instalación y Configuración Básica**

Primero, asegúrate de que tienes instalado el módulo de enrutamiento en tu proyecto Angular. Luego, crea el archivo de enrutamiento, generalmente `app-routing.module.ts`:

```typescript
// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { NotFoundComponent } from './not-found/not-found.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: '**', component: NotFoundComponent }  // Wildcard route for a 404 page
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

2. **Importar el Módulo de Enrutamiento**

A continuación, importa el `AppRoutingModule` en el módulo principal de la aplicación (`app.module.ts`):

```typescript
// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { NotFoundComponent } from './not-found/not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutComponent,
    NotFoundComponent
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

3. **Utilizar Enlaces de Ruta en Plantillas**

En tus componentes, utiliza la directiva `routerLink` para enlazar a las diferentes rutas definidas:

```html
<!-- app.component.html -->
<nav>
  <a routerLink="/">Home</a>
  <a routerLink="/about">About</a>
</nav>
<router-outlet></router-outlet>
```

El `<router-outlet>` es un marcador de posición donde Angular renderiza los componentes correspondientes a las rutas activas.

### 8.4 Parámetros de Ruta

Para manejar rutas con parámetros, define la ruta con un parámetro en el archivo de configuración de rutas:

```typescript
// app-routing.module.ts
const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'user/:id', component: UserComponent }, // Route with parameter
  { path: '**', component: NotFoundComponent }
];
```

Luego, en el componente que recibe el parámetro, puedes acceder a él usando `ActivatedRoute`:

```typescript
// user.component.ts
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
  userId: string;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.userId = this.route.snapshot.paramMap.get('id');
  }
}
```

### 8.5 Trayendo por parametros los datos de un mock
#### products.mock.ts
```ts
export const productList: Product[] = [
  { id: 1, name: 'Lavandina', prize: 10, description: 'Botella de 1 Litro' },
  { id: 1, name: 'Detergente', prize: 5, description: 'Dura 120 lavados' },
  { id: 1, name: 'Limpia vidrios', prize: 10, description: 'Vidrios transparentes' },
]

export interface Product {
  id: number | string;
  name: string;
  price: number;
  description: string;
}
```
#### product-detail.component.ts
```ts
// ...
import { Product, productsList } from '../products/products.mock';
// ...
export class ProductDetailComponent implements OnInit {

  product?: Product;
  productList: Product[] = productsList; // Traemos el productList

  constructor(private _route: ActivatedRoute) { }

  ngOnInit(): void {
    this._route.params.subscribe(params => { // Traemos toda la informacion del objeto

      // Seteamos el productp entero
      this.product = this.productList.find(product => product.id == params['productId']);
    })
  }
}
```
#### product-detail.component.html usando `ngContainer`
ngContainer es una estructura de control que no afecta al DOM, se utiliza para agrupar elementos sin agregar nodos adicionales al arbol DOM:
```html
<ng-container *ngIf="!loading">
  <h1> Producto: {{ product?.name }} </h1>
  <h1> Precio: {{ product?.prize | currency }} </h1>
  <h3 *ngIf="product?.decription"> Descripcion: {{ product?.description }} </h3>
</ng-container>

<ng-container *ngIf="loading">
  <i style="color: blue">Cargando informacion...</i>
</ng-container>
```





# 9. Estructuras de control 
### `*ngIf`, `*ngFor`, `*ngSwitch`, `ngClass`, `ngStyle` y `ngModel`
En Angular, las estructuras de control son fundamentales para gestionar la lógica de flujo en las plantillas. Estas estructuras permiten condicionar la visualización de elementos, iterar sobre listas y gestionar eventos.

### 1. `*ngIf`
La directiva `*ngIf` se utiliza para mostrar o esconder un elemento del DOM basado en una condición booleana.

**Ejemplo:**

```html
<div *ngIf="isLoggedIn; else loggedOutTemplate">
  <p>Welcome, user!</p>
</div>
<ng-template #loggedOutTemplate>
  <p>Please log in.</p>
</ng-template>
```

**Componente:**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  isLoggedIn = true; // Cambiar a false para ver el template alternativo
}
```

### 2. `*ngFor`

La directiva `*ngFor` se utiliza para iterar sobre una lista y renderizar un elemento del DOM para cada ítem de la lista.

**Ejemplo:**

```html
<ul>
  <li *ngFor="let item of items">{{ item }}</li>
</ul>
```

**Componente:**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  items = ['Item 1', 'Item 2', 'Item 3'];
}
```

### 3. `*ngSwitch`

La directiva `*ngSwitch` se utiliza para mostrar uno de varios elementos alternativos basado en una expresión.

**Ejemplo:**

```html
<div [ngSwitch]="selectedOption">
  <div *ngSwitchCase="'option1'">Option 1 selected</div>
  <div *ngSwitchCase="'option2'">Option 2 selected</div>
  <div *ngSwitchCase="'option3'">Option 3 selected</div>
  <div *ngSwitchDefault>No option selected</div>
</div>
```

**Componente:**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  selectedOption = 'option1'; // Cambiar el valor para ver diferentes resultados
}
```

### 4. `ngClass`

La directiva `ngClass` se utiliza para añadir o eliminar clases CSS basadas en una condición.

**Ejemplo:**

```html
<div [ngClass]="{ 'active': isActive, 'disabled': !isActive }">
  This div is active or disabled.
</div>
```

**Componente:**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styles: [`
    .active { color: green; }
    .disabled { color: red; }
  `]
})
export class AppComponent {
  isActive = true; // Cambiar a false para ver el efecto de la clase disabled
}
```

### 5. `ngStyle`

La directiva `ngStyle` se utiliza para aplicar estilos CSS en línea basados en una expresión.

**Ejemplo:**

```html
<div [ngStyle]="{ 'font-size.px': fontSize, 'color': fontColor }">
  This div has dynamic styles.
</div>
```

**Componente:**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  fontSize = 20; // Cambiar para modificar el tamaño de fuente
  fontColor = 'blue'; // Cambiar para modificar el color del texto
}
```

### 6. `ngModel`

La directiva `ngModel` se utiliza para enlazar datos bidireccionalmente entre el modelo y la vista.

**Ejemplo:**

```html
<input [(ngModel)]="name" placeholder="Enter your name">
<p>Hello, {{ name }}!</p>
```

**Componente:**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  name = ''; // Inicialmente vacío, se actualizará con el valor del input
}
```

### Resumen
Las estructuras de control en Angular proporcionan una forma eficiente y dinámica de gestionar la lógica de la vista directamente en las plantillas. Utilizando directivas como `*ngIf`, `*ngFor`, `*ngSwitch`, `ngClass`, `ngStyle` y `ngModel`, los desarrolladores pueden crear aplicaciones dinámicas y reactivas de manera sencilla y eficiente.




# 10. Formularios
Los formularios en Angular son una parte crucial del desarrollo de aplicaciones web, ya que permiten la captura, validación y manejo de datos del usuario. Angular proporciona dos enfoques principales para trabajar con formularios:

1. **Formularios reactivos (Reactive Forms)**
2. **Formularios dirigidos por plantillas (Template-driven Forms)**


### Formularios Reactivos (Reactive Forms)

Los formularios reactivos son gestionados y validados en el componente en lugar de en la plantilla. Este enfoque proporciona un control más detallado sobre la estructura y la lógica del formulario.

#### Paso 1: Configuración del Módulo

Primero, debes importar `ReactiveFormsModule` en tu módulo de aplicación:

```typescript
// app.module.ts
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, ReactiveFormsModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

#### Paso 2: Creación del Formulario en el Componente

En el componente, defines el formulario y sus controles utilizando `FormGroup` y `FormControl`.

```typescript
// app.component.ts
import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  userForm = new FormGroup({
    name: new FormControl('', [Validators.required, Validators.minLength(3)]),
    email: new FormControl('', [Validators.required, Validators.email]),
    age: new FormControl('', [Validators.required, Validators.min(18)])
  });

  onSubmit() {
    console.log(this.userForm.value);
  }
}
```

#### Paso 3: Plantilla del Formulario

En la plantilla, utilizas directivas como `[formGroup]` y `formControlName` para vincular los controles del formulario.

```html
<!-- app.component.html -->
<form [formGroup]="userForm" (ngSubmit)="onSubmit()">
  <div>
    <label for="name">Name:</label>
    <input id="name" formControlName="name">
    <div *ngIf="userForm.get('name').invalid && userForm.get('name').touched">
      Name is required and must be at least 3 characters long.
    </div>
  </div>
  <div>
    <label for="email">Email:</label>
    <input id="email" formControlName="email">
    <div *ngIf="userForm.get('email').invalid && userForm.get('email').touched">
      Please enter a valid email address.
    </div>
  </div>
  <div>
    <label for="age">Age:</label>
    <input id="age" formControlName="age" type="number">
    <div *ngIf="userForm.get('age').invalid && userForm.get('age').touched">
      Age is required and must be at least 18.
    </div>
  </div>
  <button type="submit" [disabled]="userForm.invalid">Submit</button>
</form>
```

### Formularios Dirigidos por Plantillas (Template-driven Forms)

Los formularios dirigidos por plantillas son gestionados principalmente en la plantilla HTML, utilizando directivas específicas de Angular.

#### Paso 1: Configuración del Módulo

Primero, debes importar `FormsModule` en tu módulo de aplicación:

```typescript
// app.module.ts
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, FormsModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

#### Paso 2: Modelo de Datos en el Componente

En el componente, defines un modelo de datos que será enlazado bidireccionalmente con el formulario en la plantilla.

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  user = {
    name: '',
    email: '',
    age: null
  };

  onSubmit(form) {
    console.log(form.value);
  }
}
```

#### Paso 3: Plantilla del Formulario

En la plantilla, utilizas directivas como `ngModel` para enlazar los controles del formulario al modelo de datos.

```html
<!-- app.component.html -->
<form #userForm="ngForm" (ngSubmit)="onSubmit(userForm)">
  <div>
    <label for="name">Name:</label>
    <input id="name" name="name" [(ngModel)]="user.name" required minlength="3">
    <div *ngIf="userForm.controls.name?.invalid && userForm.controls.name?.touched">
      Name is required and must be at least 3 characters long.
    </div>
  </div>
  <div>
    <label for="email">Email:</label>
    <input id="email" name="email" [(ngModel)]="user.email" required email>
    <div *ngIf="userForm.controls.email?.invalid && userForm.controls.email?.touched">
      Please enter a valid email address.
    </div>
  </div>
  <div>
    <label for="age">Age:</label>
    <input id="age" name="age" [(ngModel)]="user.age" required type="number" min="18">
    <div *ngIf="userForm.controls.age?.invalid && userForm.controls.age?.touched">
      Age is required and must be at least 18.
    </div>
  </div>
  <button type="submit" [disabled]="userForm.invalid">Submit</button>
</form>
```

### Comparación entre Formularios Reactivos y Formularios Dirigidos por Plantillas

1. **Control y Escalabilidad:**
   - **Formularios Reactivos:** Ofrecen un control más detallado y son más adecuados para formularios complejos y aplicaciones a gran escala.
   - **Formularios Dirigidos por Plantillas:** Son más fáciles de implementar y son adecuados para formularios simples.

2. **Validación:**
   - **Formularios Reactivos:** La validación se define en el componente, lo que permite una validación más robusta y reutilizable.
   - **Formularios Dirigidos por Plantillas:** La validación se maneja principalmente en la plantilla usando atributos de validación estándar de HTML5 y directivas de Angular.

3. **Sincronización de Datos:**
   - **Formularios Reactivos:** Los datos del formulario se mantienen en el componente, lo que permite una sincronización más precisa y eficiente.
   - **Formularios Dirigidos por Plantillas:** La sincronización de datos se realiza automáticamente mediante el enlace bidireccional (`ngModel`).




# 11. Ciclos de vida de un componente
Los ciclos de vida de los componentes en Angular son un conjunto de eventos o etapas que un componente atraviesa desde su creación hasta su destrucción. Angular proporciona varios métodos de ciclo de vida que permiten a los desarrolladores ejecutar código en diferentes etapas del ciclo de vida del componente. Estos métodos se definen como interfaces que los componentes pueden implementar para responder a estos eventos.

### 1. ngOnChanges
Este método se llama cuando uno o más valores de las propiedades de entrada vinculadas a un componente cambian.


### 2. ngOnInit
Este método se llama una vez después de que se inicializan las propiedades vinculadas. Es un buen lugar para inicializar la lógica del componente.


### 3. ngDoCheck
Este método se llama durante cada ciclo de verificación de cambios. Es útil para detectar y actuar sobre cambios que Angular no puede detectar por sí mismo.


### 4. ngAfterContentInit
Este método se llama una vez después de que Angular ha proyectado contenido externo en la vista del componente.


### 5. ngAfterContentChecked
Este método se llama después de que Angular verifica el contenido proyectado en el componente.


### 6. ngAfterViewInit
Este método se llama una vez después de que Angular ha inicializado las vistas del componente y sus hijos.


### 7. ngAfterViewChecked
Este método se llama después de que Angular verifica las vistas del componente y sus hijos.


### 8. ngOnDestroy
Este método se llama justo antes de que Angular destruya el componente. Es un buen lugar para limpiar y liberar recursos, como suscripciones o temporizadores.




# 12. Conexion Backend o APIs
### ¿Qué es una API?
Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permiten a diferentes software comunicarse entre sí. Las APIs definen la forma en que los desarrolladores pueden interactuar con una aplicación, servicio o sistema. Existen varios tipos de APIs, siendo las más comunes las APIs web, que permiten la comunicación entre aplicaciones web y servidores a través de la red utilizando protocolos como HTTP/HTTPS. Las API nos permiten:

- **Integracion de servicios**: Permiten que diferentes servicios web se integren entre si, como usar la API de google maps para mostrar mapas o la API de twitter para mostrar tweets
- **Acceso a datos externos**: Facilitan el acceso a datos y recursos que residen en servidores externos. Podemos usar APIs para obtener info de bbdd, servicios en la nube u otros recursos online
- **Interaccion con plataformas sociales**: Muchas RRSS como fb, twitter, ig proporcionan APIs que permiten a los desarrolladores acceder a funciones especificas de esas plataformas, como publicar contenido o recuperar datos de perfiles de usuario
- **Desarrollo de aplicaciones mobiles**: Las apps mobiles a menudo usan APIs para conectarse bien a servicios en la nube como a funcionalidades especificas del dispositivo
- **Automatizacion de procesos**: Una empresa puede tener un sistema de gestion de inventario que se conecta a una API de proveedores para realizar pedidos automaticamente cuando se agota el stock
- **Desarrollo de aplicaciones web**: Las webs modernas a menudo usan APIs para cargar datos de forma asincrona, lo que mejora la velocidad y eficiencia
- **Microservicios**: En arquitecturas de microservicios, los diferentes componentes del sistema se comunican a traves de APIs, lo que permite la escalabilidad y flexibilidad en el desarrollo y mantenimiento de aplicaciones


En Angular, la forma más común de hacer conexiones a una API es utilizando el servicio `HttpClient` proporcionado por el módulo `HttpClientModule`.

#### 1. Configurar el Módulo HttpClientModule

Primero, debes asegurarte de que el módulo `HttpClientModule` esté importado en tu aplicación Angular. Normalmente, esto se hace en el módulo principal `AppModule`.

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';  // Importa HttpClientModule

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule  // Agrega HttpClientModule a las importaciones
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

#### 2. Crear un Servicio para la Conexión HTTP

Luego, crea un servicio que se encargue de realizar las llamadas HTTP a la API. Aquí hay un ejemplo de un servicio que obtiene datos de una API:

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'https://jsonplaceholder.typicode.com/posts';

  constructor(private http: HttpClient) { }

  getPosts(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
```

#### 3. Usar el Servicio en un Componente

Ahora, puedes usar el servicio en un componente para obtener datos de la API y mostrarlos en la vista.

```typescript
import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-posts',
  template: `
    <div *ngFor="let post of posts">
      <h2>{{ post.title }}</h2>
      <p>{{ post.body }}</p>
    </div>
  `
})
export class PostsComponent implements OnInit {
  posts: any[] = [];

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getPosts().subscribe(
      data => {
        this.posts = data;
      },
      error => {
        console.error('Error: ', error);
      }
    );
  }
}
```

#### Explicación del Código

1. **Importar HttpClientModule**: Es necesario importar y agregar `HttpClientModule` en el módulo principal para habilitar el uso de `HttpClient` en toda la aplicación.

2. **Crear el Servicio ApiService**: Este servicio utiliza `HttpClient` para realizar una solicitud GET a la API y devuelve un observable de tipo `any[]`.

3. **Inyectar el Servicio en el Componente**: En el componente `PostsComponent`, el servicio `ApiService` se inyecta en el constructor. Luego, se suscribe al observable `getPosts` en el método `ngOnInit` para obtener los datos y almacenarlos en una variable `posts` para su uso en la plantilla.

### Conclusión

En Angular, realizar una conexión a una API es sencillo utilizando `HttpClient`. Siguiendo estos pasos, puedes configurar tu aplicación para realizar solicitudes HTTP y manejar datos asincrónicos de manera eficiente. Esta capacidad es crucial para crear aplicaciones web modernas y dinámicas que interactúan con servidores y servicios externos.








# EXTRAS
## Conexion HTTP Angular
En Angular, se realiza una conexión HTTP utilizando el módulo `HttpClient` del paquete `@angular/common/http`. `HttpClient` proporciona métodos para realizar solicitudes HTTP de manera fácil y segura, como `get()`, `post()`, `put()`, `delete()`, entre otros.

### Paso a Paso para realizar una conexión HTTP en Angular

#### 1. Importar `HttpClientModule`
Primero, necesitas importar `HttpClientModule` en tu módulo principal (`AppModule`) para que Angular sepa que vas a usar funcionalidades HTTP.

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

#### 2. Crear un servicio para manejar las solicitudes HTTP

Es una buena práctica encapsular las solicitudes HTTP dentro de servicios. Crea un servicio con Angular CLI:

```sh
ng generate service data
```

Esto generará un archivo `data.service.ts` donde implementarás las solicitudes HTTP.

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private apiUrl = 'https://jsonplaceholder.typicode.com/posts';

  constructor(private http: HttpClient) { }

  // Método para obtener datos
  getPosts(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  // Método para obtener un post por ID
  getPostById(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }

  // Método para crear un nuevo post
  createPost(post: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, post);
  }

  // Método para actualizar un post existente
  updatePost(id: number, post: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, post);
  }

  // Método para eliminar un post
  deletePost(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }
}
```

#### 3. Consumir el servicio en un componente

Ahora puedes usar el servicio en cualquier componente. Por ejemplo, en `app.component.ts`:

```typescript
import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  posts: any[];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.loadPosts();
  }

  loadPosts() {
    this.dataService.getPosts().subscribe(
      data => {
        this.posts = data;
      },
      error => {
        console.error('Error fetching posts', error);
      }
    );
  }
}
```

### Resumen

1. **Importar `HttpClientModule`**: Asegúrate de que `HttpClientModule` esté importado en tu módulo principal.
2. **Crear un servicio**: Encapsula las solicitudes HTTP dentro de un servicio para mantener tu código organizado y reutilizable.
3. **Consumir el servicio**: Inyecta el servicio en tus componentes y utiliza sus métodos para realizar las solicitudes HTTP.

### Ejemplo Completo

#### app.module.ts

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { DataService } from './data.service';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

#### data.service.ts

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private apiUrl = 'https://jsonplaceholder.typicode.com/posts';

  constructor(private http: HttpClient) { }

  getPosts(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  getPostById(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }

  createPost(post: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, post);
  }

  updatePost(id: number, post: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, post);
  }

  deletePost(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }
}
```

#### app.component.ts

```typescript
import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  posts: any[];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.loadPosts();
  }

  loadPosts() {
    this.dataService.getPosts().subscribe(
      data => {
        this.posts = data;
      },
      error => {
        console.error('Error fetching posts', error);
      }
    );
  }
}
```

#### app.component.html

```html
<div>
  <h1>Posts</h1>
  <ul>
    <li *ngFor="let post of posts">{{ post.title }}</li>
  </ul>
</div>
```

Con esta estructura, puedes realizar fácilmente conexiones HTTP en tu aplicación Angular utilizando `HttpClient`.




## Angular Elements
Angular Elements es una funcionalidad de Angular que permite empaquetar componentes de Angular como elementos personalizados (custom elements) o Web Components. Estos elementos personalizados pueden ser utilizados en aplicaciones no construidas con Angular, lo que facilita la integración de componentes Angular en diferentes contextos de aplicaciones web. 

Los Web Components son un estándar web que permite crear componentes reutilizables y encapsulados. Con Angular Elements, los componentes de Angular se pueden convertir en estos Web Components, lo que ofrece varias ventajas:

1. **Reutilización**: Permite reutilizar componentes de Angular en diferentes proyectos, incluso si estos no utilizan Angular como framework principal.
2. **Encapsulamiento**: Los Web Components están encapsulados, lo que significa que su estilo y funcionalidad no afectan al resto de la aplicación y viceversa.
3. **Compatibilidad**: Los Web Components son compatibles con todos los navegadores modernos, por lo que los componentes creados con Angular Elements pueden ser usados de manera consistente en diferentes entornos.

### ¿Cómo funcionan los Angular Elements?

1. **Creación del componente**: Se crea un componente de Angular como de costumbre.
2. **Conversión a elemento personalizado**: Se utiliza la funcionalidad de Angular Elements para convertir este componente en un Web Component.
3. **Registro del elemento personalizado**: El elemento se registra en el navegador, lo que permite que pueda ser utilizado en cualquier aplicación web.

### Ejemplo básico

1. **Instalación de Angular Elements**:
   ```bash
   ng add @angular/elements
   npm install @webcomponents/custom-elements
   ```

2. **Creación de un componente**:
   ```typescript
   import { Component } from '@angular/core';

   @Component({
     selector: 'app-hello-world',
     template: `<h1>Hello, World!</h1>`
   })
   export class HelloWorldComponent {}
   ```

3. **Conversión a elemento personalizado**:
   ```typescript
   import { Injector } from '@angular/core';
   import { createCustomElement } from '@angular/elements';
   import { HelloWorldComponent } from './hello-world/hello-world.component';
   import { NgModule, DoBootstrap } from '@angular/core';

   @NgModule({
     declarations: [HelloWorldComponent],
     entryComponents: [HelloWorldComponent]
   })
   export class AppModule implements DoBootstrap {
     constructor(private injector: Injector) {}

     ngDoBootstrap() {
       const el = createCustomElement(HelloWorldComponent, { injector: this.injector });
       customElements.define('hello-world', el);
     }
   }
   ```

4. **Uso del elemento personalizado en una aplicación no Angular**:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Angular Elements Example</title>
   </head>
   <body>
     <hello-world></hello-world>
     <script src="path/to/your/angular-elements-bundle.js"></script>
   </body>
   </html>
   ```

Con Angular Elements, puedes crear componentes que sean flexibles y reutilizables, aprovechando las capacidades avanzadas de Angular y la interoperabilidad que ofrecen los Web Components.




## JSON Web Tokens / JWT
JSON Web Token (JWT) es un estándar abierto (RFC 7519) que define una forma compacta y autocontenida de transmitir información entre dos partes como un objeto JSON. Esta información puede ser verificada y confiable porque está firmada digitalmente. Los JWT son comúnmente usados para autenticación y autorización en aplicaciones web, incluyendo aquellas construidas con Angular.

### ¿Cómo se utiliza JWT en Angular?

En una aplicación Angular, JWT se usa principalmente para manejar la autenticación y la autorización. A continuación se explica en detalle cómo se integra JWT en una aplicación Angular:

### Proceso de Autenticación con JWT

1. **Login del Usuario:**
   - El usuario ingresa sus credenciales (por ejemplo, nombre de usuario y contraseña) en el formulario de login de la aplicación Angular.
   
2. **Envío de Credenciales al Servidor:**
   - Las credenciales se envían al servidor mediante una solicitud HTTP (normalmente POST).

3. **Verificación de Credenciales:**
   - El servidor verifica las credenciales recibidas. Si son válidas, el servidor genera un JWT que incluye información relevante (por ejemplo, el ID del usuario, roles, permisos, etc.).

4. **Envío del JWT al Cliente:**
   - El servidor envía el JWT al cliente Angular como respuesta a la solicitud de autenticación.

5. **Almacenamiento del JWT en el Cliente:**
   - El cliente almacena el JWT recibido, comúnmente en el `localStorage` o `sessionStorage`.

6. **Uso del JWT para Solicitudes Autenticadas:**
   - Para todas las solicitudes HTTP subsecuentes que requieren autenticación, el cliente Angular incluye el JWT en el encabezado de autorización (`Authorization: Bearer <JWT>`).

7. **Verificación del JWT en el Servidor:**
   - El servidor verifica el JWT en cada solicitud autenticada para asegurarse de que es válido y no ha sido alterado.

### Implementación de JWT en Angular

#### 1. Instalación de Librerías

Para trabajar con JWT en Angular, puedes usar librerías como `@auth0/angular-jwt` para gestionar automáticamente la inclusión del token en las solicitudes HTTP.

```sh
npm install @auth0/angular-jwt
```

#### 2. Configuración del Interceptor

Crea un interceptor para añadir el JWT a las solicitudes HTTP.

```typescript
import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {
  constructor(private authService: AuthService) {}

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const currentUser = this.authService.currentUserValue;
    if (currentUser && currentUser.token) {
      request = request.clone({
        setHeaders: {
          Authorization: `Bearer ${currentUser.token}`
        }
      });
    }

    return next.handle(request);
  }
}
```

#### 3. Proveedor del Interceptor

Añade el interceptor en el módulo principal de la aplicación (`app.module.ts`).

```typescript
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { JwtInterceptor } from './jwt.interceptor';

@NgModule({
  // ...
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true }
  ]
})
export class AppModule { }
```

#### 4. Servicio de Autenticación

Crea un servicio de autenticación para manejar el login y almacenamiento del token.

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private currentUserSubject: BehaviorSubject<any>;
  public currentUser: Observable<any>;

  constructor(private http: HttpClient) {
    this.currentUserSubject = new BehaviorSubject<any>(JSON.parse(localStorage.getItem('currentUser')));
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue(): any {
    return this.currentUserSubject.value;
  }

  login(username: string, password: string) {
    return this.http.post<any>(`/api/authenticate`, { username, password })
      .pipe(map(user => {
        if (user && user.token) {
          localStorage.setItem('currentUser', JSON.stringify(user));
          this.currentUserSubject.next(user);
        }
        return user;
      }));
  }

  logout() {
    localStorage.removeItem('currentUser');
    this.currentUserSubject.next(null);
  }
}
```

### Resumen
El uso de JSON Web Tokens (JWT) en Angular permite la implementación de un sistema de autenticación y autorización robusto y seguro. A través de la integración con interceptores HTTP y servicios de autenticación, los desarrolladores pueden asegurar que las solicitudes autenticadas incluyan el token necesario para validar al usuario en el servidor. Esto asegura que los recursos y operaciones sensibles estén protegidos y accesibles solo para usuarios autorizados.




## Interceptores en Angular
Un interceptor en Angular es una clase especial que implementa la interfaz `HttpInterceptor` y permite interceptar y manipular las solicitudes HTTP salientes y las respuestas HTTP entrantes en una aplicación Angular. Los interceptores son una herramienta poderosa para agregar lógica de procesamiento transversal, como el manejo de errores, la autenticación y el registro, sin tener que modificar cada solicitud individualmente.

### ¿Cómo funcionan los interceptores?

Un interceptor se registra en el proveedor de Angular y se ejecuta en el contexto del flujo de solicitudes y respuestas HTTP. Cuando una solicitud HTTP se realiza, el interceptor puede modificar la solicitud antes de que se envíe al servidor. De manera similar, cuando se recibe una respuesta HTTP, el interceptor puede modificar la respuesta antes de que llegue al componente que la solicitó.

### Ejemplos de uso común de interceptores

1. **Agregar tokens de autenticación a las solicitudes**
2. **Manejo centralizado de errores**
3. **Registro de solicitudes y respuestas**
4. **Modificar encabezados HTTP**

### Creación y uso de un interceptor en Angular

#### Paso 1: Crear un interceptor

Primero, crea una nueva clase que implemente la interfaz `HttpInterceptor`.

```typescript
import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // Clona la solicitud para añadir el nuevo header.
    const clonedRequest = request.clone({
      setHeaders: {
        Authorization: `Bearer ${this.getToken()}`
      }
    });

    // Pasa la solicitud clonada en lugar de la original.
    return next.handle(clonedRequest);
  }

  // Método para obtener el token de autenticación (por ejemplo, de localStorage)
  private getToken(): string {
    return localStorage.getItem('token');
  }
}
```

#### Paso 2: Registrar el interceptor

En el archivo del módulo principal de la aplicación (`app.module.ts`), registra el interceptor en la sección de proveedores.

```typescript
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { AuthInterceptor } from './auth.interceptor';

@NgModule({
  // ...
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  // ...
})
export class AppModule { }
```

#### Ejemplo completo: Interceptor para manejo de errores

A continuación, se muestra un ejemplo de cómo se podría crear un interceptor para manejar errores HTTP de forma centralizada.

```typescript
import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    return next.handle(req).pipe(
      catchError((error: HttpErrorResponse) => {
        let errorMessage = '';
        if (error.error instanceof ErrorEvent) {
          // Error del lado del cliente
          errorMessage = `Error: ${error.error.message}`;
        } else {
          // Error del lado del servidor
          errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
        }
        // Muestra el error en la consola o muestra una notificación al usuario
        console.error(errorMessage);
        return throwError(errorMessage);
      })
    );
  }
}
```

Luego, registras este interceptor en tu módulo principal:

```typescript
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { ErrorInterceptor } from './error.interceptor';

@NgModule({
  // ...
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true }
  ],
  // ...
})
export class AppModule { }
```

### Resumen

Los interceptores en Angular son herramientas poderosas que permiten manipular todas las solicitudes y respuestas HTTP de manera centralizada. Al implementar la interfaz `HttpInterceptor`, puedes agregar lógica transversal como la autenticación, el manejo de errores y el registro de actividades sin modificar el código específico de cada solicitud HTTP en tu aplicación. Esto no solo mejora la eficiencia, sino que también mantiene el código más limpio y mantenible.




## Operaciones CRUD en Angular
Para realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en Angular hacia una API, se deben seguir varios pasos. A continuación, te proporciono una explicación completa con ejemplos para cada operación.

### Pasos Previos

1. **Instalar Angular CLI y Crear un Proyecto Angular**:
   Asegúrate de tener Angular CLI instalado y crea un nuevo proyecto Angular:
   ```sh
   npm install -g @angular/cli
   ng new crud-angular
   cd crud-angular
   ```

2. **Configurar HttpClientModule**:
   Importa `HttpClientModule` en tu módulo principal (`app.module.ts`):
   ```typescript
   import { BrowserModule } from '@angular/platform-browser';
   import { NgModule } from '@angular/core';
   import { HttpClientModule } from '@angular/common/http';
   import { AppComponent } from './app.component';

   @NgModule({
     declarations: [
       AppComponent
     ],
     imports: [
       BrowserModule,
       HttpClientModule
     ],
     providers: [],
     bootstrap: [AppComponent]
   })
   export class AppModule { }
   ```

### Servicio HTTP para CRUD

Crea un servicio Angular que manejará todas las operaciones CRUD.

#### 1. Crear el Servicio

Ejecuta el siguiente comando para generar un servicio:
```sh
ng generate service api
```

#### 2. Definir el Servicio

Edita el archivo `api.service.ts` para definir los métodos CRUD:

```typescript
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'https://jsonplaceholder.typicode.com/posts';

  constructor(private http: HttpClient) { }

  // Create
  createPost(post: any): Observable<any> {
    return this.http.post(this.apiUrl, post, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    });
  }

  // Read
  getPosts(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  // Update
  updatePost(id: number, post: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, post, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    });
  }

  // Delete
  deletePost(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }
}
```

### Componente para Interactuar con el Servicio

Crea un componente para realizar operaciones CRUD.

#### 1. Crear el Componente

Ejecuta el siguiente comando para generar un componente:
```sh
ng generate component posts
```

#### 2. Definir el Componente

Edita el archivo `posts.component.ts` para usar el servicio API:

```typescript
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {
  posts: any[] = [];
  newPost: any = { title: '', body: '' };
  updatePostData: any = { id: null, title: '', body: '' };

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.getPosts();
  }

  getPosts(): void {
    this.apiService.getPosts().subscribe(data => {
      this.posts = data;
    });
  }

  createPost(): void {
    this.apiService.createPost(this.newPost).subscribe(post => {
      this.posts.push(post);
      this.newPost = { title: '', body: '' };
    });
  }

  updatePost(): void {
    this.apiService.updatePost(this.updatePostData.id, this.updatePostData).subscribe(post => {
      const index = this.posts.findIndex(p => p.id === post.id);
      if (index !== -1) {
        this.posts[index] = post;
      }
      this.updatePostData = { id: null, title: '', body: '' };
    });
  }

  deletePost(id: number): void {
    this.apiService.deletePost(id).subscribe(() => {
      this.posts = this.posts.filter(post => post.id !== id);
    });
  }

  selectPostForUpdate(post: any): void {
    this.updatePostData = { ...post };
  }
}
```

### Plantilla del Componente

Edita el archivo `posts.component.html` para crear la interfaz de usuario:

```html
<div>
  <h1>Posts</h1>

  <h2>Create Post</h2>
  <form (ngSubmit)="createPost()">
    <input [(ngModel)]="newPost.title" name="title" placeholder="Title" required>
    <input [(ngModel)]="newPost.body" name="body" placeholder="Body" required>
    <button type="submit">Create</button>
  </form>

  <h2>Update Post</h2>
  <form (ngSubmit)="updatePost()">
    <input [(ngModel)]="updatePostData.id" name="id" placeholder="ID" readonly>
    <input [(ngModel)]="updatePostData.title" name="title" placeholder="Title" required>
    <input [(ngModel)]="updatePostData.body" name="body" placeholder="Body" required>
    <button type="submit">Update</button>
  </form>

  <h2>Posts List</h2>
  <ul>
    <li *ngFor="let post of posts">
      <strong>{{ post.title }}</strong>: {{ post.body }}
      <button (click)="selectPostForUpdate(post)">Edit</button>
      <button (click)="deletePost(post.id)">Delete</button>
    </li>
  </ul>
</div>
```

### Conclusión

Este ejemplo cubre todas las operaciones CRUD básicas utilizando Angular y una API REST. Asegúrate de tener un servidor backend configurado para manejar las solicitudes y devolver respuestas adecuadas. Las operaciones CRUD son fundamentales en el desarrollo de aplicaciones web y comprender cómo implementarlas en Angular es crucial para construir aplicaciones modernas y dinámicas.