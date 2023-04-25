""" 
    algoritmo para una empresa que requiere calcular el sueldo semanal de cada uno de los 100 trabajadores que trabajan en ella. 
    El sueldo se obtiene de la siguiente forma:
        - Si trabaja 40 horas o menos se le paga $4000 por hora.
        - Si trabaja más de 40 horas se le paga $4500 por cada una de las primeras 40 horas y $5500 por cada hora extra.
        Las horas extras se deben calcular.
        
"""

i = 1

while i <= 5:
    horas = int(input(f"¿Cuántas horas trabaja a la semana el trabajador n°{i}?: "))
    print("-" * 20)
    
    if horas <= 40:
        valor_hora = 4000
        sueldo_semanal = valor_hora * horas
    else:
        valor_hora_normal = 4500
        valor_hora_extra = 5500
        horas_normales = 40
        horas_extra = horas - horas_normales
        sueldo_semanal = (horas_normales * valor_hora_normal) + (horas_extra * valor_hora_extra)
           
    print(f"El sueldo semanal del trabajador n°{i} es: ${sueldo_semanal}")
    print("-" * 20)
    i += 1

