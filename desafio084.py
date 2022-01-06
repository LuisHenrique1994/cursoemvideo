# Faça uma lista de pessoas + pesos mostre quantas pessoas cadastradas e crie uma lista de mais pesados e mais leves

temp = []
pessoas = []
mai = men = 0

while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    pessoas.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print('-=-' * 23)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
