from Desafios.D115.Lib.Interface import *
from Desafios.D115.Lib.Arquivo import *
from time import sleep

from Desafios.D115.Lib.Interface import leiaint

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema.... Até logo!')
        break
    else:
        print('\33[31mERRO! Digite uma opção valida!\33[m')
    sleep(2)


