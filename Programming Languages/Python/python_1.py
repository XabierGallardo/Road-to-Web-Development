'''
Python introduccion
https://www.youtube.com/watch?v=BojVB1xyrKo&list=PLgQsqQBBk3lppK4L-1zixaF2rREZ_Vyyu&index=23

Clase 23 - Python / Clase20-Python.pdf
'''

# Import math Library
import math

# Python Introduccion
print("Hola mundo!")

nombre = input("Mete tu nombre: ")
#nombre = "Xan"

if (nombre[0]=="e" or nombre[0]=="E"):
    print("tu nombre empieza con e")
    print("esto tambien lo lee")
else:
    print("tu nombre no empieza con e")
    
print(len(nombre))
print (nombre.capitalize())

# https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-las-cadenas/



numeros = [2,6,7,6,2,4]
suma = 0
for n in numeros:
    suma += n

print (suma)
print (7 in numeros)
print (8 not in numeros)

edad = 40
edadStr = "40"
print (nombre + " tiene " + edadStr + " años")

print("{} tiene {} años".format(nombre, edad))



def suma(a,b):
    return a+b

print(suma(5,7))
print(5/2)



verdad = True
print(not verdad)

lista = [1,2,3,4,5,6,7,8]

print(lista[2:4])
print(lista[3:])
print(lista[-1])

lista.append(100)
print(lista)

eliminado = lista.pop(2)
print(eliminado)
print(math.pi)
