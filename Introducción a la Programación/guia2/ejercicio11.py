""" 
    Algoritmo que permita a un encuestador recopilar la información de 500 personas y calcule e imprima la cantidad de personas que tienen estudios básicos, medios, superiores y de postgrados.
    
"""

i = 1

basicos = 0
medios = 0
superiores = 0
postgrados = 0

while i <= 50:
    estudios = int(input(f'¿Hasta que nivel de estudios llegó la persona N°{i} \n 1: Básicos, 2: Medios, 3; Superiores, 4: Postgrados. \n : '))
    print('-'*30)
    
    if estudios == 1:
        basicos += 1
        i += 1
    elif estudios == 2:
        medios += 1
        i += 1
    elif estudios == 3:
        superiores += 1
        i += 1    
    elif estudios == 4:
        postgrados += 1
        i += 1
    else:
        print('Por favor seleccione una de las opciones dadas. ')
        print('-'*30)

    
print(f'{basicos} personas tienen estudios basicos')
print(f'{medios} personas tienen estudios medios')
print(f'{superiores} personas tienen estudios superiores')
print(f'{postgrados} personas tienen postgrados')
print('-'*30)
