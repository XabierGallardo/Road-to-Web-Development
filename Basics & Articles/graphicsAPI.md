# 1. ¿Qué es una API?

**API** significa *Application Programming Interface*
(en español: *Interfaz de Programación de Aplicaciones*).

Una API es:

> **Un conjunto de reglas y funciones que un sistema ofrece para que otro programa pueda usarlo sin conocer cómo funciona internamente.**

Básicamente, es un intermediario que facilita la interacción entre componentes de software.

## Características de una API:

- Define cómo solicitar y recibir datos
- Proporciona funciones y procedimientos predefinidos
- Permite reutilizar código sin conocer su implementación interna
- Ejemplos comunes: APIs de redes sociales, APIs de pago, APIs de mapas

### Analogía sencilla

Piensa en un **control remoto**:

* Tú pulsas botones (la API)
* La TV hace cosas complejas por dentro
* No necesitas saber cómo está construida

En programación:

* Llamas funciones
* El sistema hace el trabajo interno
* Tú no accedes a los detalles de bajo nivel

---

## Ejemplo simple de API (no gráfica)

En JavaScript:

```js
console.log("Hola");
```

* `console.log` es parte de una **API**
* No sabes cómo imprime texto
* Solo sabes **qué función usar**

---

# 2. ¿Qué es una API de gráficos?

Una **API de Gráficos** es un tipo específico de API diseñada para actuar como intermediaria entre tu videojuego (el software) y tu tarjeta gráfica o GPU (el hardware).

Tu computadora tiene una tarjeta gráfica muy potente, pero tu código (C++, C#, Python) no sabe hablar "el idioma eléctrico" de la tarjeta gráfica. Aquí es donde entra la API de Gráficos.

Es una API diseñada para gestionar y renderizar gráficos en aplicaciones visuales. Proporciona un conjunto de funciones para:

- Dibujar formas, texturas y modelos 3D
- Gestionar sombreadores (shaders)
- Controlar iluminación, cámaras y transformaciones
- Manejar buffers de pantalla

### ¿Cómo funciona?

En lugar de decirle a la tarjeta gráfica: *"Envía voltaje al transistor 4005 para encender el píxel rojo"*, tú usas la API para decir: *"Dibuja un triángulo rojo en estas coordenadas"*. La API traduce esa instrucción a algo que la GPU entiende y procesa.


## APIs de gráficos comunes:
- **DirectX** (específicamente Direct3D) - Windows/Xbox
- **OpenGL** - Multiplataforma
- **Vulkan** - Multiplataforma, de bajo nivel
- **Metal** - Apple (macOS, iOS)
- **WebGL** - Para navegadores web

## ¿Cómo ayuda en el desarrollo de videojuegos?

### 1. **Abstracción del hardware**
- Te permite programar sin preocuparte por los detalles específicos de tarjetas gráficas
- El mismo código puede funcionar en diferentes GPUs

### 2. **Rendimiento optimizado**
- Las APIs gráficas están altamente optimizadas para el hardware
- Aprovechan características específicas de las GPUs
- Manejan eficientemente el pipeline gráfico

### 3. **Funcionalidades avanzadas**
- Acceso a efectos gráficos modernos (ray tracing, sombras dinámicas, partículas)
- Gestión de texturas, modelos 3D y animaciones
- Soportan realidad virtual y aumentada

### 4. **Herramientas y ecosistema**
- Vienen con debuggers y herramientas de profiling
- Tienen comunidades grandes y documentación extensa
- Son soportadas por motores gráficos como Unity y Unreal Engine

### 5. **Multiplataforma**
- Algunas APIs (como Vulkan y OpenGL) permiten desarrollar juegos para múltiples plataformas
- Reducen el tiempo de desarrollo multiplataforma

### Ejemplo práctico:
En lugar de escribir código específico para cada GPU, puedes usar:
```cpp
// Con OpenGL
glDrawElements(GL_TRIANGLES, count, GL_UNSIGNED_INT, 0);

// Con DirectX
deviceContext->DrawIndexed(count, 0, 0);
```

Estas llamadas abstractas luego son traducidas por el driver de la GPU a instrucciones específicas del hardware.

### Resumen API de gráficos
Una **API de gráficos** es una API especializada en:

* Dibujar píxeles
* Dibujar formas
* Dibujar imágenes
* Mostrar animaciones
* Usar la GPU

Ejemplos conocidos:

* **Canvas 2D (HTML5)**
* **WebGL**
* **OpenGL**
* **DirectX**
* **Vulkan**
* **Metal**

Todas tienen algo en común:

> Te permiten **dibujar en pantalla** sin hablar directamente con la tarjeta gráfica.

---

# 3.¿Por qué NO dibujas píxeles “a mano”?

Sin una API gráfica, tendrías que:

* Acceder a memoria de video
* Manejar sincronización con el monitor
* Programar drivers
* Gestionar buffers

Eso es **demasiado complejo** para un videojuego normal.

La API gráfica:

* abstrae todo eso
* te deja concentrarte en **el juego**

---

## Ejemplo concreto: Canvas como API gráfica

Cuando escribes:

```js
ctx.fillRect(50, 50, 30, 30);
```

Estás usando una **API de gráficos 2D**.

Qué hace la API por ti:

* Traduce coordenadas a píxeles reales
* Maneja el escalado
* Redibuja la pantalla
* Sincroniza con el navegador

Tú solo dices **qué** dibujar, no **cómo**.

---

# 4. ¿En qué sentido una API ayuda a crear videojuegos?

## Explicacion breve
Un videojuego necesita, como mínimo:

1. Dibujar gráficos
2. Leer entradas (teclado, mouse, gamepad)
3. Reproducir sonido
4. Controlar el tiempo (frames)
5. Usar memoria eficientemente

Las APIs te dan todo eso **ya resuelto**.

---

### Beneficios directos para videojuegos

### 🧩 Abstracción

No piensas en hardware específico:

* mismo código → muchas GPUs
* mismo juego → muchos sistemas

---

### ⏱ Control del tiempo

Las APIs gráficas:

* sincronizan con la tasa de refresco
* evitan parpadeos
* permiten animación fluida

Ejemplo:

```js
requestAnimationFrame(gameLoop);
```

Eso es una API pensada para juegos.

---

### Rendimiento

* Canvas 2D → CPU + optimizaciones del navegador
* WebGL / OpenGL → GPU directamente

Sin API gráfica:

* el rendimiento sería inaceptable

---

### Separación de responsabilidades

Tú te ocupas de:

* lógica del juego
* físicas
* reglas

La API se ocupa de:

* dibujado
* buffers
* presentación

---

## Explicacion larga

Si estás haciendo juegos, las APIs gráficas son tus mejores amigas por tres razones principales:

### A. Abstracción del Hardware (La más importante)

Hay miles de modelos de tarjetas gráficas (NVIDIA, AMD, Intel), y cada una tiene una arquitectura interna diferente.

* **Sin una API:** Tendrías que escribir código diferente para cada tarjeta gráfica que existe. Sería imposible.
* **Con una API:** Escribes tu código una vez (usando, por ejemplo, OpenGL o DirectX) y la API se encarga de que funcione en cualquier tarjeta gráfica compatible.

### B. Rendimiento y Eficiencia

Las APIs modernas (como Vulkan o DirectX 12) están optimizadas para permitirte "hablar" con el hardware de forma muy directa. Te permiten:

* Manejar miles de objetos en pantalla simultáneamente.
* Calcular luces y sombras en tiempo real.
* Usar la memoria de la tarjeta de video de forma eficiente.

### C. Acceso a Funciones Avanzadas

Las APIs te dan acceso a herramientas matemáticas complejas ya resueltas, como:

* **Shaders:** Pequeños programas que deciden cómo se ve cada píxel (efectos de agua, fuego, metal).
* **Tesselation:** Aumentar el detalle de los modelos 3D dinámicamente.

---

### Un matiz importante: ¿Usas un Motor de Juego (Game Engine)?

Si usas motores como **Unity**, **Unreal Engine** o **Godot**, es probable que **tú no tengas que tocar la API gráfica directamente**.

El motor de juego hace el trabajo sucio por ti:

1. Tú escribes: "Mover personaje".
2. El Motor (Unity/Unreal) traduce eso a la **API Gráfica** (DirectX/Vulkan).
3. La API Gráfica se lo dice a la **GPU**.

Sin embargo, entender qué API estás usando es vital para optimizar tu juego o para saber por qué un juego corre bien en Windows (DirectX) pero necesita ajustes para correr en Android (Vulkan/OpenGL ES).

---

### Resumen Visual

| Nivel | Quién es | Qué hace |
| --- | --- | --- |
| **Alto Nivel** | Tu Juego / Motor | Dice: "¡Muestrame una explosión!" |
| **Intermedio** | **API Gráfica** | Traduce: "Dibuja partículas naranjas y humo en coordenadas (x,y,z)" |
| **Bajo Nivel** | Driver / GPU | Ejecuta: Cálculos matemáticos puros y enciende los píxeles del monitor. |

---

# 5. ¿Qué API gráfica deberías aprender primero?

Depende del objetivo:

### Para aprender conceptos

✔ **Canvas 2D**

* coordenadas
* frames
* colisiones
* sprites
* animación

### Para rendimiento y 3D

✔ **WebGL / OpenGL**

Canvas es ideal para:

* entender videojuegos desde cero
* aprender matemáticas gráficas
* prototipos rápidos

---

## 6. Resumen conceptual

| Concepto        | Qué es                                     |
| --------------- | ------------------------------------------ |
| API             | Conjunto de funciones para usar un sistema |
| API gráfica     | API para dibujar y mostrar gráficos        |
| Canvas          | API gráfica 2D                             |
| Motor de juegos | Usa APIs gráficas por debajo               |
| Videojuego      | Lógica + API gráfica                       |
