# Leia nome e duas notas de vários alunos e passe em uma lista composta.
# Mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno.

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-=-' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 26)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opção == 999:
        print('Finalizando...')
        break
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
print('Volte sempre!')
