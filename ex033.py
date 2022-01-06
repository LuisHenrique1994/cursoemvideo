a = int(input('Primeiro númeor: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
#verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando o maior
maior = b
if a > b and a > c:
    maior = a
if c > a and c > b:
    maior = c
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))
