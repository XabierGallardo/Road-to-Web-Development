## Self en Python
En Python, `self` es una convención utilizada para referirse al objeto actual en el que se está trabajando dentro de una clase. Cuando se define un método en una clase, el primer parámetro de ese método (usualmente llamado `self`) se refiere al objeto mismo en el que se está invocando el método.

Por ejemplo, considera la siguiente clase `Persona`:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años.")
```

En este ejemplo, `self` se utiliza dentro de los métodos `__init__()` y `saludar()`. Cuando se crea una instancia de la clase `Persona`, como en el siguiente código:

```python
persona1 = Persona("Juan", 30)
persona1.saludar()
```

La referencia `self` dentro del método `saludar()` apunta a `persona1`. Esto permite acceder a los atributos `nombre` y `edad` específicos de esa instancia particular de la clase.

La palabra clave `self` no es una palabra reservada en Python; de hecho, puedes llamarla de cualquier manera, pero se ha vuelto una convención y es ampliamente utilizada por los programadores de Python para hacer el código más legible y fácil de entender. Sin embargo, es importante respetar esta convención para evitar confusión en el código, especialmente cuando se trabaja con otros desarrolladores o se sigue un código base preexistente.