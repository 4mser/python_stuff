""" 
    Algoritmo que permita ingresar los números enteros del 1 al 100:
    
"""

#Opción 1: Programa que permita literalmente ingresar uno por uno los números del 1 al 100 y en caso de poner un número no correspondiente te pida si o sí ese número ->

i = 1

while i <= 10:
    num = int(input(f'Ingrese el N°{i}: '))
    
    if num == i:
        i += 1
    
    print('-'*20)
    
#Opción 2: Programa que despliega los números enteros del 1 al 100 automáticamente ->

num = 1

while num <= 10:
    print(num)
    num += 1