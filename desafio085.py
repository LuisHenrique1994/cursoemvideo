# Digite sete valores numéricos e cadastre-os em uma lista única que tenha separados os valores pares e ímpares.
# Mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]  # duas listas dentro de uma lista
valor = 0
for c in range(1, 8):  # conte até 7
    valor = int(input(f'Digite o {c}o. valor: '))  # receba valores
    if valor % 2 == 0:  # se for par adicione na lista de numeros na posição 0
        numeros[0].append(valor)

    else:  # se não, adicione na lista de numeros na posição 1
        numeros[1].append(valor)

print('-=-' * 20)
numeros[0].sort()  # organize de forma crescente
numeros[1].sort()
print(f'Os Valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
