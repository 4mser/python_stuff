# Programa que permita ingresar 1000 números Enteros y calcular:
# - El Promedio de los números positivos ingresados
# - La suma total de los números ingresados divisibles por 5
# - La cantidad de números impares ingresados

contador = 0
suma_positivos = 0
suma_divisibles = 0
n_positivos = 0
impares = 0

while contador < 5:
    num = int(input(f'Ingrese el número {contador + 1}: '))
    contador = contador + 1
    if num > 0:
        n_positivos = n_positivos + 1
        suma_positivos = suma_positivos + num
        promedio = suma_positivos / n_positivos
    if num % 5 == 0:
        suma_divisibles = suma_divisibles + num
    if num % 2 != 0:
        impares = impares + 1



print(f'El promedio de los números positivos ingresados es: {promedio}')
print(f'La suma total de los números ingresados divisibles por 5 es: {suma_divisibles}')
print(f'La cantidad de números ingresados impares es: {impares}')
