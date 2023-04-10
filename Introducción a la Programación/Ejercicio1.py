""" # Input 2 enteros
n1 = int(input('Ingrese un número entero: '))
n2 = int(input('Ingrese otro número Entero: '))

#Resultados
r_suma = int(n1 + n2)
r_resta = int(n1 - n2)
r_mult = int(n1 * n2)


print('Los resultados de las operaciones básicas son: ')
print(f'Suma: {r_suma}')
print('Resta: ', r_resta)
print('Multiplicación: ', r_mult)


if n2 == 0:
    print('Mod: No se puede dividir por 0')
    print('Mod: No se puede calcular el mod')
    
else: 
    r_div = float(n1 / n2)
    r_mod = int(n1 % n2)
    
    print('División: ', r_div)
    print('Mod: ', r_mod)
 """
 
 # Input 2 enteros
n1 = int(input('Ingrese un número entero: '))
n2 = int(input('Ingrese otro número Entero: '))

#Resultados
r_suma, r_resta, r_mult = n1 + n2, n1 - n2, n1 * n2

print('Los resultados de las operaciones básicas son: ')
print(f'Suma: {r_suma}')
print(f'Resta: {r_resta}')
print(f'Multiplicación: {r_mult}')

if n2 == 0:
    print('Mod: No se puede dividir por 0')
    print('Mod: No se puede calcular el mod')
else:
    r_div, r_mod = n1 / n2, n1 % n2
    print(f'División: {r_div}')
    print(f'Mod: {r_mod}')
