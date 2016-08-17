#Universidad Nacioanal Autonoma de Mexico/ Facultad de Ingenieria
#Lenguajes de programacion
#Alumnos:
#-Banda Martínez César Eduardo
#-Barriga Martínez Diego Alberto
#-Quezada Tapia Abraham
#Programa: Operaciones de polinomios de grado N
#Hecho en Python 3.6

#Inicio de programa
#Variables globales
i=0
j=0
l=0
k=0
m=1
resultado=0
def grado():
	grado=int(input("Introduce el grado maximo: "))
	return grado

def polinomioUno():
	i=0
	grado1 = grado()
	polinomioUno= []
	while i<grado1+1:
		valor=int(input(("Inserta el valor del coeficiente para x^"+str(i)+"...")))
		polinomioUno.insert(i,valor)
		i=i+1
	print ("Los valores del polinomio 1 introducido son: ")
	for l in range(len(polinomioUno)):
		print(str(polinomioUno[l])+"x^"+str(l),)
	return polinomioUno

def polinomioDos():
	i=0
	grado2=grado()
	polinomioDos= []
	while i<grado2+1:
		valor=int(input(("Inserta el valor del coeficiente para x^"+str(i)+"...")))
		polinomioDos.insert(i,valor)
		i=i+1
	print ("Los valores del polinomio 2 introducido son: ")
	for l in range(len(polinomioDos)):
		print(str(polinomioDos[l])+"x^"+str(l),)
	return polinomioDos

print("""
		1-Valor calculado en un punto
		2-Suma
		3-Resta
		4-Igualdad de 2 polinomios
		5-Polinomio opuesto
		6-Multiplicacion

		""")
opcion=int(input("Escoge una opcion: "))

#Valor en un punto
if opcion==1: 
	polinomio=polinomioUno();
	print ("Los valores del polinomio introducido son: ")
	for l in range(len(polinomio)):
		print(str(polinomio[l])+"x^"+str(l),)

	punto = int(input("Ingresa el valor del punto: "))
	z=0
	potencias=[]
	for j in range(0,len(polinomio)):
		potencias.insert(j,pow(punto,z))
		z=z+1
	multiplicacion = 0
	for k in range(0,len(polinomio)):
		multiplicacion = multiplicacion+(polinomio[k]*potencias[k])
		k=k+1
	print("El valor calculado es: "+str(multiplicacion))

#Suma de dos polinomios
elif opcion==2:
	print("Los polinomios deben ser del mismo grado")
	suma=[]
	polinomio1= polinomioUno()
	polinomio2= polinomioDos()
	for i in range(0,len(polinomio1)):
		suma.append(polinomio1[i]+polinomio2[i])
	print("El polinomio resultante es: ")
	for j in range(0,len(suma)):
		print(str(suma[j])+"x^"+str(j),),

#Resta de polinomios
elif opcion==3:
	print("Los polinomios deben ser del mismo grado")
	resta=[]
	polinomio1= polinomioUno()
	polinomio2= polinomioDos()
	for i in range(0,len(polinomio1)):
		resta.append(polinomio1[i]-polinomio2[i])
	print("El polinomio resultante es: ")
	for j in range(0,len(resta)):
		print(str(resta[j])-"x^"-str(j),),
	
#Igualdad de polinomios
elif opcion==4:
	igualdad=[]
	polinomio1 = polinomioUno()
	polinomio2 = polinomioDos()
	if grado2==grado1:
	   print("El grado del polinomio es igual")
	print("El grado del polinomio no es igual")   




