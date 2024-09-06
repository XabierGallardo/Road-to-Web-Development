# Markup Languages

# CSS
## Margin Collapse
El fenómeno por el cual la etiqueta `margin` de un elemento hijo no separa dicho elemento del contenedor padre en CSS se conoce como **colapso de márgenes** (*margin collapsing*). Este es un comportamiento estándar en CSS que afecta a los márgenes verticales (márgenes `top` y `bottom`) en ciertas situaciones.

### **¿Qué es el colapso de márgenes?**

El colapso de márgenes ocurre cuando dos márgenes verticales adyacentes (de un elemento hijo y su contenedor padre, o entre dos elementos hermanos) se combinan o "colapsan" en un solo margen. En lugar de que los márgenes se sumen, se toma solo el margen más grande de los dos.

### **Por qué sucede con los elementos hijos y el contenedor padre:**

Si un contenedor padre no tiene relleno (`padding`), borde (`border`), o contenido entre su margen superior e inferior y el de su hijo, el margen superior o inferior del hijo puede "colapsar" con el margen del padre. Esto significa que en lugar de sumar ambos márgenes, se visualiza solo el más grande de los dos.

#### **Ejemplo:**
```html
<div class="padre">
  <div class="hijo">Contenido</div>
</div>
```

```css
.padre {
  background-color: lightgray;
  margin: 20px;
}

.hijo {
  background-color: lightblue;
  margin: 30px 0;
}
```

En este caso, esperarías que el `hijo` tuviera un margen de 30px dentro del `padre`, pero puede parecer que el `padre` no se separa correctamente de su contenedor o de otros elementos debido al colapso de márgenes.

### **Cómo evitar el colapso de márgenes:**

Para asegurarte de que el margen del elemento hijo se respete dentro del contenedor, puedes aplicar alguna de las siguientes soluciones:

1. **Agregar un `padding` o `border` al contenedor padre**:
   Cuando el contenedor tiene un `padding` o `border`, el colapso de márgenes no ocurre.
   
   ```css
   .padre {
     background-color: lightgray;
     padding: 1px; /* Evita el colapso de márgenes */
   }
   ```

2. **Establecer `overflow: hidden` o `overflow: auto` en el contenedor padre**:
   Esto crea un nuevo contexto de formato que impide el colapso de márgenes.
   
   ```css
   .padre {
     overflow: hidden; /* Previene el colapso */
   }
   ```

3. **Usar `display: flex` o `display: grid` en el contenedor padre**:
   Los contenedores flexibles o de cuadrícula no colapsan márgenes con sus hijos.
   
   ```css
   .padre {
     display: flex;
   }
   ```

4. **Cambiar el flujo de diseño del hijo con `float` o `position: absolute`**:
   Un elemento que está flotando o posicionado absolutamente tampoco participará en el colapso de márgenes.
   
   ```css
   .hijo {
     float: left; /* Evita el colapso */
   }
   ```

### **Resumiendo**:
El colapso de márgenes en CSS ocurre cuando los márgenes verticales adyacentes se combinan en uno solo, causando que el margen del hijo no parezca separar el elemento hijo del contenedor padre. Puedes evitarlo usando `padding`, `border`, `overflow`, o alterando el flujo de diseño del contenedor o del hijo.