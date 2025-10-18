Algoritmo cambio_de_valores
	definir a, b, c, aux Como Entero
	
	imprimir 'En este programa veremos como en la ejecución del programa los valores cambian'
	Imprimir 'Ingrese un número'
	leer a
	
	Imprimir 'Ingrese otro número'
	leer b
	
	Imprimir 'Ingrese otro número'
	leer c
	
	Imprimir 'Lo valores ingresados son, Variable a: ', a, ' Variable b: ', b, 'Variable c: ',c
	
	aux = a
	a = b
	b = c
	c = aux
	
	Imprimir 'Ahora probamos intercambiar los valores, Variable a: ', a, ' Variable b: ', b, 'Variable c: ',c
	
	
FinAlgoritmo
