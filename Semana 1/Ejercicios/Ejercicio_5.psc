Algoritmo cambio_de_valores_letras
	definir a, b, c, aux Como Caracter
	
	imprimir 'En este programa veremos como en la ejecución del programa los valores cambian, pero con Letras'
	Imprimir 'Ingrese una palabra: '
	leer a
	
	Imprimir 'Ingrese otra palabra: '
	leer b
	
	Imprimir 'Ingrese otra palabra más: '
	leer c
	
	Imprimir 'Las palabras ingresadas son, Variable a: ', a, ' Variable b: ', b, 'Variable c: ',c
	
	aux = a
	a = b
	b = c
	c = aux
	
	Imprimir 'Ahora probamos intercambiar las palabras, Variable a: ', a, ' Variable b: ', b, 'Variable c: ',c
	
	
FinAlgoritmo

