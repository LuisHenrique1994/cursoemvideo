# Listas (parte 1) exemplo 1

# Operações básicas
numeros = [2, 5, 9, 1, 7, 8, 1]
numeros[4] = 3
numeros.append(5)
numeros.sort(reverse=True)  # Organizando de forma decrescente
numeros.insert(2, 0)  # Na posição 2 insira o valor 0
numeros.pop(3)  # Remove o numero na posiçao 3
numeros.remove(1)  # Remove a primeira aparição do numero 1 da esquerda pra direita

# Verificando se existe o numero na lista e realizando operação
if 6 in numeros:
    numeros.remove(6)
else:
    print('Não Achei o número 6')
print(numeros)
print(f'Essa lista tem {len(numeros)} elementos.\n')

# Exemplo 2

valores = []
valores.append(5)
valores.append(9)
valores.append(7)

# for conte in range(0, 3):
#     valores.append(int(input('Digite um Valor: ')))

for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista\n')

# Exemplo 3
a = [1, 2, 4, 7]
b = a[:]  # pega da posição inicial até posição final da lista 'A' e passa para B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
