jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador: '))
Jogos = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(1, Jogos+1):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['Gols'] = partidas[:]
jogador['totalGols'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O Jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador["Gols"]):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["totalGols"]} gols.')
