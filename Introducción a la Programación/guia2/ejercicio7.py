""" 
    Algoritmo que permita ingresar dos números enteros. Y calcule e imprima, lo siguiente:
        - Los números enteros que hay entre ambos números, empezando por el más pequeño.
        - Contar cuantos números hay.
        - Contar cuantos son pares.
        - Calcular la suma total de los números impares.

"""

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

while abs(num1 - num2) > 500:
    print("La diferencia entre los dos números no puede ser mayor a 500. Por favor ingrese nuevos números.")
    num1 = int(input('Ingrese el primer número: '))
    num2 = int(input('Ingrese el segundo número: '))

num1_original = num1
num2_original = num2

print('-' * 20)

pares = 0
impares = 0
numeros = []

if num1 < num2:
    while num1 < (num2 - 1):
        num1 += 1
        numeros.append(num1)
        
        if num1 % 2 == 0:
            pares += 1
        else:
            impares += num1
else:
    while num2 < (num1 - 1):
        num2 += 1
        numeros.append(num2)
        
        if num2 % 2 == 0:
            pares += 1
        else:
            impares += num2
            
cantidad_numeros = len(numeros)

numeros_str = ''
for num in numeros:
    numeros_str += str(num) + ', '
numeros_str = numeros_str[:-2] # Elimina la última coma y el espacio

print(f'Los números que hay entre {num1_original} y {num2_original} son: {numeros_str}')

print('-'*20)
print(f'Hay {cantidad_numeros} números entre ambos números')
print('-'*20)
print(f'Hay {pares} números pares entre ambos números')
print('-'*20)
print(f'La suma total de los números impares es {impares}') 
