#Universidad Nacional Autonoma de Mexico/ Facultad de Ingenieria
#Lenguajes de programacion
#Alumnos:
#-Banda Martínez César Eduardo
#-Barriga Martínez Diego Alberto
#-Quezada Tapia Abraham
#Programa: Operaciones de polinomios de grado N
#Hecho en Python 3.6

#Inicio de programa
#Importando modulos
import os
#Variables globales
i=0
j=0
l=0
k=0
sentinela = 1
m=1
resultado=0

def grado():
	grado = int(input("Introduce el grado maximo del polinomio: "))
	return grado

def crea_polinomio():
	i=0
	grado1 = grado()
	polinomio= []
	while i < grado1+1:
		coeficiente = int(input(("Inserta el valor del coeficiente para x^"+str(i)+": ")))
		polinomio.append(coeficiente)
		i=i+1
	return polinomio

def valor_punto(polinomio1):
	print("==============Valor calculado en un punto==============\n")
	punto = int(input("Ingresa el valor de x: "))
	z=0
	potencias=[]
	for j in range(0, len(polinomio1)):
		potencias.insert(j,pow(punto,z))
		z=z+1
	multiplicacion = 0

	for k in range(0,len(polinomio1)):
		multiplicacion = multiplicacion + (polinomio1[k]*potencias[k])
		k=k+1
	print("El valor calculado es: "+str(multiplicacion))
	print("")

def suma_polinomios(polinomio1):
	print("==============Suma de Polinomios==============\n")
	print("Los polinomios deben ser del mismo grado")
	suma=[]
	polinomio_aux = crea_polinomio()
	for i in range(0, len(polinomio1)):
		suma.append(polinomio1[i]+polinomio_aux[i])

	print("\t\tEl polinomio resultante es: ", end="")
	for j in range(0, len(suma)):
		print("+("+str(suma[j])+")"+"x^"+str(j), end="")
	print("")

	return suma

def resta_polinomios(polinomio1):
	print("==============Resta de Polinomios==============\n")
	print("Los polinomios deben ser del mismo grado")
	resta=[]
	polinomio_aux = crea_polinomio()
	for i in range(0, len(polinomio1)):
		resta.append(polinomio1[i]-polinomio_aux[i])

	print("El polinomio resultante es: ", end="")
	for j in range(0,len(resta)):
		print("+("+str(resta[j])+")"+"x^"+str(j), end = "")
	print("")

	return resta

def polinomio_opuesto(polinomio1):
	print("==============Polinomios opuestos==============\n")
	print("NOTA: Los polinomios deben ser del mismo grado")
	opuesto = []
	polinomio_aux = crea_polinomio()

	for i in range(0, len(polinomio_aux)):
		opuesto.append(-(polinomio_aux[i]))

	if polinomio1 == opuesto:
		print("Los polinomios son opuestos")
	else:
		print("Los polinomios no son opuestos")

def multiplica_polinomios(polinomio1):
	"""NO FUNCIONA CORRECTAMENTE"""
	print("==============Multiplicacion de Polinomios==============\n")
	producto = []
	polinomio_aux = crea_polinomio()
	for i in range(0, len(polinomio1)):
		producto.append(polinomio1[i]*polinomio_aux[i])

	print("El polinomio resultante es: ", end="")
	for j in range(0,len(producto)):
		print("+("+str(producto[j])+")"+"x^"+str(j), end = "")
	print("")

	return producto
	
def main(polinomio1):
	while sentinela != 0:
		print("""
			1-Valor calculado en un punto
			2-Suma
			3-Resta
			4-Igualdad de 2 polinomios
			5-Polinomio opuesto
			6-Multiplicacion
			0-Salir
			""")

		print("\t\tPolinomio: ", end="")
		for l in range(len(polinomio1)):
				print("+("+str(polinomio1[l])+")"+"x^"+str(l)+" ", end="")
		print("")
		opcion=int(input("Escoge una opcion: "))

		#Valor en un punto
		if opcion==1:
			valor_punto(polinomio1)

		#Suma de dos polinomios
		elif opcion==2:
			polinomio1 = suma_polinomios(polinomio1)

		#Resta de polinomios
		elif opcion==3:
			polinomio1 = resta_polinomios(polinomio1)	
				
		#Igualdad de polinomios
		elif opcion==4:
			igualdad=[]
			polinomio1 = polinomioUno()
			polinomio2 = polinomioDos()
			if grado2 == grado1:
			   print("El grado del polinomio es igual")
			print("El grado del polinomio no es igual")
		elif opcion == 5:
			polinomio_opuesto(polinomio1)
		elif opcion == 6:
			polinomio1 = multiplica_polinomios(polinomio1)
		elif opcion == 0:
			break
		else:
			print("*Error* Intenta otra opcion *Error*")

os.system("CLS")
main(crea_polinomio())