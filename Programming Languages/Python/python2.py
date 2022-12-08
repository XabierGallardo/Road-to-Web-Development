'''
Python Clase 02
Clase 24-Python02 / Clase21.pdf
'''
suma = 0
for contador in range(3):
    valor=int(input("Carga el valor {}: ".format(contador+1)))
    suma+=valor
    
print("La suma es {} y el promedio es {}".format(suma,suma/3))



nota1 = 6
nota2 = 7
nota3 = 5
promedio = (nota1 + nota2 + nota3)/3

if promedio >= 7:
    print("Promocionado")
elif promedio >= 4:
    print("Regular")
else:
    print("Reprobado")



for x in range(100):
    print(x)



contador = 1
while contador <=100:
    print(contador)
    contador+=1


'''
Desarrollar un programa que permita la carga de 5 valores por teclado
y nos muestre posteriormente la suma de los valores ingresados
y su promedio
'''

suma = 0
contador = 0
while contador<5:
    valor = int(input("Ingrese el valor {}: ".format(contador+1)))
    suma += valor
    contador+=1

promedio = suma/contador
print("La suma es {} y el promedio {}".format(suma, promedio))



'''
Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad
de piezas a procesar y luego ingrese la longitud de cada perfil,
sabiendo que la pieza cuya longitud esté comprendida en el rango de
1.20 y 1.30 son aptas.
Imprimir por pantalla la cantidad de piezas aptas.
'''

piezas_validas = 0;
cantidad = int(input("Ingrese la cantidad de piezas: "))

for x in range(cantidad):
    largo = float(input("Ingrese el largo de las piezas: "))
    if largo >= 1.20 and largo <= 1.30:
        piezas_validas+=1

print("El num de piezas validas es: {}".format(piezas_validas))


'''
for loops is used when you have definite itteration (the number of iterations is known).


for i in range(11):
    print i
    
i = 0
while i <= 10:
    print i
    i+=1
'''

for x in range(20,35):
    print(x)
    
for x in range(0,100,5):
    print(x)



'''
Escribir un programa que solicite 10 notas de alumnos
y nos informe cuantos tienen notas mayores e iguales
a 7 y cuantos menores
'''
'''
Escribir un programa que solicite 10 notas de alumnos
y nos informe cuantos tienen notas mayores e iguales
a 7 y cuantos menores
'''
aprobados = 0
desaprobados = 0

for x in range(10):
    notas=int(input("Introduzca la nota {}: ".format(x+1)))
    if notas >= 7:
        aprobados+=1
    else:
        desaprobados+=1

print("El num de aprobados es {} y el de desaprobados es {}".format(aprobados, desaprobados))

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".



'''
Dada la lista de colores, indicar la posición
y el elemento que posee
'''
lista = ["azul", "rojo", "amarillo", "verde"]
for elemento in range (len(lista)):
    print("Elemento: {} - Valor: {}".format(elemento, lista[elemento]))