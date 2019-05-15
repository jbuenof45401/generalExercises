class Casa:
    banos = 0
    ambientes=0
    def __init__(self,direccion):
        self.banos = 0
        self.ambientes = 0
        self.direccion = direccion

    def __repr__(self):
        return f'Casa ubicada en {self.direccion}'
    def __eq__(self,other):
        return self.banos == other.banos and self.ambientes==other.ambientes

class Punto:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return f'El punto esta en ({self.x},{self.y})'
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def desplazar_x(self,x):
        self.x += x
        return self
    def desplazar_y(self,y):
        self.y += y
        return self

    def hallar_pendiente(self,other):
        if(self!=other):
            m = (other.y- self.y)/(other.x-self.x)
        return f'La pendiente entre los dos puntos es {m}'


