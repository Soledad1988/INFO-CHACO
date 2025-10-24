# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

# Crear una lista vacía
mi_lista = []

# Leer 5 cadenas desde teclado
for i in range(5):
    ingreso = input(f'Ingrese una cadena ({i+1}/5): ')
    mi_lista.append(ingreso)

# Crear una nueva lista con los elementos en orden inverso
lista_inversa = mi_lista[::-1]

print(lista_inversa)

