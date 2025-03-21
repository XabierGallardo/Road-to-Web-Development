# **Diseño de Base de Datos en MySQL para una Aplicación TO-DO List Multiusuario**  
En este documento explicaremos **cómo diseñar y crear una base de datos en MySQL** para una aplicación **TO-DO List multiusuario**. Incorporando los conceptos fundamentales, desde el **modelo de datos**, las **relaciones entre tablas**, y cómo implementarlas paso a paso en MySQL.  

---

# **1️⃣ Conceptualización del Diseño**  
### **¿Qué queremos construir?**
Necesitamos una **aplicación de lista de tareas** donde **varios usuarios puedan gestionar múltiples tablones** (**boards**), y dentro de cada tablón, puedan crear múltiples **tareas** (**tasks**).  

### **📌 Requisitos del Sistema**  
✅ Un usuario puede registrarse y tener su propia cuenta.  
✅ Un usuario puede crear **múltiples tablones** (**boards**).  
✅ Cada **board** puede contener **múltiples tareas** (**tasks**).  
✅ Cada tarea tendrá un estado (pendiente, en progreso, completada).  

---

# **2️⃣ Diseño Relacional**  

## **Tablas y Relaciones**  

En una base de datos relacional, organizamos la información en **tablas** que se conectan mediante **relaciones**.  

🔹 **Usuarios (`users`)** → Cada usuario tiene su cuenta.  
🔹 **Tablones (`boards`)** → Cada usuario puede tener múltiples tablones.  
🔹 **Tareas (`tasks`)** → Cada tablón puede contener múltiples tareas.  

Esto nos lleva al siguiente modelo:

```
users  (1) ──── (N) boards  (1) ──── (N) tasks
```

Donde:  
- Un **usuario** puede tener **muchos tablones**.  
- Un **tablón** puede contener **muchas tareas**.  

### **📌 ¿Qué es una Relación en Bases de Datos?**
Las **relaciones** permiten **conectar** datos entre diferentes tablas. Se hacen con **claves foráneas (FOREIGN KEY)** que establecen vínculos entre las filas de diferentes tablas.  

---

# **3️⃣ Creación de la Base de Datos en MySQL**  

### **Paso 1: Crear la Base de Datos**
Ejecuta el siguiente comando en MySQL:

```sql
CREATE DATABASE todo_app;
USE todo_app;
```

---

## **4️⃣ Creación de Tablas con Relaciones**
### **📌 Tabla `users` (Usuarios)**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
- `id` → Identificador único del usuario.  
- `username` y `email` → Deben ser únicos.  
- `password_hash` → Se almacena la contraseña cifrada.  
- `created_at` → Guarda la fecha de registro.  

---

### **📌 Tabla `boards` (Tablones de un usuario)**
```sql
CREATE TABLE boards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```
- `user_id` → Clave foránea que relaciona con la tabla `users`.  
- `ON DELETE CASCADE` → Si un usuario es eliminado, también se eliminan sus tablones.  

---

### **📌 Tabla `tasks` (Tareas en un tablón)**
```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    board_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (board_id) REFERENCES boards(id) ON DELETE CASCADE
);
```
- `board_id` → Clave foránea que conecta la tarea con un tablón.  
- `status` → Indica si la tarea está pendiente, en progreso o completada.  
- `ON DELETE CASCADE` → Si un tablón es eliminado, sus tareas también se eliminan.  

---

# **5️⃣ Insertar Datos de Prueba**
Después de crear las tablas, podemos insertar algunos datos de prueba.

### **📌 Insertar Usuarios**
```sql
INSERT INTO users (username, email, password_hash) 
VALUES ('juanperez', 'juan@example.com', 'hashedpassword123');
```

### **📌 Insertar un Tablón para el Usuario 1**
```sql
INSERT INTO boards (user_id, name) VALUES (1, 'Trabajo');
```

### **📌 Insertar Tareas en el Tablón 1**
```sql
INSERT INTO tasks (board_id, title, description, due_date, status) 
VALUES 
(1, 'Revisar emails', 'Leer correos importantes', '2024-03-10', 'pending'),
(1, 'Enviar reporte', 'Preparar informe mensual', '2024-03-11', 'in_progress');
```

---

# **6️⃣ Consultas Útiles**
### **📌 Obtener todos los usuarios**
```sql
SELECT * FROM users;
```

### **📌 Obtener los tablones de un usuario**
```sql
SELECT * FROM boards WHERE user_id = 1;
```

### **📌 Obtener todas las tareas de un tablón**
```sql
SELECT * FROM tasks WHERE board_id = 1 ORDER BY due_date;
```

### **📌 Contar el número de tareas pendientes por tablón**
```sql
SELECT board_id, COUNT(*) AS total_pendientes 
FROM tasks WHERE status = 'pending' 
GROUP BY board_id;
```

---

# **7️⃣ Optimización y Seguridad**
### **Índices para Mejorar la Velocidad**
```sql
CREATE INDEX idx_user_id ON boards(user_id);
CREATE INDEX idx_board_id ON tasks(board_id);
```

### **Evitar Eliminaciones Accidentales**
Si queremos evitar que un usuario elimine accidentalmente un tablón con todas sus tareas, podemos **remover `ON DELETE CASCADE`** y manejar las eliminaciones manualmente.

---

# **8️⃣ Conclusión**
✅ **Hemos construido una base de datos escalable y eficiente** para una aplicación TO-DO List multiusuario.  
✅ **Hemos definido relaciones entre las tablas** utilizando claves foráneas (`FOREIGN KEY`).  
✅ **Hemos aprendido a insertar y consultar datos** de manera efectiva.  


---


# Cómo hacer si la relacion fuera *users 1 - 1 boards 1 - 1 tasks*?
Si la relación cambia a que **un usuario solo puede tener un único tablón (`board`)** y **cada tablón solo puede contener una única tarea (`task`)**, entonces el diseño de la base de datos debe modificarse.  

---

## **1️⃣ Nueva Conceptualización del Modelo**  

Ahora tenemos una estructura más simple:  

- **Usuarios (`users`)** → Cada usuario tiene **un solo tablón**.  
- **Tablones (`boards`)** → Cada tablón pertenece a **un único usuario** y contiene **una sola tarea**.  
- **Tareas (`tasks`)** → Cada tablón tiene **una única tarea**.  

📌 **Diagrama de la Relación**:  
```
users  (1) ──── (1) boards  (1) ──── (1) tasks
```

En este nuevo modelo:  
- **Cada usuario puede tener solo un tablón** (relación 1 a 1).  
- **Cada tablón solo puede contener una única tarea** (relación 1 a 1).  

---

## **2️⃣ Creación de las Tablas en MySQL**  

### **📌 Tabla `users` (Usuarios)**  
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
- `id` → Identificador único del usuario.  
- `username` y `email` → Deben ser únicos.  
- `password_hash` → Se almacena la contraseña cifrada.  

---

### **📌 Tabla `boards` (Tablones de los usuarios)**  
```sql
CREATE TABLE boards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE, 
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```
🔹 **¿Qué cambios hay aquí?**  
- `user_id` es `UNIQUE` → **Cada usuario puede tener solo un tablón**.  
- `ON DELETE CASCADE` → Si el usuario se elimina, su tablón también.  

---

### **📌 Tabla `tasks` (Tareas de los tablones)**  
```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    board_id INT NOT NULL UNIQUE, 
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE,
    status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (board_id) REFERENCES boards(id) ON DELETE CASCADE
);
```
🔹 **¿Qué cambios hay aquí?**  
- `board_id` es `UNIQUE` → **Cada tablón puede tener solo una tarea**.  
- `ON DELETE CASCADE` → Si el tablón se elimina, la tarea también.  

---

## **3️⃣ Insertar Datos de Prueba**  
### **📌 Insertar un Usuario**
```sql
INSERT INTO users (username, email, password_hash) 
VALUES ('juanperez', 'juan@example.com', 'hashedpassword123');
```

### **📌 Insertar un Tablón para el Usuario**
```sql
INSERT INTO boards (user_id, name) 
VALUES (1, 'Mi Tablón Personal');
```

### **📌 Insertar una Tarea en el Tablón**
```sql
INSERT INTO tasks (board_id, title, description, due_date, status) 
VALUES (1, 'Comprar café', 'Ir al supermercado por café', '2024-03-10', 'pending');
```

---

## **4️⃣ Consultas Útiles**
### **📌 Obtener información completa de un usuario, su tablón y su tarea**
```sql
SELECT users.username, boards.name AS board_name, tasks.title AS task_title, tasks.status
FROM users
JOIN boards ON users.id = boards.user_id
JOIN tasks ON boards.id = tasks.board_id
WHERE users.id = 1;
```

---

## **5️⃣ Conclusión**
✅ **Rediseñamos el modelo de datos para que haya una relación 1 a 1** en cada nivel.  
✅ **Aseguramos la unicidad de las relaciones** con `UNIQUE`.  
✅ **Creamos restricciones `FOREIGN KEY` con `ON DELETE CASCADE`** para mantener la integridad.  

🚀 **Este modelo es más restrictivo pero adecuado si solo permitimos un único tablón y tarea por usuario.**
