""" 
    Algoritmo que permita imprimir todos los números enteros que hay desde 1 hasta el número que introduzca el usuario

"""
print('-'*20)
print('Opción 1: Despliegue normal')
print('-'*20)

n = int(input("¿Hasta que número quieres llegar?: "))
contador = 0

while contador < n:    
    contador += 1  
    print(contador)
 
print('-'*20)   
print('Opción 2: Despliegue en cadena')
print('-'*20)   

n = int(input("¿Hasta qué número quieres llegar?: "))
contador = 0
numeros = ""

while contador < n:
    contador += 1
    if contador == 1:
        numeros += str(contador)
    else:
        numeros += ", " + str(contador)

print(numeros)
