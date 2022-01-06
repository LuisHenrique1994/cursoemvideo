from random import choice
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
nome = choice([nome1, nome2, nome3, nome4])
print('Entre os alunos {}, {}, {} e {} o escolhido para apagar o quadro é {}.'.format(nome1, nome2, nome3, nome4, nome))
