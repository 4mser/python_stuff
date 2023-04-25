""" 
    8. Algoritmo que permita a un usuario imprimir boletos de avión desde Valdivia a distintos puntos del país. 
    Por cada boleto se ingresará:
    -	Nombre del pasajero.
    -	Destino del vuelo (1: Santiago, 2: Concepción, 3: Punta Arenas).
    -	Clase (e: ejecutiva; t: turista).
    Los siguientes son los valores de los vuelos para clase turista, según el destino la clase ejecutiva lleva un recargo de $20.000 en todos los destinos:
    Destino   Valor
        1	$ 80.000
        2	$ 40.000
        3	$ 60.000

"""

pasajero = input('Ingrese su nombre: ')

print('1: Santiago, 2: Concepción, 3: Punta Arenas')
destino = int(input('Ingrese su destino: '))

print('e: Ejecutiva, t: Turista')
clase = input('¿En qué clase le gustaría viajar?: ')

print('-'*15)

if clase == 'e':
    clase = 'Ejecutiva'
    if destino == 1:
        destino = 'Santiago'
        valor = 80000 + 20000
    elif destino == 2:
        destino = 'Concepción'
        valor = 40000 + 20000
    elif destino == 3:
        destino = 'Punta Arenas'
        valor = 60000 + 20000
    
elif clase == 't':
    clase = 'Turista'
    if destino == 1:
        destino = 'Santiago'
        valor = 80000
    elif destino == 2:
        destino = 'Concepción'
        valor = 40000
    elif destino == 3:
        destino = 'Punta Arenas'
        valor = 60000
    
print(f'{pasajero}, el vuelo con destino a {destino} en clase {clase} tiene un costo de ${valor}')
