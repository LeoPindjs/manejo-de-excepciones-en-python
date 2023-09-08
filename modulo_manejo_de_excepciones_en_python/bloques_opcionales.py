try:
    numerador = 10
    denominador = 2
    res = numerador / denominador
except ZeroDivisionError as e:
    print(f'Hubo un error de tipo : {type(e).__name__}')
else:
    print('se ejecuta este bloque si el try se ejecuta')
    print(f'El resultado de la operación es: {res}')
finally:
    print('este bloque se ejecuta independiente del try o el except')
