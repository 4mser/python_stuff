# snmm = int(input('Ingrese el SNMM: '))

# pais = input('quiere los resultados en Santiago, Buenos Aires, Bogota o Lima?')

# if pais == 'Santiago':
#     mercado = float(34.9)
#     vestuario = float(2.8)
#     deportes = float(5.9)
#     utilidades = float(6.8)
#     transporte = float(10.9)
#     restaurantes = float(15.9)
#     renta = float(22.8)
    
#     mercado = snmm * mercado / 100
#     vestuario = snmm * vestuario /100
#     deportes = snmm * deportes / 100
#     utilidades = snmm * utilidades / 100
#     transporte = snmm * transporte / 100
#     restaurantes = snmm * restaurantes / 100
#     renta = snmm * renta / 100
    
#     print(f'Mercado: {mercado}')
#     print(f'Vestuario: {vestuario}')
#     print(f'Deportes: {deportes}')
#     print(f'utilidades: {utilidades}')
#     print(f'Transporte: {transporte}')
#     print(f'Restaurantes: {restaurantes}')
#     print(f'renta: {renta}')
    
# elif pais == 'Buenos Aires':
#     mercado = float(30.8)
#     vestuario = float(6)
#     deportes = float(5.3)
#     utilidades = float(8.3)
#     transporte = float(13)
#     restaurantes = float(15.9)
#     renta = float(20.8)
    
#     mercado = snmm * mercado / 100
#     vestuario = snmm * vestuario /100
#     deportes = snmm * deportes / 100
#     utilidades = snmm * utilidades / 100
#     transporte = snmm * transporte / 100
#     restaurantes = snmm * restaurantes / 100
#     renta = snmm * renta / 100
    
#     print(f'Mercado: {mercado}')
#     print(f'Vestuario: {vestuario}')
#     print(f'Deportes: {deportes}')
#     print(f'utilidades: {utilidades}')
#     print(f'Transporte: {transporte}')
#     print(f'Restaurantes: {restaurantes}')
#     print(f'renta: {renta}')
    
# elif pais == 'Bogota':
#     mercado = float(34.8)
#     vestuario = float(4.3)
#     deportes = float(5.2)
#     utilidades = float(6.3)
#     transporte = float(12.5)
#     restaurantes = float(11.4)
#     renta = float(25.5)
    
#     mercado = snmm * mercado / 100
#     vestuario = snmm * vestuario /100
#     deportes = snmm * deportes / 100
#     utilidades = snmm * utilidades / 100
#     transporte = snmm * transporte / 100
#     restaurantes = snmm * restaurantes / 100
#     renta = snmm * renta / 100
    
#     print(f'Mercado: {mercado}')
#     print(f'Vestuario: {vestuario}')
#     print(f'Deportes: {deportes}')
#     print(f'utilidades: {utilidades}')
#     print(f'Transporte: {transporte}')
#     print(f'Restaurantes: {restaurantes}')
#     print(f'renta: {renta}')
    
# elif pais == 'Lima':
#     mercado = float(32.7)
#     vestuario = float(3.2)
#     deportes = float(6.9)
#     utilidades = float(6.7)
#     transporte = float(13.2)
#     restaurantes = float(11.2)
#     renta = float(26.1)
    
#     mercado = snmm * mercado / 100
#     vestuario = snmm * vestuario /100
#     deportes = snmm * deportes / 100
#     utilidades = snmm * utilidades / 100
#     transporte = snmm * transporte / 100
#     restaurantes = snmm * restaurantes / 100
#     renta = snmm * renta / 100
    
#     print(f'Mercado: {mercado}')
#     print(f'Vestuario: {vestuario}')
#     print(f'Deportes: {deportes}')
#     print(f'utilidades: {utilidades}')
#     print(f'Transporte: {transporte}')
#     print(f'Restaurantes: {restaurantes}')
#     print(f'renta: {renta}')
    


snmm=int(input("SNMM:"))
d={'Santiago':(34.9,2.8,5.9,6.8,10.9,15.9,22.8),
'Buenos Aires':(30.8,6.0,5.3,8.3,13.0,15.9,20.8),
'Bogota':(34.8,4.3,5.2,6.3,12.5,11.4,25.5),
'Lima':(32.7,3.2,6.9,6.7,13.2,11.2,26.1)}
m,v,d1,u,t,r,r1=[snmm*i/100 for i in d[input("quiere los resultados en Santiago, Buenos Aires, Bogota o Lima?")]]
print(f"Mercado: {m}\nVestuario: {v}\nDeportes: {d1}\nUtilidades: {u}\nTransporte: {t}\nRestaurantes: {r}\nRenta: {r1}")

