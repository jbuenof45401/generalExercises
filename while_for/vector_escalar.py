def producto_escalar(escalar, vector):
    '''
    devuelve el vector_producto de un escalar

    >>> producto_escalar(2,[1,2,3])
    [2,4,6]


    :param escalar: escalar a operar
    :param vector: vector a operar
    :return: vector producto del escalar
    '''

    res =[]
    cont=0
    while cont<len(vector):
        res.append(escalar*vector[cont])
        cont+=1

    return res
