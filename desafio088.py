# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# Perguntar quantos jogos serão gerados e sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista.

from random import randint
from time import sleep

lista = []
jogos = list()
print('=' * 45)
print('             JOGA NA MEGA SENA              ')
print('=' * 45)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=-' * 4, f'SORTEANDO {quant} JOGOS ', '-=-' * 4)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=-' * 5, '<BOA SORTE!>', '-=-' * 5)
