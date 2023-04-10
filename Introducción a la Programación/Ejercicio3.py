# Programa que permita ingresar nombre y sueldo de un/a trabajador/a.
# Si el sueldo es mayor a $1.000.000 tiene un bono del 25% del sueldo.
# En caso contrario, el bono será del 50%

""" nombre = input('Ingrese su nombre: ')
sueldo = int(input('Ingrese su sueldo: '))

if sueldo > 1000000:
    bono = int(sueldo*0.25)
    sueldo_final = int(sueldo + bono)
    print(f'{nombre}, recibirá un bono de ${bono}, por lo que recibirá un total de ${sueldo_final}')
else:
    bono = int(sueldo*0.5)
    sueldo_final = int(sueldo + bono)
    print(f'{nombre}, recibirá un bono de ${bono}, por lo que recibirá un total de ${sueldo_final}')
    
      """
nombre = input('Ingrese su nombre: ')
sueldo = int(input('Ingrese su sueldo: '))

# valor_si_verdadero if condición else valor_si_falso
bono = int(sueldo * 0.25) if sueldo > 1000000 else int(sueldo * 0.5)
sueldo_final = sueldo + bono

print(f'{nombre}, recibirá un bono de ${bono}, por lo que recibirá un total de ${sueldo_final}')
