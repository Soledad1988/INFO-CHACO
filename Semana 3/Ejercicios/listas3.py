#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
#la muestre por pantalla el mensaje Yo estudio <asignatura>, 
#donde <asignatura> es cada una de las asignaturas de la lista.

asignaturas = []

# Pedir 5 asignaturas al usuario
for i in range(5):
    materia = input(f"Ingrese el nombre de la asignatura {i+1}: ")
    asignaturas.append(materia)

# Mostrar cada asignatura con el mensaje
for materia in asignaturas:
    print(f"Yo estudio {materia}")


