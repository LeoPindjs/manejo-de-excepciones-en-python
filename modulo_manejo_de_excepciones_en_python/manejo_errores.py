try:
    numerador = 10
    denominador = 0
    res = numerador / denominador
    print(f'El resultado de la operación es: {res}')
except ZeroDivisionError as e:
    print(f'Hubo un error de tipo : {type(e).__name__}')
