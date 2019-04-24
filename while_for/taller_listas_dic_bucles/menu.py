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
    flag = 1
    seleccion=[]
    if(len(vectores)<2):
        print ('debe haber ingresado almenos dos vectores, seleccione la opcion 1 para hacerlo')
        return None
    while flag<=2:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag+=1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')
    print('la suma es ',
    l.suma(vectores[seleccion[0]],vectores[seleccion[1]]))

def op_producto_punto():
    flag = 1
    seleccion=[]
    if(len(vectores)<2):
        print ('debe haber ingresado almenos dos vectores, seleccione la opcion 1 para hacerlo')
        return None
    while flag<=2:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag+=1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')
    print('el producto punto es ',
          l.producto_punto(vectores[seleccion[0]],vectores[seleccion[1]]))
def op_mayor_elemento():
    flag = 1
    seleccion=[]
    if(len(vectores)<1):
        print ('debe haber ingresado almenos 1 vector, seleccione la opcion 1 para ingresar vectores')
        return None

    while flag<=1:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag+=1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')
    print('el mayor elemento del vector es ',
          l.mayor_elemento(vectores[seleccion[0]]))
def op_menor_elemento():
    flag = 1
    seleccion=[]
    if(len(vectores)<1):
        print('debe haber ingresado almenos 1 vector, seleccione la opcion 1 para ingresar vectores')
        return None
    while flag<=1:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag+=1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')
    print('el menor elemento del vector es ',
          l.menor_elemento(vectores[seleccion[0]]))

def promedio():
    flag = 1
    seleccion=[]
    if(len(vectores)<1):
        print('debe haber ingresado almenos 1 vector, seleccione la opcion 1 para ingresar vectores')
        return None
    while flag<=1:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag+=1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')
    print('el promedio del vector es ',
          l.promedio(vectores[seleccion[0]]))

def op_desviacion_estandart():
    flag = 1
    seleccion=[]
    if(len(vectores)<1):
        print('debe haber ingresado almenos 1 vector, seleccione la opcion 1 para ingresar vectores')
        return None
    while flag<=1:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag+=1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')
    print('la desviacion estandar del vector es ',
          l.desviacion_estandar(vectores[seleccion[0]]))

def op_comparar():
    flag = 1
    seleccion=[]
    if(len(vectores)<2):
        print('debe haber ingresado almenos dos vectores, seleccione la opcion 1 para ingresar vectores')
        return None
    while flag<=2:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag+=1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')
    print('el vector ', seleccion[0] ,' es ',
          l.comparar(vectores[seleccion[0]],vectores[seleccion[1]]), ' que el vector ' , seleccion[1] )

def op_norma():
    flag = 1
    seleccion=[]
    if(len(vectores)<1):
        print('debe haber ingresado almenos 1 vector, seleccione la opcion 1 para ingresar vectores')
        return None
    while flag<=1:
        try:
            print('escoja el vector numero ',flag)
            mostrar_vectores()
            seleccion.append(input())
            flag += 1
        except:
            print('la opcion no es valida, ingrese el nombre del vector que desee')

    print('el mayor elemento del vector es ',
          l.mayor_elemento(vectores[seleccion[0]]))

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
            op_suma()
        elif opcion=='4':
            op_producto_punto()
        elif opcion == '5':
            op_mayor_elemento()
        elif opcion == '6':
            op_menor_elemento()
        elif opcion == '7':
            promedio()
        elif opcion == '8':
            op_desviacion_estandart()
        elif opcion == '9':
            op_comparar()
        elif opcion == '10':
            op_norma()

        else:
            print ('Seleccione una opcion valida')

if __name__ =='__main__':
    principal()