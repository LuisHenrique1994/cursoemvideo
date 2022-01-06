# Fatorial usando for

n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(f, n + 1):
    print(c, end='')
    print(' x ' if c > 0 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
