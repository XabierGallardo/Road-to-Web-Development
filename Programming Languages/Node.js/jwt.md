## **¿Qué es JWT (JSON Web Token)?**  
JWT (JSON Web Token) es un estándar para la autenticación y transmisión segura de información entre partes como un objeto JSON firmado digitalmente. Se usa principalmente en autenticación y autorización en aplicaciones web y APIs.

🔹 **Características principales de JWT:**  
- **Autenticación sin estado:** No necesita sesiones en el servidor.
- **Firmado digitalmente:** Usa algoritmos como HMAC o RSA.
- **Compacto y seguro:** Se puede enviar en headers HTTP o como parámetros en URLs.

---

## **Estructura de un JWT**  
Un JWT está compuesto por tres partes codificadas en Base64 y separadas por puntos (`.`):

```
HEADER.PAYLOAD.SIGNATURE
```

### **1️⃣ Header (Encabezado)**  
Contiene metadatos sobre el algoritmo de firma. Ejemplo:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
Este header indica que se usa **HMAC SHA-256** para firmar el token.

---

### **2️⃣ Payload (Cuerpo del Token)**  
Contiene la información que se quiere transmitir. Ejemplo de un payload típico:
```json
{
  "sub": "1234567890",
  "name": "Juan Pérez",
  "iat": 1712345678,
  "exp": 1712349678
}
```
🔹 **Campos comunes en el payload:**
- `sub` → Identificador del usuario.
- `iat` → Fecha de emisión (**issued at**).
- `exp` → Fecha de expiración (**expiration**).

⚠️ **Nota:** No debe contener información sensible, ya que el JWT puede ser decodificado fácilmente.

---

### **3️⃣ Signature (Firma)**
Se genera con el siguiente proceso:
```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  SECRET_KEY
)
```
Esta firma garantiza la integridad del token y evita modificaciones maliciosas.

---

## **Generar una Clave Secreta JWT para Variables de Entorno**  

### **🔹 Opción 1: Generar una clave secreta con OpenSSL**
Ejecuta en la terminal:
```sh
openssl rand -base64 32
```
Esto generará una clave aleatoria segura. Ejemplo de salida:
```
Xh+q1pBr9hJ6sE68YkR5/FtNl0V+Zdm68ZaJTxQ/gK0=
```
Esta clave será usada para firmar los JWTs.

---

### **🔹 Opción 2: Generar una clave secreta con Node.js**
Si tienes Node.js instalado, ejecuta:
```js
require('crypto').randomBytes(32).toString('hex');
```
Salida:
```
f4c8b6e3d1a2e5f05a87f1c3e5e35f08f7d6b1c3a2f5e1d4b6c8e3d1a2e5f07c
```

---

## **Configurar la Clave en Variables de Entorno**  
Una vez generada la clave, se debe almacenar de forma segura.  
Si el proyecto usa **dotenv**, agrega la clave en el archivo `.env`:

```
JWT_SECRET=f4c8b6e3d1a2e5f05a87f1c3e5e35f08f7d6b1c3a2f5e1d4b6c8e3d1a2e5f07c
```

En Node.js, se puede acceder a la clave con:
```js
require('dotenv').config();
const jwtSecret = process.env.JWT_SECRET;
console.log(jwtSecret);
```

---

## **Ejemplo de Uso de JWT en Node.js (Express)**  

### **1️⃣ Instalar jsonwebtoken**
```sh
npm install jsonwebtoken dotenv
```

### **2️⃣ Crear y verificar JWT en Express**
```js
require('dotenv').config();
const jwt = require('jsonwebtoken');
const express = require('express');
const app = express();

const SECRET_KEY = process.env.JWT_SECRET;

// Generar un token
app.post('/login', (req, res) => {
    const user = { id: 1, username: "juanperez" };
    const token = jwt.sign(user, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
});

// Middleware para verificar el token
const verifyToken = (req, res, next) => {
    const token = req.headers['authorization'];
    if (!token) return res.status(403).json({ error: "Token requerido" });

    jwt.verify(token.split(" ")[1], SECRET_KEY, (err, decoded) => {
        if (err) return res.status(403).json({ error: "Token inválido" });
        req.user = decoded;
        next();
    });
};

// Ruta protegida
app.get('/dashboard', verifyToken, (req, res) => {
    res.json({ message: `Bienvenido, ${req.user.username}` });
});

app.listen(3000, () => console.log('Servidor en http://localhost:3000'));
```

---

## **Conclusión**
✅ **JWT** permite autenticación sin estado en APIs.  
✅ **Las claves secretas** deben ser seguras y almacenadas en variables de entorno.  
✅ **Express + JWT** permite gestionar sesiones sin usar bases de datos para cada solicitud.  

🔒 **Siempre mantener la clave secreta protegida y no exponerla en repositorios públicos.** 🚀