'''
Clase25-Python Funciones
Clase 24-Python02 / Clase21.pdf
'''
# Funciones con parametros
def mensaje(saludo):
    print(saludo)

def carga():
   valor1=int(input("Introduzca el valor 1: "))
   valor2=int(input("Introduzca el valor 2: "))
   valores=[valor1, valor2]
   print("Los valores son: {}".format(valores))
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



#return permite saltarse el scope y devolver los valores por fuera
def retornar_superficie(lado):
    return lado*lado

va=int(input("Ingrese el valor del lado del cuadrado: "))
superficie = retornar_superficie(va)
print("La superficie del cuadrado es: {} m2".format(superficie))



# [10,56,23,120,94]
def sumarizar(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma

# [10,56,23,120,94]
def mayor(lista):
    may = lista[0]
    # ya asignamos primer valor, no hay que recorrerlo de vuelta
    # conviene partir desde el 2 elemento
    for x in range(1,len(lista)): 
        if lista[x]>may:
            may=lista[x]
        return may
    
def menor(lista):
    men = lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
        return men

lista_valores = [10,56,23,120,94]
print("La lista completa es: {}".format(lista_valores))
print("La suma de sus elementos es: {}".format(sumarizar(lista_valores)))
print("El menor num es: {}".format(menor(lista_valores)))


# Idealmente, para mejor performance, iterar una sola vez
def mayormenor(lista):#[1,2,3,4,5]
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("El valor mayor de la lista es: {}".format(may))
    print("El valor menor de la lista es: {}".format(men))          

                
# bloque principal

lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)
mayormenor(lista) #[1,2,3,4,5]


    
lista = [1,2,3,4,5]
mayormenor(lista)



# ej12.py
'''Desarrollar un programa que permita cargar 5 nombres de personas y
 sus edades respectivas.
Luego de realizar la carga por teclado de todos los datos imprimir los nombres 
de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas'''

#nom=["emi", "juan", "claudia"]
#ed= [15       ,40,     36]

def cargar_datos():
    nom=[]
    ed=[]
    for x in range(5):
        v1=input("Ingrese el nombre de la persona:")
        nom.append(v1)
        v2=int(input("Ingrese la edad:"))
        ed.append(v2)
    return [nom,ed]

#nom=["emi", "juan", "claudia"]
#ed= [15       ,40,     15]
def mayores_edad(nom,ed):
    print("Nombres de personas mayores de edad")
    for x in range(len(nom)):      
        if ed[x]>=18:              
            print(nom[x])


def promedio_edades(ed):
    suma=0
    for x in range(len(ed)):
        suma=suma+ed[x]
    promedio=suma//5
    print("Edad promedio de las personas: {}".format(promedio))
    

# bloque principal

nombres,edades=cargar_datos()
mayores_edad(nombres,edades)
promedio_edades(edades)



# Cantidad variable de parametros
def sumar(v1,v2,*cualca):
    suma = v1 + v2
    for x in range(len(cualca)):
        suma = suma + cualca[x]
    return suma

print("1+2 = {}".format(sumar(1,2)))
print("1+2+4 = {}".format(sumar(1,2,4)))
print("1+2+3+4+5+6+7+8+9+10 = {}".format(sumar(1,2,3,4,5,6,7,8,9,10)))



# ej13.py
# En caso de que falte un caracter, se pone & por defecto
def titulo_subrayado(titulo,caracter="&"):
    print(titulo)
    print(caracter*len(titulo))
    
titulo_subrayado("Sistema")
titulo_subrayado("Ventas","-")



# ej14.py
# Python permite saltearse el orden
# Paso parametros por nombre de argumento
def calcular_sueldo(nombre, costo_hora, cantidad_horas):
    sueldo = costo_hora * cantidad_horas
    print("{} trabajó {} horas y cobra un sueldo de ${}".format(nombre, cantidad_horas, sueldo))

calcular_sueldo("Juan", 10, 120)
calcular_sueldo(costo_hora=12, cantidad_horas=40, nombre="Ana")
calcular_sueldo(cantidad_horas=90, nombre="Luis" ,costo_hora=12)
