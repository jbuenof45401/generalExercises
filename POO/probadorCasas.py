from POO.introPOO import Casa,Punto

mi_casa = Casa('Calle 123 carrera 456')
casa_vecino = Casa('Calle 124 carrera 456')
casa_homero = Casa('Evergreen terrace 123, Springfield')

print(f'mi casa es {mi_casa}, la del vecino es {casa_vecino}, y la de homero es {casa_homero}')

mi_casa.banos = 2
mi_casa.ambientes=4

setattr(casa_vecino,'banos',3)
setattr(casa_vecino,'ambientes',6)

print(f'Mi Casa tiene {mi_casa.ambientes} ambientes'
      f'La del vecino tiene {getattr(casa_vecino,"ambientes")}')

atributos = casa_homero.__dict__
print(atributos)
for dic in atributos:
    print(f'Atributo {dic} con el valor {atributos[dic]} en la casa homero')

if mi_casa == casa_vecino:
    print('mi casa y la del vecino son iguales')
else:
    print('mi casa y la del vecino son diferentes')

Punto_inicial = Punto(1,2)
otro_punto = Punto(3,4)

print(f'El punto inicial es {Punto_inicial} y el otro punto es {otro_punto}')

print(f'el resultado de dezplazar 4 puntos en x es {Punto_inicial.desplazar_x(4)}')

print(f'el resultado de dezplazar 1 puntos en y es {Punto_inicial.desplazar_y(1)}')

print(Punto.hallar_pendiente(Punto_inicial,otro_punto))