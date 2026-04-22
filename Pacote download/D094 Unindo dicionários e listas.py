Galera = list()
Pessoa = dict()
soma = média = 0
print('-='*35)
print('{:^80}'.format('\33[1;33m<<<  ANALISANDO DADOS DAS PESSOAS  >>>\33[m'))
print('-='*35)
while True:
    Pessoa.clear()
    Pessoa['Nome'] = str(input('Nome: '))
    while True:
        Pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if Pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas o Sexo M ou F.')
    Pessoa['Idade'] = int(input('Idade: '))
    soma += Pessoa['Idade']
    Galera.append(Pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*40)
print(f'A) Ao todo temos {len(Galera)} pessoas cadastradas.')
média = soma / len(Galera)
print(f'B) A média de idade é de {média:5.1f} anos. ')
print(f'C) A mulheres cadastradas foram: ', end='')
for p in Galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in Galera:
    if p ['Idade'] >= média:
        print('   ', end=' ')
        for k, v in p.items():
            print(f' {k} =  {v}; ', end='')
        print()
print('<< ENCERRADO >>')


