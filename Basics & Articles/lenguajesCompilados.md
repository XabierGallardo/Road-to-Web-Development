# Entendiendo la compilación como un proceso determinístico.
Que un compilador **codifique en bajo nivel tu código bajo un proceso determinístico** significa que, dadas exactamente las mismas entradas, el compilador siempre producirá exactamente la misma salida, sin intervención de aleatoriedad ni decisiones no reproducibles.

Desglosemos:

## 1. "Codifica en bajo nivel"
El compilador traduce tu código fuente (alto nivel) a una representación más cercana a la máquina:
- Código ensamblador
- Código objeto / binario
- Bytecode (en el caso de JVM, .NET, etc.)

Es decir, convierte instrucciones legibles por humanos en instrucciones que la CPU (o una máquina virtual) puede ejecutar.

## 2. "Proceso determinístico"
Un proceso determinístico es aquel en el que **la misma entrada produce siempre la misma salida**, paso a paso. No hay:
- Aleatoriedad (random seeds)
- Dependencia de la hora del sistema
- Dependencia del orden de memoria no controlado
- Heurísticas que cambien entre ejecuciones

En el contexto de un compilador, esto implica que si compilas el mismo archivo fuente, con la misma versión del compilador, las mismas opciones y el mismo entorno, obtendrás **bit a bit el mismo resultado**.

## 3. Qué implica en la práctica

| Aspecto | Significado |
|---|---|
| **Reproducibilidad** | Puedes volver a compilar y obtener el mismo binario. |
| **Verificación** | Puedes comparar hashes (ej. SHA-256) del binario para detectar cambios. |
| **Auditoría** | Otros pueden reproducir tu build y verificar que no hay código malicioso inyectado. |
| **Depuración** | Los errores son reproducibles; no aparecen "a veces". |

## 4. Matices importantes
- **Determinístico no significa óptimo**: el compilador puede tomar decisiones fijas que no sean las mejores para todos los casos, pero siempre las mismas.
- **Puede haber no-determinismo** si el compilador usa:
  - Direcciones de memoria aleatorias (ASLR al compilar)
  - Timestamps incrustados
  - Paralelismo con orden no fijo
  - Hash maps con orden de iteración no garantizado
- Por eso existen iniciativas como **reproducible builds**, que buscan eliminar esas fuentes de no-determinismo.

## 5. Ejemplo concreto
Si compilas `main.c` con `gcc -O2` hoy y mañana, en la misma máquina y misma versión de GCC, el binario resultante debería ser idéntico. Eso es determinismo. Si cambiaras la hora del sistema y el binario cambiara, no sería determinístico.

En resumen: **el compilador sigue una receta fija y predecible para traducir tu código a bajo nivel, sin sorpresas ni aleatoriedad, garantizando que la misma entrada siempre dé la misma salida.**

---

# *Reverse Engineering* o Ingeniería inversa como el proceso contrario. Reconstruír el código fuente a partir del código compilado
Esa es la idea central de la ingeniería inversa, pero con matices importantes. El **reverse engineering** (ingeniería inversa) de software busca **recuperar información de alto nivel a partir del binario**, pero rara vez reconstruye el código original exacto.

## 1. La intuición básica

| Compilación | Reverse engineering |
|---|---|
| Código fuente → binario | Binario → código fuente (o algo parecido) |
| Determinístico | **No** determinístico / ambiguo |

La idea de "proceso inverso" es correcta como intuición, pero **no es una inversa matemática**: la compilación **pierde información**, y esa información no siempre se puede recuperar.

## 2. Qué información se pierde al compilar

- **Nombres de variables y funciones** (se convierten en direcciones o se eliminan)
- **Comentarios**
- **Tipos de datos** originales (un `int`, un `enum` y un puntero pueden verse igual en binario)
- **Estructuras de control** exactas (un `for`, un `while` y un `goto` pueden generar el mismo ensamblador)
- **Macros, templates, inline functions** (se expanden y desaparecen)
- **Optimizaciones** que reescriben por completo la lógica original

Por eso, de un binario **no se puede recuperar el código fuente original**, sino una **reconstrucción plausible** que sea funcionalmente equivalente.

## 3. Niveles de reverse engineering

| Nivel | Qué obtienes | Herramientas |
|---|---|---|
| **Desensamblado** | Ensamblador legible | IDA Pro, Ghidra, objdump |
| **Decompilación** | Pseudocódigo tipo C | Ghidra, Hex-Rays, RetDec |
| **Reconstrucción de estructuras** | Structs, clases, vtables | IDA, Ghidra + análisis manual |
| **Recuperación de algoritmos** | Lógica de alto nivel | Análisis manual + scripts |
| **Reimplementación** | Código fuente nuevo equivalente | Trabajo humano |

## 4. Por qué NO es un proceso inverso exacto

1. **No es inyectivo**: muchos programas fuente distintos producen el mismo binario.
2. **No es determinístico al revés**: dos analistas pueden producir reconstrucciones distintas del mismo binario.
3. **Depende del contexto**: sin saber qué hacía el programa, interpretar instrucciones es ambiguo.
4. **Ofuscación**: hay técnicas diseñadas específicamente para romper la reversibilidad (packers, control flow flattening, cifrado de strings).

## 5. Usos legítimos del reverse engineering

- **Interoperabilidad** (protocolos, formatos cerrados)
- **Seguridad**: análisis de malware, búsqueda de vulnerabilidades
- **Auditoría**: verificar que un binario hace lo que dice hacer
- **Recuperación**: código legacy sin fuentes
- **Investigación**: entender optimizaciones de compiladores

## 6. Relación con lo que hablábamos antes

- La compilación es **determinística** (misma entrada → misma salida).
- El reverse engineering **no lo es**: es un problema **inverso mal planteado (ill-posed)**, con múltiples soluciones posibles.
- Por eso existen los **reproducible builds**: si puedes recompilar el fuente y obtener el mismo binario, puedes verificar la correspondencia sin necesidad de hacer reverse engineering.

## En resumen

El reverse engineering **intenta** invertir la compilación, pero como la compilación **destruye información**, lo que se obtiene no es el código original, sino una **aproximación funcionalmente equivalente**. Es más parecido a **arqueología** que a una operación matemática inversa: reconstruyes una civilización a partir de sus ruinas, con interpretación y conjeturas.