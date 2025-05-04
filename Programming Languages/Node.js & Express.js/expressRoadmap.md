# Express.js Roadmap

# 🧭 ROADMAP TÉCNICO PARA DESARROLLADOR BACKEND SSR (Express.js + MySQL)

> Orientado a aplicaciones web dinámicas, con vistas renderizadas en el servidor, persistencia relacional y buenas prácticas de arquitectura.

**Roadmap técnico y extenso para un desarrollador backend SSR (Server-Side Rendering) con Express.js y MySQL**. Este enfoque está diseñado para quienes quieren desarrollar aplicaciones completas renderizadas en el servidor, con Express como backend y MySQL como base de datos relacional.

---

### 🧱 FASE 1: Fundamentos del Desarrollo Web y SSR

#### 🌐 Entender cómo funciona la web:
- HTML/CSS básico (para entender los requests/responses)
- JavaScript básico
  - Tipos de datos
  - Funciones y closures
  - Promesas y async/await
  - Manipulación del DOM (opcional pero útil)

- Comprender cómo funciona la web: Protocolo HTTP/HTTPS, clientes y servidores, DNS, dominios, etc.
- Ciclo de vida de una petición HTTP
- Cabeceras HTTP (status codes, content-type, cookies)
- Qué es SSR vs CSR
- Qué es un motor de plantillas y cómo funciona (EJS, Handlebars, Pug)

#### 🛠 Herramientas mínimas:
- Navegadores (DevTools)
- Postman / Insomnia
- Git y GitHub

---

### 🧠 FASE 2: JavaScript Avanzado (ES6+)

#### 💡 Profundizar en:
- Scope, Hoisting, Closures
- Callbacks, Promises, Async/Await
- Módulos ES y CommonJS
- Objetos, clases, herencia, prototype chain
- Estructuras: Map, Set, Array methods (`map`, `reduce`, `filter`)
- Patrones como Singleton y Factory (aplicables a backend)

---

### ⚙️ FASE 3: Node.js y Entorno Backend

#### 🎯 Objetivo: Entender el entorno de ejecución del backend
- ¿Qué es Node.js? Event loop, V8, single thread
- Usar `npm` o `yarn`
- Estructura básica de un proyecto en Node
- Módulos comunes: `fs`, `path`, `http`, etc.
- Debugging en Node

#### 🚀 Fundamentos de Node:
- Event Loop y EventEmitter
- Single-threaded I/O
- Streams y buffers
- File system (`fs`)
- Uso correcto de `require` vs `import`
- Crear un servidor HTTP sin frameworks

#### 🧰 Herramientas importantes:
- `nodemon`
- `dotenv`
- `nvm` para gestionar versiones de Node

---

### 🧩 FASE 4: Express.js a Nivel Profesional


#### 🎯 Objetivo 1: Aprender a crear APIs RESTful con Express.
- Crear un servidor básico
- Middlewares (qué son, cómo se usan)
- Rutas y controladores
- Manejo de errores
- Enrutamiento avanzado (params, query, nested routes)
- Uso de herramientas como `Postman` o `Insomnia`

#### 🏗 Objetivo 2: Estructura y diseño:
- Separación de rutas, controladores, servicios y modelos
- Arquitectura tipo MVC limpia
- Router modularizado

#### 🔧 Objetivo 3: Técnicas esenciales:
- Middlewares personalizados
- Middleware para manejo global de errores
- Middleware de logging (`morgan`)
- `express-session` para manejo de sesiones
- Validación con `express-validator` o `Joi`
- Subida de archivos (Multer)

#### 📦 Objetivo 4: Motores de plantillas:
- EJS (más usado con Express para SSR)
- Layouts y partials
- Incluir CSS y JS estático desde Express (`express.static`)
- Uso de `res.render()` vs `res.send()`

---

### 🗃 FASE 5: MySQL y Persistencia Relacional


#### 🎯 Objetivo: Conectar y manipular bases de datos desde Express.

- Fundamentos de bases de datos relacionales vs no relacionales
- Aprender MongoDB (más común con Node.js)
  - CRUD
  - Colecciones y documentos
- Usar Mongoose (ODM para MongoDB)
- Modelado de datos
- Validaciones


#### 🔍 Fundamentos de SQL:
- SELECT, INSERT, UPDATE, DELETE
- JOINs (INNER, LEFT, RIGHT)
- Índices y claves primarias/foráneas
- Normalización básica

#### 🧱 MySQL en el backend:
- `mysql2` o `sequelize` como cliente en Node
- Creación y conexión con pools
- Consultas preparadas para evitar SQL Injection
- Migraciones manuales o con Sequelize CLI
- Uso de ORM vs query directa
- Relacionar tablas (1:1, 1:N, N:M)

---

### 🔒 FASE 6: Seguridad y Autenticación

#### 🎯 Objetivo: Proteger la API y gestionar sesiones.

- Hashing con `bcrypt`
- Autenticación con JWT
- Middleware de autorización
- Seguridad básica:
  - Helmet
  - CORS
  - Rate limiting
  - Sanitización de entradas

#### 🛡 Seguridad básica:
- Sanitización de inputs
- CORS controlado
- Headers seguros con `helmet`
- CSRF protection en SSR
- Session fixation y cookie security flags (`HttpOnly`, `SameSite`, `Secure`)

#### 🔐 Autenticación:
- Gestión de sesiones con `express-session` + `connect-mysql` (almacenamiento de sesión en DB)
- Hashing de contraseñas con `bcrypt`
- Login clásico con sesiones y cookies (no JWT para SSR puro)
- Middleware de protección de rutas (`isAuthenticated`)

---

### 🧪 FASE 7: Testing de Aplicaciones SSR

#### 🎯 Objetivo: Asegurar la calidad del código backend.

- Fundamentos de testing (unitario, integración)
- Herramientas:
  - Jest
  - Supertest
- Escribir pruebas para rutas y lógica del backend

#### 🧼 Tests unitarios y de integración:
- Mocha + Chai o Jest
- Supertest para probar endpoints Express
- Pruebas a funciones de lógica (servicios, utilidades)
- Pruebas de rutas protegidas y formularios

---

### 📦 FASE 8: Optimización y Buenas Prácticas

#### 🎯 Objetivo: Escribir código mantenible y profesional.

- Uso de `.env` con `dotenv`
- Linter (ESLint)
- Formateador (Prettier)
- Control de versiones con Git
- Principios SOLID (básico)
- Estructura limpia del proyecto

#### 🧹 Código limpio y mantenible:
- Principios SOLID
- DRY, KISS y YAGNI
- Separación de responsabilidades

#### 🧰 Herramientas:
- ESLint + Prettier
- Husky + Lint-staged para pre-commits
- Documentación con Swagger (incluso para SSR puedes documentar API internas)

---

### 🚀 FASE 9: Despliegue Profesional

#### 🌍 Entorno de producción:
- Entornos `.env` (desarrollo, testing, producción)
- Deploy en VPS o plataformas:
  - Railway (Express + MySQL)
  - Render
  - DigitalOcean
- Nginx como proxy inverso
- PM2 para gestión de procesos Node
- Logs persistentes y rotación (`winston` o `bunyan`)
- Monitoreo básico (UptimeRobot, Logtail)

---

### 📈 Fase 10: Proyectos y Portafolio

#### 🎯 Objetivo: Aplicar todo lo aprendido en proyectos reales.

- API de tareas (To-do list)
- API de blog con autenticación
- E-commerce simple (productos, carrito, pedidos)
- Documentar APIs con Swagger o Postman
- Subir proyectos a GitHub con buen README

### 📁 ESTRUCTURA RECOMENDADA DEL PROYECTO

```plaintext
my-ssr-app/
│
├── public/               # Archivos estáticos (CSS, JS del cliente)
├── views/                # Vistas EJS/Pug/Handlebars
│   └── partials/         # Componentes reutilizables
├── src/
│   ├── routes/           # Archivos de rutas Express
│   ├── controllers/      # Lógica de manejo de rutas
│   ├── services/         # Lógica de negocio
│   ├── models/           # Modelos de base de datos (ORM o raw)
│   ├── middlewares/      # Middlewares personalizados
│   ├── config/           # Conexión a MySQL, settings
│   └── utils/            # Funciones auxiliares
├── .env
├── package.json
└── server.js             # Entry point principal
```

---

### 📚 BONUS: Proyectos Sugeridos para Consolidar Conocimientos

1. **Sistema de blog SSR**  
   - Login, CRUD de posts, comentarios, sistema de roles

2. **Sistema de reservas para restaurante o hotel**  
   - Calendario, slots, usuarios, admins

3. **Panel de administración con vistas renderizadas**  
   - Dashboard, gráficas, filtros

4. **E-commerce básico**  
   - Productos, carrito, checkout, historial de pedidos

---

# Competencias basicas para JR, SSR y SSR

### 🧠 Comparativa de Conocimientos: Express.js + MySQL (Backend)

| Área / Rol                         | 🟢 Junior                              | 🟡 Semi-Senior                         | 🔴 Senior                                |
|-----------------------------------|----------------------------------------|----------------------------------------|-------------------------------------------|
| **JavaScript / Node.js**         | Entiende estructuras básicas y async/await | Maneja el event loop, módulos propios, errores async | Profundo conocimiento del runtime, profiling, memoria, streams |
| **Express.js**                   | CRUD con rutas básicas, middlewares simples | Arquitectura modular (MVC), middlewares personalizados, gestión de errores centralizada | Diseño de microservicios, middlewares avanzados, métricas, tracing |
| **MySQL**                        | CRUD con SQL básico, conexión directa desde Node | JOINs complejos, migraciones, integridad referencial | Diseño de esquemas eficientes, tuning de consultas, replicación |
| **ORM / Query Builder**          | Uso básico de Sequelize o knex.js | Conoce relaciones, scopes, migraciones, validaciones | Personalización profunda del ORM, optimización, soporte multibase |
| **Control de versiones (Git)**  | Commit básico, ramas locales | GitFlow, pull requests, resolución de conflictos | Gestión de repos complejos, submódulos, workflows CI/CD |
| **Autenticación y sesiones**    | Login con bcrypt, sesiones simples | Middleware de autenticación, sesiones persistentes con MySQL | Seguridad avanzada (CSRF, session hijacking, expiración, OAuth2) |
| **Middlewares**                 | Usa `body-parser`, `cors`, etc. | Crea middlewares propios (auth, logging) | Middleware globales, manipulación de `req/res`, performance profiling |
| **Validaciones y Sanitización** | Valida en controladores con `express-validator` | Aplica validaciones centralizadas | Crea sistemas de validación desacoplados y consistentes |
| **Testing**                     | Pruebas manuales o unitarias básicas | Pruebas con Jest/Supertest, mocking | Pruebas completas (unitarias, integración, e2e), cobertura, TDD |
| **Estructura del proyecto**     | Script único (`server.js`) o mínima separación | Arquitectura MVC, separación de responsabilidades | Arquitecturas limpias, DDD, diseño hexagonal, escalabilidad |
| **Deploy / DevOps**             | Subir a Heroku o Railway manualmente | Automatiza con Docker básico y `.env`, PM2 | Configura entornos completos (CI/CD, Nginx, Docker Compose, monitoreo) |
| **Seguridad**                   | Entiende CORS y hashing de passwords | Aplica seguridad con `helmet`, rate limit, sanitización | Audita seguridad, implementa prácticas OWASP, CSP, políticas de cookies |
| **Documentación**               | README básico y comentarios en código | Documenta API en Postman o Swagger | Define estándares de documentación, guía de estilo para APIs |
| **Comunicación y equipo**       | Sigue instrucciones, pide ayuda frecuentemente | Participa en revisiones de código, propone soluciones | Lidera decisiones técnicas, mentoría, revisa y diseña arquitecturas |
| **Toma de decisiones**          | Ejecuta tareas asignadas | Evalúa opciones técnicas, refactoriza | Toma decisiones arquitectónicas, define estándares y procesos |

---

### 🔁 Resumen por Nivel

| Rol        | Enfoque Principal                                    |
|------------|-------------------------------------------------------|
| **Junior**     | Aprender fundamentos y escribir código funcional, aunque sea simple. |
| **Semi-Senior**| Aplicar buenas prácticas, modularizar, resolver problemas no triviales. |
| **Senior**     | Diseñar, escalar, mantener, liderar y asegurar calidad técnica y de equipo. |

---

# 
Perfecto. A continuación te presento una **guía de evaluación técnica para entrevistas** de desarrolladores backend que trabajen con **Express.js y MySQL**, basada en los niveles **Junior**, **Semi-Senior** y **Senior**.

Incluye:  
- **Ejes de evaluación** (áreas clave)  
- **Preguntas sugeridas** por nivel  
- **Criterios para identificar el nivel real del candidato**

---

# 🧪 Guía de Evaluación Técnica: Backend Express.js + MySQL

---

### 📊 Ejes de Evaluación

1. **JavaScript / Node.js**
2. **Express.js y SSR**
3. **MySQL / ORM**
4. **Autenticación / Seguridad**
5. **Estructura del proyecto / Arquitectura**
6. **Testing**
7. **DevOps y despliegue**
8. **Resolución de problemas**
9. **Soft Skills y colaboración**

---

### 🟢 NIVEL JUNIOR

#### 🧠 Expectativas:
- Conocimiento básico de JS, rutas, y operaciones CRUD.
- Puede seguir instrucciones y construir APIs funcionales.
- Usa Express y MySQL de forma directa o con ORM básico.

#### ✅ Preguntas sugeridas:
- ¿Cuál es la diferencia entre `==` y `===` en JavaScript?
- ¿Cómo configuras una ruta GET y POST en Express?
- ¿Qué es `res.send()` y `res.json()`?
- ¿Cómo harías una conexión a MySQL desde Node.js?
- ¿Cómo protegerías una contraseña en la base de datos?
- ¿Qué hace `express.static()`?
- ¿Qué herramienta usas para probar una API?

#### 🔎 Indicadores clave:
- Usa async/await con soltura
- Conoce `mysql2` o Sequelize a nivel básico
- Puede explicar el flujo de una petición desde el navegador al servidor

---

### 🟡 NIVEL SEMI-SENIOR

#### 🧠 Expectativas:
- Comprende middleware, validación, relaciones SQL, modularización.
- Ya resolvió errores comunes y entiende conceptos asincrónicos.
- Participa activamente en diseño técnico y revisiones de código.

#### ✅ Preguntas sugeridas:
- ¿Qué hace un middleware en Express? ¿Puedes darme un ejemplo?
- ¿Cómo modularizas las rutas y controladores?
- ¿Cuál es la diferencia entre `INNER JOIN` y `LEFT JOIN`?
- ¿Cómo implementarías autenticación con sesiones y cookies?
- ¿Cómo aplicarías validaciones centralizadas en formularios SSR?
- ¿Qué estructura tendría tu proyecto Express.js típico?
- ¿Cómo harías testing de una ruta POST que guarda datos en la base de datos?

#### 🔎 Indicadores clave:
- Habla con claridad sobre estructuras MVC o servicios
- Usa correctamente middlewares y validadores
- Comprende buenas prácticas de seguridad (bcrypt, helmet, CORS, etc.)
- Conoce Sequelize más allá del CRUD (relaciones, scopes)

---

### 🔴 NIVEL SENIOR

#### 🧠 Expectativas:
- Lidera arquitectura, optimiza código y base de datos.
- Es capaz de diseñar soluciones escalables.
- Participa en decisiones estratégicas del sistema y forma a otros.

#### ✅ Preguntas sugeridas:
- ¿Cómo diseñarías una arquitectura modular y escalable con Express?
- ¿Qué ventajas y desventajas tiene usar ORM vs SQL raw?
- ¿Cómo asegurarías una app SSR contra CSRF y XSS?
- ¿Qué consideraciones tomarías para escalar horizontalmente una app Express?
- ¿Cómo gestionarías sesiones en producción de forma segura?
- ¿Cómo implementarías un sistema de permisos basado en roles?
- ¿Qué opinas del patrón Repository con ORM como Sequelize?

#### 🔎 Indicadores clave:
- Usa patrones de diseño (factory, repository, singleton, etc.)
- Conoce migraciones, constraints, índices, optimización de queries
- Habla de arquitectura hexagonal, principios SOLID, DDD
- Menciona herramientas de monitoreo, testing e integración continua
- Tiene experiencia real liderando o diseñando soluciones

---

### 🧩 Evaluación Soft Skills (todos los niveles)

- ¿Cómo te aseguras de que tu código sea mantenible por otros?
- Cuéntame de un error técnico que cometiste y cómo lo resolviste.
- ¿Cómo respondes cuando te enfrentas a código legado?
- ¿Has hecho code reviews? ¿Qué buscas al revisar código ajeno?

---

### ✅ Sugerencia de Criterios de Evaluación (Plantilla tipo)

| Criterio                      | Peso | Puntaje Junior (1–3) | Semi (4–6) | Senior (7–10) |
|------------------------------|------|----------------------|------------|---------------|
| JavaScript + Node.js         | 20%  |                      |            |               |
| Express.js y Arquitectura    | 20%  |                      |            |               |
| MySQL / ORM                  | 20%  |                      |            |               |
| Seguridad / Autenticación    | 10%  |                      |            |               |
| Testing                      | 10%  |                      |            |               |
| Deploy y DevOps              | 10%  |                      |            |               |
| Soft Skills / Comunicación   | 10%  |                      |            |               |
| **Total (ajustado)**         | 100% |                      |            |               |

