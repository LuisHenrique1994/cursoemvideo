# Dicionários

#  Exemplo 1 - operações básicas
print('=' * 25, '\n Exemplo 1')
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
pessoas['sexo'] = 'F'
# del pessoas['sexo']
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-' * 25)

for k in pessoas.keys():
    print(k)

print('-' * 25)

for v in pessoas.values():
    print(v)

print('-' * 25)

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('=' * 25, '\n Exemplo 2')

# Exemplo 2

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)

print('-' * 25)

print(brasil)
print(brasil[0])
print(brasil[1]['uf'])

print('=' * 25, '\n Exemplo 3')

# Exemplo 3

brazil = list()
estado = dict()

for c in range(0, 2):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brazil.append(estado.copy())
print(brazil)

print('-' * 25)

for e in brazil:  # For para loop na lista "para cada estado em brazil"
    for k, v in e.items():  # For para loop no dicinário "para cada key e value em items"
        print(f'O campo {k} tem o valor {v}.')
    for v in e.values():  # Para cada valor em 'e'[Estado em (lista)brazil] mostre valor terminando vazio e pule linha
        print(v, end=' \n')
