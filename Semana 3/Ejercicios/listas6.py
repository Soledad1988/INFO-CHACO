#Crea una función llamada rotar_a_la_izquierda que reciba como parámetro una lista. La función debe eliminar 
#el primer elemento de la lista y luego agregar este mismo elemento al final. Retorna la lista modificada.

def rotar_a_la_izquierda(mi_lista):
    primero = mi_lista.pop(0)  # quita el primer elemento
    mi_lista.append(primero)   # lo agrega al final
    return mi_lista
# Fin
print(rotar_a_la_izquierda(['uno','dos','tres','cuatro']))
print(rotar_a_la_izquierda([1,2,3,4]))
print(rotar_a_la_izquierda(['perro','gato','pájaro','pez']))