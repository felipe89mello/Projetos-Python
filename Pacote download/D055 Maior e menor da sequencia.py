maior = 0
menor = 0
for pess in range(1, 7):
    peso = float(input('Qual é o peso da {}ª pessoa? '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}'.format(maior))
print('O menor peso lido foi {}'.format(menor))
