class OneException(Exception):
    def __init__(self):
        super().__init__('one')


class TowException(Exception):
    def __init__(self):
        super().__init__('tow')


class ThreeException(Exception):
    def __init__(self):
        super().__init__('three')


""" raise ExceptionGroup(
    'Excepciones grupales',
    [OneException(), TowException(), ThreeException()]
) """

try:
    raise ExceptionGroup(
        'Excepciones grupales',
        [OneException(), TowException(), ThreeException()]
    )

except *OneException:
    print('Error de tipo uno')
except *TowException:
    print('Error de tipo dos')
except *ThreeException:
    print('Error de tipo tres')

""" except ExceptionGroup as group:
    print(group) """


