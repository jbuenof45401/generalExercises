import json

prueba = {'prueba':['','']}
def escribir(nombre_archivo,diccionario):
    '''
    (str,{})-> str: escritura exitosa

    >>> escribir('matrices.txt',diccionario)

    :param nombre_archivo: ruta del archivo donde se guarda la info
    :return: bool: True:guardado Exitoso,False:no hay nada para guardar
    '''
    try:
        archivo=open(nombre_archivo,'w')
        archivo.write(json.dumps(diccionario))
        archivo.close()
        return True
    except:
        return False




def leer(nombre_archivo):
    '''
    (str) -> dic{diclist[][]} leer matriz de archivo

    :param nombre_archivo: str: nombre del archivo
    :return: archivo 
    '''
    
    try:
        archivo=open(nombre_archivo,'r')
        
        diccionario_leido = json.load(archivo)
        
        archivo.close()
        return diccionario_leido
    except:
        raise TypeError('hubo un error en la lectura del archivo')

