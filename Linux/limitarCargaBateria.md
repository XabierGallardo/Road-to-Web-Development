# Asus Vivobook 15 / Linux Mint 21.3
Analiazndo salida de:
```bash
sudo tlp-stat -b

ls /sys/class/power_supply/
```

**Perfecto — con esa información ya sabemos **que tu **ASUS Vivobook SÍ soporta oficialmente el límite de carga por hardware** 

Además, **TLP ya está usando el driver correcto (`asus_wmi / natacpi`)**, así que lo mejor es configurarlo ahí.

Tu salida dice:

```
Supported features: charge threshold
STOP_CHARGE_THRESH_BAT0: 0..100
charge_control_end_threshold = 100
```

➡️ Eso significa: **puedes fijar el tope de carga (STOP) al valor que quieras, por ejemplo 80%.**

Vamos paso a paso.

---

# ✅ Opción recomendada: fijar el límite al 80% con TLP

## 1️⃣ Edita la configuración de TLP

Abre el archivo:

```bash
sudo nano /etc/tlp.conf
```

Busca estas líneas (si están comentadas con `#`, quítaselo y edítalas):

```ini
STOP_CHARGE_THRESH_BAT0=80
```

> Si ves también una línea para `BAT1`, ignórala (tu equipo tiene solo `BAT0`).

⚠️ **No pongas START**, ASUS normalmente solo usa STOP.

Guarda con:
`Ctrl + O` → Enter → `Ctrl + X`

---

## 2️⃣ Reinicia TLP o reinicia el equipo

Sin reiniciar el sistema:

```bash
sudo tlp start
```

---

## 3️⃣ Verifica que quedó activado

```bash
tlp-stat -b
```

Deberías ver algo así:

```
/sys/class/power_supply/BAT0/charge_control_end_threshold = 80 [%]
```

Y cuando la batería llegue al **80% enchufado, dejará de cargar** ✔

---

# 🔁 Para volver a cargar al 100% (si algún día lo necesitas)

Edita otra vez `/etc/tlp.conf`:

```ini
STOP_CHARGE_THRESH_BAT0=100
```

Y aplica:

```bash
sudo tlp start
```

---

# 🧠 Qué está pasando “por debajo”

TLP está escribiendo en este archivo del kernel:

```
/sys/class/power_supply/BAT0/charge_control_end_threshold
```

Si quisieras probarlo manualmente (no necesario, pero sirve para ver que funciona):

```bash
echo 80 | sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold
```

Solo que **TLP lo deja persistente entre reinicios** — por eso es mejor usarlo.

---

# ℹ️ Detalles sobre tu batería

Tu salida muestra:

```
energy_full_design = 42067 mWh
energy_full        = 38287 mWh
```

Eso significa:

🟢 Capacidad actual ≈ **91% de fábrica**
(lo cual es muy bueno)

💡 Limitar la carga a 80% **reducirá el desgaste futuro**.

---

# ⚠️ Nota importante

En ASUS modernos:

* Solo **STOP_CHARGE_THRESH_BAT0 funciona**
* No existe un límite inferior (START) configurable oficialmente
* El cargador puede reconectar cuando baja lo suficiente (suele ser ~78–79%)

Eso es normal.

---

# 🎯 Resumen claro

✔ Tu portátil **sí soporta límite de carga por hardware**
✔ La forma correcta en Linux Mint es **TLP con plugin ASUS**
✔ Solo necesitas definir:

```ini
STOP_CHARGE_THRESH_BAT0=80
```

✔ Y TLP se encarga solo, siempre.
