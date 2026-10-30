# Cuándo usar `event.stopPropagation()`?
**Hay propagacion cuando hay anidacion? hay propagacion cuando es un contenido dinamico?**

La propagación está relacionada principalmente con la relación entre los elementos del DOM, no con que el contenido sea estático o dinámico.

Vamos por partes.

## 1. ¿Hay propagación cuando hay anidación?

Sí. Cuando tenés elementos HTML anidados, los eventos que admiten propagación (como `click`, `submit`, `input`, etc.) pueden propagarse desde el elemento objetivo hacia sus elementos antecesores.

Ejemplo:

```html
<div id="abuelo">
    <div id="padre">
        <button id="hijo">Click</button>
    </div>
</div>
```

```javascript
document.getElementById("abuelo").addEventListener("click", () => {
    console.log("Abuelo");
});

document.getElementById("padre").addEventListener("click", () => {
    console.log("Padre");
});

document.getElementById("hijo").addEventListener("click", () => {
    console.log("Hijo");
});
```

Al hacer clic en el botón:

text

```
Hijo
Padre
Abuelo
```

Esto es event bubbling.

Importante: la propagación no significa que todos los elementos anidados tengan que tener listeners. Significa que el evento puede recorrer sus antecesores y ejecutar los listeners que encuentre.

---

## 2. ¿Hay propagación cuando el contenido es dinámico?

Sí. Que un elemento se haya creado dinámicamente mediante JavaScript no modifica el mecanismo de propagación.

Por ejemplo, en tu código tenés:

```javascript
contenedorProductos.innerHTML = `
    <ul>
        <li>
            <button id="updateProduct-button">
                Actualizar producto
            </button>
        </li>
    </ul>
`;
```

Ese botón fue creado dinámicamente.

Sin embargo, cuando hacés clic en él, su evento sigue propagándose normalmente por el DOM:

text

```
button
  ↑
li
  ↑
ul
  ↑
contenedorProductos
  ↑
main
  ↑
body
```

La propagación funciona exactamente igual que con elementos creados directamente en HTML.


---


## 3. Una particularidad importante: delegación de eventos

Acá aparece algo muy interesante.

Imaginemos que querés escuchar los clics de todos los botones que se creen dinámicamente dentro de `contenedorProductos`.

En lugar de agregar un listener a cada botón, podés agregar uno solo al contenedor:

```javascript
contenedorProductos.addEventListener("click", event => {

    if (event.target.id === "updateProduct-button") {
        console.log("Actualizar producto");
    }

});
```

¿Por qué funciona?

1. El usuario hace clic en el botón dinámico.
2. Se dispara el evento `click`.
3. El evento se propaga hacia sus antecesores.
4. Llega a `contenedorProductos`.
5. Su listener detecta que el objetivo original fue el botón.

Esto se conoce como delegación de eventos (Event Delegation).

Es especialmente útil cuando trabajás con listas, tablas, productos o elementos que se generan dinámicamente.

## 4. Resumen: tres conceptos diferentes

| Situación | ¿Hay propagación? |
| --- | --- |
| Elementos HTML anidados | Sí, si el evento admite propagación |
| Elementos creados dinámicamente | Sí, si el evento admite propagación |
| Elementos sin relación de parentesco | No se propagan eventos entre ellos directamente |

Regla mental para recordar

- Anidación: permite que el evento suba por los antecesores.
- Contenido dinámico: también participa de la propagación.
- Delegación: aprovecha esa propagación para escuchar eventos desde un elemento antecesor.
- `stopPropagation()`: permite detener ese recorrido.

Mi recomendación: prestale especial atención a la delegación de eventos. En tu proyecto, donde utilizás `innerHTML` para crear productos y botones dinámicamente, es una técnica que te puede simplificar bastante el código.