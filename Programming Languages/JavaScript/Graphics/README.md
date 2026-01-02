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



# Comprendiendo `getBoundingClientRect()`

## 📌 El código a explicar

```js
let rect = canvas.getBoundingClientRect();
const scaleX = canvas.width / rect.width;
const scaleY = canvas.height / rect.height;

const xOrigin = (event.clientX - rect.left) * scaleX;
const yOrigin = (event.clientY - rect.top) * scaleY;
```

---

## 🔍 Contexto antes de empezar

Cuando el usuario mueve o hace clic con el ratón:

* `event.clientX` y `event.clientY` → posición del ratón en **pantalla (ventana del navegador)**.
* El `canvas` puede estar:

  * desplazado por márgenes
  * dentro de contenedores
  * escalado por CSS
  * afectado por zoom

Entonces **no coinciden directamente** con las coordenadas internas del `canvas`.

Estas líneas convierten esas coordenadas **a coordenadas reales del canvas**, de forma correcta.

---

## 🧠 Línea 1

```js
let rect = canvas.getBoundingClientRect();
```

### 🔹 ¿Qué hace?

Llama al método `getBoundingClientRect()` que devuelve un objeto así:

```js
{
  left:   posición x del borde izquierdo del canvas en pantalla,
  top:    posición y del borde superior,
  width:  ancho visible del canvas en pixeles CSS,
  height: alto visible del canvas,
  right:  left + width,
  bottom: top + height
}
```

---

## 📏 Línea 2

```js
const scaleX = canvas.width / rect.width;
```

### 🔹 ¿Qué hace?

Calcula el **factor de escala horizontal**.

Porque:

* `canvas.width` = resolución real interna del canvas (por defecto 300)
* `rect.width` = tamaño visible en pantalla (puede ser distinto)

Esto corrige:

✔ CSS zoom
✔ HiDPI / Retina
✔ escalas responsivas

---

## 📐 Línea 3

```js
const scaleY = canvas.height / rect.height;
```

Hace lo mismo pero en vertical.

---

## 🎯 Línea 4

```js
const xOrigin = (event.clientX - rect.left) * scaleX;
```

Vamos parte por parte.

### 1️⃣ `event.clientX`

Posición X del mouse **en la ventana del navegador**.

---

### 2️⃣ Restar el offset del canvas

```js
event.clientX - rect.left
```

➡️ Eso ya es **la posición del mouse relativa al canvas**
(no a la ventana)

---

### 3️⃣ Ajustar la escala

```js
* scaleX
```

Si `scaleX = 0.5`:

```
250 * 0.5 = 125
```

Entonces:

> El ratón está en **x = 125 pixeles reales del canvas**

Y eso es lo que guardas en `xOrigin`.

---

## 🎯 Línea 5

```js
const yOrigin = (event.clientY - rect.top) * scaleY;
```

Exactamente igual pero en vertical.

---

## 🧠 Resumen final

| Línea                     | Explicación                                                    |
| ------------------------- | -------------------------------------------------------------- |
| `getBoundingClientRect()` | Obtiene posición y tamaño visible del canvas                   |
| `scaleX / scaleY`         | Calculan relación entre tamaño real y visible                  |
| `clientX - rect.left`     | Convierte posición del mouse a coordenadas relativas al canvas |
| `* scaleX / scaleY`       | Corrige el escalado para obtener coordenadas REALES del canvas |

