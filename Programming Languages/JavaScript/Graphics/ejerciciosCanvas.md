# 1. Enunciados ejercicios guiados para aprender Canvas 
# 2. Cuaderno de prácticas para aprender Canvas

# 1. Enunciados ejercicios guiados

> Cada ejercicio incluye:
> 🔹 Objetivo
> 🔹 Explicación visual/matemática
> 🔹 Guía paso a paso
> 🔹 Variante para ir un poco más lejos

No necesitas más que HTML + JavaScript.

---

## 🟩 Ejercicio 1 — Dibuja una “cuadrícula de precisión”

### 🎯 Objetivo

Aprender el **sistema de coordenadas del canvas** y entender la relación entre píxeles y unidades.

### 🧠 Matemática visual

Canvas usa este sistema:

```
(0,0) — esquina superior izquierda
+X → derecha
+Y → abajo
```

Esto rompe el hábito del plano cartesiano tradicional (donde Y crece hacia arriba).
Aquí **Y crece hacia abajo**.

### 🧪 Lo que haremos

Dibujar líneas cada 50px para crear una cuadrícula.

### 🧭 Paso a paso

1. Dibuja líneas verticales cada 50px
2. Luego horizontales
3. Marca los ejes

Mientras lo haces, imagina:

* Cada celda = 50×50 píxeles
* Tu canvas es un “papel milimetrado”

### ⭐ Variante

Pinta los ejes X e Y de otro color.
Eso te ayudará muchísimo en los siguientes ejercicios.

---

## ⚫ Ejercicio 2 — Dibuja un círculo donde haga clic el mouse

### 🎯 Objetivo

Conectar **eventos → coordenadas → dibujo**.

### 🧠 Matemática visual

Un círculo en canvas usa:

```
ctx.arc(x, y, r, 0, 2π)
```

Donde:

* `(x,y)` es el centro
* `r` es el radio
* `2π radianes = 360 grados`

Así que **ángulos en gráficos = radianes**:

```
π rad = 180°
π/2 rad = 90°
2π rad = 360°
```

### 🧪 Lo que haremos

Cada vez que hagas clic, dibujar un círculo en esa posición.

### 🔍 Detalle importante

Las coordenadas del mouse vienen en **coordenadas de pantalla**, no del canvas.
Por eso restamos el `getBoundingClientRect()`.

### ⭐ Variante

Cambia el tamaño del círculo según la posición X.
Eso introduce la idea de **mapear valores**.

---

## 🟥 Ejercicio 3 — Movimiento lineal: una pelota que cruza la pantalla

### 🎯 Objetivo

Entender **velocidad = cambio por unidad de tiempo**.

### 🧠 Matemática visual

Si:

```
posición = posición + velocidad
```

entonces:

```
x = x + dx
```

En cada frame avanza `dx`.

Esto es **cinemática básica**.

### 🧪 Lo que haremos

Pelota que se mueve hacia la derecha.

Sin borrar, verás una línea.
Cuando borres cada frame, verás movimiento fluido.

> Has entendido el concepto de **render loop** 🎉

### ⭐ Variante

Haz que también se mueva en Y.

---

## 🏓 Ejercicio 4 — Rebote en los bordes (colisión con paredes)

### 🎯 Objetivo

Aprender detección de colisión.

### 🧠 Matemática visual

Una pelota con radio `r` choca cuando:

```
x + r > width   (pared derecha)
x - r < 0       (pared izquierda)
```

Al chocar:

```
dx = -dx
```

Es decir, **inviertes el signo de la velocidad**.

### 🧪 Lo que haremos

Pelota que rebota dentro del canvas.

### ⭐ Variante

Cambia el coeficiente de rebote:

```
dx = -dx * 0.8
```

→ ahora pierde energía
→ estás simulando física 🧪

---

## 🧲 Ejercicio 5 — Movimiento circular con seno y coseno

### 🎯 Objetivo

Entender que **seno y coseno describen un círculo**.

### 🧠 Matemática visual

Para dibujar un punto en un círculo:

```
x = cx + r * cos(θ)
y = cy + r * sin(θ)
```

Donde:

* `(cx, cy)` = centro
* `r` = radio
* `θ` = ángulo en radianes

Visualízalo así:

```
cos(θ) → eje X
sin(θ) → eje Y
```

Y al variar θ, el punto gira.

### 🧪 Lo que haremos

Un puntito girando en círculo.

### ⭐ Variante

Dibuja la trayectoria → obtendrás un círculo perfecto.

---

## 🛩 Ejercicio 6 — Rotar una figura alrededor de un punto

### 🎯 Objetivo

Entender transformaciones geométricas.

### 🧠 Matemática visual

Para rotar respecto a un punto:

1️⃣ Traslada el sistema al centro
2️⃣ Rota
3️⃣ Dibuja
4️⃣ Vuelve atrás

En Canvas:

```
save()
translate()
rotate()
draw()
restore()
```

### 🧪 Lo que haremos

Un rectángulo girando.

### ⭐ Variante

Combina escala (`scale()`).

---

## 🎮 Ejercicio 7 — Jugador que se mueve con flechas

### 🎯 Objetivo

Comprender:

* entrada de usuario
* actualización de estado
* renderizado por frame

### 🧠 Matemática visual

Posición es un vector:

```
p = (x, y)
```

Velocidad también:

```
v = (vx, vy)
```

Movimiento:

```
p = p + v
```

Te acaban de introducir **álgebra vectorial** sin dolor 😄

### 🧪 Lo que haremos

Un cuadrado controlado por teclado.

### ⭐ Variante

Añade fricción:

```
vx *= 0.9
```

---

## 🧮 Ejercicio 8 — Colisión entre dos círculos

### 🎯 Objetivo

Aprender a medir distancia.

### 🧠 Matemática visual

La distancia entre dos puntos:

```
d = sqrt((x2-x1)² + (y2-y1)²)
```

Dos círculos colisionan cuando:

```
d < r1 + r2
```

### 🧪 Lo que haremos

Pelota que detecta si toca a otra.

### ⭐ Variante

Haz que cambie de color al tocarse 🎨

---

## 📈 Ejercicio 9 — Gráfico animado de una función

### 🎯 Objetivo

Visualizar matemáticas.

### 🧠 Matemática visual

Dibuja:

```
y = sin(x)
```

y verás una onda.

### 🧪 Lo que haremos

Un osciloscopio simple animado.

### ⭐ Variante

Combina con:

```
y = sin(x * frecuencia)
```

---

## 🌌 Ejercicio 10 — Sistema de partículas

### 🎯 Objetivo

Pensar en **muchos objetos independientes**.

Cada partícula tiene:

```
posición
velocidad
vida
color
```

Y en cada frame:

```
actualiza → dibuja → envejece
```

Esto es la base de efectos como:

✨ fuego
✨ nieve
✨ explosiones

### ⭐ Variante

Gravedad:

```
vy += g
```

Has llegado a **física clásica simulada** 👏

---

## 🧠 Conceptos matemáticos que ya usamos jugando con graficos!

✔ Sistema de coordenadas
✔ Álgebra vectorial básica
✔ Cinemática
✔ Trigonometría
✔ Funciones periódicas
✔ Distancias en el plano
✔ Transformaciones afines
✔ Física simple



---


# 2. Cuaderno de prácticas para aprender Canvas

> Todos los ejemplos usan solo HTML + JavaScript “vanilla”, sin librerías.

---

# 📘 Cuaderno de Prácticas — Gráficos con Canvas

## 🔹 Configuración base (para todos los ejercicios)

Crea un archivo `index.html` así:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Canvas Practice</title>
  <style>
    canvas { border:1px solid #333; }
  </style>
</head>
<body>
  <canvas id="canvas" width="600" height="400"></canvas>
  <script src="script.js"></script>
</body>
</html>
```

Y un archivo `script.js` vacío para ir llenándolo.

---

## 🟦 Ejercicio 1 — Dibuja una cuadrícula (base para coordenadas)

### 🎯 Objetivo

Comprender el sistema de coordenadas de Canvas.

### 🧠 Concepto clave

* El origen `(0,0)` está en la **esquina superior izquierda**.
* El eje X aumenta hacia la **derecha**
* El eje Y aumenta hacia **abajo**

### 👨‍🏫 Tarea

Dibuja una cuadrícula cada 50px.

### ✅ Solución explicada

```js
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const step = 50;

ctx.strokeStyle = "#ccc";

for (let x = 0; x <= canvas.width; x += step) {
  ctx.beginPath();
  ctx.moveTo(x, 0);
  ctx.lineTo(x, canvas.height);
  ctx.stroke();
}

for (let y = 0; y <= canvas.height; y += step) {
  ctx.beginPath();
  ctx.moveTo(0, y);
  ctx.lineTo(canvas.width, y);
  ctx.stroke();
}
```

### 📌 Matemática visual

Esto representa rectángulos de 50×50 → subdividiendo el plano.

---

## 🟥 Ejercicio 2 — Dibuja una circunferencia

### 🎯 Objetivo

Entender ángulos en radianes.

### 🧠 Concepto clave

Canvas usa **radianes**:

[
360^\circ = 2\pi\ \text{radianes}
]

### 👨‍🏫 Tarea

Dibuja un círculo en el centro.

### ✅ Solución

```js
ctx.beginPath();
ctx.arc(300, 200, 80, 0, Math.PI * 2);
ctx.strokeStyle = "red";
ctx.stroke();
```

---

## 🟩 Ejercicio 3 — Animar un punto en línea recta

### 🎯 Objetivo

Trabajar con velocidad constante.

### 🧠 Concepto matemático

Si la posición inicial es (x_0) y la velocidad es (v):

[
x(t) = x_0 + vt
]

### 👨‍🏫 Tarea

Haz que un círculo se mueva de izquierda a derecha.

### ✅ Solución

```js
let x = 0;

function loop() {
  ctx.clearRect(0,0,canvas.width,canvas.height);

  ctx.beginPath();
  ctx.arc(x, 200, 20, 0, Math.PI*2);
  ctx.fill();

  x += 2;
  requestAnimationFrame(loop);
}
loop();
```

---

## 🟨 Ejercicio 4 — Movimiento circular

### 🎯 Objetivo

Aplicar seno y coseno.

### 🧠 Matemática

Radio (R), centro ((cx, cy)):

[
x = cx + R\cos(\theta)
]
[
y = cy + R\sin(\theta)
]

### 👨‍🏫 Tarea

Haz que un punto gire.

### ✅ Solución

```js
let angle = 0;
const cx = 300;
const cy = 200;
const R = 100;

function loop() {
  ctx.clearRect(0,0,600,400);

  const x = cx + R * Math.cos(angle);
  const y = cy + R * Math.sin(angle);

  ctx.beginPath();
  ctx.arc(x, y, 10, 0, Math.PI*2);
  ctx.fill();

  angle += 0.03;
  requestAnimationFrame(loop);
}
loop();
```

---

## 🟪 Ejercicio 5 — Rebote en las paredes

### 🎯 Objetivo

Detectar colisiones.

### 👨‍🏫 Tarea

Haz que una bola rebote.

### 🧠 Concepto

Cuando toca un borde:

[
v = -v
]

### ✅ Solución

```js
let x = 100, y = 100;
let vx = 3, vy = 2;

function loop() {
  ctx.clearRect(0,0,600,400);

  ctx.beginPath();
  ctx.arc(x,y,15,0,Math.PI*2);
  ctx.fill();

  x += vx;
  y += vy;

  if (x <= 15 || x >= 585) vx *= -1;
  if (y <= 15 || y >= 385) vy *= -1;

  requestAnimationFrame(loop);
}
loop();
```

---

## 🧮 Ejercicio 6 — Dibuja una función matemática

### 🎯 Objetivo

Graficar funciones.

### 👨‍🏫 Tarea

Dibuja:

[
y = \sin(x)
]

### 🧠 Nota

Hay que escalar porque sin(x) ∈ [-1,1].

### ✅ Solución con explicación

```js
ctx.beginPath();
ctx.moveTo(0,200);

for (let x = 0; x < 600; x++) {
  const y = 200 + Math.sin(x * 0.05) * 80;
  ctx.lineTo(x, y);
}
ctx.stroke();
```

* `0.05` → comprime en X
* `*80` → estira en Y
* `+200` → baja la función al centro

---

## 🧲 Ejercicio 7 — Física aplicada: caída libre con gravedad

### 🎯 Objetivo

Simular aceleración.

### 🧠 Física

Con aceleración (a):

[
v(t) = v_0 + at
]
[
y(t) = y_0 + v_0 t + \frac{1}{2}at^2
]

En discrete steps:

```js
v += a * dt
y += v * dt
```

### 👨‍🏫 Tarea

Simula una pelota cayendo con gravedad y rebotando.

### ✅ Solución

```js
let y = 50;
let v = 0;
const g = 0.5;
const radius = 20;

function loop() {
  ctx.clearRect(0,0,600,400);

  ctx.beginPath();
  ctx.arc(300,y,radius,0,Math.PI*2);
  ctx.fill();

  v += g;     // aceleración
  y += v;     // posición

  // rebote
  if (y >= 400 - radius) {
    y = 400 - radius;
    v = -v * 0.8; // pierde energía
  }

  requestAnimationFrame(loop);
}
loop();
```

### 📌 Qué estás aprendiendo

✔ Movimiento acelerado
✔ Energía y amortiguamiento
✔ Simulación numérica

---

## 🎨 Ejercicio 8 — Interacción: controla un objeto con el teclado

### 🎯 Objetivo

Capturar eventos.

### 👨‍🏫 Tarea

Mover un cuadrado con flechas.

### ✅ Solución

```js
let x = 250, y = 150;

document.addEventListener("keydown", e => {
  if(e.key === "ArrowUp") y -= 10;
  if(e.key === "ArrowDown") y += 10;
  if(e.key === "ArrowLeft") x -= 10;
  if(e.key === "ArrowRight") x += 10;
});

function loop() {
  ctx.clearRect(0,0,600,400);
  ctx.fillRect(x,y,40,40);
  requestAnimationFrame(loop);
}
loop();
```

---

## 🧠 Extra — Combina todo: mini-juego sencillo

Crea:
✔ un jugador
✔ gravedad
✔ plataformas
✔ colisiones


---

## 📎 Consejos para seguir practicando

✅ Cambia colores y formas
✅ Ajusta velocidades
✅ Dibuja ejes X-Y
✅ Grafica otras funciones

* parabólica (y = x^2)
* exponencial
* ruido aleatorio

✅ Experimenta con física

* fricción
* empujes
* colisiones entre bolas

---

## 🚀 Propuestas para el siguiente nivel

* rotaciones y matrices
* sprites
* colisiones AABB
* partículas
* simulación física más realista
