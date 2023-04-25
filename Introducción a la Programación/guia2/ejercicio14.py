""" 
    Algoritmo que simule un turno en una caja registradora de un almacén.

"""
#Contador de clientes
cliente = 1 
#Contador de productos por cliente
producto = 1 

#Acumulador total compra cliente
total_cliente = 0 
#Acumulador total compra clientes durante el turno
total_diario = 0 
#Acumulador cantidad de productos comprados durante el turno
productos_totales = 0 

#Interruptor para agregar nuevo cliente
cliente_nuevo = True 

#Ciclo para agregar cliente nuevo o finalizar turno
while cliente_nuevo == True:
    
    #Imprimimos el número del cliente en el turno
    print('-'*25)
    print(f'Cliente N°{cliente}')
    print('-'*25)
    
    #Interruptor para agregar producto nuevo al cliente de turno
    producto_nuevo = True
    
    #Ciclo de agregado de producto
    while producto_nuevo == True:
        
        #Acumulamos la cantidad de productos del turno entero
        productos_totales += 1
            
        #Pedios el precio del producto
        precio_producto = int(input(f'Precio producto N°{producto}: '))
        
        #Acumulamos el total de la compra del cliente de turno
        total_cliente += precio_producto
        
        #Acumulamos el total de la compra de todos los clientes en el turno
        total_diario += precio_producto
        
        #Preguntamos si se agregará otro producto al mismo cliente
        print('-'*15)
        r = input('¿Agregar otro producto? (s/n): ')
        print('-'*15)
        
        #Si la respuesta es 's' se agregará un producto nuevo al cliente y se repetirá el ciclo de producto_nuevo. 
        if r == 's':
            producto_nuevo = True
            producto += 1
        #En caso contrario, el producto volverá a ser el primero, se terminará el ciclo de producto nuevo, se dará el total de la compra del cliente y volverá a ser 0 para repetir el proceso
        elif r == 'n':
            producto = 1
            producto_nuevo = False
            print(f'Total compra cliente N°{cliente}: ${total_cliente}')
            print('-'*15)
            total_cliente = 0
    
    #Preguntamos si se desea agregar un cliente nuevo para repetir todo el ciclo completo.
    cerrar = input('¿Cliente nuevo? (s/n):')

    if cerrar == 's':
        cliente += 1
        cliente_nuevo = True
    #En caso contrario, se dan los datos de las ventas generales del turno, considerando la cantidad de productos vendidos, los clientes que hubo y el total vendido.
    elif cerrar == 'n':
        print('-'*25)
        print(f'Se vendió un total de {productos_totales} productos entre {cliente} clientes')
        print('-'*25)
        print(f'El total de venta el día de hoy fue de ${total_diario}')
        print('-'*25)
        cliente_nuevo = False    