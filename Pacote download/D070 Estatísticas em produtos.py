total = totmil = menor = cont = 0
barato = ''
while True:
    print('-'*30)
    print('LOJA SUPER BARATÃO')
    print('-'*30)
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print('O total da compra foi R$ {:.2f}'.format(total))
print(f'Temos {totmil} produtos custando mais de R$ 1000,00.')
print(f'O produto mais barato foi o {barato} e custa R$ {menor:.2f}')
