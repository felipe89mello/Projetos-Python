pessoas = []
dados = []
maipeso = menpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maipeso = menpeso = dados[1]
    else:
        if dados[1] > maipeso:
            maipeso = dados[1]
        if dados[1] < menpeso:
            menpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-*'*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maipeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maipeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menpeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menpeso:
        print(f'[{p[0]}] ', end='')
print()

