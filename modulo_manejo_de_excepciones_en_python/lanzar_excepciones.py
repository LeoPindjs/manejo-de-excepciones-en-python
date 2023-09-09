def validar_usuario(usuario=None):
    if usuario == None:
        raise Exception('El usuario es obligatorio')
    if len(usuario) < 6:
        raise Exception('el usuario debe tener más de 6 caracteres')
    return True


try:
    res = validar_usuario('asd')
except Exception as e:
    print(e)
else:
    print(res)
