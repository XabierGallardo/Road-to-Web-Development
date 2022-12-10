# Programación Orientada a Objetos
*Clase 23.pdf*

## Introducción
Python nos permite utilizar distintas metodologías de programación, prácticamente todos los lenguajes de los últimos 25 años implementan la posibilidad de trabajar con POO.

Python permite trabajar con
- **Programación Lineal**: Cuando desarrollamos todo el código sin emplear funciones. El código es una secuencia lineal de comandos.

- **Programación Estructurada**: Cuando planteamos funciones que agrupan actividades a desarrollar y luego dentro del programa llamamos a dichas funciones, bien dentro del mismo archivo (módulo) o en una librería separada.

- **Programación Orientada a Objetos**: Es cuando planteamos clases y definimos objetos de las mismas.

## Objeto
Un objeto es una encapsulación genérica de datos y de los procedimientos para manipularlos.
**La clase es la plantilla con la que creamos objetos**
El objeto es una instancia de la clase, al crear un objeto se adquieren sus atributos y métodos
```py
class Persona:
	piernas=2

	def inicializar(self,nombre):
		self.nombre=nombre
	
	def imprimir(self):
		print("Nombre: {}".format(self.nombre))

persona1=Persona() #Creamos el OBJETO persona1
```

