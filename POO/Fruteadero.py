class Fruteadero:
    nombre=""
    inventario_frutas={}

    def __init__(self,nombre,inventario):
        self.nombre = nombre
        self.inventario_frutas=inventario



class Frutas:
    sabor = ""
    pelada = False
    cantidad = 0
    __TIPOS__ = {'banano':[3,100],'manzana':[6,50],'pera':[6,60],'piña':[20,1500],'papaya':[30,2000]}

    def __init__(self,sabor,pelada,cantidad):
        self.sabor = sabor
        self.pelada = pelada
        self.cantidad = cantidad

    def __repr__(self):
        return f'hay {self.cantidad} unidades de La fruta {self.sabor}'

    def pelar(self):
        '''
        Pela la fruta si no esta pelada
        :return: El estado de la fruta
        '''
        if not self.pelada:
            self.pelada = True
        else:
            raise ValueError('La fruta ya esta pelada')
        return self.pelada


    def cortar(self,cantidad_usar):
        '''
        Corta la cantidad de frutas indicada, solo si esta pelada
        :param cantidad_usar: la cantidad de frutas cortadas
        :return: La cantidad de fruta producida

        '''
        if cantidad_usar > self.cantidad:
            raise ValueError('No hay suficiente fruta')
        elif not self.pelada:
            raise ValueError('Pele la fruta primero')
        elif(len(self.__TIPOS__[self.sabor])>0):
            return self.__TIPOS__[self.sabor][0]*cantidad_usar
        else:
            raise ValueError('No tenemos esa fruta')

    def licuar(self,cantidad_usar):
        '''
        (float)-> float: cantidad de jugo producido

        :param cantidad:
        :return:
        '''
        if cantidad_usar>self.cantidad:
            raise ValueError('No hay suficiente fruta')
        elif not self.pelada:
            raise ValueError('Pele la fruta primero')
        elif(len(self.__TIPOS__[self.sabor])>0):
            return self.__TIPOS__[self.sabor][1]*cantidad_usar
        else:
            raise ValueError('No tenemos esa fruta')

class Jugo(Frutas):
    cantidad_hecha = 0
    def __init__(self,nombre):
        self.sabor = nombre
    def __repr__(self):
        return f'jugo de {self.sabor}'

    def preparar(self,cantidad_jugo_mililitros):
        fruta_a_usar = cantidad_jugo_mililitros/self.__TIPOS__[self.sabor][1]
        super(Jugo, self).cortar(fruta_a_usar)
        self.cantidad_hecha += super(Jugo,self).licuar(fruta_a_usar)
        return f'Se preparo {cantidad_jugo_mililitros} mililitros de jugo de {self.sabor} '
    def cuantojugohay(self):
        return f'Hay {self.cantidad_hecha} mililitros de jugo listo'