# Leia nome e média de um aluno, guardando a situação em um dicionário. Mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=-' * 15)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
