def invertir_lista(lista):
    '''
    (list)-> list: invierte una variable


    >>> invertir_lista(['a',10,'jose',True])
    [True,'jose',10,'a']
    :param lista: lista a invertir
    :return: list: lista invertida
    '''

    resultado = []
    for i in range(-1,-len(lista)-1,-1):
        resultado.append(lista[i])
    for elemento in lista:
        resultado.insert(0,elemento)

    copia = lista.copy()

    while copia:
        resultado.append(copia.pop())

    return resultado



