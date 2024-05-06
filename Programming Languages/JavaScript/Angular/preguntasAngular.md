1. **¿Qué es Angular y cuáles son sus características principales?**
   - Angular es un framework de desarrollo de aplicaciones web desarrollado por Google. Sus características principales incluyen la creación de aplicaciones de una sola página (SPA), enlace de datos bidireccional, modularidad a través de componentes, inyección de dependencias, enrutamiento, y mucho más.

2. **¿Cuál es la diferencia entre AngularJS y Angular?**
   - AngularJS es la versión anterior de Angular (v1.x), mientras que Angular se refiere a las versiones más recientes (v2 y posteriores).
   - Angular está reescrito desde cero utilizando TypeScript, mientras que AngularJS se basa en JavaScript.
   - Angular ofrece un rendimiento mejorado, una arquitectura más modular y una mejor escalabilidad en comparación con AngularJS.

3. **¿Cómo se crea un nuevo componente en Angular?**
   - Un nuevo componente en Angular se crea utilizando el comando `ng generate component <nombre-componente>` o manualmente creando un archivo TypeScript para la lógica del componente y un archivo HTML para la plantilla de la vista.

4. **¿Qué es el enlace de datos en Angular y cuáles son sus tipos?**
   - El enlace de datos en Angular establece una conexión entre los datos en el modelo y la vista de la aplicación.
   - Los tipos de enlace de datos disponibles en Angular son: enlace de datos unidireccional (`{{}}`), enlace de datos bidireccional (`[(ngModel)]`), enlace de atributo (`[atributo]`), y enlace de eventos (`(evento)`).

5. **¿Qué son los servicios en Angular y cómo se utilizan?**
   - Los servicios en Angular son clases que encapsulan la lógica de negocio y proporcionan funcionalidades reutilizables.
   - Se utilizan creando una clase de servicio con el decorador `@Injectable()` y luego se inyectan en los componentes o en otros servicios que los necesiten.

6. **¿Qué son los módulos en Angular y cuál es su propósito?**
   - Los módulos en Angular se utilizan para organizar la aplicación en funcionalidades cohesivas y reutilizables.
   - Su propósito es facilitar la organización y la gestión de la aplicación mediante la agrupación de componentes, servicios y otros artefactos relacionados.

7. **¿Cómo se implementa la inyección de dependencias en Angular?**
   - La inyección de dependencias en Angular se implementa mediante el mecanismo de inyección de dependencias de Angular.
   - Se utiliza el decorador `@Injectable()` para marcar una clase como un servicio inyectable y se inyecta en los componentes o en otros servicios que lo necesiten mediante el constructor.

8. **¿Qué es el enrutamiento en Angular y cómo se configura?**
   - El enrutamiento en Angular permite la navegación entre diferentes componentes y vistas de la aplicación.
   - Se configura mediante la definición de rutas en un módulo de enrutamiento (`RouterModule.forRoot()`), donde se especifica el camino URL y el componente asociado.

9. **¿Qué son las directivas en Angular y cuál es su propósito?**
   - Las directivas en Angular son atributos que modifican el comportamiento de un elemento DOM.
   - Su propósito es proporcionar funcionalidades adicionales a los elementos DOM, como mostrar u ocultar elementos, iterar sobre listas, agregar clases CSS dinámicamente, y más.

10. **¿Qué son los observables en Angular y cuál es su uso?**
    - Los observables en Angular son una forma de manejar secuencias de eventos asíncronos.
    - Se utilizan para manejar eventos de manera reactiva, como las solicitudes HTTP, eventos del usuario, y otras operaciones asincrónicas.

11. **¿Cómo se realiza la validación de formularios en Angular?**
    - La validación de formularios en Angular se realiza utilizando las clases del módulo `FormsModule` y/o `ReactiveFormsModule`.
    - Se puede aplicar validación tanto en el lado del cliente como en el del servidor, utilizando directivas predefinidas o validadores personalizados.

12. **¿Qué es el decorador `@ViewChild` en Angular y cuál es su propósito?**
    - El decorador `@ViewChild` en Angular se utiliza para acceder a un elemento hijo desde un componente padre.
    - Se utiliza para interactuar con elementos DOM o componentes hijos en el componente padre.

13. **¿Cuál es la diferencia entre las estrategias de detección de cambios `OnPush` y `Default`?**
    - La estrategia de detección de cambios `OnPush` solo verifica los cambios cuando se detecta un cambio en las entradas de un componente o en sus eventos.
    - La estrategia de detección de cambios `Default` verifica los cambios en cada detección de cambios, independientemente de si hay cambios en las entradas o eventos del componente.

14. **¿Qué es la interpolación en Angular y cómo se utiliza?**
    - La interpolación en Angular es una forma de vincular datos del componente a la vista.
    - Se utiliza colocando expresiones entre dobles llaves `{{ }}` dentro de las plantillas de la vista.

15. **¿Qué es la propagación de eventos en Angular y cómo se maneja?**
    - La propagación de eventos en Angular se refiere a la propagación de eventos desde un elemento DOM hijo hasta su elemento DOM padre.
    - Se maneja utilizando la directiva `@Output` para emitir eventos desde el componente hijo y la directiva `(evento)` para escuchar eventos en el componente padre.

16. **¿Cómo se realiza la comunicación entre componentes en Angular?**
    - La comunicación entre componentes en Angular se realiza mediante el uso de servicios compartidos, @Input() para pasar datos de un componente padre a un componente hijo, @Output() para emitir eventos desde un componente hijo a un componente padre, y mediante el uso de @ViewChild para acceder a un componente hijo desde un componente padre.

17. **¿Qué es la modularidad en Angular y por qué es importante?**
    - La modularidad en Angular se refiere a la organización de la aplicación en módulos cohesivos y reutilizables.
    - Es importante porque facilita la gestión, el mantenimiento y la escalabilidad de la aplicación al dividirla en partes más pequeñas y manejables.

18. **¿Qué son los servicios HTTP en Angular y cómo se utilizan?**
    - Los servicios HTTP en Angular se utilizan para realizar solicitudes HTTP a un servidor y manejar las respuestas.
    - Se utilizan importando el módulo `HttpClientModule` en el módulo de la aplicación y luego inyectando el servicio `HttpClient` en los componentes o servicios que lo necesiten.

19. **¿Cómo se gestionan las dependencias de terceros en Angular?**
    - Las dependencias de terceros en Angular se gestionan utilizando el sistema de gestión de paquetes npm.
    - Se instalan utilizando el comando `npm install nombre-paquete` y luego se importan en el código de la aplicación según sea necesario.

20. **¿Qué es el precompilador de Angular y cómo se utiliza?**
    - El precompilador de Angular, también conocido como AOT (Ahead-of-Time) compiler, se utiliza para compilar la aplicación Angular antes de ser ejecutada en el navegador.
    - Se utiliza para mejorar el rendimiento y la seguridad de la aplicación, así como para reducir el tiempo de carga inicial.

21. **¿Qué es el Lazy Loading en Angular y cuál es su propósito?**
    - El Lazy Loading en Angular es una técnica que carga módulos de forma diferida, es decir, solo cuando son necesarios.
    - Su propósito es mejorar el rendimiento de la aplicación al reducir el tiempo de carga inicial y cargar los módulos según sea necesario.

22. **¿Qué es el Internationalization (i18n) en Angular y cuál es su propósito?**
    - El Internationalization (i18n) en Angular es una técnica que permite la internacionalización de la aplicación, es decir, la adaptación de la aplicación a diferentes idiomas y regiones.
    - Su propósito es hacer que la aplicación sea accesible para una audiencia global al permitir la traducción de textos y la adaptación de formatos de fecha, moneda, etc.

23. **¿Qué es el unit testing en Angular y cómo se realiza?**
    - El unit testing en Angular es una técnica que se utiliza para probar unidades individuales de código, como componentes, servicios y directivas.
    - Se realiza utilizando herramientas como Jasmine y Karma, y se escribe utilizando el framework de testing de Angular.

24. **¿Qué es el concepto de "Tree-shaking" en Angular?**
    - El concepto de "Tree-shaking" en Angular se refiere a la eliminación de código muerto o no utilizado durante el proceso de construcción de la aplicación.
    - Se utiliza para reducir el tamaño de los archivos generados y mejorar el rendimiento de la aplicación.

25. **¿Qué es el concepto de "Angular Universal" y cuál es su propósito?**
    - El concepto de "Angular Universal" se refiere a la capacidad de Angular para renderizar aplicaciones en el servidor, en lugar de solo en el navegador.
    - Su propósito es mejorar el SEO (optimización para motores de búsqueda) y la velocidad de carga inicial de la aplicación al enviar una versión renderizada en el servidor al cliente.

26. **¿Qué es el concepto de "Angular Elements" y cuál es su propósito?**
    - El concepto de "Angular Elements" se refiere a la capacidad de Angular para crear componentes web personalizados que se pueden utilizar en cualquier framework de JavaScript.
    - Su propósito es facilitar la reutilización de componentes de Angular en aplicaciones desarrolladas con otros frameworks, como React o Vue.

27. **¿Qué es el "Error Handling" en Angular y cómo se realiza?**
    - El "Error Handling" en Angular se refiere al manejo de errores durante la ejecución de la aplicación.
    - Se realiza utilizando bloques try-catch para capturar errores, interceptores de errores para manejar errores de forma global, y el operador catchError en observables para manejar errores en solicitudes HTTP y otras operaciones asincrónicas.

28. **¿Qué es el concepto de "Content Projection" en Angular y cómo se utiliza?**
    - El concepto de "Content Projection" en Angular se refiere a la capacidad de pasar contenido HTML dinámico a un componente desde el exterior.
    - Se utiliza utilizando la directiva `<ng-content>` en la plantilla del componente para indicar dónde se proyectará el contenido proporcionado desde el exterior.

29. **¿Qué es el concepto de "Dependency Injection (DI)" y cómo se implementa en Angular?**
    - El concepto de "Dependency Injection (DI)" en Angular se refiere a la técnica de suministrar las dependencias de un componente desde el exterior en lugar de crearlas dentro del componente.
    - Se implementa utilizando el sistema de inyección de dependencias de Angular, que proporciona las dependencias a través del constructor del componente.

30. **¿Qué son las "Directivas Estructurales" en Angular y cuáles son algunas de las más comunes?**
    - Las "Directivas Estructurales" en Angular son directivas que modifican la estructura del DOM agregando, eliminando o reemplazando elementos.
    - Algunas de las directivas estructurales más comunes son `*ngIf`, `*ngFor`, y `*ngSwitch`.

