# Tips para sentencias SQL

```js
    //Cual es una mejor consulta SQL?

    // Opcion 1
    const sql = `SELECT * FROM usuarios WHERE usuarios.nombre = ?`;
    return await connection.query(sql, [nombre]);

    // Opcion 2
   const sql = `SELECT * FROM usuarios WHERE usuarios.nombre = ${name}`;
    return await connection.query(sql);
```

La primera opción es **mucho mejor** y más segura que la segunda.

## **1. Primera opción (recomendada)**
```javascript
const sql = `SELECT * FROM usuarios WHERE usuarios.nombre = ?`;
return await connection.query(sql, [nombre]);
```

### **Ventajas:**
1. **Prevención de inyección SQL**:
   - Al usar `?` como marcador de posición y pasar los valores en un array (`[nombre]`), la librería de base de datos (como `mysql2` o `pg`) se encarga de escapar correctamente los valores, evitando la inyección SQL.
   - La inyección SQL es un ataque donde un usuario malintencionado puede manipular la consulta SQL para acceder, modificar o eliminar datos de la base de datos.

2. **Legibilidad y mantenibilidad**:
   - Separar la consulta SQL de los valores hace que el código sea más limpio y fácil de mantener.

3. **Compatibilidad**:
   - Este enfoque es compatible con la mayoría de las librerías de bases de datos en Node.js, como `mysql2`, `pg` (PostgreSQL), `sqlite3`, etc.

4. **Reutilización**:
   - Puedes reutilizar la misma consulta SQL con diferentes valores simplemente cambiando el array de parámetros.

---

## **2. Segunda opción (no recomendada)**
```javascript
const sql = `SELECT * FROM usuarios WHERE usuarios.nombre = ${name}`;
return await connection.query(sql);
```

### **Problemas:**
1. **Vulnerable a inyección SQL**:
   - Si `name` proviene de una entrada del usuario (por ejemplo, un formulario), un atacante podría manipular la consulta SQL. Por ejemplo:
     ```javascript
     const name = "'; DROP TABLE usuarios; --";
     const sql = `SELECT * FROM usuarios WHERE usuarios.nombre = ${name}`;
     ```
     Esto generaría la consulta:
     ```sql
     SELECT * FROM usuarios WHERE usuarios.nombre = ''; DROP TABLE usuarios; --';
     ```
     ¡Lo que eliminaría la tabla `usuarios`!

2. **Dificultad para mantener**:
   - Si necesitas cambiar la consulta o agregar más parámetros, el código se vuelve más complicado y propenso a errores.

3. **Problemas con tipos de datos**:
   - Si `name` es un string, debes agregar comillas manualmente (`'${name}'`), lo que aumenta el riesgo de errores y vulnerabilidades.

---

## **¿Por qué es importante prevenir la inyección SQL?**
La inyección SQL es uno de los ataques más comunes y peligrosos en aplicaciones web. Puede permitir a un atacante:
- Acceder a datos sensibles (contraseñas, información personal, etc.).
- Modificar o eliminar datos.
- Ejecutar comandos peligrosos en el servidor de base de datos.

---

## **Ejemplo completo con la primera opción**
El siguiente es un ejemplo completo de cómo usar la primera opción de manera segura:

```javascript
const mysql = require('mysql2/promise'); // Usando mysql2 para MySQL

async function getUserByName(nombre) {
    const connection = await mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'password',
        database: 'mi_base_de_datos'
    });

    try {
        const sql = `SELECT * FROM usuarios WHERE usuarios.nombre = ?`;
        const [rows] = await connection.query(sql, [nombre]);
        return rows;
    } catch (error) {
        console.error('Error en la consulta:', error);
        throw error;
    } finally {
        await connection.end(); // Cerrar la conexión
    }
}

// Uso
(async () => {
    const usuarios = await getUserByName('Juan');
    console.log(usuarios);
})();
```

---

## **Conclusión**
- **Usa siempre la primera opción**: `SELECT * FROM usuarios WHERE usuarios.nombre = ?` con parámetros separados.
- **Nunca concatenes valores directamente en la consulta SQL**: Esto expone tu aplicación a ataques de inyección SQL.
- **Usa librerías seguras**: Asegúrate de usar librerías como `mysql2`, `pg`, o `sqlite3` que soportan parámetros preparados.

La seguridad es fundamental en el desarrollo de aplicaciones, y prevenir la inyección SQL es una de las mejores prácticas más importantes.