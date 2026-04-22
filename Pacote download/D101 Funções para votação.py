from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA')
    elif idade >= 18 and idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL')

print('-' * 30)
nascimento = int(input('Digite o ano de nascimento: '))
voto(nascimento)