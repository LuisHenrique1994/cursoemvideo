# Criando e mostrando lista em ordem decrescente com o total de elementos e verificando se existe o 5 na lista

numbers = []

while True:
    numbers.append(int(input('Digite um valor: ')))

    ans = input('Quer continuar: [S/N] ')
    if ans in 'Nn':
        break

print('-=-' * 20)
print(f'Você digitou {len(numbers)} elementos.')

numbers.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numbers}')

if 5 in numbers:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
