# lista de números infinita a comando do usuário, recusa número duplicado e mostra em ordem crescente.

números = []

while True:
    num = int(input('Digite um valor: '))
    if num not in números:
        números.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = (input('Quer continuar? [S/N] '))
    if r in "Nn":
        break
print('-=-' * 20)
números.sort()
print(f'Você digitou os valores {números}')
