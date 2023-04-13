# Programa que permita leer 10 números Enteros y calcule e imprima ->
# -> la suma total de los números ingresados.

contador = 1
suma = 0

while contador <= 10:
    num = input(f'Ingrese el número {contador} : ')
    suma = int(suma) + int(num)
    contador = contador + 1

print(f'El total es: {suma}')
