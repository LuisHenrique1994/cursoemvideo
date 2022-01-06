# Criando lista completa e depois separando lista pares e ímpares

completa = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    completa.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    res = input('Quer continuar? [S/N] ')
    if res in 'Nn':
        break
print('-=-' * 20)
print(f'A lista completa é {completa}')
print(f'A Lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
