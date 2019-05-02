from while_for import vectores_menu as v
matrices = {}

def ingresar_vector():
    '''Permite leer un vector del usuario...'''
    vector = []

    while True:
        num = input('Ingrese su escalar o "s" para terminar')
        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print (num, 'no es un escalar')
        else:
            break
    return vector


def op_leer_matriz():
    '''
    Lee una matriz por teclado
    :return:(list of list of int) la matriz del usuario
    '''
    resultado = []
    while True:
        entrada = input('desea ingresar una fila? s/n')
        if entrada == 'n':
            break
        resultado.append(ingresar_vector()[1:])

    return resultado

def op_suma_matrices(matrizuno,matrizdos):
    '''
    (list[][],list[][]) -> list[][]: matriz resultante de la suma.

    >>> op_suma_matrices([[1,3,5],[2,1,1]],[[1,2,3],[3,2,1]])
    [[2,5,8],[5,4,4]]

    :param matrizuno: list[][]: matriz uno
    :param matrizdos: list[][]: matriz dos
    :return: list[][]: matriz resultante
    '''
    tamtotal = 0
    tam = len(matrizuno)
    tamdos = len(matrizdos)
    if tam >= tamdos:
        tamtotal = tam



def principal():
    MENSAJE = '''Seleccione una opcion:
    0. Salir
    1. ingresar Matriz
    2. mostrar matrices
    '''
    while True:

        opcion = input(MENSAJE)
        if opcion == '0':
            print('muchas gracias por participar!')
            break
        elif opcion == '1':
            nombre = input('¿Cual es el nombre de su matriz?')
            matriz = op_leer_matriz()
            matrices[nombre] = matriz
        elif opcion == '2':
            print('sus matrices')
            for matriz in matrices:
                print(matriz,'=')
                print(matrices[matriz])
        elif opcion == '3':
            print('sus matrices')
            for matriz in matrices:
                print(matriz, '=')
                for fila in matrices[matriz]:
                    print(fila)
        else:
            print('Seleccione una opcion valida')


if __name__ == '__main__':
    principal()