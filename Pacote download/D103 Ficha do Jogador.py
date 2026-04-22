def ficha(jog='<desconhecido>', gols='0'):
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')

#programa principal
print('-'*30)
nome = str(input('Digite o nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)