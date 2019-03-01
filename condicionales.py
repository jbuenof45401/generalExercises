def armar_mensajes(numero):
    '''

    (float) -> str
    recibe numero float y retorna

    >>> armar_mensajes(3)
    'El numero es positivo'

    >>> armar_mensajes(-3)
    'El numero es negativo'

    :param numero:
    :return:
    '''

    if(numero<0):
        return 'El numero es negativo'

    return 'El numero es positivo'


# print(armar_mensajes(float(input("numero float"))))