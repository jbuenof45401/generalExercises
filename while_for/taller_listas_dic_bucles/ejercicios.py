import math as m

def suma(vector_uno,vector_dos):
    '''
    (list,list)-> num: suma de los vectores

    >>> suma([8,2,3],[2,8,7])
    [10, 10, 10]

    >>> suma([7,8,0],[3,1,10])
    [10, 9, 10]

    :param vector_uno: num: primer valor a sumar
    :param vector_dos: num: segundo valor a sumar
    :return: list: vector resultante
    '''
    try:
        vector_a_operar = []
        vector_a_operar_dos = []
        tam_uno = len(vector_uno)
        tam_dos = len(vector_dos)
        tam_max = 0;
        tam_min = 0;
        if(tam_uno>=tam_dos):
            tam_max = tam_uno
            tam_min = tam_dos
            vector_a_operar = vector_uno
            vector_a_operar_dos = vector_dos
        else:
            tam_max = tam_dos
            tam_min = tam_uno
            vector_a_operar = vector_dos
            vector_a_operar_dos = vector_uno
        cont=0
        escalar = 0
        vector_final=vector_a_operar
        while(cont<tam_max):
            if(cont<tam_min):
                vector_final[cont] = vector_a_operar[cont] + vector_a_operar_dos[cont]
            else:
                vector_final[cont] = vector_a_operar[cont]
            cont += 1

        return vector_final


    except:
        return ('ingrese un vector con numeros')

def producto_punto(vector_uno,vector_dos):
    '''
    (list,list)->float: el producto punto de dos vectores

    >>> producto_punto([1,4,6],[1,2,3])
    27

    >>> producto_punto([1,2,3],[4,5,6])
    32

    :param vector_uno: list: primer vector a operar
    :param vector_dos: list: segundo vector a operar
    :return: float: producto punto de la operacion
    '''
    if(list != type(vector_uno) != type(vector_dos)):
        raise TypeError('por favor ingrese solo vectores')

    if (not all(isinstance(escalar,(int,float)) for escalar in vector_uno)
            or not all(isinstance(escalar_dos,(int,float)) for escalar_dos in vector_dos)):
        raise TypeError('Ingrese solo numeros en los vectores')

    vector_a_operar = []
    vector_a_operar_dos = []
    tam_uno = len(vector_uno)
    tam_dos = len(vector_dos)
    tam_max = 0
    tam_min = 0
    if(tam_uno>=tam_dos):
        tam_max = tam_uno
        tam_min = tam_dos
        vector_a_operar = vector_uno
        vector_a_operar_dos = vector_dos
    else:
        tam_max = tam_dos
        tam_min = tam_uno
        vector_a_operar = vector_dos
        vector_a_operar_dos = vector_uno
    cont=0
    escalar = 0
    while(cont<tam_max):
        if(cont<tam_min):
            escalar += vector_a_operar[cont] * vector_a_operar_dos[cont]
        else:
            escalar += vector_a_operar[cont]
        cont += 1

    return  escalar

def mayor_elemento(elementos):
    '''
    (list)-> num: retorna el mayor elemento de un arreglo

    >>> mayor_elemento([10,100,1000])
    1000

    >>> mayor_elemento([30000,50000,1])
    50000

    >>> mayor_elemento('sodasod')
    'ingrese un vector con numeros'

    :param elementos: list: lista de elementos a comparar
    :return: num: mensaje con el mayor elemento de un arreglo
    '''

    try:
        if list != type(elementos):
            raise ValueError
        tam_vector = len(elementos)
        cont = 0
        mayor = 0
        while(cont<tam_vector):
            if mayor == 0:
                mayor = elementos[cont]
            elif(mayor<elementos[cont]):
                mayor = elementos[cont]
            cont += 1
        return mayor
    except ValueError:
        return ('ingrese un vector con numeros')

def menor_elemento(elementos):
    '''
    (list)-> num: el menor elemento de un arreglo

    >>> menor_elemento([2000,1000,1])
    1

    >>> menor_elemento([1,2,0])
    0

    :param elementos: list: Lista de elementos a comparar
    :return: num: el menor elemento
    '''

    try:
        if list != type(elementos):
            raise ValueError
        tam_vector = len(elementos)
        cont = 0
        menor = 0
        while(cont<tam_vector):
            if menor == 0:
                menor = elementos[cont]
            elif(menor>elementos[cont]):
                menor = elementos[cont]
            cont += 1
        return menor
    except ValueError:
        return ('ingrese un vector con numeros')

def promedio(elementos):
    '''
    (list)-> float: promedio de los elementos del vector

    >>> promedio([4,8,12])
    8.0

    >>> promedio([2,4,6])
    4.0

    :param elementos: list: lista de elementos a comparar
    :return: float: el promedio del vector
    '''

    try:
        promedio = 0
        for num in elementos:
            promedio += num
        return promedio/len(elementos)
    except:
        return ('ingrese un vector con numeros')

def desviacion_estandar(datos):
    '''
    (list)-> float: desviacion estandar del arreglo

    >>> desviacion_estandar([1,2,3,5])
    1.479019945774904

    :param datos: list: vector a operar
    :return: float: desviacion estandart del arreglo
    '''
    try:
        media = promedio(datos)
        totaldatos = 0
        for dato in datos:
            totaldatos += (dato-media)**2
        return m.sqrt(totaldatos/len(datos))
    except:
        return ('ingrese un vector con numeros')

def norma(vector):
    '''
    (list)-> num: la norma de un vector

    >>> norma([3,4,6])
    13.0

    >>> norma([5,1,3])
    9.0

    :param vector: list: el vector a operar
    :return: num: la norma del vector
    '''

    try:
        norma = 0
        for elem in vector:
            norma += elem
        return m.sqrt(norma**2)
    except:
        return ('ingrese un vector con numeros')

def comparar(vector_uno,vector_dos):
    '''
    (list,list)-> str: indica si el vector uno es mayor, menor o igual al vector dos

    >>> comparar([1,2,4],[3,5,1])
    'menor'

    >>> comparar([4,2,6],[1,2,1])
    'mayor'

    >>> comparar([1,4,5],[1,4,5])
    'igual'

    :param vector_uno: list: primer vector a comparar
    :param vector_dos: list: segundo vector a comparar
    :return: str: indica si el vector uno es mayor, menor o igual que el segundo vector
    '''
    try:
        if norma(vector_uno)>norma(vector_dos):
            return 'mayor'
        elif norma(vector_uno)<norma(vector_dos):
            return 'menor'
        return 'igual'
    except:
        return ('ingrese un vector con numeros')