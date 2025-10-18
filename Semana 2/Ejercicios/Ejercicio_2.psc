Algoritmo condicionales_ejemplo2
	definir color_1, color_2, color_3 Como Caracter
	
	color_1 = 'Blanco'
	color_2 = 'Negro'
	color_3 = 'Blanco'
	
	si color_1 = color_2 Entonces
		Imprimir 'Los colores 1 y 2 son iguales'
	SiNo si color_1 = color_3 Entonces
			Imprimir 'Los colores 1 y 3 son iguales'
		SiNo
			Imprimir 'Los colores 2 y 3 son iguales'
		finSi
	FinSi
	
FinAlgoritmo
