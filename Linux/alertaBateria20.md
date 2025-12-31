# Alerta Bateria 20% en Linux
- Config específica para **Linux Mint 21.3 Cinnamon**!
- Cinnamon ya trae `zenity`, así que no hay que instalar nada.
- `notify-send` ya funciona en Cinnamon, no hace falta configurar DISPLAY.

#### Crearemos un script en bash que:

- ✔️ Comprueba la batería **cada 2 minutos**
- ✔️ **Solo avisa cuando está descargando**
- ✔️ **Avisa a ≤20%** (notificación normal)
- ✔️ **Avisa a ≤10%** (notificación crítica + ventana grande con Zenity)
- ✔️ **Si conectas el cargador → NO avisa más**
- ✔️ **Mientras sigas desenchufado, repite el aviso cada 2 minutos**

---

## 🟩 Paso 1 — Crear el script de comprobación

Abre una terminal y ejecuta:

```bash
nano ~/bateria20.sh
```

```bash
#!/usr/bin/env bash

# Detectar batería
BAT=$(upower -e | grep BAT)
LEVEL=$(upower -i "$BAT" | awk '/percentage/ {gsub("%",""); print $2}')
STATE=$(upower -i "$BAT" | awk '/state/ {print $2}')

# ❌ Si NO está descargando → salir sin avisar
if [[ "$STATE" != "discharging" ]]; then
  exit 0
fi

# 🔴 Aviso crítico ≤10% (con ventana grande)
if [[ $LEVEL -le 10 ]]; then
  notify-send "🛑 Batería muy baja" "Te queda $LEVEL% — conecta el cargador" -u critical

  if command -v zenity >/dev/null 2>&1; then
    zenity --warning \
      --title="🛑 BATERÍA MUY BAJA" \
      --width=450 --height=200 \
      --text="Tu batería está en $LEVEL%.\n\nGuarda tu trabajo y conecta el cargador."
  fi

  exit 0
fi

# 🟡 Aviso normal ≤20%
if [[ $LEVEL -le 20 ]]; then
  notify-send "⚠ Batería baja" "Nivel actual: $LEVEL%" -u normal
fi
```


Otorgamos permisos de ejecución:

```bash
chmod +x ~/bateria20.sh
```

🔍 **Este script hace:**

| Situación          | Acción                           |
| ------------------ | -------------------------------- |
| Cargando o llena   | No avisa                         |
| Descargando y 21%+ | No avisa                         |
| Descargando y ≤20% | Notificación cada 2 min          |
| Descargando y ≤10% | Notificación + Zenity cada 2 min |
| Vuelves a enchufar | Deja de avisar                   |

---

## 🟩 Paso 2 — Crear el servicio systemd (usuario)

Creamos un servicio que ejecuta el script:

```bash
mkdir -p ~/.config/systemd/user
nano ~/.config/systemd/user/bateria.service
```


```ini
[Unit]
Description=Mostrar alertas de batería baja

[Service]
Type=oneshot
ExecStart=%h/bateria20.sh
```

---

## 🟩 Paso 3 — Crear el temporizador cada 2 minutos

```bash
nano ~/.config/systemd/user/bateria.timer
```


```ini
[Unit]
Description=Comprobar batería cada 2 minutos

[Timer]
OnBootSec=30sec
OnUnitActiveSec=2min
Unit=bateria.service

[Install]
WantedBy=timers.target
```


---

## 🟩 Paso 4 — Activar el temporizador


```bash
systemctl --user daemon-reload
systemctl --user enable --now bateria.timer
```

Comprueba que está activo:

```bash
systemctl --user list-timers
```

---


## (Opcional) añade sonido si quieres

Dentro del bloque de 10% agrega:

```bash
paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga
```

---

## 🎯 ¿Qué conseguimos?

✔️ **No molesta cuando está cargando**
✔️ **Cuando desenchufas y bajas a ≤20% → avisa**
✔️ **Mientras siga desenchufado → repite cada 2 minutos**
✔️ **A ≤10% hace un aviso más visible**
✔️ **Si enchufas → se detienen los avisos**
✔️ **Funciona aunque reinicies sesión**

Todo controlado por systemd, limpio y estable.