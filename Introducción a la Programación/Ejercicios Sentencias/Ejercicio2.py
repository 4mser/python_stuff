# Una empresa quiere pagar a sus trabajadores un bono del 25% de su sueldo.
# Crear un programa que muestre el nombre, sueldo y bono que obtiene

nombre = str(input('Ingrese su nombre: '))
sueldo = int(input('Ingrese su sueldo: '))

bono = int(sueldo * 25 / 100)
s_final = int(sueldo + bono)

print(f'{nombre}, el bono que recibirá es de: ${bono}, por lo que recibirá un total de: ${s_final}')

