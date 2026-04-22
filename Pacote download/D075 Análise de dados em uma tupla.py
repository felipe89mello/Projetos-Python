um = int(input('Digite um número: '))
dois = int(input('Digite outro número: '))
três = int(input('Digite mais um número: '))
quatro = int(input('Digite o último número: '))
num = (um, dois, três, quatro)
print(f'Você digitou os números {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



