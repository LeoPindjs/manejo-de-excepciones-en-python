try:
    lista = [0, 1, 2, 3, 4]
    res = lista[4] / lista[0]
except Exception as e:
    print(f'hubo un error de tipo: {type(e).__name__}')
else:
    print(f'El resultado de la operación es: {res}')
finally:
    print('este bloque se ejecuta independiente del try o el except')
