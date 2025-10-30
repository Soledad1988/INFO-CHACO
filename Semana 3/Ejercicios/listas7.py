#Crea una función llamada juntar_arreglos que reciba dos parámetros, arreglo1 y arreglo2, 
#y retorne una nueva lista con los elementos de ambas listas excluyendo el primer elemento de cada una.

#Ejemplos:
#print(juntar_arreglos([1, 2, 3], [4, 5, 6]))  # [2, 3, 5, 6]
#print(juntar_arreglos(["hola", "mundo"], ["desde", "python"]))  # ["mundo", "python"]

def juntar_arreglos(arreglo1, arreglo2):
    nueva_lista = arreglo1[1:] +  arreglo2[1:]
    return nueva_lista



# Fin
print(juntar_arreglos([1,2,3,4], [5,6,7,8]))
print(juntar_arreglos(['a','b','c'], ['d','e','f']))
print(juntar_arreglos(['uno','dos','tres'], ['cuatro','cinco','seis']))