contmaior = homem = mulher = mulhermaior =  0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Qual a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        contmaior += 1
    print('-'*30)
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=======PROGRAMA FINALIZADO=======')
print('Total de pessoas com mais de 18 anos: {}'.format(contmaior))
print (f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')