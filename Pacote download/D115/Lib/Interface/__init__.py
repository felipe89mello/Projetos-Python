def leiaint(msg):
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


def linha(tam = 42):
    return'-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\33[33m{c} - \33[34m{item}\33[m')
        c += 1
    print(linha())
    opc = leiaint('\33[33mSua Opção: \33[m')
    return opc









