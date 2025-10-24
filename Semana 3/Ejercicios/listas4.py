#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
#la muestre por pantalla el mensaje Yo estudio <asignatura>, 
#donde <asignatura> es cada una de las asignaturas de la lista.

# Lista con las asignaturas del curso
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Mostrar cada asignatura con el mensaje
for materia in asignaturas:
    print(f"Yo estudio {materia}")
