'''
Clase 26 - Python POO
Clase23.pdf
Un objeto es una encapsulación genérica de datos
y de los procedimientos para manipularlos.
La clase es la plantilla con la que creamos objetos

El objeto es una instancia de la clase,
al crear un objeto se adquieren sus atributos y métodos
'''
class Persona:
    piernas=2

    def inicializar(self,nombre):
        self.nombre=nombre
    
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))

persona1=Persona() #Creamos el OBJETO persona1
persona1.inicializar("Pedro")
persona1.imprimir()
print(persona1) # Imprimimos la posición de memoria del objeto

persona2=Persona()
persona2.inicializar("Maria")
persona2.imprimir()
print(persona2)



# Ejercicio 2
class Alumno:
    
    def inicializar(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Nota: {}".format(self.nota))
        print("\n")
        
    def mostrar_estado(self):
        if self.nota >=4:
            print("Regular")
        else:
            print("Desaprobado")

alumno1=Alumno()
alumno1.inicializar("Diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("Ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()



# Ejercicio 3
'''
To understand the meaning of classes
we have to understand the built-in __init__() function.

All classes have a function called __init__(),
which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created:

The __init__() function is called automatically
every time the class is being used to create a new object.
'''
class Empleado:
    
    # init se ejecuta automaticamente cuando se inicializa la clase
    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado: ")
        self.sueldo=float(input("Ingrese el sueldo: "))
        
    # Una vez llamado al objeto, borramos su espacio en memoria
    # uno de sus usos es cerrar la conexion a la BD y limpiar memoria
    def __del__(self):
        print("Metodo delete llamado")
        
    def imprimir(self):
        print("Nombre: {}".format(self.nombre))
        print("Sueldo: {}".format(self.sueldo))
        
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

'''
__srt__()

The __str__() function controls what should be returned
when the class object is represented as a string.

If the __str__() function is not set, the string representation
of the object is returned:



self

The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:
'''

# Ejercicio 5
class Operacion:
    
    def __init__(self):
        self.valor1=int(input("Ingrese primer valor: "))
        self.valor2=int(input("Ingrese segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()
        
    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es: {}".format(suma))
    
    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es: {}".format(resta))
    
    def multiplicar(self):
        multi=self.valor1*self.valor2
        print("La multiplicacion es: {}".format(multi))
    
    def dividir(self):
        div=self.valor1/self.valor2
        print("La division es: {}".format(div))
    
    
operacion1=Operacion()



# Ejercicio 6
class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion!=4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.notas_altas()

    def cargar(self):
        for x in range(5):
            nombre=input("Ingrese nombre del alumno:")
            self.nombres.append(nombre)
            nota=int(input("Nota del alumno:"))
            self.notas.append(nota)

    def listar(self):
        print("Listado completo de alumnos")
        for x in range(5):
            print("{} - {}".format(self.nombres[x],self.notas[x]))
        print("_____________________")
        
    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for x in range(5):
            if self.notas[x]>=7:
                print("{} - {}".format(self.nombres[x],self.notas[x]))
            print("_____________________")                


# bloque principal
alumnos=Alumnos()
alumnos.menu()



'''
# Ejercicio 7
Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco
requiere que al final del día calcule la cantidad de dinero que hay depositado.
'''
class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

    def extraer(self,monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print("{} tiene depositada la suma de {}".format(self.nombre,self.monto))


class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es: {}".format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


# bloque principal        

banco1=Banco()
banco1.operar()
banco1.depositos_totales()



'''
Ejercicio 8
Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino
"perdió"
'''
import random

class Dado:

    def tirar(self):
        self.valor=random.randint(1,6)

    def imprimir(self):
        print("Valor del dado: {}".format(self.valor))

    def retornar_valor(self):
        return self.valor


class JuegoDeDados:

    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        if self.dado1.retornar_valor()==self.dado2.retornar_valor() and self.dado1.retornar_valor()==self.dado3.retornar_valor():
            print("Ganó")
        else:
            print("Perdió")


# bloque principal del programa

juego_dados=JuegoDeDados()
juego_dados.jugar()