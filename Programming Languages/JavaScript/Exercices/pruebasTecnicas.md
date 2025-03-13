## 1 [Isogramas en JavaScript](https://github.com/goncy/interview-challenges/tree/main/ejercicios-algoritmos/sesion-1/isograma)
Un isograma es una palabra que no tiene letras repetidas
```js
// Isogramas, palabras que no tienen letras repetidas
/* murcielago -> true, reto -> false, casa -> false
   perro -> false, PeRrO  -> true, GaTo -> true */

function esIsograma(palabra) {

  // Filtro strings vacios
  if(palabra === "") {
    return true;
  }
  
  // Filtrar mas de una palabra
  if(palabra.includes(" ")) {
    return false;
  }
  
  // Array vacio y array con caracteres separados de nuestro string
  let arrayUnico = [];
  let arrayPalabra = palabra.split('');
  
  // Se itera y solo se guardan las letras que no estén repetidas
  for(const letra of palabra) {
    
    if(!arrayUnico.includes(letra)){
      arrayUnico.push(letra);
      console.log(arrayUnico);
      
      // Si los dos arrays son identicos, devuelve true
      if(JSON.stringify(arrayUnico) === JSON.stringify(arrayPalabra)) {
        return true
      }
      
    } else {
      // Si se va a guardar una letra repetida devuelve false
      return false
    }
  }
}

console.log(esIsograma("gato"))
```