from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep
import os


def clear():
    os.system('cls')


arq = 'cursoemvideo.txt'


if not arquivoExiste(arq):
    criarArquivo(arq)


clear()
while True:
    resposta = menu(['Pessoas Cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa.
        clear()
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\33[31mERRO! Digite uma opção válida!\33[m')
    sleep(1.5)

