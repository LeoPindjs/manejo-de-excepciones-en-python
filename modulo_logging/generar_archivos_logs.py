import logging as lg
import traceback

lg.basicConfig(
    level=lg.ERROR,
    filename='errors.log',
    format='%(asctime)s : %(levelname)s : %(message)s'
)


def imprimir_logs_de_error(e):
    exception_info = {
        'message': str(e),
        'description': traceback.format_exc(),
    }
    """ lg.error(str(e)) """
    lg.error(exception_info)


try:
    numerador = 10
    denominador = 0
    res = numerador / denominador
except Exception as e:
    imprimir_logs_de_error(e)
