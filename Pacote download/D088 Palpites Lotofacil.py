from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
print('-'*40)
print('               \33[1;35mLOTOFÁCIL\33[m        ')
print('-'*40)
quant = int(input('Quantos jogos deseja gerar? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 25)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 15:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'\33[1;30;44mSORTEANDO {quant} JOGOS\33[m', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '\33[1;33m< BOA SORTE >\33[m', '-='*5)