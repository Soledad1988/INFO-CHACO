frutas = ["manzana", "banana", "cereza", "dátil"]
print("manzana" in frutas)  # True
print("kiwi" in frutas)

#Crea una función llamada miembro_en_dos que recibe 3 parámetros:
#arr1, arr2, y valor. La función debe retornar True si valor está presente en ambas listas arr1 y arr2, 
#y False en caso contrario.

def miembro_en_dos(arr1, arr2, valor):
    if valor in arr1 and valor in arr2:
        return True
    else:
        return False

# Fin
arr1 = ["Nueva York", "Londres", "Tokio", "Sídney"]
arr2 = ["Londres", "París", "Tokio", "Berlín"]

print(miembro_en_dos(arr1, arr2, "Londres"))  
print(miembro_en_dos(arr1, arr2, "París"))   
print(miembro_en_dos(arr1, arr2, "Tokio"))