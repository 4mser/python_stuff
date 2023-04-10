def es_natural_y_vocal(numero, letra):
    if numero >= 0 and numero % 1 == 0 and letra in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False
