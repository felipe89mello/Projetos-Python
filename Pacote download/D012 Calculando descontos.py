preço = float(input('Qual o valor do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O Produto que custava R${:.2f}, com o desconto de 5% vai custar R${:.2f}'.format(preço, novo))

