num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
'dezoito', 'dezenove', 'vinte')
cont2 = ' '
resp = 0
while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    if 0 <= resp <= 20:
        print('Você digitou o número {}.'.format(num[resp]))
        cont2 = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    else:
        print('Tente novamente.', end=' ')
    if cont2 not in 'SN':
        cont2 = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    elif cont2 in 'N':
        break
print('FIM DO PROGRAMA')