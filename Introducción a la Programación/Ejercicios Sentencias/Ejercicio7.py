#Entrada y lectura de datos

print('Ingrese tres números distintos')

a = int(input())
b = int(input())
c = int(input())

#Proceso

if a > b:
    if a > c:
        if b > c:
            print("Los números ordenados de mayor a menor son: ", a, b, c)
        else:
            print("Los números ordenados de mayor a menor son: ", a, c, b)
    else:
        print("Los números ordenados de mayor a menor son: ", c, a, b)
else:
    if b > c:
        if a > c:
            print("Los números ordenados de mayor a menor son: ", b, a, c)
        else:
            print("Los números ordenados de mayor a menor son: ", b, c, a)
    else:
        print("Los números ordenados de mayor a menor son: ", c, b, a)