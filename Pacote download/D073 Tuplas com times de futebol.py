tabela = ('Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense',
          'Athletico PR', 'Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol',
          'Flamengo', 'Coritiba', 'Santos', 'Botafogo', 'Vitória', 'Remo',
          'Atlético MG', 'Internacional', 'Cruzeiro', 'Vasco')
print (f'Tabela do Brasileirão: {tabela}')
print('~'*100)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('~'*100)
print(f'Os quatro ultimos são: {tabela[-4:]}')
print('~'*100)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('~'*100)
print(f'A Chapecoense está na {tabela.index('Chapecoense')+1}ª posição.')


