# Tutorial de API Canvas de HTML5 con JavaScript


# 🎨 1. ¿Qué es `<canvas>`?

`<canvas>` es un lienzo en blanco dentro de una página web donde puedes **dibujar píxeles mediante JavaScript**.
No es como una imagen fija: **tú decides qué se dibuja y cuándo**.

Ejemplo básico:

```html
<canvas id="miCanvas" width="500" height="300"></canvas>

<script>
const canvas = document.getElementById("miCanvas");
const ctx = canvas.getContext("2d");   // contexto de dibujo en 2D
</script>
```

* `canvas` = el lienzo
* `ctx` = el “pincel virtual”

> Canvas no tiene sistema de objetos: si dibujas algo, queda “pintado”. Si quieres cambiarlo, debes dibujar de nuevo o borrar.

---

# 🧠 2. Sistema de Coordenadas

Canvas usa un plano **X–Y** como este:

```
(0,0)  → esquina superior izquierda
X → derecha
Y → abajo
```

Ejemplo:

```js
ctx.fillRect(0, 0, 50, 50); 
```

Dibuja un cuadrado desde la esquina superior izquierda.

---

# 🟥 3. Dibujar Formas Básicas

## 🔹 Rectángulos

```js
ctx.fillStyle = "red";        // color de relleno
ctx.fillRect(20, 20, 100, 50);
```

Borde:

```js
ctx.strokeStyle = "blue";
ctx.lineWidth = 3;
ctx.strokeRect(20, 20, 100, 50);
```

Borrar:

```js
ctx.clearRect(0, 0, canvas.width, canvas.height);
```

---

# 🖌 4. Rutas (Paths) y Líneas

Rutas = secuencia de puntos conectados.

```js
ctx.beginPath();
ctx.moveTo(50, 50);     // punto inicial
ctx.lineTo(150, 50);    // dibuja línea
ctx.lineTo(150, 100);
ctx.closePath();        // opcional
ctx.stroke();           // dibuja
```

Rellenar:

```js
ctx.fillStyle = "orange";
ctx.fill();
```

---

# ⚪ 5. Círculos y Arcos

```js
ctx.beginPath();
ctx.arc(150, 150, 50, 0, Math.PI * 2); // x,y,radio,ángulo ini,ángulo fin
ctx.fillStyle = "purple";
ctx.fill();
```

Semicírculo:

```js
ctx.arc(150, 150, 50, 0, Math.PI);
```

---

# 🖍 6. Texto

```js
ctx.font = "24px Arial";
ctx.fillStyle = "black";
ctx.fillText("Hola Canvas", 100, 50);
```

Contorno:

```js
ctx.strokeText("Hola", 100, 100);
```

---

# 🌈 7. Colores, Gradientes y Transparencia

Transparencia:

```js
ctx.fillStyle = "rgba(255,0,0,0.5)";
```

Gradiente lineal:

```js
const grad = ctx.createLinearGradient(0,0,200,0);
grad.addColorStop(0,"red");
grad.addColorStop(1,"yellow");
ctx.fillStyle = grad;
ctx.fillRect(20,20,200,100);
```

---

# 🖼 8. Dibujar Imágenes

```html
<img id="img" src="foto.png" hidden>
```

```js
const img = document.getElementById("img");
img.onload = () => ctx.drawImage(img, 0, 0);
```

Escalado:

```js
ctx.drawImage(img, 0, 0, 100, 100);
```

---

# 🔁 9. Animación — Concepto Clave

La **programación gráfica moderna** se basa en este ciclo:

1️⃣ borrar
2️⃣ actualizar posiciones
3️⃣ redibujar
4️⃣ repetir

En Canvas usamos:

```js
function loop(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  // dibujar aquí
  requestAnimationFrame(loop);
}
loop();
```

---

# ⚽ 10. Ejemplo Completo: Pelota en Movimiento

```html
<canvas id="c" width="500" height="300"></canvas>

<script>
const canvas = document.getElementById("c");
const ctx = canvas.getContext("2d");

let x = 50, y = 50;
let dx = 2, dy = 2;
let r = 20;

function loop(){
  ctx.clearRect(0,0,canvas.width,canvas.height);

  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI*2);
  ctx.fillStyle="red";
  ctx.fill();

  x += dx;
  y += dy;

  if(x+r > canvas.width || x-r < 0) dx *= -1;
  if(y+r > canvas.height || y-r < 0) dy *= -1;

  requestAnimationFrame(loop);
}
loop();
</script>
```

Esto ya introduce:

✔️ movimiento
✔️ colisiones
✔️ animación fluida

---

# 🔄 11. Transformaciones (Rotar, Escalar, Trasladar)

## Trasladar sistema de coordenadas

```js
ctx.translate(100,100);
```

## Rotar

```js
ctx.rotate(Math.PI / 4); // 45°
```

## Escalar

```js
ctx.scale(2,1);
```

⚠️ Siempre usa `save()` / `restore()`:

```js
ctx.save();
ctx.translate(100,100);
ctx.rotate(Math.PI/4);
ctx.fillRect(0,0,50,50);
ctx.restore();
```

---

# 🧩 12. Eventos del Mouse

```js
canvas.addEventListener("mousemove", e=>{
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  console.log(x,y);
});
```

---

# 📐 13. Conceptos Fundamentales de Programación Gráfica

Aprender Canvas también implica entender estos conceptos:

---

## 🔹 1. Espacio de Coordenadas

Canvas usa un **sistema cartesiano orientado hacia abajo**.
En gráficos avanzados lo transformarás para trabajar más cómodo.

---

## 🔹 2. Rederización Bufferizada

Aunque no lo veas, Canvas trabaja **píxel a píxel**.
Cada frame redibuja todo.

---

## 🔹 3. Ciclo de Renderizado

Es el corazón de los motores gráficos:

```
entrada → lógica → física → render → repetir
```

---

## 🔹 4. Tiempo y Velocidad

Movimiento correcto basado en tiempo:

```js
let last = 0;
function loop(ts){
  const dt = (ts - last)/1000;
  last = ts;

  // usar dt
  x += vx * dt;

  requestAnimationFrame(loop);
}
loop();
```

---

## 🔹 5. Colisiones

Ejemplo círculo–pared:

```js
if(x+r > width || x-r < 0) dx *= -1;
```

---

# 🎮 14. Ejemplo Final: Mini Juego Simple

```html
<canvas id="game" width="500" height="400"></canvas>

<script>
const c = document.getElementById("game");
const ctx = c.getContext("2d");

let player = {x:230, y:350, w:40, h:20, speed:5};
let bullets = [];
let keys = {};

document.addEventListener("keydown", e=> keys[e.key]=true);
document.addEventListener("keyup", e=> keys[e.key]=false);

function loop(){
  ctx.clearRect(0,0,c.width,c.height);

  if(keys["ArrowLeft"]) player.x -= player.speed;
  if(keys["ArrowRight"]) player.x += player.speed;
  if(keys[" "]) bullets.push({x:player.x+18,y:player.y});

  bullets.forEach(b=> b.y -= 5);
  bullets = bullets.filter(b=> b.y>0);

  ctx.fillStyle="blue";
  ctx.fillRect(player.x, player.y, player.w, player.h);

  ctx.fillStyle="red";
  bullets.forEach(b=> ctx.fillRect(b.x,b.y,4,10));

  requestAnimationFrame(loop);
}
loop();
</script>
```

🎉 Ya has creado un motor de juego básico.

---

# 📌 15. Buenas Prácticas

- ✔️ separar lógica y render
- ✔️ usar `requestAnimationFrame`
- ✔️ usar `save()` / `restore()`
- ✔️ redibujar cada frame
- ✔️ medir tiempo (delta time)

---

# 📚 16. Qué puedes aprender después

Cuando domines esto, puedes avanzar a:

🔹 WebGL
🔹 Librerías como PixiJS
🔹 Motores como Phaser
🔹 Física 2D real
🔹 IA en juegos

---


