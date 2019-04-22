def mejora_receta(pizza,topping):
    '''
    (list,str)-> list: pizza mejorada

    >>> mejora_receta(['queso','maiz tierno','carne desmechada'],'camarones')
    ['queso', 'maiz tierno', 'carne desmechada', 'camarones']

    >>> mejora_receta('queso','camarones')
    ingrese una lista y un string con el topping a adicionar
    'queso'

    >>> mejora_receta('queso',['camarones'])
    ingrese una lista y un string con el topping a adicionar
    'queso'

    :param pizza: list: pizza a mejorar
    :param topping: str: topping a agregar
    :return: list: pizza mejorada
    '''

    try:
        if topping not in pizza:
            nueva_pizza= pizza
            nueva_pizza.append(topping)
    except TypeError:
        print('ingrese una lista y un string con el topping a adicionar')
    except AttributeError:
        print('ingrese una lista y un string con el topping a adicionar')

    return  sorted(nueva_pizza)

def doble_queso(pizza):
    '''
    (list)-> list: pizza doble queso

    >>> doble_queso(['queso','carne','queso'])
    ['queso', 'carne', 'queso']

    >>> doble_queso(['queso','carne','pollo'])
    ['queso', 'carne', 'pollo', 'queso']

    >>> doble_queso(['carne','pollo'])
    ['queso', 'carne', 'pollo', 'queso']

    :param pizza: pizza actual
    :return: list: pizza doble queso
    '''

    try:
        nueva_pizza = pizza
        if not(nueva_pizza[0]=='queso'):
            pizza.insert(0,'queso')
        if not(nueva_pizza[-1]=='queso'):
            pizza.append('queso')


    except TypeError:
        print('bored')

    return pizza

import ejerciciosIn as vocales


def contar_vocales(cadena):
    '''
    str-> int: cuenta numero de vocales en una cadena

    >>> contar_vocales('mama')
    2

    >>> contar_vocales('murcielago')
    5

    :param cadena:str: palabra con vocales
    :return: int: numero de vocales en una cadena
    '''
    cont = 0
    for vocal in cadena:
        if(vocales.siesvocal(vocal)):
            cont+=1
    return cont

def contar_consonantes(cadena):
    '''
    (list)->int: numero de consonantes

    >>> contar_consonantes('mama')
    2

    >>> contar_consonantes('perro')
    3

    :param lista_cadenas: lista de cadenas para contar las consonantes
    :return: int: numero de consonantes
    '''
    cont = 0
    for consonante in cadena:
        if vocales.siesconsonante(consonante):
            cont+=1
    return cont



def contartodo(cadenas):
    '''
    (list)-> list[int,int]

    cuenta vocales en la primera posicion y cuenta consonantes en la segunda

    >>> contartodo(['mama','perro','sebastian'])
    [8, 10]

    >>> contartodo(['juan','Sebastian','Bueno','Feria'])
    [12, 11]


    :param cadenas: list: lista de cadenas a analizar
    :return: list[int,int]: lista de enteros contando vocales y consonantes
    '''
    cont=[0,0]
    for cadena in cadenas:
        for letra in cadena:
            if vocales.siesvocal(letra):
                cont[0]+=1
            elif vocales.siesconsonante(letra):
                cont[1]+=1

    return cont