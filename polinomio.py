#Universidad Nacional Autonoma de México/ Facultad de Ingeniería
#Lenguajes de programación
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
sentinela = 1

def grado():
	grado = int(input("Introduce el grado maximo del polinomio: "))
	return grado

def crea_polinomio():
	i=0
	grado_ini = grado()
	polinomio = []
	while i < grado_ini+1:
		coeficiente = int(input(("Inserta el valor del coeficiente para x^"+str(i)+": ")))
		polinomio.append(coeficiente)
		i += 1
	return polinomio

def valor_punto(polinomio):
	print("==============Valor calculado en un punto==============\n")
	punto = int(input("Ingresa el valor de x: "))
	z = 0
	potencias=[]
	for j in range(0, len(polinomio)):
		potencias.insert(j,pow(punto,z))
		z+=1
	multiplicacion = 0
	print("\t\t==========================================")
	for k in range(0,len(polinomio)):
		multiplicacion = multiplicacion + (polinomio[k]*potencias[k])
		k+=1
	print("\t\t\tEl valor calculado es: "+str(multiplicacion))
	print("\t\t==========================================")
	print("")

def suma_polinomios(polinomio):
	print("==============Suma de Polinomios==============\n")
	print("Los polinomios deben ser del mismo grado")
	suma = []
	polinomio_aux = crea_polinomio()
	for i in range(0, len(polinomio)):
		suma.append(polinomio[i]+polinomio_aux[i])

	print("\t\t==========================================")
	print("\t\tEl polinomio resultante es: ", end="")
	for j in range(0, len(suma)):
		print("+("+str(suma[j])+")"+"x^"+str(j), end="")
	print("\n\t\t==========================================")
	print("")

	return suma

def resta_polinomios(polinomio):
	print("==============Resta de Polinomios==============\n")
	print("Los polinomios deben ser del mismo grado")
	resta=[]
	polinomio_aux = crea_polinomio()
	for i in range(0, len(polinomio)):
		resta.append(polinomio[i]-polinomio_aux[i])
	
	print("\t\t==========================================")
	print("\t\tEl polinomio resultante es: ", end="")
	for j in range(0,len(resta)):
		print("+("+str(resta[j])+")"+"x^"+str(j), end = "")
	print("\n\t\t==========================================")

	print("")
	return resta


def igualdad_polinomio(polinomio):
	print("==============Igualdad de polinomios==============\n")
	print("NOTA: Los polinomios deben ser del mismo grado")
	polinomio_aux = crea_polinomio()
	print("\t\t==========================================")
	if polinomio != polinomio_aux:
		print("\t\t\tLos polinomios son DIFERENTES")
	else:
		print("\t\t\tLos polinomios son IGUALES")
	print("\t\t==========================================")

def polinomio_opuesto(polinomio):
	print("==============Polinomios opuestos==============\n")
	print("NOTA: Los polinomios deben ser del mismo grado")
	opuesto = []
	polinomio_aux = crea_polinomio()

	for i in range(0, len(polinomio_aux)):
		opuesto.append(-(polinomio_aux[i]))
	print("\t\t==========================================")
	if polinomio == opuesto :
		print("\t\t\tLos polinomios SON opuestos")
	else:
		print("\t\t\tLos polinomios NO son opuestos")
	print("\t\t==========================================")

def multiplica_polinomios(polinomio):
	"""NO FUNCIONA CORRECTAMENTE"""
	print("==============Multiplicacion de Polinomios==============\n")

	polinomio_aux = crea_polinomio()
	grado_ini = len(polinomio)-1
	grado_aux = len(polinomio_aux)-1
	grado_total = grado_ini + grado_aux

	producto = []
	resultado = []
	if grado_aux > grado_ini:
		for su in range(0, grado_aux):
			producto.append(0)
			producto[su] = list(range(grado_total+1))

	elif grado_aux < grado_ini:
		for su in range(0, grado_ini):
			producto.append(0)
			producto[su] = list(range(grado_total+1))
			
	else:
		for su in range(0, grado_aux): #Arbitrario po ser de igual grado
			producto.append(0)
			producto[su] = list(range(grado_total+1))
	

	for i in range(0, grado_total+1):
		resultado.append(0)

	for i in range(0, len(producto)):
		for j in range(0, len(producto[i])):
			producto[i][j] = 0
			
	for i in range(0, len(polinomio_aux)):
		for j in range(0, len(polinomio)):
			producto[i][j+i] = polinomio_aux[i]*polinomio[j]
	

	for i in range(0, len(producto)):
		for j in range(0, len(producto[i])):
			resultado[j] = resultado[j] + producto[i][j]

	print("\t\t==========================================")
	print("\t\tEl polinomio resultante es: ", end="")
	for j in range(0,len(resultado)):
		print("+("+str(resultado[j])+")"+"x^"+str(j), end = "")
	print("\n\t\t==========================================")
	print("")

	return resultado

	
def main(polinomio):
	while sentinela != 0:
		print("\t\t*********OPERACIONES CON POLINOMIMOS*********")
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
		for l in range(len(polinomio)):
				print("+("+str(polinomio[l])+")"+"x^"+str(l)+" ", end="")
		print("")
		opcion=int(input("Escoge una opcion: "))

		#Valor en un punto
		if opcion==1:
			valor_punto(polinomio)
		#Suma de dos polinomios
		elif opcion==2:
			polinomio = suma_polinomios(polinomio)
		#Resta de polinomios
		elif opcion==3:
			polinomio = resta_polinomios(polinomio)	
		#Igualdad de polinomios
		elif opcion==4:
			igualdad_polinomio(polinomio)
		elif opcion == 5:
		#Polinomios opuestos
			polinomio_opuesto(polinomio)
		elif opcion == 6:
		#Multiplicación de polinomios
			polinomio = multiplica_polinomios(polinomio)
		elif opcion == 0:
			os.system("CLS")
			print(""" ____________________________
< Developed by Ptolomeo Team >
#-Banda Martínez César Eduardo
#-Barriga Martínez Diego Alberto
#-Quezada Tapia Abraham
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||""")
			break
		else:
			print("*Error* Intenta otra opcion *Error*")

os.system("CLS")
main(crea_polinomio())