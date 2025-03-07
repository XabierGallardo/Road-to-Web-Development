# 6 formas de conectarse a una BBDD MySQL en Express.js

En una aplicación de **Express.js**, hay múltiples formas de conectarse a una base de datos **MySQL**:

---

### 1. **Usando el módulo `mysql`**
El módulo `mysql` es una de las opciones más comunes para conectarse a MySQL en Node.js. Es ligero y fácil de configurar, pero no soporta Promesas de manera nativa.

#### Instalación:
```bash
npm install mysql
```

#### Ejemplo:
```javascript
const mysql = require('mysql');

// Crear una conexión
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'my_database',
});

// Conectar a la base de datos
connection.connect(err => {
  if (err) {
    console.error('Error al conectar a MySQL:', err);
    return;
  }
  console.log('Conexión exitosa a MySQL');
});

// Realizar una consulta
connection.query('SELECT * FROM users', (err, results) => {
  if (err) throw err;
  console.log('Datos:', results);
});

// Cerrar la conexión
connection.end();
```

**Ventajas:**
- Simple y directo para casos de uso básicos.
- Permite conexiones persistentes o reutilizables.

**Desventajas:**
- No soporta Promesas de manera nativa (requiere callbacks o envolver en Promesas).
- Más propenso a problemas de rendimiento en aplicaciones de gran escala debido a su enfoque sin conexión por defecto.

---

### 2. **Usando el módulo `mysql2`**
`mysql2` es una versión mejorada y moderna del módulo `mysql`. Tiene soporte nativo para Promesas y es compatible con la mayoría de los métodos de `mysql`.

#### Instalación:
```bash
npm install mysql2
```

#### Ejemplo:
Con Promesas:
```javascript
const mysql = require('mysql2/promise');

// Crear conexión usando Promesas
(async () => {
  const connection = await mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'my_database',
  });

  console.log('Conexión exitosa a MySQL');

  const [rows] = await connection.execute('SELECT * FROM users');
  console.log('Datos:', rows);

  await connection.end();
})();
```

**RECOMENDADO / Con un pool de conexiones:**
```javascript
const mysql = require('mysql2/promise');

// Crear un pool de conexiones
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'my_database',
});

// Consultas usando el pool
(async () => {
  const [rows] = await pool.execute('SELECT * FROM users');
  console.log('Datos:', rows);
})();
```

**Ventajas:**
- Soporte nativo para Promesas, ideal para trabajar con `async/await`.
- Compatible con `mysql` para una fácil migración.
- Admite conexiones individuales y pools de conexiones.

**Desventajas:**
- Dependencia de terceros (aunque ampliamente utilizada y bien mantenida).

---

### 3. **Usando un ORM: `Sequelize`**
`Sequelize` es un **ORM (Object Relational Mapper)** que permite interactuar con bases de datos relacionales, incluido MySQL, utilizando una abstracción basada en modelos. Es ideal para aplicaciones que necesitan un enfoque estructurado y soporta múltiples bases de datos.

#### Instalación:
```bash
npm install sequelize mysql2
```

#### Ejemplo:
```javascript
const { Sequelize, DataTypes } = require('sequelize');

// Configurar Sequelize
const sequelize = new Sequelize('my_database', 'root', 'password', {
  host: 'localhost',
  dialect: 'mysql',
});

// Definir un modelo
const User = sequelize.define('User', {
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

// Conectar y sincronizar
(async () => {
  try {
    await sequelize.authenticate();
    console.log('Conexión exitosa a MySQL con Sequelize');

    await sequelize.sync(); // Sincronizar modelos con la base de datos

    // Crear un usuario
    const newUser = await User.create({ name: 'John Doe', email: 'john@example.com' });
    console.log('Usuario creado:', newUser.toJSON());

    // Consultar usuarios
    const users = await User.findAll();
    console.log('Usuarios:', users.map(user => user.toJSON()));
  } catch (error) {
    console.error('Error:', error);
  } finally {
    await sequelize.close();
  }
})();
```

**Ventajas:**
- Abstracción de la base de datos mediante modelos.
- Soporte para múltiples bases de datos (MySQL, PostgreSQL, SQLite, etc.).
- Incluye herramientas avanzadas como validaciones, relaciones entre tablas, y migraciones.

**Desventajas:**
- Sobrecarga de rendimiento comparado con el uso directo de `mysql` o `mysql2`.
- Mayor complejidad inicial para configurar y aprender.

---

### Comparación rápida

| Característica          | `mysql`      | `mysql2`       | `Sequelize`          |
|-------------------------|--------------|----------------|----------------------|
| **Promesas nativas**    | No           | Sí             | Sí                   |
| **Pools de conexiones** | Sí           | Sí             | Sí                   |
| **Complejidad**         | Baja         | Baja           | Media/Alta           |
| **Flexibilidad**        | Alta         | Alta           | Media (por abstracción) |
| **Casos de uso**        | Básicos      | Intermedios    | Avanzados (con ORM)  |

### Conclusión
- Usa `mysql` si necesitas simplicidad y no requieres Promesas.
- Usa `mysql2` para aplicaciones modernas que aprovechen `async/await`.
- Usa `Sequelize` si deseas trabajar con una capa de abstracción basada en modelos o si tu aplicación necesita manejar relaciones complejas.


---


Además de las opciones más populares como `mysql`, `mysql2`, y `Sequelize`, existen otros métodos para conectarse a una base de datos MySQL en aplicaciones de **Express.js**. Aquí hay tres alternativas adicionales:

### 4. **Usando `TypeORM`**
`TypeORM` es otro **ORM (Object Relational Mapper)**, diseñado para trabajar con múltiples bases de datos relacionales, incluyendo MySQL. Está escrito en TypeScript, lo que lo convierte en una excelente opción para proyectos modernos que utilizan este lenguaje.

#### Instalación:
```bash
npm install typeorm mysql2
```

#### Ejemplo:
```javascript
const { DataSource } = require('typeorm');

// Configuración de TypeORM
const AppDataSource = new DataSource({
  type: 'mysql',
  host: 'localhost',
  port: 3306,
  username: 'root',
  password: 'password',
  database: 'my_database',
  synchronize: true, // No usar en producción
  logging: false,
  entities: [User], // Modelos
});

// Definición de una entidad
const User = AppDataSource.getRepository('User').createEntitySchema({
  name: 'User',
  columns: {
    id: {
      primary: true,
      type: 'int',
      generated: true,
    },
    name: {
      type: 'varchar',
    },
    email: {
      type: 'varchar',
    },
  },
});

// Inicializar y trabajar con TypeORM
(async () => {
  await AppDataSource.initialize();
  console.log('Conexión exitosa a MySQL con TypeORM');

  // Crear un usuario
  const user = await AppDataSource.getRepository(User).save({ name: 'John', email: 'john@example.com' });
  console.log('Usuario creado:', user);

  // Consultar usuarios
  const users = await AppDataSource.getRepository(User).find();
  console.log('Usuarios:', users);
})();
```

**Ventajas:**
- Soporte avanzado para relaciones entre tablas, validaciones, y migraciones.
- Integración nativa con TypeScript.
- Buenas herramientas para proyectos grandes.

**Desventajas:**
- Más complejo que `Sequelize`.
- Puede ser excesivo para proyectos pequeños.

---

### 5. **Usando `Knex.js`**
`Knex.js` es un **query builder** para Node.js que funciona con varias bases de datos, incluyendo MySQL. Proporciona una capa de abstracción para construir consultas SQL de forma programática, sin la necesidad de usar un ORM completo.

---

### 6. **Usando `Prisma`**
`Prisma` es un ORM moderno que se enfoca en proporcionar una experiencia de desarrollo fluida. Es altamente opinado y genera modelos de base de datos automáticamente a partir de un esquema definido.


---

### Comparativa adicional:

| Herramienta | Abstracción | Relaciones | Complejidad | Escalabilidad | Soporte para MySQL |
|-------------|-------------|------------|-------------|---------------|--------------------|
| `TypeORM`   | Alta        | Sí         | Alta        | Alta          | Excelente          |
| `Knex.js`   | Baja        | No         | Media       | Alta          | Excelente          |
| `Prisma`    | Muy alta    | Sí         | Media       | Alta          | Excelente          |
