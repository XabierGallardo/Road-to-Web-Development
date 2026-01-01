# 👻 Qué es un `Daemon`?
Un **daemon** (se pronuncia *déimon* o *dímon*) es un **proceso que se ejecuta en segundo plano en un sistema operativo**, normalmente sin interacción directa con el usuario.
Viene de la palabra griega **δαίμων (daímōn)**, que significa “espíritu que trabaja de fondo”, y fue adoptada en informática por esa idea.

En Linux y Unix:

* Un daemon suele iniciarse **automáticamente al arrancar el sistema**
* **no tiene ventana ni interfaz gráfica**
* permanece **esperando eventos o tareas**
* realiza funciones del sistema **de manera continua o periódica**

### 🔧 Ejemplos típicos de daemons

* `sshd` → espera conexiones SSH
* `cupsd` → gestiona impresoras
* `cron` → ejecuta tareas programadas
* `NetworkManager` → gestiona la red

En sistemas modernos como Linux Mint, muchos daemons son gestionados por **systemd**, que es el gestor de servicios (por eso hablábamos de *systemd services y timers* en tu configuración de batería).

### Diferencia con un programa normal

| Programa normal          | Daemon                          |
| ------------------------ | ------------------------------- |
| Lo ejecutas tú           | Se ejecuta automáticamente      |
| Tiene ventana o terminal | No tiene interfaz               |
| Termina cuando cierras   | Normalmente siempre está activo |

Si quieres, te explico también la diferencia entre **daemon, servicio y proceso** 👍


---


# Diferencia entre **proceso, servicio y daemon** en Linux

# 🧩 1️⃣ ¿Qué es un **proceso**?

Un **proceso** es simplemente **un programa en ejecución**.

👉 Cada vez que abres:

* Firefox
* la terminal
* un editor de texto
* o incluso el script de batería

…el sistema crea **un proceso**.

📌 Características:

* Tiene un **PID** (Process ID → número único)
* Puede estar en **primer plano** (lo ves) o en **segundo plano**
* Empieza… y termina cuando el programa termina

📍 Ejemplos de procesos:

* `firefox`
* `gedit`
* `bash`
* `top`

> 🔑 Todo daemon y todo servicio **son procesos**, pero no todo proceso es daemon o servicio.

---

# 🛎️ 2️⃣ ¿Qué es un **servicio**?

Un **servicio** es un **proceso gestionado por un gestor de servicios**, como:

* `systemd` (Linux actual — incluido Linux Mint)
* `init` (sistemas antiguos)
* `launchd` (macOS)
* `Service Control Manager` (Windows)

Un servicio puede:

✔️ iniciarse al arrancar el sistema
✔️ reiniciarse si falla
✔️ detenerse/arrancarse con comandos
✔️ correr en segundo plano

📍 Ejemplos de servicios:

* `ssh.service` → permite conexiones remotas
* `bluetooth.service`
* `NetworkManager.service`
* `bateria.service` (el que creaste tú 😊)

📌 Se controlan así:

```bash
systemctl status nombre.service
systemctl start nombre.service
systemctl stop nombre.service
```

---

# 👻 3️⃣ ¿Qué es un **daemon**?

Un **daemon** es un **tipo de servicio** (o proceso) que:

✔️ corre en **segundo plano**
✔️ **no tiene interfaz**
✔️ normalmente **se ejecuta siempre o espera eventos**

Históricamente, los daemons:

* se nombraban acabando en **`d`**

  * `sshd`
  * `cupsd`
  * `crond`
  * `systemd`

Hoy en día, **casi todos los daemons son servicios gestionados por systemd**…
pero **no todos los servicios son necesariamente daemons** (por ejemplo, un servicio que ejecuta algo puntual y termina).

---

# 🧠 Entonces… ¿cómo se relacionan?

Piensa así ⬇️

### 🔹 Proceso

👉 Programa en ejecución (concepto más general)

### 🔹 Servicio

👉 Proceso **gestionado por systemd u otro gestor**

### 🔹 Daemon

👉 Servicio/proceso **en segundo plano sin interfaz**, que normalmente corre siempre

---

# 📌 Ejemplo usando e; script `bateria20.sh`

Cuando se ejecuta → es un **proceso**

## ✔️ Tu `bateria.service`

Es un **servicio systemd**

## ✔️ ¿Es un daemon?

No exactamente — porque:

* no permanece en ejecución
* `Type=oneshot`
* corre → comprueba la batería → termina

🔹 Pero si tuvieras un programa que corriera **todo el tiempo en segundo plano** vigilando la batería…
entonces sí sería un **daemon**.

---

# 🧾 Resumen rápido

| Concepto     | Qué es                                 | Ejemplo                           |
| ------------ | -------------------------------------- | --------------------------------- |
| **Proceso**  | Programa ejecutándose                  | `firefox`, `bash`, `bateria20.sh` |
| **Servicio** | Proceso gestionado por systemd         | `ssh.service`, `bateria.service`  |
| **Daemon**   | Servicio en segundo plano sin interfaz | `sshd`, `cupsd`, `crond`          |

---

# Resumen conceptual

* **Un daemon (o “demonio”)** es un programa que corre en segundo plano, normalmente desde que arranca el sistema, y no necesita interacción directa del usuario.
* **Los servicios de systemd** son la forma moderna de gestionar estos procesos en Linux.
* **systemd tiene dos tipos principales de servicios**:

  1. **Servicios del sistema (system services)** → afectan a todo el sistema.
  2. **Servicios de usuario (user services)** → solo afectan a tu sesión de usuario.

---

## 🧠 Qué es un daemon en Linux

Un **daemon** es un programa que:

✔️ corre en segundo plano
✔️ no tiene ventana gráfica
✔️ normalmente arranca automáticamente
✔️ se queda “escuchando” o realizando tareas periódicas

Ejemplos muy comunes:

* `cupsd` → maneja impresoras
* `sshd` → permite conexiones remotas
* `NetworkManager` → administra redes
* `cron` → ejecuta tareas programadas

👉 La idea clave:
**un daemon NO es algo que abres tú manualmente — está siempre ahí trabajando “silenciosamente”.**

---

## 🏗️ Qué es systemd y cómo entra en todo esto

Hoy en día, en la mayoría de distros (incluida Linux Mint), quien administra los daemons es **systemd**.

systemd es:

> El sistema que arranca el sistema operativo y administra los servicios.

Permite:

* iniciar servicios
* detenerlos
* reiniciarlos
* configurarlos
* monitorearlos

Con comandos como:

```bash
systemctl start nombre.service
systemctl status nombre.service
systemctl enable nombre.service
```

---

## 👥 Servicios de Sistema vs Servicios de Usuario

### 🔹 1. Servicios del sistema (nivel root)

📂 Ubicación típica:

```
/etc/systemd/system
/usr/lib/systemd/system
```

Características:

✔️ corren incluso sin usuario logueado
✔️ afectan a todo el sistema
✔️ normalmente requieren root
✔️ ejemplo: `sshd.service`, `bluetooth.service`

Se manejan con:

```bash
sudo systemctl start nombre.service
sudo systemctl enable nombre.service
```

---

### 🔹 2. Servicios de usuario (sin root, por sesión)

📂 Ubicación:

```
~/.config/systemd/user
```

Características:

✔️ corren solo cuando inicias sesión
✔️ pertenecen a TU usuario
✔️ no afectan al resto
✔️ no necesitan sudo
✔️ perfectos para scripts personales (como tu alerta de batería 🔋)

Se manejan con:

```bash
systemctl --user start nombre.service
systemctl --user enable nombre.service
```

Y arrancan automáticamente **cuando inicias sesión**.

---

## 🔌 Diferencia importante entre ambos

| Concepto                    | Servicio del sistema     | Servicio de usuario              |
| --------------------------- | ------------------------ | -------------------------------- |
| ¿Requiere root?             | Sí                       | No                               |
| ¿Afecta a todo el sistema?  | Sí                       | No, solo tu usuario              |
| ¿Corre sin sesión iniciada? | Sí                       | No (normalmente)                 |
| Ubicación                   | `/etc/systemd/system`    | `~/.config/systemd/user`         |
| Ideal para                  | Red, hardware, seguridad | Scripts personales, apps, tareas |

---

## 🔔 Aplicándolo al script de alertas de batería

Características:

✅ que el script corra en segundo plano
✅ que te avise de niveles bajos
✅ que deje de avisar al conectar el cargador
✅ que se repita mientras siga en nivel crítico
✅ que sea simple y sin tocar el sistema

👉 Por eso se debe hacer como **user systemd service**. De esta manera:

* no necesitas sudo
* no tocas archivos del sistema
* se ejecuta solo en tu sesión
* es fácil de activar / desactivar
* puedes editarlo libremente

Ejemplo de manejo:

```bash
systemctl --user start battery-alert.service
systemctl --user enable battery-alert.service
systemctl --user status battery-alert.service
```

---

## 🧩 Y… ¿qué es exactamente un “daemon” en el caso anterior?

Tu script + systemd service = **un daemon de usuario**

Porque:

* corre siempre en segundo plano
* trabaja sin mostrar consola
* monitorea el estado de batería
* lanza ventanas *cuando corresponde*

