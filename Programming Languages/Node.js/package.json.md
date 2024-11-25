# `package.json`
El archivo **`package.json`** es un componente fundamental en cualquier proyecto de **Node.js**. Sirve como una especie de "manual" o "descripción" del proyecto, proporcionando información clave sobre la aplicación o biblioteca, como su nombre, versión, dependencias, scripts de ejecución y más. Este archivo permite gestionar el proyecto de manera ordenada y estandarizada.

A continuación, se explica de manera técnica y detallada cada aspecto del archivo **`package.json`**.

---

### **1. ¿Qué es `package.json`?**
El archivo **`package.json`** es un documento JSON ubicado en el directorio raíz de un proyecto **Node.js**. Contiene metadatos esenciales del proyecto, configuraciones, dependencias y comandos para facilitar su desarrollo, despliegue y mantenimiento.

### **2. Propósito del `package.json`**
1. **Gestión de Dependencias:** Lista todas las bibliotecas y herramientas que el proyecto necesita para ejecutarse o desarrollarse.
2. **Automatización:** Define scripts que permiten ejecutar tareas como pruebas, compilación o despliegue.
3. **Portabilidad:** Proporciona toda la información necesaria para clonar y ejecutar el proyecto en diferentes entornos.
4. **Versionado:** Permite mantener un control de versiones del proyecto.
5. **Distribución:** Si el proyecto es un paquete de Node.js, **`package.json`** incluye información necesaria para publicarlo en el **registro de npm**.

---

### **3. Estructura del Archivo `package.json`**

El archivo **`package.json`** sigue una estructura en formato JSON con campos clave. A continuación se explican los campos más importantes:

---

#### **3.1. Metadata Básica**
Incluye información básica del proyecto.

- **`name`** (obligatorio):  
  El nombre del proyecto o paquete. Debe ser único si se publica en **npm**.  
  - Reglas:  
    - Solo puede contener letras minúsculas, números, guiones (`-`) y guiones bajos (`_`).
    - No puede contener espacios.  
  **Ejemplo:**
  ```json
  "name": "mi-proyecto"
  ```

- **`version`** (obligatorio):  
  Indica la versión del proyecto utilizando el formato **SemVer (Semantic Versioning)**.  
  **Formato:** `X.Y.Z`, donde:  
  - `X`: Versión principal (major). Cambia si hay cambios importantes o incompatibles.
  - `Y`: Versión secundaria (minor). Cambia si se añaden nuevas funcionalidades compatibles.
  - `Z`: Versión de parche (patch). Cambia si se corrigen errores.  
  **Ejemplo:**
  ```json
  "version": "1.0.0"
  ```

- **`description`** (opcional):  
  Breve descripción del proyecto.  
  **Ejemplo:**
  ```json
  "description": "Una aplicación para gestionar tareas."
  ```

- **`author`** (opcional):  
  Información del autor del proyecto.  
  **Ejemplo:**
  ```json
  "author": "Juan Pérez <juan.perez@example.com>"
  ```

- **`license`** (opcional):  
  Indica la licencia bajo la cual se distribuye el proyecto.  
  **Ejemplo:**
  ```json
  "license": "MIT"
  ```

- **`repository`** (opcional):  
  Proporciona información sobre el repositorio del proyecto.  
  **Ejemplo:**
  ```json
  "repository": {
    "type": "git",
    "url": "https://github.com/usuario/mi-proyecto.git"
  }
  ```

---

#### **3.2. Dependencias**
Gestiona las bibliotecas necesarias para que el proyecto funcione o se desarrolle.

- **`dependencies`:**  
  Lista las dependencias necesarias en producción.  
  **Ejemplo:**
  ```json
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.0.1"
  }
  ```
  - `^`: Acepta versiones que comparten el mismo número principal, pero pueden variar en secundarios o parches.
  - `~`: Acepta solo actualizaciones de parches, manteniendo el mismo número principal y secundario.

- **`devDependencies`:**  
  Lista las dependencias necesarias solo para el desarrollo, como herramientas de prueba o compilación.  
  **Ejemplo:**
  ```json
  "devDependencies": {
    "nodemon": "^2.0.15",
    "eslint": "^8.21.0"
  }
  ```

---

#### **3.3. Scripts**
Define comandos personalizados que se pueden ejecutar con **`npm run`**.  
**Ejemplo:**
```json
"scripts": {
  "start": "node app.js",
  "dev": "nodemon app.js",
  "test": "jest"
}
```
- Ejecutar un script:
  ```bash
  npm run start
  ```

---

#### **3.4. Keywords**
Lista palabras clave asociadas con el proyecto, útiles para mejorar la búsqueda en **npm**.  
**Ejemplo:**
```json
"keywords": ["node", "express", "api", "backend"]
```

---

#### **3.5. Configuración Avanzada**
- **`main`:**  
  Especifica el archivo de entrada principal del proyecto. Por defecto es `index.js`.  
  **Ejemplo:**
  ```json
  "main": "app.js"
  ```

- **`engines`:**  
  Especifica las versiones de Node.js compatibles con el proyecto.  
  **Ejemplo:**
  ```json
  "engines": {
    "node": ">=14.0.0"
  }
  ```

- **`peerDependencies`:**  
  Indica dependencias que el usuario debe instalar manualmente para garantizar la compatibilidad.  
  **Ejemplo:**
  ```json
  "peerDependencies": {
    "react": "^18.0.0"
  }
  ```

---

### **4. Crear un archivo `package.json`**

Puedes crear el archivo manualmente o usando comandos de **npm**:

#### **Con comando interactivo:**
```bash
npm init
```
Este comando te guiará para llenar cada campo del archivo.

#### **Crear un archivo básico automáticamente:**
```bash
npm init -y
```
Esto generará un archivo `package.json` con valores predeterminados.

---

### **5. Ejemplo Completo de `package.json`**

```json
{
  "name": "mi-proyecto",
  "version": "1.0.0",
  "description": "Una API RESTful para gestionar tareas",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "dev": "nodemon app.js",
    "test": "jest"
  },
  "keywords": ["node", "api", "rest", "express"],
  "author": "Juan Pérez <juan.perez@example.com>",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.0.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.15",
    "jest": "^28.0.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/usuario/mi-proyecto.git"
  },
  "engines": {
    "node": ">=14.0.0"
  }
}
```

---

### **6. Conclusión**
El archivo **`package.json`** es el núcleo de cualquier proyecto de **Node.js**, ya que organiza y define cómo funciona, qué dependencias utiliza y cómo interactuar con él. Comprender su estructura y configurarlo adecuadamente es esencial para crear aplicaciones eficientes, portables y fáciles de mantener.