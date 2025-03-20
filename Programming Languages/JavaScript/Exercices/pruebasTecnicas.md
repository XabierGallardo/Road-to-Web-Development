## 1 [Isogramas en JavaScript](https://github.com/goncy/interview-challenges/tree/main/ejercicios-algoritmos/sesion-1/isograma)
```js
/* 
  1. Isograma
  Un isograma es una palabra que no tiene letras repetidas

  murcielago -> true, reto -> false, casa -> false
  perro -> false, PeRrO  -> true, GaTo -> true 
*/

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


## 2 [Elementos pares](https://github.com/goncy/interview-challenges/tree/main/ejercicios-algoritmos/sesion-1/elementos-pares)
```js
/* 
  2. Elementos pares

  Dada una lista de elementos (array), crear una funcion que retorne una nueva lista con solo los elementos que aparecen una cantidad pares de veces.
  **EXTRA, AGREGADA NUEVA LISTA CON NUMERO DE REPETICIONES DE CADA ELEMENTO UNICO**

  Ejemplo
  ["A","B","A","C","C","C","C"] // -> ["A","C"]
  [1,2,3,1,2] // -> [1,2]
*/


// Resolucion
function nuevoArray(arr) {
  let listaUnica = [];
  let contador = 0;
  let listaContador = [];
  let listaPar = [];
  
  // Armar lista unica para tener nuestros indices para la busqueda
  for(let elemento of arr) {
    // Separar elementos unicos
    if(!listaUnica.includes(elemento)) {
      listaUnica.push(elemento)
      console.log(listaUnica);
    } 
  }
  
  for(let i = 0; i < listaUnica.length; i++) {
    
    for(let x = 0; x < arr.length; x++) {
      
      if(listaUnica[i] === arr[x]) {
        contador++;
      }
    }
    listaContador.push(listaUnica[i]);
    listaContador.push(contador);
    if(contador % 2 === 0) {
      listaPar.push(listaUnica[i]);
    }
    contador = 0;
    
    console.log(listaContador)
  }
  console.log("La lista par es: ", listaPar)
}

nuevoArray(["A","B","A","C","C","C","C"]);
```


## 3 [Letras por numeros](https://github.com/goncy/interview-challenges/tree/main/ejercicios-algoritmos/sesion-1/letras-por-numeros)
```js
/*
  3. Letras por numeros
  Reemplazar las letras de un string por su index en el alfabeto (e.g. A = 1 , B = 2 , C = 3 ...)

  Consideraciones Adicionales:
  - Ignorar espacios.
  - Hacer clean up del string antes de comenzar el swap (para eliminar acentos y caracteres especiales, se sugiere meter en este proceso de clean up el ignorado de espacios).
*/

let abecedario = "abcdefghijklmnopqrstuvwxyz";

function cambiarNumeros (palabra) {
  let nuevoString = "";
  
  // Eliminando todos los espacios en el string
  let formato = palabra.replaceAll(" ", ""); 
  
  for(let letra of formato) {
      nuevoString += `${abecedario.indexOf(letra)}, `
  }
  
  palabra = nuevoString.trim(" ").slice(0, -1);
  return palabra;  
}

cambiarNumeros("pal abra ");
```