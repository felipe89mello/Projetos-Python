from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções: 
[ 0 ] Pedra
[ 1 ) Papel
[ 2 ) Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('-='*30)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-='*30)
print('Você jogou {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-='*30)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')