""" 
Leer 15 números enteros negativos, convertirlos a positivos e imprimir dichos números

"""

barra = '------------------'

contador = 1

print('Ingrese números negativos: ')

while contador <= 15:
    num = int(input())
    print(barra)
    
    
    if num < 0:
        num_positivo = num * -1
        print(f'{num} Convertido a positivo sería {num_positivo}')
        print(barra)
        contador = contador + 1
        
    
    else:
        print('Solo se aceptan números negativos y distintos de 0')
        print(barra)
        
        