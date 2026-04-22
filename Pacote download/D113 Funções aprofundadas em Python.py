def leia_int(msg):
    print('-'*30)
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[0;31mERRO! Digite um número inteiro válido.\33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\33[0;31mERRO! Entrada de dados interrompida pelo usuário.\33[m')
            return 0
        else:
            return n


def leia_float(msg):
    print('-'*30)
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[0;31mERRO! Digite um número real válido.\33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\33[0;31mERRO! Entrada de dados interrompida pelo usuário.\33[m')
            return 0
        else:
             return n

# Programa principal
ni = leia_int('Digite um número inteiro: ')
nr = leia_float('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {ni} e o número real {nr}')
