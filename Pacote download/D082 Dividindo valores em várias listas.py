lista = []
lpares = []
límpares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lpares.append(v)
    elif v % 2 == 1:
        límpares.append(v)
print('-*-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lpares}')
print(f'A lista de ímpares é {límpares}')

