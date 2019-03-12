def numero_negativo(num):
    '''
    (num)-> bool

    determina si el numero es negativo

    >>> numero_negativo(-2)
    'el numero es negativo'

    >>> numero_negativo(2)
    'el numero es positivo'

    >>> numero_negativo('ff')
    Traceback (most recent call last):
    ..
    TypeError: <class 'str'> no es un entero

    :return: str: true si es negativo
    '''
    if(int!=type(num)!=float):
        raise TypeError(str(type(num))+' no es un entero')

    if(num<0):
        return 'el numero es negativo'
    else:
        return 'el numero es positivo'



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

    if(int != type(numero)):
        raise  TypeError('debe ingresar solo enteros')

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
    'Ambos tienen la misma edad'

    :param edad_uno: num: edad primer persona
    :param edad_dos: num: edad segunda persona
    :return: str: mensaje si es mayor, menor o tienen la misma edad
    '''
    if(int != type(edad_uno)!=type(edad_dos)):
        raise TypeError('ingrese solo numeros enteros')

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
    if(int != type(hora)):
        raise TypeError('ingrese solo numeros enteros')

    if(hora<12):
        return 'Buenos dias'
    elif(hora>=12 and hora<18):
        return 'Buenas tardes'
    else:
        return 'Buenas noches'

def parentesis(caracter):
    '''
    (str of len = 1) -> str

    Analisa si el caracter recibido es un parentesis

    >>> parentesis('c')


    >>> parentesis('(')
    'El caracter es un parentesis'

    >>> parentesis('xa')
    Traceback (most recent call last):
    ..
    TypeError: xa no es un parentesis

    :param caracter: char: caracter a analisar
    :return: str: el mensaje indicando si es o no parentesis
    '''
    if(len(caracter)!=1):
        raise TypeError(str(caracter) + ' no es un parentesis')
    if(caracter in '()'):
        return 'El caracter es un parentesis'

def division(dividendo,divisor):
    '''
    (num,num) -> float

    divide un nùmero entre otro

    >>> division(3,3)
    1.0

    >>> division(3,0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError

    >>> division('sjd',34)
    Traceback (most recent call last):
    ..
    TypeError: sjd or 34 no son numeros

    >>> division([1,2,3],3)
    Traceback (most recent call last):
    ..
    TypeError: [1, 2, 3] or 3 no son numeros

    >>> division(1,0.0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError

    :param dividendo: num: el numero a dividir
    :param divisor: num: el numero que divide
    :return: float: el resultado de la divisiòn
    '''
    if(int != type(dividendo) != float):
        raise TypeError(str(dividendo) + ' or ' + str(divisor) + ' no son numeros')
    elif (int != type(divisor) != float):
        raise TypeError(str(dividendo) + ' or ' + str(divisor) + ' no son numeros')
    elif(divisor==0):
        raise ZeroDivisionError
    return dividendo/divisor

def el_doble_impar(numero):
    '''
    (int)-> str

    determina si el numero ingresado es el doble de un numero impar

    >>> el_doble_impar('str')
    Traceback (most recent call last):
    ..
    TypeError: str no es un entero

    >>> el_doble_impar(14)
    'El numero 14 es el doble de 7.0, que es impar'

    :param numero: entero a validar
    :return: str: si el numero es el doble de un entero retorna el mensaje correspondiente
    '''
    if(int!= type(numero)):
        raise TypeError(str(numero) + " no es un entero")
    if(numero%2==0):
        return 'El numero ' + str(numero) + ' es el doble de ' + str(numero/2) + ', que es impar'

def par_o_impar(num):
    '''
    (float)->str
    imprime un mensaje si el numero es par o no

    >>> par_o_impar(2)
    'el numero es par'

    >>> par_o_impar(3)
    'el numero es impar'

    >>> par_o_impar('s')
    Traceback (most recent call last):
    ..
    TypeError: <class 'str'> no es un entero

    :param: num: el numero a analizar
    :return: str: mensaje si el numero es par o impar
    '''

    if(int !=type(num)):
        raise TypeError(str(type(num)) + ' no es un entero')

    if(num<0):
        raise TypeError('el numero no debe ser menor a 0')
    elif(par(num)):
        return 'el numero es par'
    else:
        return 'el numero es impar'

def numero_primo(num):
    '''
    (int)-> str: si es primo o no

    >>> numero_primo(31)
    'es un numero primo'

    >>> numero_primo(400)
    'no es un numero primo'

    >>> numero_primo('s')
    Traceback (most recent call last):
    ..
    TypeError: <class 'str'> no es un entero

    :param num: numero a determinar si es o no primo
    :return: str: mensaje si el numero es primo o no
    '''

    if(int != type(num)):
        raise  TypeError(str(type(num))+ ' no es un entero')

    if((num%2==0 and num!=2) or (num%3==0 and num!=3) or (num%5==0 and num!=5) or (num%7==0 and num != 7)):
        return 'no es un numero primo'
    else:
        return 'es un numero primo'


def par(num):
    '''
    (bool)->bool...

    si es impar false, si no true
    >>>par(1)
    false
    >>>par(2)
    true
    :param num:representa un numero entero
    :return: bool, si el numero es par true, si no false
    '''
    return num%2==0
