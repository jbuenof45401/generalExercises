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