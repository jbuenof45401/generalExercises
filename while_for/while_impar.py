def analizar_hv(perfil,competencias):
    '''
    (list,list)-> float: porcentaje de cumplimiento del perfil

    >>> analizar_hv(['ingeniero de sistemas','c#', '.net'],['ingeniero de sistemas','python','java'])
    33.33

    :param perfil: list: lista de requisitos
    :param competencias: list: lista de habilidades
    :return: float: porcentaje de cumplimiento
    '''
    if (list != type(perfil) or list!= type(competencias)):
        raise TypeError('Por favor ingrese lista de perfiles y competencias')

    cumplimiento = 0
    tam = len(perfil)
    copia = perfil.copy()
    while copia:
        requisito = copia.pop()
        if requisito in competencias:
            cumplimiento += (1/tam) * 100

    return cumplimiento



pizza = []
cont=1
while True:
    ingrediente = input('ingrese el ingrediente:\n')
    if ingrediente=='no mas':
        break
    pizza.append(ingrediente)

print (' su pizza esta lista :  ', pizza)




flag = True
while flag:
    dato = input('ingrese un dato:\n')
    try:
        dato = int(dato)
        if (int != type(dato)):
            print (dato)
        else:
            if (dato % 2 != 0):
                flag = False
            else:
                print (dato)
    except:
        print (dato)

print ("por fin le pego" , dato)



