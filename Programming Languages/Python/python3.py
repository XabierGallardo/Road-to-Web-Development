'''
Clase25-Python Funciones

'''
# Funciones con parametros
def mensaje(saludo):
    print(saludo)

def carga():
   valor1=int(input("Introduzca el valor 1: "))
   valor2=int(input("Introduzca el valor 2: "))
   suma(valor1, valor2)
   
def suma(valor1, valor2):
    suma = valor1+valor2
    print(suma)

mensaje("Hola")
carga()
mensaje("chau nos vimos")



def carga_suma(cantidad_veces):
    for x in range(cantidad_veces):
        valor1=int(input("Introduzca el valor 1: "))
        valor2=int(input("Introduzca el valor 2: "))
        suma=valor1 + valor2
        print("La suma de los dos valores es {}".format(suma))

def separacion():
    print("************************")
    
cantidad = int(input("Introduzca el numero de sumas: "))
carga_suma(cantidad)
#carga_suma(3)
separacion()

#42:03
