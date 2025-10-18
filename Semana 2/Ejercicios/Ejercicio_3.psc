Algoritmo condicionales_ejemplo3
	
	definir monto_ingresado, valor_estacionamiento, vuelto Como Entero
	valor_estacionamiento = 1000
	
	Imprimir 'Bienvenido al estacionamiento dl info. El valor del estacionamiento es de: $1000'
	Imprimir 'Por favor ingrese el monto que va a pagar (solo en números):'
	
	leer monto_ingresado
	
	si monto_ingresado = valor_estacionamiento Entonces
		Imprimir 'Muchas gracias, ahora la barrera se levantará'
	sino si monto_ingresado >= valor_estacionamiento Entonces
			vuelto <- monto_ingresado - valor_estacionamiento 
			Imprimir 'Muchas gracias, puede ingresar. Su vuelto es: ', vuelto
		SiNo
			Imprimir 'El monto ingresado es menor al requerido. La barrera no se levantará'
		FinSi
	FinSi
	
FinAlgoritmo
