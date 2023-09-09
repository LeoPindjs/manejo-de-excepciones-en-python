class UsuarioNullException(Exception):
    def __init__(self):
        self.msj = 'El usuario es obligatorio'
        super().__init__(self.msj)


class UsuarioLenException(Exception):
    def __init__(self, msj_usuario):
        self.msj = f'{msj_usuario} debe tener más de 6 caracteres'
        super().__init__(self.msj)
