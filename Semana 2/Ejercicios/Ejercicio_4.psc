Algoritmo condicionales_ejemplo4
	
	definir monto_ingresado, valor_estacionamiento, vuelto Como Entero
	valor_estacionamiento = 1000
	
	Imprimir 'Bienvenido al estacionamiento dl info. El valor del estacionamiento es de: $1000'
	Imprimir 'Por favor ingrese el monto que va a pagar (solo en números):'
	
	leer monto_ingresado
	
	Mientras monto_ingresado <> valor_estacionamiento hacer
		Imprimir 'El monto ingresado no es correcto. La barrera no se levantará'
		Imprimir 'Ingrese nuevamente el monto a pagar'
		
		leer monto_ingresado
	FinMientras
	
	Imprimir 'El monto ingresado es correcto. La barrera se levantará'
	
FinAlgoritmo
