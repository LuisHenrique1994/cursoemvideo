# lista de 5 números mostrando maiores, menores e suas posições.

listanum = []
maior = menor = 0
for count in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {count}: ')))
    if count == 0:
        maior = menor = listanum[count]
    else:
        if listanum[count] > maior:
            maior = listanum[count]
        if listanum[count] < menor:
            menor = listanum[count]

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior número digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
