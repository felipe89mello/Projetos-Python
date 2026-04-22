print('-=-'*30)
print('\33[4;7mCALCULANDO O ÍNDICE DE MASSA CORPORAL\33[m')
print('-=-'*30)
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você estã na faixa de PESO NORMAL!')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
input('Aperte enter para fechar.')
