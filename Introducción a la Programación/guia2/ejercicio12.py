""" 
    Algoritmo que permita calcular la siguiente suma 100+ 98+96+……..+4+2+0 en este orden.
    
"""

i = 50
num = 100
suma = 0

while i >= 0:
    suma += num
    num -= 2
    i -= 1
    
print('-'*20)
print(f'100 + 98 + 96 + … + 4 + 2 + 0 es igual a {suma}')
print('-'*20)

