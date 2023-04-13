""" 
Leer 10 números e imprimir solamente los números positivos

"""

barra = '---------------------'

contador = 1
positivos = 0

while contador <= 10:
    num = float(input(f'Ingrese el n°{contador}: '))
    print(barra)
    
    contador = contador + 1
    
    if num > 0:
        print(f'{num} es positivo')
        positivos = positivos + 1
        print(barra)

print(f'Hay {positivos} números positivoss')