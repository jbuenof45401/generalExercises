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

def siesconsonante(consonante):
    '''
    str (len(1)) -> bool

    recibe una letra y retorna true si es vocal si no false

    >>> siesconsonante('x')
    True

    >>> siesconsonante('a')
    False



    :param consonante: letra a analizar
    :return: true si es consonante, false si no
    '''

    return consonante in 'BCDFGHJKLMNÑPQRSTVWXYZbcdfghjklmnñpqrstvwxyz' and len(consonante) == 1