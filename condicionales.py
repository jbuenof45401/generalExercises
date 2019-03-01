import time

def armar_mensajes(numero):
    '''

    (float) -> str
    recibe numero float y retorna

    >>> armar_mensajes(3)
    'El numero es positivo'

    >>> armar_mensajes(-3)
    'El numero es negativo'

    :param numero: float el numero flotante a validar
    :return: str: si es positivo o negativo
    '''

    if(numero<0):
        return 'El numero es negativo'

    return 'El numero es positivo'

def quien_es_mayor(edad_uno,edad_dos):
    '''
    (num) -> str

    indica quien de los dos es mayor

    >>> quien_es_mayor(18,20)
    'El mayor es el segundo'

    >>> quien_es_mayor(29,19)
    'El mayor es el primero'

    >>> quien_es_mayor(29,29)
    'los dos tienen la misma edad'

    :param edad_uno: num: edad primer persona
    :param edad_dos: num: edad segunda persona
    :return: str: mensaje si es mayor, menor o tienen la misma edad
    '''

    mensaje = ''

    if (edad_uno > edad_dos):
        mensaje = 'El mayor es el primero'
    elif (edad_uno < edad_dos):
        mensaje = 'El mayor es el segundo'
    else:
        mensaje = 'Ambos tienen la misma edad'


    return mensaje

def saludo_segun_hora(hora):
    '''
    (num)-> str

     >>> saludo_segun_hora(19)
     'Buenas noches'

     >>> saludo_segun_hora(1)
     'Buenos dias'

     >>> saludo_segun_hora(12)
     'Buenas tardes'

    :param hora: num: la hora actual
    :return: str: el saludo segun la hora
    '''

    if(hora<12):
        return 'Buenos dias'
    elif(hora>=12 and hora<18):
        return 'Buenas tardes'
    else:
        return 'Buenas noches'

print(saludo_segun_hora(int(time.strftime("%H"))))