time = list()
jogadores = dict()
partidas = list()
while True:
    jogadores.clear()
    jogadores['Nome'] = str(input('Nome do Jogador: '))
    Jogos = int(input(f'Quantas partidas {jogadores["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, Jogos):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogadores['Gols'] = partidas[:]
    jogadores['totalGols'] = sum(partidas)
    time.append(jogadores.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ',end='')
for i in jogadores.keys():
    print(f'{i:<15} ',end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe um jogador com {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<< VOLTE SEMPRE >>>')
