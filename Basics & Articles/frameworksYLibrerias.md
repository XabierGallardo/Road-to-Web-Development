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