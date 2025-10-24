#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas 
#por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []

# Leer por teclado las 5 notas
for i in range(5):
    ingreso = float(input(f'Ingrese nota {i+1}: '))
    notas.append(ingreso)

media = sum(notas) / len(notas)
maxima = max(notas)
minima = min(notas)

print("Las notas son :", notas)
print('La media es: ', media)
print('La nota máxima es: ', maxima)
print('La nota mínima es: ', minima)