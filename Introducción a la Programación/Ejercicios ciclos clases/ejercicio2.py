# Programa que permita ingresar la edad de 50 personas y calcular ->
#-> cuantas son mayores de edad y cuantas son menores

mayores = 0
menores = 0
contador = 1

while contador <= 5:
    contador = contador + 1
    
    edad = input(f'Ingrese la edad de la persona n°{contador}: ')
    
    if int(edad) >= 18:
        mayores = mayores + 1
    else:
        menores = menores + 1 

print(f'Hay {mayores} personas mayores de edad y {menores} menores.')