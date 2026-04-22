print('\33[1;30;43mBem vindo ao aprovador!\33[m')
imóvel = float(input('QUal o valor do imóvel? R$ '))
salário = float(input('Qual é o seu salário? R$ '))
tempo = int(input('Em quantos anos deseja pagar? '))
prestação = imóvel / (tempo * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(imóvel,tempo), end='')
print(' a prestação será de R$ {:.2f}.'.format(prestação))
if prestação <= mínimo:
    print('\33[1;32mO emprestimo pode ser concedido!\33[m')
else:
    print('\33[1;31mEmprestimo Negado!\33[m')

