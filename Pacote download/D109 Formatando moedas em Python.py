import Moedas109


p = float(input('Digite o preço R$ '))
print(f'A metade de {Moedas109.moeda(p)} é {Moedas109.metade(p, True)}.')
print(f'O dobro de {Moedas109.moeda(p)} é {Moedas109.dobro(p, True)}.')
print(f'Aumentando 10%, temos {Moedas109.aumentar(p, 10, True)}.')
print(f'Reduzindo 13%, temos {Moedas109.diminuir(p, 13, True)}.')
