# JavaScript variales
Tiene sentido asignar variables `const` en el siguiente ejemplo?
```js
const personas = [
    { nombre: 'Ana', edad: 25 },
    { nombre: 'Juan', edad: 17 },
    { nombre: 'María', edad: 30 }
];

const mayores = personas.filter(persona => persona.edad >= 18);
console.log(mayores);
```

## Reasignacion y cambio de valor
Es correcto señalar que `const` se usa para declarar variables que no cambiarán su valor (no se pueden reasignar). **Sin embargo, en el caso de arrays y objetos, `const` no impide que su contenido interno cambie, solo evita que la variable sea reasignada a un nuevo array u objeto**. 

## Explicación detallada:

### Uso de `const` con arrays y objetos:
1. **No se puede reasignar la variable**:
   ```javascript
   const personas = [/*...*/];
   personas = []; // Error: no se puede reasignar
   ```

2. **Pero sí se puede modificar el contenido**:
   ```javascript
   const personas = [/*...*/];
   personas.push({nombre: 'Carlos', edad: 20}); // Esto SÍ funciona
   ```

### ¿Por qué usar `const` en este ejemplo?
1. **Intención semántica**: Estás comunicando que la referencia al array no cambiará (aunque su contenido pueda cambiar)
2. **Buenas prácticas**: Es preferible usar `const` por defecto y solo usar `let` cuando necesites reasignar
3. **Inmutabilidad**: En el ejemplo específico, `filter()` crea un NUEVO array (`mayores`), no modifica el original

### Ejemplo con reasignación (que NO funcionaría):
```javascript
const mayores = personas.filter(p => p.edad >= 18);
mayores = []; // Error: no se puede reasignar una constante
```

### Casos donde usarías `let`:
```javascript
let resultados = personas.filter(p => p.edad >= 18);
resultados = resultados.concat(otrosMayores); // Necesitas let para reasignar
```

## Diferencias clave:
|               | `const`                  | `let`                    |
|---------------|--------------------------|--------------------------|
| Reasignación  | No permitida             | Permitida                |
| Modificación  | Permitida (en objetos/arrays) | Permitida         |
| Uso recomendado | Por defecto           | Cuando necesites reasignar |

En tu ejemplo, `const` es la elección correcta porque:
1. No estás reasignando `personas` ni `mayores`
2. Refleja mejor la intención del código
3. Previene accidentalmente reasignaciones futuras