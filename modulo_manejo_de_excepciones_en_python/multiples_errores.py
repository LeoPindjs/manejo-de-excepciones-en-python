try:
    numerador = 10
    denominador = 2
    lista = [1, 2, 3, 4]
    lista[4]
    res = numerador / variable
except ZeroDivisionError as e:
    print(f'Hubo un error de tipo : {type(e).__name__}')
except NameError as e:
    print(f'error de tipo {type(e).__name__}: variable no definida')
except IndexError as e:
    print('lo sentimos no es posible acceder a ese indice')
else:
    print('se ejecuta este bloque si el try se ejecuta')
    print(f'El resultado de la operación es: {res}')
finally:
    print('este bloque se ejecuta independiente del try o el except')
