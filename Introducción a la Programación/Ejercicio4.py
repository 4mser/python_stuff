# Ingresar un número entero y calcule e imprima si es positivo, negativo o neutro

# Entrada y lectura de dato
n = int(input('Ingrese un número entero: '))

# Proceso
if n > 0:
    print(f'El número {n} es positivo')
elif n == 0:
    print(f'El número {n} es neutro')
else:
    print(f'El número {n} es negativo')
    