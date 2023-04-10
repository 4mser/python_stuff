""" Ejercicio 5 - Aprueba o Reprueba """
# Programa que muestre si un alumno aprueba o reprueba. 

""" Requerimientos """
# Necesita un promedio mayor a 4 y asistencia mayor al 50%

""" Porcentajes por nota """
# Primera nota: 15%
# Segunda nota: 20%
# Tercera nota: 35%
# Cuarta nota: 30%

"""  """
# Entrada y lectura de datos

nombre = input('Ingrese su nombre: ')

print('Ingrese sus notas: ')

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

asistencia = int(input('Ingrese su porcentaje de asistencia: '))

# Cambiamos las notas ingresadas por su respectivo porcentaje y guardamos su suma en una variable "Promedio"

n1 = n1 * 0.15
n2 = n2 * 0.2
n3 = n3 * 0.35
n4 = n4 * 0.3

promedio = n1 + n2 + n3 + n4

# Proceso

if promedio >= 4 and asistencia >= 50:
    print(f'Wena {nombre}, pasaste!')
elif promedio < 4 and asistencia < 50:
    print(f'Estimado {nombre}, es de mi desagrado informarle que reprobó por las notas y la asistencia. Pongase las pilas pa la otra')
elif promedio < 4:
    print(f'Compare {nombre}, reprobó por las notas u-u')
else:
    print(f'Compare {nombre}, reprobó por la asistencia wjqejqw como tan wn tabien si hermanito mío a cualquiera le puede pasar bendiciones se me cuida')
