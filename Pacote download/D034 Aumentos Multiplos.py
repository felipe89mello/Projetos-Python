sálario = float(input('Qual o sálario do funcionário? R$'))
if sálario <= 1250:
    novo = sálario + (sálario * 15 / 100)
else:
    novo = sálario + (sálario * 10 / 100)
print('Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}'.format(sálario, novo))


