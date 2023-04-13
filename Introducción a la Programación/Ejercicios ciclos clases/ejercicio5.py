""" 
Programa que permita ingresar el nombre y las 3 notas de 40 alumnos de
un curso y calcule e imprima:
    - El promedio y situación final para cada alumno (Aprueba si promedio es mayor o igual a 4)
    - Cantidad de alumnos aprobados y reprobados
    - Promedio general del curso
    
"""

contador = 1
suma_notas_curso = 0
aprobados = 0
reprobados = 0
promedio_curso = 0

barra = '---------------------'

while contador <= 5:
    name = input(f'Ingrese el nombre del alumno n°{contador}: ')
    print(f'Ingrese las notas de {name}: ')
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    print(barra)
    
    suma_notas = n1 + n2 + n3
    
    promedio = suma_notas / 3
    
    suma_notas_curso = suma_notas_curso + promedio
        
    contador = contador + 1
    
    if promedio < 4:
        reprobados = reprobados + 1
        print(f'{name} reprobó con un {promedio}')
        print(barra)
    else:
        aprobados = aprobados + 1
        print(f'{name} aprobó con un {promedio}')
        print(barra)
        
    
        
""" --- End While --- """

if aprobados < 1:
    print('Ningún alumno aprobó')
else: 
    if aprobados == 1:
        print('Aprobó solo un alumno')
    elif aprobados > 1:
        print(f'{aprobados} alumnos aprobaron')


if reprobados < 1:
    print('Ningún alumno reprobó')
else: 
    if reprobados == 1:
        print('Reprobó solo un alumno')
    elif reprobados > 1:
        print(f'{reprobados} alumnos reprobaron')

    
print(barra)

promedio_curso = suma_notas_curso / (contador - 1)

print(f'El promedio general del curso fue de {promedio_curso}')

print(barra)

