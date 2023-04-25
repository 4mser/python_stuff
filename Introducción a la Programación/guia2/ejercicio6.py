""" 
    Algoritmo que permita ingresar 100 números enteros y calcule e imprima la cantidad de números pares ingresados y la cantidad de números impares ingresados.
"""

pares = 0
impares = 0
contador = 1


while contador <= 5:
    num = int(input(f'Ingrese el N°{contador}: '))
    contador += 1
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print(f'Hay {pares} números pares y {impares} números impares.')