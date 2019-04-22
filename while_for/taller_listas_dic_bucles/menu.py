import while_for.taller_listas_dic_bucles.ejercicios as l
vectores = {}
def ingresar_vector():
    '''Permite leer un vector del usuario...'''
    vector = [input('¿Cual es el nombre de su vector?')]

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

def mostrar_vectores():
    for nombre in vectores:
        print (nombre, 'contiene', vectores[nombre])

def op_suma():


def principal():
    MENSAJE='''Seleccione una opcion:
    0. Salir
    1. Ingresar Vector
    2. Mostrar Vectores
    3. suma    
    4. Producto punto
    5. mayor elemento
    6. menor elemento
    7. promedio
    8. desviacion estandar
    9. comparar -> mayor, menor o igual
    10. norma
    
    '''
    while True:

        opcion = input(MENSAJE)
        if opcion=='0':
            print('muchas gracias por participar!')
            break
        elif opcion=='1':
            vector = ingresar_vector()
            vectores[vector[0]] = vector[1:]
            print('su vector ', vector[0],' es ', vectores[vector[0]])
        elif opcion=='2':
            mostrar_vectores()
        elif opcion=='3':
            l.suma()
        elif opcion=='4':
            l.producto_punto()
        elif opcion == '5':
            l.mayor_elemento()
        elif opcion == '6':
            l.menor_elemento()
        elif opcion == '7':
            l.promedio()
        elif opcion == '8':
            l.desviacion_estandar()
        elif opcion == '9':
            l.comparar()
        elif opcion == '10':
            l.norma()

        else:
            print ('Seleccione una opcion valida')

if __name__ =='__main__':
    principal()