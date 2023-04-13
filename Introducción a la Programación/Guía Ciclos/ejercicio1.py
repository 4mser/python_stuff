""" 
Calcular el promedio de un alumno que tiene 7 notas en la asignatura “Programación II”.

"""

barra = '--------------------'

contador = 1
suma_notas = 0

while contador <= 7:
    nota = float(input(f'Ingrese nota {contador}: '))
    print(barra)
    
    suma_notas = suma_notas + nota
    
    contador = contador + 1

promedio = suma_notas / (contador - 1)

print(f'Tiene un promedio de {promedio}')

print(barra)
    