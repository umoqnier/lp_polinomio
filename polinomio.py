#Operaciones de polinomios de grado N

#Inicio de programa

print("""\n\n\t////Este programa realiza operaciones de polinomios////
\t//////////////Selecciona una opcion//////////////////
		 .
		 .
		 1- Valor en un punto
		 2- Suma
		 3- Resta
		 4- Igualdad de 2 polinomios
		 5- Multiplicacion
		 .
		 .
		 """)


opcion = input("\t\tSelecciona un apartado...")
#Valor en un punto
if opcion == "1":
	grado = int(input("Ingresa el grado maximo del polinomio: "))
	polinomio= []
	i=0
	l=0
	while i < grado+1:
		valor = int(input(("Inserta el valor del coeficiente para x^"+str(i)+"...")))
		polinomio.insert(i,valor)
		i=i+1
	print ("Los valores del polinomio introducido son: ")

	for l in range(len(polinomio)):
		print(str(polinomio[l])+"x^"+str(l), end="")

	punto = int(input("Ingresa el valor del punto"))

	for l in range(len(polinomio))
		resultado = polinomio[l]
