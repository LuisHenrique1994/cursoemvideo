# Refazendo ex09 (tabuada) usando FOR
n = int(input('Digite um numero para ver a sua tabuada: '))
print('-' * 20)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('-' * 20)
