numero = input('ingrese un numero')
numero2 = input('ingrese otro numero')
try:
    print('la division del numero {0} y el numero {1} da {2}'.format(numero,numero2,int(numero)/int(numero2)))
except ZeroDivisionError:
    print('hubo un error en la division, el divisor no puede ser 0')
except ValueError:
    print('ingrese solo numeros')

