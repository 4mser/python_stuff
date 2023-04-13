""" 
Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos son
ceros.

"""

barra = '--------------------'

contador = 1
positivos = 0
negativos = 0
ceros = 0

while contador <= 4:
    num = float(input(f'Ingrese el n°{contador}: '))
    print(barra)
    
    contador = contador + 1
    
    if num > 0:
        positivos = positivos  + 1
    else:
        if num == 0:
            ceros = ceros + 1
        elif num < 0:
            negativos = negativos + 1

print('Hay:')

if positivos > 1:
    print(f'{positivos} números positivos')
else:
    if positivos == 1:
        print(f'{positivos} número positivo')
    elif positivos < 1:
        print('No hay números positivos')
        
if negativos > 1:
    print(f'{negativos} números negativos')
else:
    if negativos == 1:
        print(f'{negativos} número negativo')
    elif negativos < 1:
        print('No hay números negativos')
        
if ceros > 1:
    print(f'{ceros} ceros')
else:
    if ceros == 1:
        print(f'{ceros} cero')
    elif ceros < 1:
        print('No hay ceros')
        
print(barra)
