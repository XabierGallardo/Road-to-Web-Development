# Bases de datos

## 1. Introduccion a las Bases de Datos

## Conceptos fundamentales

### 1. Base de Datos (Database)

Una **base de datos** es un conjunto organizado de datos almacenados electrónicamente. Está diseñada para **almacenar, organizar, y recuperar información** de manera eficiente, y puede contener desde datos simples (como nombres y direcciones) hasta información compleja (como registros financieros o información científica).

- **Ejemplos**: Un sistema de ventas podría tener una base de datos que almacena información sobre clientes, productos y transacciones.
- **Estructura**: Las bases de datos pueden organizarse en tablas, documentos, nodos, etc., dependiendo del modelo de datos que usen (relacional, NoSQL, gráfico, etc.).

---

### 2. Lenguaje de Base de Datos (Database Language)

Un **lenguaje de base de datos** es el **conjunto de instrucciones** utilizado para **crear, consultar, actualizar y eliminar** datos en una base de datos. Este lenguaje permite a los usuarios o aplicaciones interactuar con la base de datos y realizar operaciones en ella.

- **Ejemplo principal**: SQL (Structured Query Language) es el lenguaje más común para trabajar con bases de datos relacionales, permitiendo operaciones como:
    - **DDL** (Data Definition Language): Definición de estructuras, como la creación o eliminación de tablas.
    - **DML** (Data Manipulation Language): Manipulación de datos, como inserción, actualización, o eliminación de registros.
    - **DCL** (Data Control Language): Control de acceso y permisos en la base de datos.
    - **TCL** (Transaction Control Language): Gestión de transacciones para asegurar la integridad de los datos.

- **Ejemplos de lenguajes de base de datos**: SQL, MongoDB Query Language (MQL), Cypher (para bases de datos de grafos como Neo4j).

**Diferencia**: Una base de datos es el sistema de almacenamiento, mientras que el lenguaje de base de datos es el conjunto de comandos que permiten manipular esa base de datos.

---

### 3. Sistema de Gestión de Bases de Datos (DBMS - Database Management System)

Un **sistema de gestión de bases de datos (DBMS)** es el **software** que permite a los usuarios **crear, administrar y mantener bases de datos**. Actúa como un intermediario entre el usuario o la aplicación y la base de datos, y proporciona funcionalidades para:
- **Administrar datos**: Crear, leer, actualizar y eliminar datos.
- **Seguridad y control de acceso**: Asegurar que solo usuarios autorizados puedan acceder o modificar la base de datos.
- **Integridad de datos**: Mantener la exactitud y consistencia de los datos.
- **Eficiencia**: Optimizar el acceso y la manipulación de datos.
- **Transacciones**: Permitir transacciones ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad) para bases de datos relacionales.

- **Ejemplos de DBMS**: MySQL, PostgreSQL, Oracle Database, MongoDB, Microsoft SQL Server.

**Diferencia**: Un DBMS es el sistema que facilita la creación y gestión de bases de datos usando lenguajes de base de datos. La base de datos es el almacenamiento real, mientras que el DBMS es el software que permite interactuar con ella.

---

### 4. Administrador de Bases de Datos (DBA - Database Administrator)

Un **administrador de bases de datos (DBA)** es una **persona o equipo responsable de la gestión y mantenimiento** de las bases de datos dentro de una organización. El DBA se asegura de que el sistema de bases de datos funcione de manera óptima y segura.

- **Funciones del DBA**:
    - **Instalación y configuración**: Configuración inicial del DBMS y las bases de datos.
    - **Mantenimiento**: Realizar copias de seguridad, recuperación de datos, y asegurar la integridad de la información.
    - **Optimización y monitoreo**: Monitorear el rendimiento de las consultas y optimizar los tiempos de respuesta.
    - **Seguridad**: Gestionar el acceso de usuarios y proteger la base de datos contra amenazas.
    - **Actualizaciones**: Mantener el DBMS actualizado y aplicar parches de seguridad.
    - **Planificación de la capacidad**: Asegurar que el sistema de bases de datos pueda manejar el crecimiento de los datos y el aumento de la carga.

**Diferencia**: Mientras que el DBMS es el software, el administrador de bases de datos es la persona que usa este software para administrar, proteger y optimizar la base de datos.

---

### Resumen de las Diferencias

| Concepto                       | Descripción                                                                                           | Ejemplos                                          |
|--------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| **Base de Datos**              | Sistema organizado de almacenamiento de datos.                                                       | Tienda, sistema de ventas, registros médicos.     |
| **Lenguaje de Base de Datos**  | Conjunto de instrucciones para interactuar con la base de datos.                                     | SQL, MQL, Cypher.                                 |
| **Sistema de Gestión de BD**   | Software que permite crear, administrar y mantener bases de datos.                                   | MySQL, PostgreSQL, MongoDB, Oracle Database.      |
| **Administrador de BD (DBA)**  | Persona que gestiona, protege y optimiza la base de datos y el DBMS.                                 | DBA (rol en una organización o departamento).     |

En resumen:
- La **base de datos** es donde los datos están almacenados.
- El **lenguaje de base de datos** permite interactuar con esos datos.
- El **DBMS** es el software que facilita la interacción entre los datos y el usuario o aplicación.
- El **administrador de base de datos (DBA)** es la persona encargada de gestionar, proteger y optimizar el sistema de bases de datos.


___

## Bases de Datos, MySQL y administradores de BBDD como phpmyadmin
Las **bases de datos** son sistemas organizados para almacenar, gestionar y recuperar datos de manera estructurada y eficiente. Están diseñadas para que múltiples aplicaciones o usuarios puedan acceder y manipular grandes cantidades de información de manera rápida y segura.

Una **base de datos** permite:
1. **Almacenamiento persistente**: Los datos no se pierden cuando la aplicación o el sistema se apaga.
2. **Organización y búsqueda**: Permite almacenar datos en estructuras organizadas, lo que facilita la búsqueda y la manipulación.
3. **Control de acceso**: Asegura que solo usuarios autorizados puedan acceder o modificar la información.

### Tipos de Bases de Datos

1. **Bases de datos relacionales** (RDBMS): Organizan los datos en tablas y se basan en un modelo relacional. Usan SQL (Structured Query Language) para gestionar los datos. Ejemplos: **MySQL**, **PostgreSQL**, **Oracle**.
2. **Bases de datos NoSQL**: Usan diferentes modelos de datos, como documentos, gráficos o valores-clave, para manejar datos no estructurados o semiestructurados. Ejemplos: **MongoDB**, **Redis**, **Cassandra**.

---

## ¿Qué es MySQL?

**MySQL** es un sistema de gestión de bases de datos relacionales (RDBMS) de código abierto. Almacena los datos en **tablas** que pueden relacionarse entre sí mediante **claves** y **restricciones**. Está diseñado para manejar grandes volúmenes de datos y es compatible con SQL (Structured Query Language) como lenguaje de consultas para gestionar y manipular datos.

### Características de MySQL

- **Modelo relacional**: Los datos se organizan en tablas, cada una con filas (registros) y columnas (campos), que pueden relacionarse entre sí.
- **Lenguaje SQL**: Utiliza SQL para gestionar las operaciones de bases de datos.
- **Escalabilidad**: MySQL es muy adecuado para aplicaciones de cualquier tamaño, desde sitios web pequeños hasta aplicaciones grandes y de alto rendimiento.
- **Seguridad**: Ofrece opciones de autenticación, control de acceso y encriptación.
- **Rápido y confiable**: Está optimizado para manejar operaciones de lectura y escritura de manera rápida, lo cual es crucial para aplicaciones de alto tráfico.

### Ejemplo de Uso de MySQL

1. **Instalación de MySQL**: Puedes instalar MySQL en tu computadora o utilizarlo en un servidor.
2. **Crear una base de datos**:
   
   ```sql
   CREATE DATABASE tienda;
   ```

3. **Crear una tabla** en la base de datos "tienda":

   ```sql
   USE tienda;
   
   CREATE TABLE productos (
     id INT AUTO_INCREMENT PRIMARY KEY,
     nombre VARCHAR(50),
     precio DECIMAL(10, 2),
     cantidad INT
   );
   ```

   En este ejemplo:
   - Creamos una tabla llamada **productos**.
   - **id** es un campo entero con **AUTO_INCREMENT** y **PRIMARY KEY** para que cada producto tenga un identificador único.
   - **nombre**, **precio**, y **cantidad** son los datos de cada producto.

4. **Insertar datos** en la tabla:

   ```sql
   INSERT INTO productos (nombre, precio, cantidad) VALUES 
   ('Camisa', 20.50, 100),
   ('Pantalón', 35.75, 50);
   ```

5. **Consultar datos** en la tabla:

   ```sql
   SELECT * FROM productos;
   ```

   Esta consulta selecciona todos los registros de la tabla **productos**.

MySQL se usa frecuentemente en aplicaciones web y sistemas que requieren un backend relacional, como sistemas de gestión empresarial, e-commerce y plataformas de redes sociales.

---

## Administradores de Bases de Datos (DBMS)

Los administradores de bases de datos o DBMS (Database Management Systems) son programas que permiten **gestionar y administrar** una base de datos. Facilitan el acceso a los datos, la modificación de registros, la creación de estructuras, el control de acceso y las operaciones de backup y recuperación.

### Funciones de un DBMS

- **Creación y administración de bases de datos**: Permite crear, modificar y eliminar bases de datos.
- **Control de acceso**: Define qué usuarios o aplicaciones pueden acceder a qué datos y qué operaciones pueden realizar.
- **Integridad de datos**: Asegura que los datos permanezcan correctos y coherentes.
- **Gestión de consultas**: Permite realizar consultas de datos con SQL.
- **Recuperación y respaldo de datos**: Facilita la recuperación de datos en caso de fallo del sistema.

### Ejemplo de DBMS: MySQL

MySQL es un DBMS que ofrece funcionalidades de creación, administración y manipulación de bases de datos. Permite crear bases de datos, definir permisos de usuario y realizar consultas SQL. Es uno de los DBMS más usados por su facilidad de uso y rendimiento.

---

## ¿Qué es phpMyAdmin?

**phpMyAdmin** es una herramienta de administración de bases de datos MySQL que permite a los usuarios **gestionar bases de datos desde una interfaz gráfica web**. Está desarrollado en PHP y es muy popular por su facilidad de uso y por ser de código abierto.

### Características de phpMyAdmin

- **Interfaz gráfica**: Permite a los usuarios interactuar con las bases de datos sin necesidad de escribir consultas SQL complejas.
- **Operaciones CRUD**: Permite crear, leer, actualizar y eliminar registros en una base de datos.
- **Gestión de usuarios y permisos**: Posibilita la administración de usuarios y sus permisos de acceso.
- **Exportación e importación de datos**: Facilita la exportación de bases de datos a formatos como SQL, CSV y otros, y permite importar datos fácilmente.
- **Consultas SQL personalizadas**: Incluye un área donde los usuarios pueden escribir consultas SQL personalizadas.

### Ejemplo de Uso de phpMyAdmin

Imaginemos que queremos crear una base de datos y una tabla en phpMyAdmin:

1. **Crear una base de datos**:
   - Inicia sesión en phpMyAdmin.
   - En la pantalla de inicio, haz clic en "Nueva" en el panel izquierdo.
   - Ingresa el nombre de la base de datos, por ejemplo, "tienda", y selecciona el juego de caracteres deseado (por ejemplo, `utf8mb4`).
   - Haz clic en "Crear".

2. **Crear una tabla**:
   - Selecciona la base de datos "tienda" en el panel izquierdo.
   - Haz clic en "Crear tabla" y escribe el nombre de la tabla, como "productos".
   - Define los campos: "id" (tipo `INT`, marcado como `AUTO_INCREMENT` y `PRIMARY KEY`), "nombre" (tipo `VARCHAR`), "precio" (tipo `DECIMAL`) y "cantidad" (tipo `INT`).
   - Haz clic en "Guardar".

3. **Insertar datos en la tabla**:
   - Selecciona la tabla "productos".
   - Haz clic en "Insertar".
   - Completa los campos: por ejemplo, **nombre** = "Camisa", **precio** = 20.50, **cantidad** = 100.
   - Haz clic en "Continuar".

4. **Consultar datos en la tabla**:
   - Selecciona la tabla "productos".
   - Haz clic en "Examinar" para ver todos los registros de la tabla.

Gracias a su interfaz gráfica, phpMyAdmin permite realizar estas operaciones sin tener que escribir SQL directamente, aunque también ofrece la opción de ejecutar consultas SQL personalizadas.

---

## Resumen

- **Base de datos**: Un sistema de almacenamiento organizado que permite almacenar y recuperar datos eficientemente.
- **MySQL**: Es un sistema de gestión de bases de datos relacionales que usa SQL para gestionar y manipular datos en una estructura de tablas. Es muy usado en aplicaciones web y empresariales.
- **DBMS (Database Management System)**: Software que administra y organiza bases de datos. Facilita la creación, acceso y manejo de datos de forma segura y eficiente.
- **phpMyAdmin**: Es una herramienta basada en PHP que facilita la gestión de bases de datos MySQL mediante una interfaz gráfica web. Permite realizar operaciones CRUD, administrar usuarios y ejecutar consultas SQL.


___



## 2. Guión Diseño de Bases de Datos y Modelo Entidad-Relación

### Estructura de la Clase
1. **Introducción a las bases de datos**
2. **Conceptos fundamentales del diseño de bases de datos**
3. **Modelo Entidad-Relación**
4. **Ejemplo Práctico: Diseño de una base de datos para una biblioteca**
5. **Ejercicio de práctica y cierre**

---

### 1. **Introducción a las bases de datos**

#### a. ¿Qué es una base de datos?

Una **base de datos** es una colección organizada de datos estructurados que se almacena electrónicamente en un sistema computacional. Las bases de datos permiten almacenar, organizar, gestionar y recuperar información de manera eficiente.

#### b. Bases de datos relacionales

Las bases de datos relacionales organizan los datos en **tablas** (similares a hojas de cálculo), donde cada tabla representa una entidad o concepto. Las **bases de datos relacionales** son las más comunes y están basadas en el modelo de relaciones (o relaciones entre entidades).

*Una entidad es un objeto del mundo real que se representa en la base de datos como una tabla. Cada entidad tiene sus propios atributos que se representan como columnas en la tabla.* Las entidades son la base sobre la cual se construye la estructura de la base de datos y se relacionan entre sí para representar la información de manera más completa y organizada.

En una base de datos MySQL, una **tabla es una estructura que almacena datos de manera organizada en filas y columnas. Cada tabla está formada por columnas que representan los campos de la tabla y filas que contienen los registros de datos.**


- **Ejemplos de bases de datos relacionales**: MySQL, PostgreSQL, Oracle.

**Ejemplo**: Supongamos que queremos almacenar datos de una biblioteca. Necesitaremos varias tablas para representar:
   - Libros
   - Autores
   - Usuarios
   - Préstamos

Cada tabla contendrá información específica sobre una entidad y estará relacionada con las demás según sea necesario.

---

### 2. **Conceptos Fundamentales del Diseño de Bases de Datos**

#### a. ¿Qué es el diseño de bases de datos?

El **diseño de una base de datos** es el proceso de planificar y estructurar una base de datos para cumplir con los requisitos de almacenamiento, eficiencia, integridad y seguridad de los datos.

#### b. Pasos del diseño de una base de datos

1. **Recopilación de Requisitos**: Identificar los datos que deben almacenarse y cómo se relacionan entre sí.
2. **Identificación de Entidades y Atributos**: Determinar las entidades principales y los detalles que necesita cada una.
3. **Diseño del Modelo Entidad-Relación**: Crear un modelo que represente las entidades y las relaciones entre ellas.
4. **Normalización**: Organizar las tablas para reducir la redundancia y mejorar la eficiencia.
5. **Implementación**: Crear la base de datos en un sistema de gestión de bases de datos (como MySQL).

#### c. Entidades y Atributos

- **Entidad**: Un objeto o concepto sobre el cual queremos almacenar información.
- **Atributo**: Las propiedades o características de una entidad.

**Ejemplo**:
   - Entidad: **Libro**
   - Atributos: Título, Autor, Año de Publicación, ISBN, Género.

#### d. Claves Primarias y Foráneas

- **Clave Primaria**: Un identificador único para cada registro en una tabla.
- **Clave Foránea**: Un campo que vincula una tabla con otra, formando una relación.

**Ejemplo**:
   - En una tabla `Libro`, el `ISBN` puede actuar como clave primaria.
   - En una tabla `Prestamo`, el campo `usuario_id` será una clave foránea que hace referencia a la tabla `Usuario`.

---

### 3. **Modelo Entidad-Relación (ER)** 

El **modelo entidad-relación (ER)** es una herramienta visual utilizada en el diseño de bases de datos para representar las entidades, sus atributos y las relaciones entre ellas. Se representa a través de un **diagrama ER**.

#### a. Componentes de un Diagrama ER

1. **Entidades**: Representadas por rectángulos. Ejemplo: **Libro**, **Autor**, **Usuario**.
2. **Atributos**: Representados por óvalos y conectados a las entidades. Ejemplo: Para `Libro`, los atributos pueden ser **título** y **fecha de publicación**.
3. **Relaciones**: Representadas por rombos y conectadas a las entidades involucradas. Ejemplo: Un `Usuario` puede tener una relación de `Préstamo` con el `Libro`.

#### b. Tipos de relaciones

1. **Uno a Uno (1:1)**: Cada registro de una entidad se relaciona con un único registro de otra entidad.
2. **Uno a Muchos (1:N)**: Un registro de una entidad se relaciona con varios registros de otra entidad.
3. **Muchos a Muchos (M:N)**: Varios registros de una entidad se relacionan con varios registros de otra entidad.

**Ejemplo**:
   - Relación 1:N: Un **autor** puede escribir varios **libros** (un autor tiene varios libros, pero cada libro tiene un solo autor).
   - Relación M:N: Un **libro** puede ser prestado a varios **usuarios**, y un **usuario** puede tomar prestados varios **libros**.

#### c. Ejemplo del modelo ER en una biblioteca

1. **Entidad `Usuario`**
   - Atributos: `id_usuario`, `nombre`, `fecha_registro`
2. **Entidad `Libro`**
   - Atributos: `id_libro`, `título`, `año_publicacion`, `genero`
3. **Entidad `Prestamo`**
   - Atributos: `id_prestamo`, `fecha_prestamo`, `fecha_devolucion`

Relaciones:
   - Un `Usuario` puede tener muchos `Préstamos`.
   - Un `Préstamo` está asociado a un único `Libro` y un `Usuario`.

---

### 4. **Ejemplo Práctico: Diseño de una base de datos para una biblioteca** 

#### Paso 1: Identificar Entidades y Atributos

1. **Usuario**
   - `id_usuario` (Clave Primaria)
   - `nombre`
   - `email`
   - `fecha_registro`
2. **Libro**
   - `id_libro` (Clave Primaria)
   - `titulo`
   - `autor`
   - `año_publicacion`
   - `genero`
3. **Préstamo**
   - `id_prestamo` (Clave Primaria)
   - `id_usuario` (Clave Foránea que referencia `Usuario`)
   - `id_libro` (Clave Foránea que referencia `Libro`)
   - `fecha_prestamo`
   - `fecha_devolucion`

#### Paso 2: Crear el Diagrama ER

**Instrucciones**:
   - Dibujar un rectángulo para cada entidad.
   - Añadir óvalos conectados a cada entidad para representar sus atributos.
   - Crear rombos entre entidades para representar las relaciones.

#### Paso 3: Implementación en SQL (si es posible en la clase)

```sql
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE Usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(100),
  fecha_registro DATE
);

CREATE TABLE Libro (
  id_libro INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255),
  autor VARCHAR(100),
  año_publicacion YEAR,
  genero VARCHAR(50)
);

CREATE TABLE Prestamo (
  id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT,
  id_libro INT,
  fecha_prestamo DATE,
  fecha_devolucion DATE,
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
  FOREIGN KEY (id_libro) REFERENCES Libro(id_libro)
);
```

---

### 5. **Ejercicio de práctica y cierre**

#### Actividad:

1. Formar equipos de 2-3 personas.
2. Proveer un caso práctico (por ejemplo, una tienda en línea) y pedir a los equipos que:
   - Identifiquen las entidades y los atributos.
   - Definan las relaciones entre las entidades.
   - Dibujen un diagrama ER para el caso proporcionado.

#### Discusión y Cierre:

- Revisar los diagramas creados por los equipos y discutir posibles mejoras.
- Resolver dudas y recordar la importancia de un buen diseño de bases de datos para asegurar la eficiencia y escalabilidad.

**Resumen**:
   - Los diagramas ER son esenciales para planificar bases de datos y evitar errores de diseño.
   - La implementación adecuada en SQL asegura la integridad y eficiencia de la base de datos.
