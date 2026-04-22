Galera = list()
Pessoa = dict()
opção = 0
while opção != 3:
    print('-' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('-' * 50)
    print(''' \33[1;33m\t\t1 - \33[0;34mVer pessoas cadastradas 
        \33[1;33m2 - \33[0;34mCadastrar nova pessoa
        \33[1;33m3 - \33[0;34mSair do Sistema\33[m''')
    print('-' * 50)
    opção = int(input('\33[1;33mSua Opção: \33[m'))
    if opção > 3:
        print('\33[1;31mOpção Inválida. Tente novamente.\33[m')
    elif opção == 2:
        print('-' * 50)
        print('NOVO CADASTRO'.center(50))
        print('-' * 50)
        Pessoa.clear()
        Pessoa['Nome'] = str(input('Nome: '))
        Pessoa['Idade'] = int(input('Idade: '))
        Galera.append(Pessoa.copy())
    elif opção == 1:
        print('-' * 50)
        print('PESSOAS CADASTRADAS'.center(50))
        print('-' * 50)
        for p in Galera:
                print(f'{p["Nome"]:<35} \t{p["Idade"]} anos')


