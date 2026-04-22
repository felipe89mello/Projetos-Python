def area(l, c):
    a = l * c
    print(f'A área de um terreno {largura} x {comprimento} é de {a}m².')


print('   CONTROLE DE TERRENOS   ')
print('-'*40)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
