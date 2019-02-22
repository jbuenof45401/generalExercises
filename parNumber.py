import math


def area_circulo(radio):
    '''
    (num)-> float

    calcula el area de un circulo dado el radio
    >>> area_circulo(1)
    3.141592653
    >>>area_circulo(2)
    6.2831
    :param radio: representa el radio del circulo
    :return float que representa el area del circulo
'''
    return radio * math.pi

def perimetro_triangulo(luno,ldos,ltres):
    '''
    (num,num,num) -> num...

    >>>perimetro_triangulo(1,2,3)
    6
    >>>perimetro_triangulo(2,2,2)
    6
    :param luno: primer lado del triangulo
    :param ldos: segundo lado del triangulo
    :param ltres: tercer lado del triangulo
    :return: float que representa el perimetro del triangulo
    '''
    return  luno+ldos+ltres

def semi_perimetro_triangulo(luno,ldos,ltres):
    '''
    (num,num,num)->num...

    >>>semi_perimetro_triangulo(1,2,3)
    3
    >>>semi_perimetro_triangulo(2,2,2)
    3
    :param luno: primer lado del triangulo
    :param ldos: segundo lado del triangulo
    :param ltres: tercer lado del triangulo
    :return: float que representa el perimetro del triangulo
    '''
    return  perimetro_triangulo(luno,ldos,ltres)/2

def area_triangulo(luno,ldos,ltres):
    '''
    (num,num,num)->num...

    >>>area_triangulo(1,2,4)
    3
    >>>area_triangulo(2,2,2)
    3
    :param luno: primer lado del triangulo
    :param ldos: segundo lado del triangulo
    :param ltres: tercer lado del triangulo
    :return: float que representa el area del triangulo
    '''
    semiperimetro=semi_perimetro_triangulo(luno, ldos, ltres)
    area =math.sqrt((semiperimetro*(semiperimetro-luno))*(semiperimetro*(semiperimetro-ldos))*(semiperimetro*(semiperimetro-ltres)))
    '''area = float(math.sqrt((semiperimetro*(semiperimetro-luno)(semiperimetro-ldos)(semiperimetro-ltres))))'''
    return area

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

def si_es_par(num):
    '''
    (str)->muestra un mensaje si el numero es par

    indica si el numero es par
    >>>si_es_par(45)
    el numero no es par
    param num: numero para validar si es o no par
    :return: str mensaje que indica si el numero es par
    '''
    return print('el numero ',num,' es par ',par(num))


def area_circulo(radio):
    '''
    (num) -> float

    >>> area_circulo(3)
    25.82484413952496

    >>> area_circulo(2)
    10.566370614359172
    :param radio: num: el radio de un circulo
    :return: el area del circulo
    '''

    areaCirculo = math.pi * (radio**2)
    areacuadrado = math.sqrt((radio+radio))

    return areaCirculo-areacuadrado

