""" 
    Algoritmo que permita ingresar 50 números y calcule e imprima el valor del número menor ingresado. 
    
"""

i = 1
num = int(input(f'Ingrese el N°{i}: '))
menor = num

while i <= 50:
    i += 1
    num = int(input(f'Ingrese el N°{i}: '))
    if num < menor:
        menor = num

print(f'El número menor es {menor}')    
    
