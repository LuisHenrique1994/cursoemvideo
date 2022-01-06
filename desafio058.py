# Refazendo desafio 28 com while para tentar advinhar novamente o número randomico do computador

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Tente advinhar qual foi.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo.')
        elif jogador > computador:
            print('Menos... Tente de novo.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
