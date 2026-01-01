# Evitar lienzos estirados en `<canvas>`
Cuando **das el mismo ancho y alto en `fillRect()` debería verse un cuadrado**… **salvo que el lienzo (canvas) esté estirado**.

Canvas tiene **dos tamaños distintos**:

#### 1️⃣ Tamaño real de dibujo (atributos HTML)

Ej.:

```html
<canvas id="myCanvas" width="600" height="400"></canvas>
```

### 2️⃣ Tamaño visual en pantalla (CSS)

Ej.:

```css
canvas {
  width: 1200px;
  height: 400px;
}
```

Si **estos tamaños no tienen la misma proporción**, el navegador **escala el dibujo de forma no uniforme** → y los cuadrados se convierten en rectángulos.

📌 Es decir, si el canvas dibuja 30×30 “píxeles de lienzo”,
pero en pantalla esos píxeles están estirados → ya no es cuadrado.

### Define SIEMPRE `width` y `height` en el HTML

```html
<canvas id="myCanvas" width="600" height="400"></canvas>
```

Y en CSS NO cambies la escala (o usa auto):

```css
canvas{
  width: 600px;
  height: 400px;
}
```

O directamente **sin CSS**.



---



# Comparando `moveTo() + lineTo() + stroke()` vs `fillRect()`

## 🎨 Método 1 — `moveTo() + lineTo() + stroke()`

```js
ctx.moveTo(0, 0);
ctx.lineTo(200, 100);
ctx.stroke();
```

### 🔹 ¿Qué hace?

Dibuja **una línea** desde el punto:

```
(0,0)  →  (200,100)
```

Pero ojo:

* `moveTo()` solo mueve el lápiz (no dibuja)
* `lineTo()` define el segmento
* `stroke()` dibuja el contorno de ese segmento

### 🔹 Es un **trazo vectorial**

Ventajas:

✔ No rellena un área
✔ Usa el `strokeStyle` y `lineWidth`
✔ Se puede conectar con más líneas
✔ Ideal para figuras, gráficos, contornos

Ejemplo: dibujar polígonos, caminos, etc.

---

## 🟩 Método 2 — `fillRect()`

```js
ctx.fillStyle = fondo;
ctx.fillRect(0, 0, game.width, game.height);
```

### 🔹 ¿Qué hace?

Dibuja **un rectángulo relleno** desde (0,0) con:

```
ancho = game.width
alto = game.height
```

Si coincide con el tamaño del canvas → **pinta todo el fondo**.

### 🔹 Es un **relleno de área**

Ventajas:

✔ Más rápido para pintar grandes superficies
✔ Ideal para limpiar/redibujar el fondo en animaciones
✔ Usa `fillStyle` (no stroke)

---

## 🧠 Diferencia conceptual importante

| Concepto      | Método 1              | Método 2               |
| ------------- | --------------------- | ---------------------- |
| Tipo          | Línea (contorno)      | Rectángulo relleno     |
| Dibuja con    | `stroke()`            | `fill()`               |
| Color que usa | `strokeStyle`         | `fillStyle`            |
| Forma         | Segmento entre puntos | Área rectangular       |
| Uso típico    | Dibujar figuras       | Pintar fondo / bloques |

---

## ⚙️ Diferencia técnica (muy importante en animación)

### 🏃‍♂️ Si estás animando…

Normalmente cada frame haces:

```js
fillRect(0,0,width,height)
```

para **borrar lo anterior**
y luego dibujas lo nuevo.

Si no lo haces, verás “fantasmas” porque los dibujos quedan.

---

# 📐 Relación matemática (visual)

Método 1 trabaja con **geometría de vectores**:

```
Punto A (x1,y1)
Punto B (x2,y2)
```

Mientras que `fillRect()` trabaja con:

```
posición (x,y)
ancho w
alto h
```

Son abstracciones distintas.

---

# 🧪 Ejemplo simple comparando

## Línea diagonal

```js
ctx.strokeStyle = "red";
ctx.lineWidth = 3;

ctx.moveTo(0, 0);
ctx.lineTo(200, 200);
ctx.stroke();
```

## Fondo verde

```js
ctx.fillStyle = "green";
ctx.fillRect(0,0,300,300);
```

👉 Una cosa **no reemplaza a la otra**.
Son herramientas diferentes.

---

# 💡 Analogía sencilla

Imagina que el canvas es una hoja:

🖊 **Método 1 = dibujar con un bolígrafo (líneas)**
🖌 **Método 2 = pintar con un rodillo (rellenos)**

---

# 🔍 Si quieres comparar rendimiento

📌 `fillRect()` es extremadamente eficiente
porque Canvas lo optimiza internamente.

📌 `stroke()` puede ser más costoso
si los caminos son complejos.

Pero en la mayoría de apps, **la diferencia es irrelevante**.

---

# 🎯 Conclusión corta

✔ `moveTo + lineTo + stroke` → dibuja líneas (contornos)
✔ `fillRect` → pinta áreas rellenas (normalmente el fondo)

❌ No son equivalentes
✔ Se usan juntos en animación

---
