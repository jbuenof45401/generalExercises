def siesvocal(vocal):
    '''
    str (len(1)) -> bool

    recibe una letra y retorna true si es vocal si no false

    >>> siesvocal('x')
    False

    >>> siesvocal('a')
    True



    :param vocal: letra a analizar
    :return: true si es vocal, false si no
    '''

    return vocal in 'aeiouAEIOU' and len(vocal) == 1