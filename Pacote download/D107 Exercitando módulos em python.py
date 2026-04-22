import Moedas


p = float(input('Digite o preço R$ '))
print(f'A metade de R${p} é R${Moedas.metade(p)}.')
print(f'O dobro de R${p} é R${Moedas.dobro(p)}.')
print(f'Aumentando 10%, temos R${Moedas.aumentar(p, 10)}.')
print(f'Reduzindo 13%, temos R${Moedas.diminuir(p, 13)}.')