# API, API Rest, librerias, bibliotecas y frameworks


## 🔷 **¿Qué es una API?**
**API** (Application Programming Interface) es un conjunto de reglas y protocolos que permite que diferentes aplicaciones se comuniquen entre sí.

**Ejemplo simple:** Piensa en un restaurante:
- **Tú** = Cliente (aplicación)
- **Mesero** = API
- **Cocina** = Servidor/sistema

Tú no vas a la cocina, le das tu pedido al mesero (API) y él te trae la comida.

```javascript
// Ejemplo: API del tiempo
// Tú preguntas: "¿Qué temperatura hay?"
// La API responde: {"temp": 25, "condition": "soleado"}
```

---

## 🔷 **¿Qué es una API REST?**
Es un **tipo específico de API** que sigue principios REST (Representational State Transfer):

- Usa **HTTP** (GET, POST, PUT, DELETE)
- **Stateless** (sin estado entre peticiones)
- **Estructura uniforme** de URLs
- Devuelve datos generalmente en **JSON/XML**

```javascript
// Ejemplo API REST:
GET    /api/users     // Obtener usuarios
POST   /api/users     // Crear usuario
PUT    /api/users/1   // Actualizar usuario 1
DELETE /api/users/1   // Eliminar usuario 1
```

---


## 🔷 **Librería vs Biblioteca**
**En programación son SINÓNIMOS** - ambos términos se refieren a lo mismo:

- **Librería/Biblioteca**: Conjunto de código preescrito que proporciona funcionalidades específicas
- Se **importa/requiere** en tu código
- **Tú llamas** a sus funciones

```javascript
// Ejemplo usando una librería (axios)
const axios = require('axios'); // Importas la librería
axios.get('https://api.example.com'); // Tú llamas a sus métodos
```

---


## 🔷 **¿Un módulo de NPM es una API?**

**NO, generalmente no.** Un módulo de NPM es normalmente una **librería/biblioteca**.

### ✅ **Es una LIBRERÍA cuando:**
```javascript
const express = require('express');
const app = express(); // Tú controlas cómo usas Express
app.get('/', (req, res) => {
  res.send('Hola mundo');
});
// Express es una librería - tú llamas sus métodos
```

### ✅ **Proporciona una API cuando:**
```javascript
// Este mismo código CREA una API REST
app.get('/api/users', (req, res) => {
  res.json([{id: 1, name: 'Juan'}]);
});
// Ahora tienes una API que otros pueden consumir
```

---

## 📊 **Resumen de diferencias:**

| Concepto | Propósito | Dirección del flujo |
|----------|-----------|---------------------|
| **Librería** | Funcionalidades reutilizables | Tú → Librería |
| **API** | Comunicación entre sistemas | Sistema A ↔ Sistema B |
| **API REST** | Tipo de API con reglas específicas | Cliente ↔ Servidor vía HTTP |

**Respuesta directa:** Un módulo de NPM que descargas es típicamente una **librería**, no una API (a menos que específicamente sea un cliente para consumir una API externa).

---

## 🔷 **¿Qué es un Framework?**

Un **framework** (marco de trabajo) es una estructura predefinida que proporciona una **base** para desarrollar aplicaciones, imponiendo una **arquitectura** y **flujo de trabajo** específicos.

## 🆚 **Framework vs Librería - La DIFERENCIA clave**

### **Inversión de Control (IoC)**
- **Librería**: **Tú controlas** el flujo, llamas a la librería cuando la necesitas
- **Framework**: **El framework controla** el flujo, tú te adaptas a su estructura

### **Analogía de la construcción:**
- **Librería** = Herramientas sueltas (martillo, serrucho) - tú decides cómo usarlas
- **Framework** = Casa prefabricada - tú instalas muebles y decoras, pero la estructura ya está definida

## 📊 **Ejemplos prácticos:**

### **Librería (Tú controlas):**
```javascript
// axios - LIBRERÍA
const axios = require('axios');

// TÚ decides CUÁNDO y CÓMO usarla
function obtenerUsuarios() {
    return axios.get('/api/users'); // Tú inicias la llamada
}

// Tú controlas el flujo del programa
obtenerUsuarios()
    .then(response => console.log(response.data));
```

### **Framework (El framework controla):**
```javascript
// Express - FRAMEWORK web
const express = require('express');
const app = express();

// El FRAMEWORK define DÓNDE pones tu código
app.get('/users', (req, res) => {
    // Express TE LLAMA cuando llega una petición GET /users
    // Tú solo proves la lógica específica
    res.json([{id: 1, name: 'Juan'}]);
});

// El framework controla el ciclo de vida
app.listen(3000, () => {
    console.log('Servidor iniciado'); // Express decide cuándo ejecutar esto
});
```

## 🎯 **Características de un Framework:**

1. **Estructura predefinida** - Te dice cómo organizar tu código
2. **Inversión de control** - El framework llama a tu código
3. **Arquitectura específica** - Sigue patrones como MVC
4. **Convenciones over configuration** - Menos configuraciones, más convenciones

## 📋 **Ejemplos comunes:**

### **Frameworks:**
- **Backend**: Express.js, NestJS, Django (Python), Spring (Java)
- **Frontend**: Angular, React (con hooks se acerca a framework), Vue.js
- **Mobile**: React Native, Flutter

### **Librerías:**
- **Utilidades**: Lodash, Axios, Moment.js
- **UI**: React (componentes), jQuery
- **Base de datos**: Mongoose, Sequelize

## 🏗️ **Metáfora del restaurante extendida:**

- **Librería** = Recetas individuales que usas cuando quieres
- **Framework** = Todo el restaurante con su menú, cocina y procesos establecidos
- **API** = El servicio de delivery que conecta tu restaurante con clientes externos

## 📊 **Tabla comparativa completa:**

| Aspecto | Librería | Framework | API |
|---------|----------|-----------|-----|
| **Control** | Tú tienes el control | Framework tiene el control | Comunicación entre sistemas |
| **Uso** | La llamas tú | Te llama a ti | La consumes o provees |
| **Flexibilidad** | Alta - usas lo que necesitas | Media - sigues la estructura | Depende del contrato |
| **Ejemplo** | `axios.get()` | `app.get()` en Express | `fetch('https://api.com')` |

## 🔄 **El caso especial de React:**
React es interesante porque empezó como librería pero con hooks y ecosistema se comporta más como framework:

```javascript
// React - Entre librería y framework
function MiComponente() {
    // React controla CUÁNDO se renderiza y actualiza
    const [estado, setEstado] = useState('');
    
    // Tú proves la lógica, React maneja el ciclo de vida
    return <div>Hola {estado}</div>;
}
```

**En resumen:** Un **framework** te da la estructura y tú rellenas los espacios, mientras que una **librería** son herramientas que tú usas dentro de tu propia estructura.