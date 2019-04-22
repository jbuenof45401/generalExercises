def euros_en_monedas(euros):
    '''
    (num) -> str: el discriminado en billetes y monedas del valor

    >>> euros_en_monedas(434)
    '2 billetes de 200'
    '1 billete de 20'
    '1 billete de 10'
    '2 monedas de 2'
    >>> euros_en_monedas(304)
    '1 billetes de 200'
    '1 billete de 100'
    '2 monedas de 2'

    :param euros: cantidad de euros a procesar
    :return: str: mensaje segun el valor de euros ingresados
    '''

    if(int != type(euros)):
        raise TypeError('lampara')
    mensaje = ""
    billetes_500 = euros//500
    mod_500 = euros%500
    mod_200 = 0
    mod_100 = 0
    mod_10 = 0
    if billetes_500:
        mensaje += str(billetes_500) + ' billetes de 500'
    if mod_500:
        billetes_200 = mod_500//200
        mod_200 = euros%mod_500
        if billetes_200:
            mensaje += str(billetes_200) + ' billetes de 200'
    if mod_200:
        billetes_100=mod_200//100
        mod_100=euros%mod_200
        if billetes_100:
            mensaje+=str(billetes_100) + ' billetes de 100'
    if mod_100:
        billetes_10=mod_100//10
        mod_10=euros%mod_100
        if billetes_10:
            mensaje += str(billetes_10) + ' billetes de 10'
    if mod_10:
        monedas_dos=mod_10//2
        mod_dos=euros%2







    return mensaje


