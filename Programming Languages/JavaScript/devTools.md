# Expandiendo `console.log` en DevTools
Cuando imprimimos por consola un objeto o array se muestra una copia, pero al expandirlo se ve con los valores actualizados. 
Lo que ves en la consola del navegador no es un "bug", sino **cómo funciona el logging en DevTools**.

---

### 🔎 Lo que pasa realmente

Cuando haces algo como:

```js
const obj = { a: 1 };
console.log(obj);

obj.a = 2;
```

En la **consola de Chrome/Firefox**, verás `{ a: 1 }`.
Pero si despliegas el objeto **después** de haberlo modificado, te mostrará `{ a: 2 }`.

Esto ocurre porque:

1. `console.log()` **no guarda una “foto” inmediata** del objeto.
   Guarda **una referencia** al objeto en memoria.
2. Cuando expandes el objeto en DevTools, este lo renderiza con el **estado actual** (el último) del objeto, no con el estado que tenía cuando lo logueaste.

---

### 🧩 Ejemplo clásico

```js
let arr = [1, 2];
console.log(arr); // Muestra [1, 2]

arr.push(3);
arr.push(4);

// Al desplegar en consola → verás [1, 2, 3, 4]
```

Pero si en vez de eso haces:

```js
let arr = [1, 2];
console.log([...arr]); // Copia el array

arr.push(3);
arr.push(4);

// El log queda como [1, 2]
```

---

### ✅ Cómo forzar un “snapshot” (captura del momento)

Si querés ver el valor **en el momento exacto del log** y no una referencia mutable:

* **Clonar el objeto o array**:

  ```js
  console.log(JSON.parse(JSON.stringify(obj)));
  console.log([...arr]);
  ```
* **Usar `console.table()`** (especialmente útil en arrays/objetos):

  ```js
  console.table(arr);
  ```
* **Congelar el objeto antes de loguear**:

  ```js
  console.log(Object.freeze({...obj}));
  ```

---

📌 En resumen:
La consola muestra referencias en vivo, por eso al desplegar ves el estado más reciente. Si querés el valor “congelado” en el momento del log, tenés que clonar el objeto o usar técnicas como `JSON.stringify`, spread operator o `console.table`.
