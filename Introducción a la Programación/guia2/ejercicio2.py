""" 
    Algoritmo que permita ingresar los números enteros del 100 al 1

"""
#Opción 1: Programa que permita literalmente ingresar uno por uno los
#números del 100 al 1 y en caso de poner un número no correspondiente 
#te pida si o sí ese número ->

i = 100

while i >= 1:
    num = int(input(f'Ingrese el N°{i}: '))
    
    if num == i:
        i -= 1
        
    print('-'*20)
    
#Opción 2: Programa que despliega los números enteros del 100 al 1
#automáticamente ->

print('-'*30)

num = 100

while num >= 1:
    print(num)
    num -= 1

