'''
num = int(input("Ingrese un numero: "))
i=1
while num > 0:
    i=i*num
    num -=1
print(f'El resultado de i es: {i}')
'''

# Ejercicio 6

class Alumnos:
	def __init__(self):
		self.nombres=[]
		self.notas=[]
		self.listar()

	def listar(self):
		print("Listado completo de alumnos:")
		for x in range(5):
			print("{} - {}".format(self.nombres[x], self.notas[x]))
		print("__________________")


alumnos=Alumnos()
