""" 
    Algoritmo que permita obtener la nota final de los 20 alumnos y el promedio del curso. 
    Para la nota final debe considerar lo siguiente: 
        - El promedio de las notas parciales equivale a un 70% de la nota final.
        - El examen equivale al 30% de la nota final
"""

cont = 1
suma = 0
barra = '-------------------------------------------'

while cont <= 20:
    nota = float(input(f"Ingrese el promedio del alumno n°{cont}: "))
    suma += nota
    cont += 1
    prom = suma / (cont - 1)
    print(barra)

print(f'El promedio del curso fue de {prom}')