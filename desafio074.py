# Sorteio de 5 numeros mostrando maior e menor usando tupla

from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in lista:
    print(f'{n} ', end='')
print(f'\nO Maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
