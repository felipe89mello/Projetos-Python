def leia_int(msg):
    ok = False
    valor = 0
    print('-'*30)
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mERRO! Digite um número inteiro válido.\33[m')
        if ok:
            break
    return valor


# Programa principal
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
