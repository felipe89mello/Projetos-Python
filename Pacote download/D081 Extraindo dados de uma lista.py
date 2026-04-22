lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-*-' * 30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 apareceu na lista')
else:
    print('O valor 5 NÃO apareceu na lista')

