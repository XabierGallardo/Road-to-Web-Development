# Entendiendo los módulos en Express.js

### Ejemplo de exportacion de conexion BBDD en Express con mysql2
```ts
// TypeScript
import mysql, { Pool } from "mysql2/promise"; // Tipando la conexion/pool
import environments from "../config/environments.ts";

const { database } = environments;

const connection: Pool = mysql.createPool({
    host: database.host,
    database: database.name,
    user: database.user,
    password: database.password
});

export default connection;
```

---

# 1. Modulos en Express
**Todo archivo en TypeScript o JavaScript que use `import` o `export` se convierte en un módulo ES (ESM, *ECMAScript Module*)**.

En **Node.js con TypeScript**, un **módulo** es simplemente un archivo `.ts` o `.js` que **exporta algo** (funciones, clases, objetos, constantes) y que puede ser **importado en otro archivo**.


## 🔹 Tipos de exportación en un módulo

En un módulo ESM, podés tener:

1. **Exportaciones nombradas** (`export const ...`, `export function ...`):

   ```ts
   // utils.ts
   export const sum = (a: number, b: number) => a + b;
   export const multiply = (a: number, b: number) => a * b;
   ```

   ```ts
   import { sum, multiply } from "./utils";
   ```

2. **Exportación por defecto** (`export default ...`):

   ```ts
   // logger.ts
   export default function logger(msg: string) {
       console.log(`[LOG] ${msg}`);
   }
   ```

   ```ts
   import logger from "./logger";
   ```

3. **Mezcla de ambos** (aunque no siempre se recomienda):

   ```ts
   // config.ts
   export const PORT = 3000;
   export default {
       db: "mysql",
       host: "localhost"
   };
   ```

---

## 🔹 Volviendo al ejemplo anterior

 El ejemplo anterior (`export default connection` o `export const connection`) **es una exportación dentro de un módulo**.
El archivo entero (`connection.ts`) **es el módulo**.

Si ese archivo no tuviera ni `import` ni `export`, entonces sería considerado **script global** y no un módulo.

---

# 2. CommonJS vs ES Modules en Node.js

Históricamente, **Node.js nació con CommonJS (CJS)** porque JavaScript no tenía un sistema de módulos estandarizado.
Más tarde, **ECMAScript Modules (ESM)** se convirtió en el estándar oficial de JS (lo que hoy usamos con `import` y `export`).

---

## 1. CommonJS (CJS)

* Sintaxis tradicional en Node.js.
* Usa `require` y `module.exports`.
* Cada archivo es un módulo.
* Se ejecuta **de manera síncrona** (cuando hacés `require`, carga inmediatamente el archivo).

Ejemplo:

```js
// connection.cjs
const mysql = require("mysql2/promise");

const connection = mysql.createPool({ ... });

module.exports = connection;
```

Y se importa así:

```js
const connection = require("./connection.cjs");
```

👉 Ventajas: rápido, ampliamente soportado, era el estándar de Node.
👉 Desventajas: no es el estándar oficial de ECMAScript, no soporta `import/export` sin transpilar.

---

## 2. ECMAScript Modules (ESM)

* Estándar oficial desde **ES6 (2015)**.
* Usa `import` y `export`.
* Soportado nativamente en Node.js desde la versión 12+ (estable desde Node 14+).
* Maneja las importaciones de manera **asíncrona** y soporta `top-level await`.

Ejemplo:

```ts
// connection.ts (ESM con TypeScript)
import mysql from "mysql2/promise";

const connection = mysql.createPool({ ... });

export default connection;
```

Y se importa así:

```ts
import connection from "./connection.js"; // (en TS, transpila a .js)
```

👉 Ventajas: estándar oficial, interoperable con frontends (React, Vue, etc.), soporta async/await mejor.
👉 Desventajas: al principio fue más restrictivo (ej: necesitabas `"type": "module"` en `package.json` o usar `.mjs`).

---

## 3. Diferencias clave

| Característica    | CommonJS (CJS)               | ES Modules (ESM)         |
| ----------------- | ---------------------------- | ------------------------ |
| Sintaxis          | `require` / `module.exports` | `import` / `export`      |
| Estándar oficial  | ❌ No (es de Node.js)         | ✅ Sí (ECMAScript 2015+)  |
| Compatibilidad    | 100% Node.js                 | Node.js 12+, navegadores |
| Ejecución         | Síncrona                     | Asíncrona (lazy loading) |
| Top-level `await` | ❌ No                         | ✅ Sí                     |
| Recomendado hoy   | Solo proyectos legacy        | ✅ Sí, nuevos proyectos   |

---

## 4. TypeScript y módulos

Cuando usás **TypeScript**, podés elegir qué módulo transpilar en tu `tsconfig.json`:

```json
{
  "compilerOptions": {
    "module": "ESNext",  // o "CommonJS"
    "target": "ES2022",
    "moduleResolution": "Node"
  }
}
```

* Si usás `"module": "CommonJS"`, TS compila a `require`/`module.exports`.
* Si usás `"module": "ESNext"`, TS compila a `import`/`export`.

👉 Hoy lo recomendado es `ESNext`, porque es el estándar y es el que usa Node.js moderno (junto a `"type": "module"` en `package.json`).

---

## 5. ¿Cuál usar hoy?

* **Proyectos nuevos (Express, NestJS, etc.)** → ✅ **ESM (`import/export`)**.
* **Proyectos legacy** o que dependen de librerías viejas → 🤝 **CJS (`require/module.exports`)**.

---

⚡ Ejemplo final:

**CommonJS**:

```js
const express = require("express");
const app = express();
module.exports = app;
```

**ESM**:

```ts
import express from "express";
const app = express();
export default app;
```
