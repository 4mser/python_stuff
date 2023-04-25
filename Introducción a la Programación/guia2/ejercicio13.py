""" 
    Algoritmo que permita resolver el siguiente problema:
    Se necesitan leer los 250000 votos otorgados a los 3 candidatos a alcalde y se debe imprimir el número del candidato ganador y su cantidad de votos.

"""

i = 1

candidato1 = 0
candidato2 = 0
candidato3 = 0

while i <= 2500:
    print('1: Candidato 1, 2: Candidato 2, 3: Candidato 3')
    print('-'*20)
    print(f'Voto n°{i}')

    voto = int(input('Ingrese el número del candidato por el que desea votar: '))

    print('-'*15)
    
    if voto == 1:
        candidato1 += 1
        i += 1
    elif voto == 2:
        candidato2 += 1
        i += 1
    elif voto == 3:
        candidato3 += 1
        i += 1
    else:
        print('Ingrese un candidato válido.')

if candidato1 > candidato2 and candidato1 > candidato3:
    print(f'El candidato 1 fue el ganador con {candidato1} votos.')

elif candidato2 > candidato1 and candidato2 > candidato3:
    print(f'El candidato 2 fue el ganador con {candidato2} votos.')

else:
    print(f'El candidato 3 fue el ganador con {candidato3} votos.')