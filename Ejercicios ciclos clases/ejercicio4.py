""" """ """ """ """ """ """ """ """ """  """ """ """ """ """ """ """ """ """
Programa que permita ingresar el nombre, edad y sueldo de 500 trabajadores
de una empresa, calcule e imprima:
    - La cantidad de trabajadores que su sueldo es menor a $500.000 pesos
    - El promedio de edad de los trabajadores de la empresa
    - El total de dinero que cancela la empresa por concepto de sueldo
    
 """ """ """ """ """ """ """ """ """ """  """ """ """ """ """ """ """ """ """

barra = '---------------------------------'

contador = 1
pobres = 0
total = 0
suma_edades = 0

while contador <= 5:
    name = input(f'Ingrese el nombre del trabajador n°{contador}: ')
    edad = int(input(f'Ingrese la edad de {name}: '))
    sueldo = int(input(f'Ingrese el sueldo de {name}: '))
    
    print(barra)
    
    contador = contador + 1
    
    suma_edades = suma_edades + edad 
    
    #Contador - 1 es debido a que, si bien el ciclo se hará x veces, el contador 
    #...terminará siendo x + 1 al ser contador = contador + 1 
    promedio_edades = suma_edades / (contador - 1)
    
    total = total + sueldo
    
    if sueldo < 500000:
        pobres = pobres + 1
    
    
print(f'Hay {pobres} trabajadores que ganan menos de $500.000 pesos.')
print(f'El promedio de edad de los trabajadores es de {promedio_edades}')
print(f'La empresa cancela un total de ${total} por concepto de sueldo.')