# Docker resumido
Docker es una plataforma que permite **empaquetar aplicaciones y todas sus dependencias** en unidades llamadas **contenedores (containers)**. Esto facilita que una aplicación funcione de la misma manera en cualquier entorno: tu computadora, un servidor o la nube.

### ¿Qué problema resuelve?

Imagina que desarrollas una aplicación en tu equipo y funciona perfectamente, pero al desplegarla en un servidor aparecen errores porque:

* La versión de Python es diferente.
* Faltan librerías.
* La configuración del sistema no coincide.

Con Docker, empaquetas todo lo necesario dentro de un contenedor, evitando esos problemas.

### Conceptos básicos

#### 📦 Imagen (Image)

Es una plantilla que contiene:

* El sistema base (por ejemplo, Linux).
* Tu aplicación.
* Las dependencias necesarias.

#### 🚀 Contenedor (Container)

Es una instancia en ejecución de una imagen.

Por ejemplo:

```bash
docker run nginx
```

Esto descarga (si no existe) y ejecuta un contenedor de Nginx.

#### 📄 Dockerfile

Archivo donde defines cómo construir una imagen.

Ejemplo:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

### Ventajas de Docker

✅ Portabilidad: funciona igual en cualquier lugar.
✅ Aislamiento: cada aplicación tiene su propio entorno.
✅ Despliegue rápido.
✅ Menor consumo de recursos que una máquina virtual.
✅ Ideal para microservicios y desarrollo moderno.

### Docker vs Máquina Virtual

| Docker                         | Máquina Virtual                  |
| ------------------------------ | -------------------------------- |
| Comparte el kernel del sistema | Tiene sistema operativo completo |
| Más ligero                     | Más pesada                       |
| Inicio en segundos             | Inicio en minutos                |
| Menor consumo de recursos      | Mayor consumo                    |

### Ejemplo práctico

Supongamos que tienes una API en Python:

1. Creas un `Dockerfile`.
2. Construyes la imagen:

   ```bash
   docker build -t mi-api .
   ```
3. Ejecutas el contenedor:

   ```bash
   docker run -p 5000:5000 mi-api
   ```
4. Tu aplicación queda accesible en el puerto 5000.

En resumen, **Docker es una herramienta para crear y ejecutar aplicaciones en contenedores, garantizando que funcionen igual en cualquier entorno**.


---

# Entendiendo Docker desde 0
Imagínate que vas a mudarte de casa. En lugar de meter tu ropa, tus libros y tus platos sueltos en el camión (y rezar para que nada se rompa o se pierda por el camino), lo metes todo en **cajas de mudanza perfectamente etiquetadas**. Cada caja tiene dentro todo lo necesario para que lo que hay dentro funcione al llegar a la nueva casa.

Eso es **Docker**, pero para software.

En el mundo de la programación, un "camión de mudanza" es tu computadora, y la "nueva casa" es el servidor de internet o la computadora de un compañero de trabajo.

---

## El problema que resuelve: "En mi máquina sí funcionaba"

Antes de Docker, era muy común que un programa funcionara en la computadora del programador, pero al pasarlo a otra persona o subirlo a internet, dejara de funcionar. ¿Por qué? Porque faltaba una actualización, la base de datos era de otra versión o el sistema operativo era diferente.

Docker soluciona esto metiendo el programa y **todo lo que necesita para vivir** dentro de un contenedor virtual. Si funciona en tu contenedor, funcionará en cualquier computadora que tenga Docker instalado.

---

## Los 3 conceptos clave que debes conocer

Para entender Docker, solo necesitas dominar tres palabras:

### 1. El Dockerfile (La receta)

Es un archivo de texto simple donde escribes las instrucciones para construir tu entorno. Es como la receta para hacer un pastel: *"Usa este sistema operativo, instala esta versión de Python, copia estos archivos y ejecuta este comando"*.

### 2. La Imagen (La caja cerrada)

Cuando ejecutas la receta (el Dockerfile), el resultado es una **Imagen**. Es como la caja de mudanza ya empacada y sellada. No se puede modificar, está congelada en el tiempo y lista para ser enviada a cualquier parte.

### 3. El Contenedor (La caja abierta y funcionando)

Cuando "enciendes" una imagen, se convierte en un **Contenedor**. Es la aplicación ejecutándose en la vida real. Puedes encender diez contenedores iguales al mismo tiempo si necesitas que diez personas usen tu aplicación a la vez.

---

## ¿Por qué todo el mundo lo usa?

* **Es ultra ligero:** A diferencia de las "máquinas virtuales" antiguas (que emulaban una computadora entera dentro de otra y volvían tu laptop lentísima), los contenedores de Docker comparten el cerebro de tu propia computadora. Son increíblemente rápidos y usan muy poca memoria.
* **Formatear tu PC ya no da miedo:** Si necesitas probar una base de datos nueva, la corres en un contenedor. Cuando terminas, borras el contenedor y tu computadora queda impecable, sin "basura" instalada.
* **Consistencia total:** Lo que ves en tu pantalla es exactamente lo que verá el usuario final en internet.

> 💡 **En resumen:** Docker es una herramienta que empaqueta tu aplicación con todas sus dependencias en un "contenedor" estandarizado, asegurando que funcione igual en cualquier computadora del mundo.


---

# Profundizando Docker
Como dev , es comun toparse con el infierno de dependencias: *"Para este proyecto necesito Node v14, pero para el otro necesito Node v20"*, o *"En mi máquina local corre con SQLite, pero en producción usa PostgreSQL y algo se rompió en las migraciones"*.

Docker elimina esto mediante la **aislación a nivel de sistema operativo**. Vamos a desglosar cómo funciona bajo el capó.

---

## 1. Contenedores vs. Máquinas Virtuales (VMs)

Es un error común pensar que un contenedor es una máquina virtual pequeña. No lo es.

* **Máquinas Virtuales (Hypervisor):** Cada VM incluye una aplicación, los binarios necesarios y **un sistema operativo invitado completo (Guest OS)**. Si corres tres VMs, tienes tres sistemas operativos consumiendo RAM y CPU por encima de tu sistema operativo real.
* **Contenedores Docker:** Los contenedores **comparten el Kernel del sistema operativo Host** (el de tu máquina). Docker utiliza características nativas de Linux llamadas `namespaces` (para aislar lo que ve el contenedor: procesos, red, usuarios) y `cgroups` (para limitar cuánta RAM y CPU puede usar).

Por eso un contenedor levanta en milisegundos y pesa megabytes, mientras que una VM tarda minutos y pesa gigabytes.

---

## 2. El flujo de trabajo real: Del código al contenedor

Para un desarrollador web, el día a día con Docker se resume en crear y configurar tres archivos/conceptos:

### El `Dockerfile` (La infraestructura como código)

Es el archivo donde defines el entorno de tu app. En lugar de instalar cosas a mano, lo automatizas. Mira este ejemplo para una app básica de Node.js:

```dockerfile
# 1. Descarga una imagen oficial de Node.js como base
FROM node:20-alpine

# 2. Crea el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copia los archivos de dependencias
COPY package*.json ./

# 4. Instala las dependencias (dentro del contenedor)
RUN npm install

# 5. Copia el resto del código de tu app
COPY . .

# 6. Expone el puerto en el que escucha tu servidor express/nest
EXPOSE 3000

# 7. El comando que se ejecuta cuando el contenedor encienda
CMD ["npm", "start"]

```

### La Imagen y el concepto de Capas (Layers)

Cuando corres `docker build -t mi-app .`, Docker lee el Dockerfile y crea una **Imagen**.
Lo interesante aquí es que cada línea del Dockerfile crea una **capa de solo lectura**. Docker es inteligente: si cambias un archivo de tu código pero no has instalado librerías nuevas, Docker usará la caché para las capas del `npm install`, haciendo que los builds posteriores sean instantáneos.

### El Contenedor (La capa de escritura)

Al ejecutar `docker run -p 3000:3000 mi-app`, Docker toma la imagen de solo lectura y le añade una delgada **capa de escritura** encima. Tu app de Node ya está corriendo de forma totalmente aislada. El parámetro `-p 3000:3000` (puertos) es un puente: le dice a Docker que mapee el puerto 3000 de tu localhost al puerto 3000 interno del contenedor.

---

## 3. Dos herramientas clave que usarás a diario

Como desarrollador web, rara vez usarás solo `docker run` desde la terminal porque las apps modernas tienen backend, frontend y base de datos. Aquí entran:

### Docker Compose (Multicontenedores)

Es una herramienta que te permite definir y correr aplicaciones de múltiples contenedores usando un único archivo YAML (`docker-compose.yml`).
¿Necesitas un backend en Node y una base de datos PostgreSQL? En lugar de levantar cada uno por separado y configurar redes manualmente, tiras un `docker compose up` y listo:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: mi_password_secreto

```

### Volúmenes (Persistencia de datos)

Por defecto, los contenedores son **efímeros**. Si tu base de datos corre dentro de un contenedor y el contenedor se apaga o se borra, **los datos se pierden**.
Para solucionar esto usamos **Volúmenes** (`Volumes`), que básicamente consisten en mapear una carpeta de tu máquina real (Host) con una carpeta dentro del contenedor. Así, aunque el contenedor muera, los datos de tu base de datos física siguen a salvo en tu disco duro.

---

## Resumen conceptual:

1. **Dockerfile:** Define *cómo se construye* el entorno de un microservicio.
2. **Docker Compose:** Coordina *cómo interactúan* varios contenedores entre sí (ej: App + Base de datos).
3. **Puertos (`-p`):** Abren la puerta para que puedas ver el contenedor desde el navegador de tu máquina.
4. **Volúmenes (`-v`):** Evitan que tus bases de datos se borren al apagar el contenedor.