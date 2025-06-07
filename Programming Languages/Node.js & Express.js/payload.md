# Payload como convención para devolver datos
```js
const respuesta = await User.selectAllUsers();

res.status(200).json({
    payload: respuesta[0]
});
```

El uso de la palabra `payload` es una **convención** y no una obligación técnica de JavaScript ni de Express.js.


---

### 🔍 ¿Qué significa "payload"?

**"Payload"** en inglés significa "carga útil". En el contexto de APIs y programación, **se refiere a los datos reales que se transmiten en una respuesta o solicitud HTTP**, es decir, el contenido que importa.

Por ejemplo:

```json
{
  "payload": [ { "id": 1, "name": "Juan" }, { "id": 2, "name": "Ana" } ]
}
```

Aquí, `payload` contiene el arreglo de usuarios. El nombre indica al consumidor de la API: acá están los datos que pediste”.

---

### ✅ ¿Es obligatorio usar "payload"?

**No.** Puedes usar cualquier clave que tenga sentido para ti o para tu equipo. Algunos ejemplos comunes:

```js
res.status(200).json({ users: respuesta[0] });     // más semántico
res.status(200).json({ data: respuesta[0] });      // muy común
res.status(200).json({ payload: respuesta[0] });   // común en APIs RESTful y GraphQL
res.status(200).json({ result: respuesta[0] });    // otra opción válida
```

---

### 📐 ¿Por qué muchos usan "payload"?

* Es **neutro**: no asume qué tipo de datos son (usuarios, productos, comentarios).
* Es **consistente** cuando se trabaja con respuestas estructuradas que contienen más cosas, como:

```json
{
  "success": true,
  "payload": [...],
  "message": "Usuarios obtenidos exitosamente"
}
```

Esto se ve mucho en APIs REST que devuelven estructuras completas.

---

### 🧠 Buenas prácticas

En lugar de usar simplemente:

```js
res.json(respuesta[0]);
```

Usar una estructura con `payload`, `message`, `error`, etc. mejora la legibilidad y facilita la depuración del lado del cliente.

---

### 📌 Conclusión

`payload` es una **convención semántica** útil, pero **no obligatoria**. Es una forma clara y general de indicar que “estos son los datos importantes que te devuelvo”. Puedes usarla si te gusta esa estructura o cambiarla por una más específica como `users`, `products`, `data`, etc.

¿Quieres que te muestre un ejemplo completo con distintas claves (`payload`, `message`, `error`) para estandarizar respuestas en Express.js?
