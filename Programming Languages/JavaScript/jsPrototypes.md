# 1. JavaScript está basado en prototipos
Los objetos de JavaScript pueden **delegar la búsqueda de propiedades y métodos a otro objeto**, llamado su **prototipo**.

La idea central es esta:

```text
objeto
   │
   │ si no encuentra algo
   ↓
prototipo
   │
   │ si tampoco lo encuentra
   ↓
prototipo del prototipo
   │
   ↓
...
```

Esto forma una **cadena de prototipos** (*prototype chain*).

---

# 2. Empecemos con un objeto común

Supongamos:

```js
const user = {
    name: "Juan"
};
```

El objeto tiene una propiedad:

```js
console.log(user.name);
```

JavaScript encuentra:

```text
user
└── name → "Juan"
```

Pero ahora hacemos:

```js
console.log(user.toString());
```

Nosotros nunca escribimos `toString` dentro de `user`.

Entonces:

> ¿De dónde salió `toString()`?

Acá empieza lo interesante.

---

# 3. El prototipo de un objeto

Todo objeto JavaScript tiene internamente una referencia a otro objeto que funciona como su prototipo.

Podemos acceder a ella mediante:

```js
Object.getPrototypeOf(user)
```

Por ejemplo:

```js
const user = {
    name: "Juan"
};

console.log(Object.getPrototypeOf(user));
```

Vas a obtener un objeto relacionado con:

```js
Object.prototype
```

Conceptualmente:

```text
user
  │
  ↓
Object.prototype
```

Y `Object.prototype` contiene métodos como:

```text
toString()
hasOwnProperty()
valueOf()
...
```

Por eso podemos hacer:

```js
user.toString();
```

aunque `user` no tenga directamente una propiedad `toString`.

JavaScript la busca en su prototipo.

---

# 4. La búsqueda de propiedades

Esto es fundamental.

Tenemos:

```js
const user = {
    name: "Juan"
};
```

Cuando hacemos:

```js
user.name
```

JavaScript busca:

```text
¿user tiene "name"?
       │
       └── Sí → "Juan"
```

Pero cuando hacemos:

```js
user.toString()
```

ocurre algo parecido a:

```text
¿user tiene "toString"?
       │
       └── No
           ↓
¿su prototipo tiene "toString"?
       │
       └── Sí
           ↓
        ejecutarlo
```

Por eso se habla de **prototype chain**.

---

# 5. Podemos verlo directamente

Podemos comprobar que el objeto tiene un prototipo:

```js
const user = {
    name: "Juan"
};

console.log(
    Object.getPrototypeOf(user) === Object.prototype
);
```

Resultado:

```text
true
```

Por lo tanto:

```text
user
 ↓
Object.prototype
```

Y el prototipo de `Object.prototype` es:

```js
Object.getPrototypeOf(Object.prototype)
```

que devuelve:

```text
null
```

Entonces la cadena termina:

```text
user
 ↓
Object.prototype
 ↓
null
```

`null` significa:

> No hay otro prototipo que buscar.

---

# 6. ¿Por qué esto es útil?

Porque permite que **muchos objetos compartan comportamiento**.

Imaginá que tenés:

```js
const user1 = {
    name: "Juan"
};

const user2 = {
    name: "Ana"
};

const user3 = {
    name: "Pedro"
};
```

No sería necesario que cada objeto tuviera su propia copia de:

```js
toString()
hasOwnProperty()
valueOf()
```

Todos pueden utilizar los métodos que proporciona:

```js
Object.prototype
```

Conceptualmente:

```text
             Object.prototype
             ├── toString()
             ├── valueOf()
             └── hasOwnProperty()
                    ↑
          ┌─────────┼─────────┐
          │         │         │
        user1     user2     user3
```

Esto permite **reutilizar comportamiento**.

---

# 7. ¿Y los arrays?

Acá se vuelve todavía más evidente.

Cuando escribís:

```js
const numbers = [10, 20, 30];
```

podés hacer:

```js
numbers.push(40);
```

¿Dónde está `push()`?

No está escrito directamente dentro del array como si cada array tuviera una copia independiente del código.

Existe:

```js
Array.prototype
```

que contiene métodos como:

```text
push()
pop()
map()
filter()
find()
reduce()
...
```

Conceptualmente:

```text
numbers
   ↓
Array.prototype
   ├── push()
   ├── pop()
   ├── map()
   ├── filter()
   └── reduce()
          ↓
     Object.prototype
          ↓
         null
```

Por eso:

```js
numbers.map(...)
```

funciona.

JavaScript busca `map` en el objeto/prototipo correspondiente.

---

# 8. Esto explica algo que ya conocés

Seguramente ya usaste:

```js
const numbers = [1, 2, 3];

numbers.map(...)
numbers.filter(...)
numbers.reduce(...)
```

Ahora podés entender mejor qué está pasando.

Cuando escribís:

```js
numbers.map()
```

JavaScript esencialmente busca:

```text
numbers
   ↓
¿tiene map?
   ↓
no directamente
   ↓
Array.prototype
   ↓
¡Encontró map!
   ↓
ejecutarlo
```

Por eso los métodos de arrays son métodos compartidos mediante el prototipo.