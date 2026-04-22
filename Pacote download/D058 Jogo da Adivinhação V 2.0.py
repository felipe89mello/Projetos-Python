from random import randint
from time import sleep
computador = randint(0, 10)
print('\33[2;7;40m-=-=-=-=-=-JOGO DA ADIVINHAÇÃO-=-=-=-=-=-= V 2.0\33[m')
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('PARABÉNS! Acertou com {} tentativas!'.format(palpites))
