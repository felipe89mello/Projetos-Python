import Moedas108


p = float(input('Digite o preço R$ '))
print(f'A metade de {Moedas108.moeda(p)} é {Moedas108.moeda(Moedas108.metade(p))}.')
print(f'O dobro de {Moedas108.moeda(p)} é {Moedas108.moeda(Moedas108.dobro(p))}.')
print(f'Aumentando 10%, temos {Moedas108.moeda(Moedas108.aumentar(p, 10))}.')
print(f'Reduzindo 13%, temos {Moedas108.moeda(Moedas108.diminuir(p, 13))}.')
