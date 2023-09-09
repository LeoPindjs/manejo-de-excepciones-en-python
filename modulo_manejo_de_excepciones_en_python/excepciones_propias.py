from excepciones_personalizadas import UsuarioNullException as UNException
from excepciones_personalizadas import UsuarioLenException as ULException


def validar_usuario(usuario=None):
    if usuario == None:
        raise UNException()
    if len(usuario) < 6:
        raise ULException(f'ERROR: usuario {usuario}')
    return True


try:
    res = validar_usuario('abc')
except Exception as e:
    print(e)
else:
    print(res)
